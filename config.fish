set PATH /clang64/bin /mingw64/bin /usr/bin /opt/bin /c/Windows/system32 /c/Windows /c/Windows/system32/OpenSSH
set -gx INFOPATH /usr/info /usr/share/info /usr/info /share/info $INFOPATH
set -gx PKG_CONFIG_PATH /usr/lib/pkgconfig /usr/share/pkgconfig /lib/pkgconfig
set -gx MANPATH /usr/share/fish/man /usr/share/man
set -gx SYSCONFDIR /etc

set ORIGINAL_TMP $TMP
set ORIGINAL_TEMP $TEMP
set -e TMP
set -e TEMP
set -gx tmp (cygpath -w $ORIGINAL_TMP 2> /dev/null)
set -gx temp (cygpath -w $ORIGINAL_TEMP 2> /dev/null)
set -gx TMP /tmp
set -gx TEMP /tmp
