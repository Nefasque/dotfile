# ~/.bashrc
#

[[ $PS1 && -f /usr/share/bash-completion/bash_completion ]] && \
    . /usr/share/bash-completion/bash_completion
# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias gep='grep --color=auto'
alias v='nvim'
alias src='source ~/.bashrc'

# command Exa Options

# alias ls='~/.cargo/bin/exa --color=always --group-directories-first --icons --git -s extension -b --time-style=iso -t created -b'

alias l='~/.cargo/bin/exa -x -1 --color=always --group-directories-first --icons --git -s extension -b --time-style=iso -t created -b'

alias la='~/.cargo/bin/exa -x -a -1 --color=always --group-directories-first --icons --git -s extension -b --time-style=iso -t created -b'

alias ll='~/.cargo/bin/exa -x -l --color=always --group-directories-first --icons --git -s extension -b --time-style=iso -t created -b'

alias lla='~/.cargo/bin/exa -x -l -a --color=always --group-directories-first --icons --git -s extension -b --time-style=iso -t created -b'

alias tree='~/.cargo/bin/exa -x -T --color=always --group-directories-first --icons --git -s extension -b --time-style=iso -t created -b'

# mdcat
alias mdcat='~/.cargo/bin/mdcat'

#  -> bat 
alias bat='~/.cargo/bin/bat'

# agg 
alias agg='~/.cargo/bin/agg'

# str -> /opt/st/reload.sh
alias str='/opt/st/reload.sh'

# fd
alias fd='~/.cargo/bin/fd'

# git
alias g='git'
alias gs='git status -s'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log'
alias gls='git log --oneline --abbrev-commit --graph --decorate --all --color=always'
alias gd='git diff'
alias gco='git checkout'

# Created by `pipx` on 2023-11-11 16:25:08
export PATH="$PATH:/home/nefasque/.local/bin"

# auto jump start 
. /usr/share/autojump/autojump.bash

# 
# alias record='cd ${BYZANZ_REPO_CLONE_PATH} && ./byzanz-record-region.sh'
alias record='cd ~/workspace/repos/byzanz/ && ./byzanz-record-region.sh'
alias byzanz-record='~/workspace/repos/byzanz/byzanz-record-region.sh'

parse_git_branch() {
    git branch 2>/dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}


export PS1=" \[\e[31m\] \u  \[\e[m\]\[\e[32m\] \w\[\e[m\]\[\e[35m\]\`parse_git_branch\`\[\e[m\]\\n~>"


# loader colorscheme of wal. 
#(cat ~/.cache/wal/sequences &)
#cat ~/.cache/wal/sequences
#source ~/.cache/wal/colors-tty.sh
