#!/bin/bash

# conpy configuration file
mkdir -p .config &>/dev/null

# array of test
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
  "../.tmux/"
)


# copy only file with changed 
updates=()
for i in "${array[@]}"; do
  if [[ $(diff -rq ~/.config/"$i" .config/"$i") ]]; then
    echo "update $i"
    rm -rf .config/"$i"
    cp -rf ~/.config/"$i" .config/
    updates+=("$i")
  else 
    cp -rf ~/.config/"$i" .config/
    updates+=("$i")
  fi
done

# case of no update
if [[ ${#updates[@]} == 0 ]]; then
  echo "no updates"
  exit
fi


git add .
git commit -m "update ${updates[*]}"
git push origin master
