#!/bin/bash
set -eoux pipefail

#adduser sidney sudo
#adduser luwey sudo

apt-get install apache2 zsh curl wget git
#apt-get install expect


#add a way to link the github to server

## oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"