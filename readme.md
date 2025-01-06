# How to use

## Installation

The preferred way of instaling genconf is via a git submodule; Running `git submodule add https://github.com/Wilaz/genconf .vscode/genconf` at the root of your project should work if you have a git repo already initialized.

## Config

Genconf is configured by a singular settings.jstemp instide the `.vscode` folder. For example, to use templating on `xyz`, you would have `${xyz}` in the jstemp. Additionally, comments are allowed via `// comment`. The templates directory contains a few premade examples that better explain how it works.

## Todos

- [x] Replace keys.toml with an interactive cli
- [x] Add more example configs
