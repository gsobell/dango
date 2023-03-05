# dango 🍡
dango is a terminal based Go board written in python

> **dan•go** [だんご]  
> noun
> 1. A Japanese dumpling made from *mochiko* (rice flour) 
> 2. A Japanese [go term](https://senseis.xmp.net/?Dango), meaning "dumpling shape";  a solid mass of stones without eyes, and with few liberties

<h3 align="center"><img src="https://github.com/gsobell/dango/blob/dan/resources/splash.png" width=50% height=50%></h3>


## Usage
### Installation
To download and launch, run the following:
```shell
git clone https://github.com/gsobell/dango.git
cd dango && chmod +x dango.py
./dango.py
```

To install on Arch-based distros, use the [PKGBUILD](https://github.com/gsobell/dango/blob/dan/PKGBUILD):
```shell
curl -O https://raw.githubusercontent.com/gsobell/dango/dan/PKGBUILD
makepkg -i
```

Alternatively, you can [download a zip of the main branch.](https://github.com/gsobell/dango/archive/refs/heads/dan.zip)
Add to your `$PATH` to run from anywhere. Since dango is still in early stages of development, please open an issue if you encounter any hitch or glitch!

### Gameplay

| To place a stone on A1: | To pass: | To quit:|
|-------------------------|----------|---------|
|         `A1`            |  `PASS`  |  `:q`   |

Two consecutive passes end the game.


## Features
### Current
- Two player games
- Play against [GnuGo](https://www.gnu.org/software/gnugo/)
- Easy to use TUI (terminal user interface)
- Only allows legal moves
- Captured stone tally
- Full support for `GTP` (Go Text Protocol)

### Future
- `nCurses` interface
- Persistent config
- Optional move timer
- Import/Export of games
- Integration with in-house Go engine [goma](https://github.com/gsobell/goma) (in development)


Also note that `dango.sh` has been renamed [`dango-legacy`](https://github.com/gsobell/dango-legacy) and no further development will be done.

Find dango and more Go clients on [Sensei's Library](https://senseis.xmp.net/?GoClient).
If you like this, you might also enjoy [termsuji](https://github.com/lvank/termsuji), , [sabaki](https://github.com/SabakiHQ/Sabaki), [baduk-fortune](https://github.com/gsobell/baduk-fortune), [cbonsai](https://gitlab.com/jallbrit/cbonsai), and [haikunator](https://github.com/usmanbashir/haikunator).
If you want to support this project, consider ~~buying me a [cup of coffee](https://www.buymeacoffee.com/gsobell)~~ playing me in a [game of Go](https://online-go.com/player/1080938/).

***

Inspired by [chs](https://github.com/nickzuber/chs)
