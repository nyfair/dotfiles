set PATH /clang64/bin /mingw64/bin /usr/bin /opt/bin $PATH
set MANPATH /usr/share/fish/man /usr/share/man $MANPATH
set -gx INFOPATH /usr/info /usr/share/info /usr/info /share/info $INFOPATH
set -gx PKG_CONFIG_PATH /usr/lib/pkgconfig /usr/share/pkgconfig /lib/pkgconfig
set -gx MANPATH $MANPATH

set -gx SYSCONFDIR /etc

set ORIGINAL_TMP $TMP
set ORIGINAL_TEMP $TEMP
set -e TMP
set -e TEMP
set -gx tmp (cygpath -w $ORIGINAL_TMP 2> /dev/null)
set -gx temp (cygpath -w $ORIGINAL_TEMP 2> /dev/null)
set -gx TMP /tmp
set -gx TEMP /tmp

if test -n $ACLOCAL_PATH
    set -gx ACLOCAL_PATH $ACLOCAL_PATH
end

set -gx LC_COLLATE C
for postinst in /etc/post-install/*.post
    if test -e $postinst
        sh -c $postinst
    end
end
