from __future__ import annotations

from LSP.plugin import LspPlugin
from LSP.plugin import Notification
from LSP.plugin import notification_handler
from LSP.plugin import OnPreStartContext
from LSP.plugin.core.protocol import Error
from LSP.protocol import ExecuteCommandParams
from LSP.protocol import LSPAny
from lsp_utils import NodeManager
from pathlib import Path
from sublime_lib import ResourcePath
from typing import Any
from typing import Dict # Deprecated in 3.9
from typing import final
from typing import Tuple # Deprecated in 3.9
from typing_extensions import override

# `glint-language-server` asks its client to run commands against tsserver, so that Glint and
# TypeScript agree on which `tsconfig.json` governs a file, and so that Glint can read component
# metadata that only `@glint/tsserver-plugin` knows about.
#
# The server calls `sendNotification('tsserver/request', [seq, command_name, command_args])`. Given a
# single argument that is a list, vscode-jsonrpc wraps it in another list, so the notification arrives
# with `params` of `[[seq, command_name, command_args]]` - one positional argument, not three.
#
# The reply has to be nested the same way. The server's handler is `([id, res]) => ...`, and
# vscode-jsonrpc spreads positional params across the handler's arguments, so `[seq, body]` would
# call it as `handler(seq, body)` and the destructuring would fail on `seq`.
TsserverRequest = Tuple[int, str, Dict[str, Any]]
TsserverRequestParams = Tuple[TsserverRequest]

TYPESCRIPT_PLUGIN_NAME = 'LSP-typescript'


def plugin_loaded():
    LspTemplateTagPlugin.register()


def plugin_unloaded():
    LspTemplateTagPlugin.unregister()


@final
class LspTemplateTagPlugin(LspPlugin):

    @classmethod
    @override
    def on_pre_start_async(cls, context: OnPreStartContext) -> None:
        package_name = cls.plugin_storage_path.name
        NodeManager.on_pre_start_async(
            context,
            cls.plugin_storage_path,
            ResourcePath('Packages', package_name, 'server'),
            Path('node_modules', '@glint', 'ember-tsc', 'bin', 'glint-language-server.js'),
            node_version_requirement='>=22',
        )

    @notification_handler('tsserver/request')
    def on_tsserver_request(self, params: TsserverRequestParams) -> None:
        session = self.weaksession()
        if not session:
            return
        manager = session.manager()
        if not manager:
            return
        seq, command_name, command_args = params[0]
        typescript_session = manager.get_session(TYPESCRIPT_PLUGIN_NAME, command_args['file'])
        if not typescript_session:
            print(
                f'[LSP-ember] {TYPESCRIPT_PLUGIN_NAME} not found, or it has not loaded '
                '@glint/tsserver-plugin. Try restarting Sublime Text.'
            )
            self._on_execute_command_response(seq, {'body': None})
            return
        execute_command_params: ExecuteCommandParams = {
            'command': 'typescript.tsserverRequest',
            'arguments': [
                command_name,
                command_args,
                {'isAsync': True, 'lowPriority': True},
            ]
        }
        typescript_session.execute_command(execute_command_params, progress=False).then(
            lambda result: self._on_execute_command_response(seq, result)
        )

    def _on_execute_command_response(self, seq: int, result: LSPAny | Error) -> None:
        if session := self.weaksession():
            body = result['body'] if isinstance(result, dict) and 'body' in result else None
            session.send_notification(Notification('tsserver/response', [[seq, body]]))
