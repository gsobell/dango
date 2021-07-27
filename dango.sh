#!/bin/bash

echo "


         ○●
         ●●
         ●○
  ●○○○●○ ●●   ●○○○●●○●   ●○ ○○○●○●      ●○○○●○ ○●    ●○○○●○●
●●     ○●○●         ○●●  ●●○     ●○●  ●●     ○●●   ●●       ●●
●○       ●○   ●○●●○○○●●  ●●       ●●  ●○      ○●●  ●○       ○●
 ●●     ○●●  ●●      ●○  ●○       ●○  ●●     ○●●   ●●       ●●
  ○●○●●○ ●●   ○●○○○○ ●○  ○●       ○●    ○●○●○○●○     ○○●●●●○ 
                                       ●○      ●●
                                         ●●○○○○
" 

if ! command -v gnugo &> /dev/null; then
echo "A one time install of GNU Go is neccesary to continue"   
        sudo pacman -S gnugo  ||    
        sudo apt install gnugo ||
        sudo yum install gnugo ||
        sudo pkg install gnugo ||
        sudo zypper install gnugo ||  
        sudo install gnugo
else sleep 1
fi


# Default settings
level=10
color=black

rules=Japanese
ruleset=--japanese-rules

out=no
outfile=

size=19
komi="6.5"
theme=modern
config=default

# Load user's saved presets
config="~/.config/dango/config"
[[ -f ~/.config/dango/config ]] && . ~/.config/dango && is_config=user

clear

while : 
do

echo -e "\e[1;34m       dango\e[0m"
echo
echo -e ┌"\e[1;5;31m Start Game\e[0m"
echo -e │
echo -e ├────────"\e[1mOptions\e[0m"───────┐ 
echo -e ├"\e[1m Rule Set\e[0;36m $rules   \e[0m(1)"
echo -e ├"\e[1m Color\e[0;36m $color      \e[0m   (2)"
echo -e ├"\e[1m Komi\e[0;36m $komi        \e[0m    (3)"
echo -e ├"\e[1m AI Strength \e[0;36m $level\e[0m     (4)" 
echo -e ├"\e[1m Board size \e[0;36m $size x $size \e[0m(5)"
echo -e ├"\e[1m Save game? \e[0;36m $out \e[0m     (6)"
echo -e ├"\e[1m Theme \e[0;36m $theme \e[0m      (7)"
echo -e ├"\e[1m Save presets? \e[0;36m $is_config \e[0m     (8)"


echo -e "Select a number to edit,\e[0;31m enter\e[0m to start game"
read option

        while true; do
        case $option in
        1) echo "Chose Japanese or Chinese ruleset " 
                select rules in Japanese Chinese; do 
                case $rules in
                Japanese) ruleset="--japanese-rules"; break;;
                Chinese)  ruleset="--chinese-rules";  break;;
                esac
                done
                clear;
                break;;
        2) echo "Choose a color"
                select color in black white; do
                case $color in
                black) break;; # Without the case, it gets
                white) break;; # stuck in loop. Why??
                esac
                done;
                clear;
                break;;
        3) read -r -p "Chose a number of komi "      komi; clear; break;;
        4) read -r -p "Select an AI strength (1-10)"level; clear; break;;
        5) read -r -p " " komi; clear; break;;
        6) read -r -p "Chose path to save game: " outfile ;
                echo $outfile; echo $out;
                [ -z "$outfile" ] && out=No;
                echo $out
                sleep 2
                clear;
                break;;
        7) echo "Choose a theme"
                echo "Color is only fully supported on rxvt"
                echo "
5 . . . . .     
4 . . . . .     
3 . . . . .     
2 . . . . .     
1 . . . . .     
  A B C D E     A B C D E

  Classic       Modern          Color
                
"
                select theme in Classic Modern Color; do
                case $theme in
                Classic) break;;
                Modern) break;;
                Color) break;;
                esac
                done;
                clear;
                break;;
        8) mkdir -p ~/.config/dango
        touch ~/.config/dango/config
        echo "level=$level
              color=$color
              ruleset=$ruleset
              out=$out
              outfile=$outfile
              komi=$komi
              theme=$theme" > ~/.config/dango/config

        echo "Current settings saved"
        sleep 1
        clear;
                break;;
        "") echo "Let the game begin"; break;;
        :q) exit; break;;
        esac
done
done 

echo "you got out of the loop!"

gnugo --level $level --color $color --outfile $outfile --size $size --komi $komi

# `clear
# menu options

# save location

# gnugo | sed -e 's/(/\x1b[32;43m(\x1b[0m/g;s/)/\x1b[32;43m)\x1b[0m/g;s/X /\x1b[30;43m● \x1b[0m/g;s/O/\x1b[97;43m●\x1b[0m/g;s/\./\x1b[30;43m·\x1b[0m/g;s/+/\x1b[30;43m+\x1b[0m/g;s/ /\x1b[30;43m \x1b[0m/g;s/[1-9]/\x1b[30;43m&\x1b[0m/g;s/[1-9][0-9]/\x1b[30;43m&\x1b[0m/g'

#gnugo | sed -e 's/(/\x1b[32;43m(\x1b[0m/g;s/)/\x1b[32;43m)\x1b[0m/g;s/X /\x1b[30;43m● \x1b[0m/g;s/O/\x1b[97;43m●\x1b[0m/g;s/\./\x1b[30;43m·\x1b[0m/g;s/+/\x1b[30;43m+\x1b[0m/g;s/ /\x1b[30;43m \x1b[0m/g;s/[1-9]/\x1b[30;43m&\x1b[0m/g;s/[1-9][0-9]/\x1b[30;43m&\x1b[0m/g'
