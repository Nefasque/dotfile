#!/bin/bash

array=( 
  "i3" 
  "polybar"
  "cmus"
  "dunst"
  "neofetch"
  "picom"
  "ranger"
  "qterminal.org"
  "rofi"
  "wal"
  "zathura"
)

for i in "${array[@]}"; do
  if [[ $(diff -rq ~/.config/"$i" .config/"$i") ]]; then
    echo "Hay cambios"
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
