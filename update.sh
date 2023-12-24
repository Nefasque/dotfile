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
)

# lipear files
rm -rf .config/*

for file in "${array[@]}"; do
  cp -rfv ~/.config/"$file" .config
done
