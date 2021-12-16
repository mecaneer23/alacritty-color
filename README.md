# Alacritty Color
A command-line utility to easily change your Alacritty color scheme

## Dependencies
 - [Alacritty](https://github.com/alacritty/alacritty) ([Install](#install-alacritty))
 - [Python3.10+](https://www.python.org/) ([Install](#install-python-310))

## Install Alacritty Color
 - Clone this repository
 - Run the following command to install:
```bash
$ sudo mv /path/to/alacritty-color /bin/alacritty-color
```
### Recommended configuration changes (~/.config/alacritty/alacritty.yml)
 - Add `###DEFAULT_THEME###` to the line directly before your favorite theme -
 otherwise it will default to the first theme in the list (alphabetically)
 - make sure every color scheme in your list has the following format:
```yml
 theme-name: &theme-name
  ...
```
 - make sure you have a line somewhere in your file with the follwing:
```yml
colors: *theme-name
```
### Recommended aliases
Add these to the end of your `~/.bashrc`:
```bash

alias ac="alacritty-color"
alias acc="alacritty-color --current"
alias acr="alacritty-color --random"
acl() {
  if [[ ! $1 ]]; then
    alacritty-color --list
  else
    alacritty-color --list | grep $1
  fi
}

```

## Install Alacritty
### Arch
```bash
$ sudo pacman -S alacritty
```
### Debian/Ubuntu
```bash
$ sudo apt install cargo; cargo install alacritty
```

## Install Python 3.10
### Windows
[Python.org](https://www.python.org/downloads/windows/)
### Arch
```bash
$ sudo yay -S python310
```
### Debian/Ubuntu
```bash
$ sudo apt install python3.10
```
