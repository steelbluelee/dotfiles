# ~/.config/fish/config.fish
set -gx PATH $HOME/.bin $HOME/.local/bin $PATH
set -gx EDITOR nvim
# set fish_key_bindings fish_vi_key_bindings
set fish_key_bindings fish_user_key_bindings
# bind -M insert \cf forward-char

set -g theme_display_date no

umask 022

# set fish_color_escape 'orange' '--bold'
# set fish_color_operator 'orange'

# Solarized Light & Magenta highlight for man page
set -g man_blink -o red
set -g man_bold -o magenta
set -g man_standout -b white 586e75
set -g man_underline -u 586e75

# Solarized Dark & Green highlight
# set -g man_blink -o red
# set -g man_bold -o green
# set -g man_standout -b black 93a1a1
# set -g man_underline -u 93a1a1

# this if for bobthefish theme
# set -g theme_color_scheme gruvbox
set -g theme_color_scheme base16
# set -g theme_color_scheme solarized-dark

set -l BREW_HOME "/home/linuxbrew"
set -l linuxbrew_bin_path "$BREW_HOME/.linuxbrew/bin"
set -l linuxbrew_sbin_path "$BREW_HOME/.linuxbrew/sbin"
set -l linuxbrew_manpath "$BREW_HOME/.linuxbrew/share/man"
set -l linuxbrew_infopath "$BREW_HOME/.linuxbrew/share/info"

contains -- $linuxbrew_bin_path $PATH
  or set -gx PATH $linuxbrew_bin_path $PATH

contains -- $linuxbrew_sbin_path $PATH
  or set -gx PATH $linuxbrew_sbin_path $PATH

contains -- $linuxbrew_manpath $MANPATH
  or set -gx MANPATH $linuxbrew_manpath $MANPATH

contains -- $linuxbrew_infopath $INFOPATH
  or set -gx INFOPATH $linuxbrew_infopath $INFOPATH

set -gx PATH /home/linuxbrew/.linuxbrew/opt/node@10/bin $PATH
