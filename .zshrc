autoload -U compinit && compinit
autoload -U colors && colors
PS1="%F{2}nyfair%F{3}@%F{6}%1d %f"
[[ -n "${key[PageUp]}" ]] && bindkey "${key[PageUp]}" history-beginning-search-backward
[[ -n "${key[PageDown]}" ]] && bindkey "${key[PageDown]}" history-beginning-search-forward
bindkey "\e[3~" delete-char
bindkey "\e[H" beginning-of-line
bindkey "\e[F" end-of-line

setopt complete_aliases
setopt auto_cd
setopt auto_pushd
setopt pushd_ignore_dups
setopt pushd_silent
setopt no_hist_beep
setopt hash_list_all
setopt hist_ignore_all_dups
setopt hist_reduce_blanks
setopt hist_ignore_space
setopt hist_verify
setopt hist_expire_dups_first
setopt list_types
setopt numeric_glob_sort
setopt inc_append_history

zmodload -i zsh/complist
zstyle ':completion:*' ignore-parents parent pwd directory
zstyle ':completion:*' menu select

alias ll='ls -o'
alias df='df -Th'
alias du='du -h'
alias grep='grep --color'
alias md='mkdir -p'
alias rd='rm -rf'

# personal configuration
alias rb=ruby
alias lua=luajit
alias py=python3
alias python='python3 -i'
alias ss='all_proxy=socks5://127.0.0.1:17727'
alias conv='noglob luajit /opt/fi-luajit/test/conv.lua'
export C_INCLUDE_PATH=/usr/include
export CPLUS_INCLUDE_PATH=/usr/include
export EDITOR='/c/Program\ Files\ \(x86\)/Microsoft\ VS\ Code/code --locale=en-US'
alias vv=$EDITOR
alias cgr='cargo build --release'
export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
alias http='py -m http.server'
