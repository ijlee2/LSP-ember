# LSP-ember

_Provides language features for `<template>` tags in Sublime Text_

This is a helper package that automatically installs and updates
[Glint](https://github.com/typed-ember/glint) for you, so that you get type
checking, completions, go-to-definition, and hover documentation inside
`*.gjs` and `*.gts` files (the [template tag
format](https://guides.emberjs.com/release/components/template-tag-format/)
used by Ember).


## Installation

Install the following packages via [Sublime Text Package
Control](https://packagecontrol.io/), then restart Sublime Text.

1. [LSP](https://packagecontrol.io/packages/LSP)
1. [LSP-typescript](https://packagecontrol.io/packages/LSP-typescript)
1. [LSP-ember](https://packagecontrol.io/packages/LSP-ember)
1. [Template Tag](https://packagecontrol.io/packages/Template%20Tag)

> [!NOTE]
>
> `LSP-typescript` is a required dependency, not an optional one. See
> [How it works](#how-it-works).

> [!NOTE]
>
> `Template Tag` provides the syntax definition (`source.template-tag`) that
> this package uses to recognize `*.gjs` and `*.gts` files.

Your project must be a Glint v2 project: add
[`@glint/ember-tsc`](https://www.npmjs.com/package/@glint/ember-tsc) to your
`devDependencies` and follow the [migration
guide](https://github.com/typed-ember/glint/blob/main/docs/v2-upgrade.md).
Glint v1 (`@glint/core`, loose-mode `*.hbs` templates) is not supported.


## Configuration

Open the configuration file using the Command Palette with the `Preferences:
LSP-ember Settings` command, or from the menu bar
(`Sublime Text` > `Settings` > `Package Settings` > `LSP` > `LSP-ember`).


## How it works

Glint v2 is built on [Volar](https://volarjs.dev/) and splits its work across
two processes, the same way the [Glint
VSCode extension](https://marketplace.visualstudio.com/items?itemName=typed-ember.glint2-vscode)
does.

- `glint-language-server` (from `@glint/ember-tsc`) is started by this package
  and serves `*.gjs` and `*.gts` files. It understands `<template>` tags and
  maps them onto TypeScript.

- [`@glint/tsserver-plugin`](https://www.npmjs.com/package/@glint/tsserver-plugin)
  is a TypeScript server plugin. This package contributes it to
  `LSP-typescript` through [`typescript-plugins.json`](typescript-plugins.json),
  so that a single `tsserver` holds the whole project. That is what lets
  `*.ts` files import from `*.gts` files, and what lets features like
  auto-import and rename work across both.

The two halves talk to each other: `glint-language-server` sends
`tsserver/request` notifications, and [`plugin.py`](plugin.py) forwards them to
the `LSP-typescript` session as `typescript.tsserverRequest` commands, then
sends the reply back as `tsserver/response`. Without `LSP-typescript`
installed, the language server has no `tsserver` to ask, and most features
will not work.


## License

This project is licensed under the [MIT License](LICENSE.md).
