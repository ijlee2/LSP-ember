[![This project uses GitHub Actions for continuous integration.](https://github.com/ijlee2/LSP-ember/actions/workflows/ci.yml/badge.svg)](https://github.com/ijlee2/LSP-ember/actions/workflows/ci.yml)

# LSP-ember

_Provides LSP for `<template>` tags for Sublime Text_


## Installation

Install the following packages via [Sublime Text Package Control](https://packagecontrol.io/), then restart Sublime Text.

1. [LSP](https://packagecontrol.io/packages/LSP)
1. [LSP-ember](https://packagecontrol.io/packages/LSP-ember)
1. [LSP-typescript](https://packagecontrol.io/packages/LSP-typescript)
1. [Template Tag](https://packagecontrol.io/packages/Template%20Tag)

> [!NOTE]
>
> `LSP-typescript` is a required dependency, not an optional one. `Template Tag` provides syntax highlighting.


## Configuration

Open the configuration file using the Command Palette with the `Preferences: LSP-ember Settings` command, or from the menu bar (`Sublime Text` > `Settings` > `Package Settings` > `LSP` > `LSP-ember`).


## How it works

Glint v2 is built on [Volar](https://volarjs.dev/) and splits its work across two processes, the same way the [Glint VSCode extension](https://marketplace.visualstudio.com/items?itemName=typed-ember.glint2-vscode) does.

- `glint-language-server` (from `@glint/ember-tsc`) is started by this package and serves `*.gjs` and `*.gts` files. It understands `<template>` tags and maps them onto TypeScript.
- [`@glint/tsserver-plugin`](https://www.npmjs.com/package/@glint/tsserver-plugin) is a TypeScript server plugin. This package contributes it to `LSP-typescript` through [`typescript-plugins.json`](typescript-plugins.json), so that a single `tsserver` holds the whole project. That is what lets `*.ts` files import from `*.gts` files, and what lets features like auto-import and rename work across both.

The two halves talk to each other: `glint-language-server` sends `tsserver/request` notifications, and [`plugin.py`](plugin.py) forwards them to the `LSP-typescript` session as `typescript.tsserverRequest` commands, then sends the reply back as `tsserver/response`. Without `LSP-typescript` installed, the language server has no `tsserver` to ask, and most features will not work.


## License

This project is licensed under the [MIT License](LICENSE.md).
