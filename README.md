[![This project uses GitHub Actions for continuous integration.](https://github.com/ijlee2/LSP-ember/actions/workflows/ci.yml/badge.svg)](https://github.com/ijlee2/LSP-ember/actions/workflows/ci.yml)

# LSP-ember

_Provides LSP (Language Server Protocol) for Ember in Sublime Text_

<div align="center">
  <img alt="In a .gts file, we can hover over code to see additional information." src="https://github.com/user-attachments/assets/bee8f160-396a-44bf-833f-68ad8093591a" />
</div>


## Installation

Install these 5 packages via [Package Control](https://packagecontrol.io), then restart Sublime Text.

- Handlebars
- LSP
- LSP-ember
- LSP-typescript
- [Template Tag](https://github.com/ijlee2/sublime-syntax-definition-template-tag)

<details>

<summary>How to Install</summary>

1. Open Sublime Text.
1. Open Package Control by pressing <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> (Mac) or <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> (Windows). Alternatively, in the menu bar, click on `Sublime Text` > `Settings` > `Package Control`.
1. Type `install` in the search bar so that you can find and select `Package Control: Install Package`.
1. Search for `LSP-ember`, then select to install. Repeat steps 2-3 for the remaining packages.
1. Restart Sublime Text.

</details>

> [!NOTE]
>
> Should [LSP-ember](https://packagecontrol.io/packages/LSP-ember) be unavailable, you can use `Package Control: Add Repository` instead.
>
> Type `https://raw.githubusercontent.com/ijlee2/LSP-ember/main/repository.json` to download code, then use `Package Control: Install Package` to install LSP-ember.

> [!NOTE]
>
> Glint v1 is not supported.


## Configuration

There's currently little to configure. You can use the Command Palette to run `Preferences: LSP-ember Settings`.


## Contributing

See the [Contributing](CONTRIBUTING.md) guide for details.


## Credits

Thanks to the maintainers of [Glint](https://github.com/typed-ember/glint) for providing a TypeScript server plugin.


## License

This project is licensed under the [MIT License](LICENSE.md).
