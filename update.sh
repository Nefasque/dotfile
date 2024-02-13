#!/bin/bash

####
# funciones 

# cp 
cmd_cp (){
  [[ "$HOME/$1" ]] && command cp -r "$HOME/$1" "./$1"; return

  echo "\e[33mno existe $1\e[0m"
}

# load tha changed files
loadchanged() {
  local dir=$1

  # diferencia que deber ser agregadas 
  if [ -d "./$dir" ]; then 
    rm -rf ./"$dir"
    cmd_cp "$dir"
    echo "archivos $dir actualizado"
    return
  fi 

  # archivos agragado por primera ves
  if [ -d "./$(dirname $dir)" ] ; then
    cmd_cp "$dir"
    echo "agragando $dir"
    return
  fi 

  # diretorio agrado por primera ves
  mkdir -p ./$dir
  cmd_cp "$dir"
  echo "agragando $dir"
}

array=( 
  ".config/i3/" 
  ".config/polybar/"
  ".config/cmus/"
  ".config/dunst/"
  ".config/neofetch/"
  ".config/picom/"
  ".config/ranger/"
  ".config/qterminal.org/"
  ".config/rofi/"
  ".config/wal/"
  ".config/zathura/"
  ".bashrc"
  ".fehbg"
  ".tmux.conf"
  ".local/bin/statusbar/"
  ".local/bin/git_status_promt"
)

for i in "${array[@]}"; do
  diff=$(diff -rs $HOME/"$i" ./"$i" 2>/dev/null || echo "error")

  if [[ $diff == ""  ]]; then
    echo "--------------"
    echo "No hay cambios $i"
    echo "--------------"
  else 
    echo "--------------"
    loadchanged "$i"
    echo "--------------"
  fi
done


