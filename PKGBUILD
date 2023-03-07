# Contributor: @gsobell
# Maintainer:  @gsobell

pkgname=dango
pkgver=0.3.0
pkgrel=1
pkgdesc='a terminal based Go board written in python'
arch=('any')
url='https://github.com/gsobell/dango'
license=('GPL')
provides=("$pkgname")
optdepends=('gnugo: computer opponent')
# install=
source=("$url/archive/refs/tags/v${pkgver}.tar.gz")
noextract=()
sha256sums=('2ce6b26be4e0d53ef84f66cb21edf8a23a203d142b83c4e900e81dd73000f153')

package() {
    cd "$srcdir/$pkgname-$pkgver"
    install -m 755 -TD "$pkgname.py" "$pkgdir/usr/bin/$pkgname"
    install -m 755 -TD "game_play.py" "$pkgdir/usr/bin/game.py"
    install -m 755 -TD "goban.py" "$pkgdir/usr/bin/goban.py"
    install -m 644 -TD "README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
    install -m 644 -TD "LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
