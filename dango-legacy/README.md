# dango-legacy 🍡
dango-legacy is a shell wrapper for the ASCII interface of GNU Go, in an attempt to make it more user friendly.

Development on dango-legacy has now ceased, and no further changes will be made.

> **dan•go** [だんご]
> noun
> 1. A Japanese dumpling made from *mochiko* (rice flour) 
> 2. A Japanese [go term](https://senseis.xmp.net/?Dango), meaning "dumpling shape";  a solid mass of stones without eyes, and with few liberties

<h3 align="center"><img src="https://i.imgur.com/914njtc.png"></h3>  
<h6 align="center">Available board themes</h6>

## Usage
To download and launch, run the following:
```shell
curl -O https://raw.githubusercontent.com/gsobell/dango/home/dango-legacy/dango-legacy.sh
sh dango.sh
```
Since dango-legacy was never propperly finished, bugs should be expected, along with some artifacting when using the color board.

## Features
- Verifies GNU Go is installed at launch
- Easy to use TUI (terminal user interface)
- XDG conforming persistent user settings
- Game caching, with optional user defined save location
- Three board choices (full color support on urxvt only)

## Q&A
Q: Doesn't GNU Go have a color mode?  
A: Yes, however, it's a training tool, and gives the status of groups (alive, dead, critical, etc),  while dango aims to improve board readability and ease of use. GNU Go's extensive documentation can be found [here](https://www.gnu.org/software/gnugo/gnugo_toc.html).

Q: You don't know how to use `sed`, do you?  
A: No, not really. If I did, it would look a whole lot nicer. It's a shame I don't; most software in existence can be replaced by a well placed regular expression. 

Find dango and more Go clients on [Sensei's Library](https://senseis.xmp.net/?GoClient).  
If you like this, you might also enjoy [cbonsai](https://gitlab.com/jallbrit/cbonsai), [sabaki](https://github.com/SabakiHQ/Sabaki), [baduk-fortune](https://github.com/gsobell/baduk-fortune), and [haikunator](https://github.com/usmanbashir/haikunator).

If you want to support this project, consider ~~buying me a [cup of coffee](https://www.buymeacoffee.com/gsobell)~~ playing me in a [game of Go](https://online-go.com/player/1080938/).

***

Inspired by [chs](https://github.com/nickzuber/chs)

