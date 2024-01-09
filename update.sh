#!/bin/bash

# conpy configuration file
mkdir -p .config &>/dev/null

# array of test
array=( 
  ".config/i3" 
  ".config/polybar"
  ".config/cmus"
  ".config/dunst"
  ".config/neofetch"
  ".config/picom"
  ".config/ranger"
  ".config/qterminal.org"
  ".config/rofi"
  ".config/wal"
  ".config/zathura"
  ".bashrc"
  ".local/bin/statusbar/"
)

for i in "${array[@]}"; do
  rm -rf ./"$i"
  mkdir -p ./"$i"
  cp -rf ~/"$i" ./"$i"
done
