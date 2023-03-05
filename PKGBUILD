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
depends=('python')
optdepends=('gnugo: computer opponent')
source=("$url/archive/refs/tags/v${pkgver}.tar.gz")
noextract=()
sha256sums=('e9bf8341f8ee1b97a97d02386dfb12257998a0fca8f6c403847f55e280e8a7c4')

package() {
    cd "$srcdir/$pkgname-$pkgver"
    sed -i /"from game import *"/d  dango.py
    sed -i /"from goban import Board"/d  game.py
    cat goban.py game.py $pkgname.py >> $pkgname
    install -m 755 -TD "$pkgname" "$pkgdir/usr/bin/$pkgname"
    install -m 644 -TD "README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
    install -m 644 -TD "LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
