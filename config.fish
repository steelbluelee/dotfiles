# ~/.config/fish/config.fish
set -gx PATH $HOME/.bin $HOME/.local/bin $HOME/.gem/ruby/2.5.0/bin $HOME/go/bin $PATH
set -gx EDITOR nvim
# set fish_key_bindings fish_vi_key_bindings
set fish_key_bindings fish_user_key_bindings
bind -M insert \cf forward-char

set -g theme_display_date no

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
