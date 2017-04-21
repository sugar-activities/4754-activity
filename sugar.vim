set guioptions-=m
set guioptions-=T

set nocompatible               " be iMproved
filetype off                   " required!

" indentation
set autoindent
set softtabstop=4 shiftwidth=4 expandtab

" visual
highlight Normal ctermbg=black
set background=dark
set cursorline
set t_Co=256

" syntax highlighting
syntax on
"filetype on                 " enables filetype detection
"filetype plugin indent on   " enables filetype specific plugins

" colorpack
" colorscheme inkpot
colo desert 

set guifont=Terminus\ 14

if has("autocmd")
  au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$")
    \| exe "normal! g'\"" | endif
endif
