# Contributor: @gsobell
# Maintainer:  @gsobell

pkgname=dango
pkgver=0.2.0
pkgrel=1
pkgdesc='a terminal based Go board written in python'
arch=('any')
url='https://github.com/gsobell/dango'
license=('GPL')
depends=("$pkgname")
provides=("$pkgname")
conflicts=('dango')
optdepends=('gnugo: computer opponent')
source=("$url/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('2ce6b26be4e0d53ef84f66cb21edf8a23a203d142b83c4e900e81dd73000f153')

package() {
  cd "$srcdir/$pkgname-v$pkgver"
  make DESTDIR="$pkgdir/" PREFIX="/usr" install
}
