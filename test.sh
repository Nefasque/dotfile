#!/bin/bash

array=( 
  ".config/i3" 
  ".config/polybar"
  ".config/cmus"
  ".config/dunst"
  ".config/neofetch"
  ".tmux"
  ".config/picom"
  ".config/ranger"
  ".config/qterminal.org"
  ".config/rofi"
  ".config/wal"
  ".config/zathura"
)

for i in "${array[@]}"; do
  if [[ $(diff -rq ~/"$i" ./"$i") ]; then
    echo "Hay cambios"
  else
    echo "No hay cambios"
  fi
done

# dateModificionGuardada=("$(printf "%s\n" "${dateModificionGuardada[@]}" | sort -r)")
#
#
# if [[ $dateModificion != $dateModificionGuardada ]]; then 
#   echo "Hay cambios"
# else
#   echo "No hay cambios"
# fi
