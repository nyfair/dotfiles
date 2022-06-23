set PATH /usr/bin /opt/bin /c/Windows/system32 /c/Windows /c/Windows/system32/OpenSSH

function fish_user_key_bindings
  bind \e\[1\;5A backward-kill-bigword
  bind \e\[1\;5B backward-kill-path-component
end