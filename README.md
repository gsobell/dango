# dango 🍡
dango is a terminal based Go board written in python

> **dan•go** [だんご]  
> noun
> 1. A Japanese dumpling made from *mochiko* (rice flour) 
> 2. A Japanese [go term](https://senseis.xmp.net/?Dango), meaning "dumpling shape";  a solid mass of stones without eyes, and with few liberties

<h3 align="center"><img src="https://i.imgur.com/914njtc.png"></h3>  
<h6 align="center">Themes from original project, new version completely in color</h6>

## Usage
### Installation
To download and launch, run the following:
```shell
git clone https://github.com/gsobell/dango.git
cd dango
python dango.py
```
Alternatively, you can [download a zip of the main branch.](https://github.com/gsobell/dango/archive/refs/heads/dan.zip)
Add to your `$PATH` to run from anywhere. Since dango is still in early stages of development, please open an issue if you encounter any hitch or glitch!

### Gameplay
To make a move (e.g. A1):
```
A1
```
To pass:
```
PASS
```
Two consecutive passes end the game.


## Features
### Current
- Two player games
- Easy to use TUI (terminal user interface)
- Only allows legal moves (sorry, no self-atari)

### Future
- `nCurses` interface
- Automatic score tally
- Full support for `GTP` (Go Text Protocol)
- Optional move timer
- Import/Export of games
- Heavy integration with in-house Go engine [goma](https://github.com/gsobell/goma) (in development)

Note that there may be considerable overlap and shared files between `dango` and [goma](https://github.com/gsobell/goma).

Also note that `dango.sh` has been renamed `dango-legacy` and no further development will be done.

Find dango and more Go clients on [Sensei's Library](https://senseis.xmp.net/?GoClient).
If you like this, you might also enjoy [termsuji](https://github.com/lvank/termsuji), , [sabaki](https://github.com/SabakiHQ/Sabaki), [baduk-fortune](https://github.com/gsobell/baduk-fortune), [cbonsai](https://gitlab.com/jallbrit/cbonsai), and [haikunator](https://github.com/usmanbashir/haikunator).
If you want to support this project, consider ~~buying me a [cup of coffee](https://www.buymeacoffee.com/gsobell)~~ playing me in a [game of Go](https://online-go.com/player/1080938/).

***

Inspired by [chs](https://github.com/nickzuber/chs)
