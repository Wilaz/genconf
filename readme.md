# How to use

## Installation

The preferred way of instaling genconf is via a git submodule; Running `git submodule add https://github.com/Wilaz/genconf .vscode/genconf` at the root of your project should work if you have a repo already initialized.

## Config

Configs are stored in the `.vscode/config` directory in the form of two files: `keys.toml` and `settings.jstemp`

### keys.toml

In here you store what you want shown. Set your keys to `true` or `false`

### settings.jstemp

In here you store your settings.json template. For example, to use templating on `xyz`, you would have `${xyz}` in the jstemp then `xyz =` (`true` or `false`) in keys. Unlike json, comments are allowed via `// comment`.

## Templates

The templates directory contains a few premade templates.

## Todos

- [ ] Replace keys.toml with an interactive cli
- [x] Add more example configs
