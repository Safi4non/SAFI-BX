#created by Safi4non; CHA DA SCRIPT COPY KRO AGHAY DA PLAAAAR SAT PA SABON WEENZM. 
#bin/bash

clear
echo -e "
\033[1;92m  _________   _____  ___________.___         ______________  ___
 /   _____/  /  _  \ \_   _____/|   |        \______   \   \/  /
 \_____  \  /  /_\  \ |    __)  |   |  ______ |    |  _/\     / 
 /        \/    |    \|     \   |   | /_____/ |    |   \/     \ 
/_______  /\____|__  /\___  /   |___|         |______  /___/\  \
        \/         \/     \/                         \/      \_/
\033[1;91m<═══\033[1;41m\033[1;97m Created by Safi4non \033[;0m\033[1;91m═══>\033[1;92m"

grn="\e[92m"

echo
echo -e $grn"LG SBR WKA SHI DA PKG DRLA INSTALL KM YAAR"
echo
apt update -y
echo -e $grn'PKG UPDATE SHO'
apt upgrade -y
echo -e $grn'PKG UPGRADE SHO'
termux-setup-storage
echo -e $grn'PERMISSION WRTA ALLOW KA'
apt install tor -y
echo -e $grn'TOR PKG INSTALL SHO'
apt install python -y
echo -e $grn'PYTHON PKG INSTALL SHO'
apt install wget -y
echo -e $grn'WGET PKG INSTALL SHO'
pip install --upgrade pip
echo -e $grn
pip install lolcat
echo -e $grn'LOLCAT PKG INSTALL SHO'
pip install bs4
echo -e $grn'BS4 PKG INSTALL SHO'
pip install requests
echo -e $grn'REQUESTS PKG INSTALL SHO'
pip install requests[socks]
echo -e $grn
pip install requests --upgrade
echo -e $grn
pip install stem
echo -e $grn'STEM PKG INSTALL SHO'
pip install instagram-py
echo -e $grn'INSTA PY PKG INSTALL SHO'
pip install instagram-py --upgrade
echo -e $grn
mv instapy-config.json /$HOME
rm /data/data/com.termux/files/usr/etc/tor/torrc
mv torrc /data/data/com.termux/files/usr/etc/tor
echo -e $grn
echo $grn'PKGS INSTALL SHO BS \nSAFI-BX BA WS START SHI MEHRABANI..'
python SAFI-BX.py
