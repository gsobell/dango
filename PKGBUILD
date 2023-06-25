# Contributor: @gsobell
# Maintainer:  @gsobell

pkgname=dango
pkgver=0.4.2
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
sha256sums=('0856ca9563baee36c922875e62efab3ac3399339e0fad4cc957ebdc11af67f04')

package() {
    cd "$srcdir/$pkgname-$pkgver"
    install -m 755 -TD "$pkgname.py" "$pkgdir/usr/bin/$pkgname"
    install -m 644 -TD "README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
    install -m 644 -TD "LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
