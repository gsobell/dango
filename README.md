# dango 🍡
dango is a shell wrapper for the ASCII interface of GNU Go, in an attempt to make it more user friendly.

> **dan•go** [だんご]  
> noun
> 1. A Japanese dumpling made from *mochiko* (rice flour) 
> 2. A Japanese [go term](https://senseis.xmp.net/?Dango), meaning "dumpling shape";  a solid mass of stones without eyes, and with few liberties

<h3 align="center"><img src="https://i.imgur.com/914njtc.png"></h3>  
<h6 align="center">Available board themes</h6>

## Usage
To download and launch, run the following:
```shell
curl -O https://raw.githubusercontent.com/gsobell/dango/home/dango.sh
sh dango.sh
```
Add to your `$PATH` to run from anywhere. Since dango is still in early stages of development, bugs should be expected, along with some artifacting when using the color board.

## Features
### Current
- Verifies GNU Go is installed at launch
- Easy to use TUI (terminal user interface)
- XDG conforming persistent user settings
- Game caching, with optional user defined save location
- Three board choices (full color support on urxvt only)

### Future
- Rewrite in Python with `nCurses` interface
- Support for `GTP` (Go Text Protocol)
- Heavy integration with in-house Go engine [goma](https://github.com/gsobell/goma) (in development)

What does these plans mean for the current iteration of `dango`? Most likely when the python interface facelift is complete (and stable!), the shell script will be made legacy, and no further changes will be made to it. Howerever, it will still be accesible from this repository.

Find dango and more Go clients on [Sensei's Library](https://senseis.xmp.net/?GoClient).  
If you like this, you might also enjoy [cbonsai](https://gitlab.com/jallbrit/cbonsai), [sabaki](https://github.com/SabakiHQ/Sabaki), [baduk-fortune](https://github.com/gsobell/baduk-fortune), and [haikunator](https://github.com/usmanbashir/haikunator).

If you want to support this project, consider ~~buying me a [cup of coffee](https://www.buymeacoffee.com/gsobell)~~ playing me in a [game of Go](https://online-go.com/player/1080938/).

***

Inspired by [chs](https://github.com/nickzuber/chs)
