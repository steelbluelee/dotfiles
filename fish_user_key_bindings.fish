function fish_user_key_bindings
  fzf_key_bindings
  fish_vi_key_bindings
  bind -M insert -m default jk backward-char force-repaint
  bind -M default H beginning-of-line accept-autosuggestion
  bind -M default L end-of-line accept-autosuggestion
end
