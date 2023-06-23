# Contributor: @gsobell
# Maintainer:  @gsobell

pkgname=dango
pkgver=0.4.0
pkgrel=1
pkgdesc='A terminal based Go board written in python'
arch=('any')
url='https://github.com/gsobell/dango'
license=('GPL')
provides=("$pkgname")
depends=('python')
optdepends=('gnugo: computer opponent')
source=("$url/archive/refs/tags/v${pkgver}.tar.gz")
noextract=()
sha256sums=('70c0a5eec64ae78712eced23c75ab29ffc748f486c77125c62a473b9511c26a2')

package() {
    cd "$srcdir/$pkgname-$pkgver"
    install -m 755 -TD "$pkgname.py" "$pkgdir/usr/bin/$pkgname"
    install -m 644 -TD "README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
    install -m 644 -TD "LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
