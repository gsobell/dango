#!/bin/bash

if [ "$1" == "-h" ]; then # flags
        echo "$(basename $0) All options are configured from within, no flags are needed."
        exit 0
elif [ "$1" == "--help" ]; then
        echo "$(basename $0) All options are configured from within, no flags are needed."
        exit 0
elif [ "$1" == "-V" ]; then
        echo dango version 0.2-alpha 
fi

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
# If the splash screen doesn't render properly, it means the ASCII board probably won't either.

if ! command -v gnugo &> /dev/null; then
echo "A one time install of GNU Go is necessary to continue"
        sudo pacman -S gnugo      || # Arch
        sudo apt install gnugo    || # Debian
        sudo yum install gnugo    || # Red Hat
        sudo pkg install gnugo    || # Termux
        sudo zypper install gnugo || # OpenSuse
echo "GNU Go has failed to install, please search on your distro's package manager, or consult it/'s wiki."
else sleep 1
fi

# Default settings

ruleset=--japanese-rules
rules=Japanese
level=10
color=black
komi="6.5"
outdir=$HOME/.cache/dango/"$(date +%F) $(date +%X)"
size=19
theme=Modern
config=default
                
mkdir "$HOME/.cache/dango"
mkdir "$HOME/.config/dango"

# Load user's saved presets
[[ -f ~/.config/dango/config ]] && . ~/.config/dango/config && is_config=Loaded

if [ -n "$outdir" ] # Checks if output is loaded from config
then out=Yes
else out=No
fi

clear

while : # Start of menu 
do

echo -e "\e[1;34m          dango\e[0m"
echo -e  
echo -e " ┌───────\e[1mOptions\e[0m───────┐ "
echo -e 1├"\e[1m Rule Set\e[0;36m $rules   \e[0m"
echo -e 2├"\e[1m Color\e[0;36m $color      \e[0m"
echo -e 3├"\e[1m Komi\e[0;36m $komi        \e[0m"
echo -e 4├"\e[1m AI Strength \e[0;36m $level\e[0m" 
echo -e 5├"\e[1m Board size \e[0;36m $size x $size \e[0m"
echo -e 6├"\e[1m Save game? \e[0;36m $out \e[0m"
echo -e 7├"\e[1m Theme \e[0;36m $theme \e[0m"
echo -e 8├"\e[1m Config Options \e[0;36m $is_config \e[0m"
echo

echo -e "Select a number to edit,\e[1;5;31m enter\e[0m to\e[1;31m start game \e[0m"

read -r option
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
                select color in black white; do clear
                break 2
                done;;
        3) read -r -p "Chose a number of komi "      komi; clear; break;;
        4) read -r -p "Select an AI strength: " level; 
                if   [ "$level" -ge 11 ]; then
                echo "Please choose a value less than 10"
                elif [ "$level" -eq 0  ]; then
                echo "Please choose a value greater than 0"
                else clear; break;        
                fi;;

        5) read -r -p "Chose a board size: " size; clear; break;;
        6) read -r -p "Chose path to save game: " outdir ;
                if [ -n "$outdir" ]; # Unsaved games are cached 
                then out=Yes && echo "Game will be saved to: $outdir"; 
                else out=No  && echo "Game will not be saved.";
                fi;
                sleep 2;
                clear;
                break;;
        7) echo "Choose a theme"
                echo "Color is only fully supported on rxvt"
                echo -e "
                
 5 . . . . .    5 · · · · ·   \e[30;43m 5 · · · · · \e[0m
 4 . . . O .    4 · · · ○ ·   \e[30;43m 4 · · · \e[97;43m● \e[30;43m· \e[0m
 3 . . . O .    3 · · · ○ ·   \e[30;43m 3 · · · \e[97;43m● \e[30;43m· \e[0m
 2 . X . . .    2 · ● · · ·   \e[30;43m 2 · ● · · · \e[0m
 1 . . X . .    1 · · ● · ·   \e[30;43m 1 · · ● · · \e[0m
   A B C D E      A B C D E   \e[30;43m   A B C D E \e[0m

    Classic        Modern         Color
                
"
                select theme in Classic Modern Color; do
                break
                done;
                clear;
                break;;
        8|:w) echo Save current config, or restore default?
        select con in Save Default; do
        case $con in
        
              Save) mkdir -p ~/.config/dango
              touch ~/.config/dango/config
        echo "ruleset=$ruleset
              color=$color
              komi=$komi
              level=$level
              size=$size
              outdir=$outdir
              theme=$theme" > ~/.config/dango/config

        echo "Current settings saved"
        sleep 1
        break;;
        
               Default) rm  ~/.config/dango/config
               [[ -f "$HOME/.config/dango/config" ]] &&
               rm  ~/.config/dango/config
               . "$(dirname $(readlink -f $0))" && is_config=Default
               break;;
        esac
        done 
        clear;
        break;;
        
        "") break 2;;
        q|:q|exit) exit; break;;
        esac

done # End of case
done # End of menu

clear

#Start GNU Go, dependent on selected color, default=modern

case $theme in
        Classic) gnugo --mode ascii --boardsize $size --komi $komi --level $level --color $color --outfile "$outdir" ;;
        Modern)  gnugo --mode ascii --boardsize $size --komi $komi --level $level --color $color --outfile "$outdir" | sed -e 's/X/●/g;s/O/○/g;s/\./·/g';;
        Color)   gnugo | sed -e 's/(/\x1b[32;43m(\x1b[0m/g;s/)/\x1b[32;43m)\x1b[0m/g;s/X /\x1b[30;43m● \x1b[0m/g;s/O/\x1b[97;43m●\x1b[0m/g;s/\./\x1b[30;43m·\x1b[0m/g;s/+/\x1b[30;43m+\x1b[0m/g;s/ /\x1b[30;43m \x1b[0m/g;s/[1-9]/\x1b[30;43m&\x1b[0m/g;s/[1-9][0-9]/\x1b[30;43m&\x1b[0m/g'
                ;;
esac

echo "Play again? (y/n)" 
read YN
case $YN in
y|Y|yes) sh "$0";;
n|N|No) break;;
esac

clear
echo "Thank you for the game."
sleep 1
clear
echo "See you!"
sleep 1
clear
exit
