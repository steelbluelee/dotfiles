function fish_user_key_bindings
  fish_vi_key_bindings
  bind -M insert -m default jk backward-char force-repaint
  bind -M default H beginning-of-line
  bind -M default L end-of-line
  fzf_key_bindings
end
