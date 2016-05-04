set -v

aclocal
autoheader
autoconf
automake --add-missing
