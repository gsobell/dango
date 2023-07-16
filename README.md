# dango 🍡
dango is a nCurses Go board for the terminal

> **dan•go** [だんご]  
> noun
> 1. A Japanese dumpling made from *mochiko* (rice flour) 
> 2. A Japanese [go term](https://senseis.xmp.net/?Dango), meaning "dumpling shape";  a solid mass of stones without eyes, and with few liberties

<h3 align="center"><img src="https://github.com/gsobell/dango/blob/dan/resources/splash.png" width=50% height=50%></h3>


## Usage

To try it without installing:
```shell
python <(curl -s https://raw.githubusercontent.com/gsobell/dango/dan/dango.py)
```
### Installation

To download and launch, run the following:
```shell
curl -O https://raw.githubusercontent.com/gsobell/dango/dan/dango.py
mv dango.py dango && chmod +x dango
./dango
```

To install on Arch-based distros, use the [PKGBUILD](https://github.com/gsobell/dango/blob/dan/PKGBUILD):
```shell
curl -O https://raw.githubusercontent.com/gsobell/dango/dan/PKGBUILD
makepkg -i
```

Alternatively, you can [download a zip of the main branch.](https://github.com/gsobell/dango/archive/refs/heads/dan.zip)
If you encounter any bugs, open a issue on GitHub.

### Gameplay

Use the arrow or vim keys to navigate the board. Enter or space places a stone.
Use `u` to undo, `p` to pass, `q` to quit.
Also supports mouse input; click to move, double click to place stone.

<!-- Two consecutive passes end the game. -->

## Features
Due to implementing the `nCurses` interface, there has been some feature regression. They will be re-implemented soon.
### Current
- `nCurses` interface
- Two player games
- Easy to use TUI (terminal user interface)
- Full support for `GTP` (Go Text Protocol)
- Toggle _kifu_ (game record) with `n` during gameplay
- Undo on user v. user games
- Only allows legal moves
- Start menu with settings


### Future
- Play against [GnuGo](https://www.gnu.org/software/gnugo/)
- Persistent config
- Captured stone tally
- Optional move timer
- Import/Export of games
- Integration with in-house Go engine [goma](https://github.com/gsobell/goma) (in development)



Also note that `dango.sh` has been renamed [`dango-legacy`](https://github.com/gsobell/dango-legacy) and no further development will be done.

Find dango and more Go clients on [Sensei's Library](https://senseis.xmp.net/?GoClient).
If you like this, you might also enjoy [termsuji](https://github.com/lvank/termsuji), , [sabaki](https://github.com/SabakiHQ/Sabaki), [baduk-fortune](https://github.com/gsobell/baduk-fortune), [cbonsai](https://gitlab.com/jallbrit/cbonsai), and [haikunator](https://github.com/usmanbashir/haikunator).
If you want to support this project, consider ~~buying me a [cup of coffee](https://www.buymeacoffee.com/gsobell)~~ playing me in a [game of Go](https://online-go.com/player/1080938/).

***

Inspired by [chs](https://github.com/nickzuber/chs)
