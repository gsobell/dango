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
- Integrated game review
- Better color support
- Implement `dialog` or `whiptail` menu framework

## Q&A
Q: Doesn't GNU Go have a color mode?  
A: Yes, however, it's a training tool, and gives the status of groups (alive, dead, critical, etc),  while dango aims to improve board readability and ease of use. GNU Go's extensive documentation can be found [here](https://www.gnu.org/software/gnugo/gnugo_toc.html).

Find dango and more Go clients on [Sensei's Library](https://senseis.xmp.net/?GoClient).  
If you like this, you might also enjoy [cbonsai](https://gitlab.com/jallbrit/cbonsai), [sabaki](https://github.com/SabakiHQ/Sabaki), [baduk-fortune](https://github.com/gsobell/baduk-fortune), and [haikunator](https://github.com/usmanbashir/haikunator).

***

Inspired by [chs](https://github.com/nickzuber/chs)
