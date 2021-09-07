#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

# Pywal Terminal Theme
(cat ~/.cache/wal/sequences &)

# Starship Prompt
eval "$(starship init bash)"
