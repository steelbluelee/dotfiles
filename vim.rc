" $HOME/.config/nvim/init.vim
" $HOME/.vimrc

" if &shell =~# 'fish$'
"     set shell=sh
" endif
" set pythonthreedll=$HOME . '\scoop\apps\python\current\python3.dll'
set fileformats=unix,dos

let g:ale_vim_vint_executable='vint'
let g:dbext_default_profile_dragonStack='type=pgsql:host=localhost:user=node_user:dbname=dragonstack'

set guifont=Source\ Code\ Pro\ for\ Powerline:h12:cANSI

augroup project_dragonstack
    autocmd!
    autocmd BufRead */dragonstack/backend/bin/sql/* DBSetOption profile=dragonStack
augroup END

set completefunc=syntaxcomplete#Complete

" open the current windows in a new tab.
" this is like maximizing the current windows.
function! OpenCurrentAsNewTab()
    let l:currentPos = getcurpos()
    tabedit %
    call setpos('.', l:currentPos)
endfunction
nnoremap t% :call OpenCurrentAsNewTab()<CR>
nnoremap td :tabclose<CR>
nnoremap <Leader>tn :tabnew<CR>
nnoremap tp :tabprevious<CR>
nnoremap tn :tabnext<CR>
nnoremap <A-t><A-t> :tabnext<CR>

" set omnifunc=syntaxcomplete#Complete
set completeopt-=preview
set completeopt+=menuone
set completeopt+=noinsert
set completeopt+=noselect
" set dictionary+=/usr/share/dict/words
" set completeopt=menu

if filereadable('./dict.txt')
    " set dictionary+=expand("%:p:h")
    let &dictionary=expand('%:p:h') . '/dict.txt'
    set complete+=k
endif

let g:UltiSnipsExpandTrigger = '<f5>'        " Do not use <tab>
let g:UltiSnipsJumpForwardTrigger = '<C-i>'  " Do not use <c-j>


let g:mucomplete#chains = {}
let g:mucomplete#chains.markdown = ['keyn', 'dict', 'uspl']
let g:mucomplete#chains.vim = ['path', 'cmd', 'keyn']
let g:mucomplete#chains.default = [ 'ulti', 'incl', 'omni', 'path']
let g:mucomplete#chains.sql = [ 'incl', 'user', 'omni', 'path']
let g:mucomplete#completion_delay = 0

imap <tab> <plug>(MUcompleteFwd)
imap <S-tab> <plug>(MUcompleteBwd)
" imap <unique> <tab> <plug>(MUcompleteFwd)
" imap <unique> <S-tab> <plug>(MUcompleteBwd)
let g:mucomplete#enable_auto_at_startup = 1

augroup auto_ch_dir
    autocmd!
    " autocmd InsertEnter * let save_cwd = getcwd() | set autochdir
    " autocmd InsertLeave * set noautochdir | execute 'cd' fnameescape(save_cwd)
    autocmd InsertEnter * let save_cwd = getcwd() | lcd %:p:h
    autocmd InsertLeave * execute 'cd' fnameescape(save_cwd)
augroup END

" nnoremap <A-l><A-n> :lnext<CR>
" nnoremap <A-l><A-p> :lprevious<CR>
" nnoremap <A-l><A-f> :lfirst<CR>
" nnoremap <A-l><A-l> :llast<CR>
nnoremap <A-c><A-l> :let g:which_navigator="linter"<CR>
nnoremap <A-c><A-c> :let g:which_navigator="quickfix"<CR>
" function! ToggleLinterQuickFixWindow()
"
" endfunction
let g:which_navigator='linter'
function! GoToTheFirst()
    if g:which_navigator ==# 'quickfix'
        cfirst
    else
        lfirst
    endif
endfunction
function! GoToTheNext()
    if g:which_navigator ==# 'quickfix'
        cnext
    else
        lnext
    endif
endfunction
function! GoToThePrevious()
    if g:which_navigator ==# 'quickfix'
        cprevious
    else
        lprevious
    endif
endfunction
function! GoToTheLast()
    if g:which_navigator ==# 'quickfix'
        clast
    else
        llast
    endif
endfunction

nnoremap <A-f> :call GoToTheFirst()<CR>
nnoremap <A-j> :call GoToTheNext()<CR>
nnoremap <A-k> :call GoToThePrevious()<CR>
nnoremap <A-l> :call GoToTheLast()<CR>

" vim-plug : vim plugins                 {{{
""""""""""""""""""""""""""""""""""""""""""""""""
if has('nvim')
    call plug#begin('~/.nvim/vim-plug')
else
    call plug#begin('~/.vim/vim-plug')
endif

" common
Plug 'https://github.com/scrooloose/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'
Plug 'https://github.com/skywind3000/asyncrun.vim'
Plug 'https://github.com/vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'https://github.com/tpope/vim-fugitive'
Plug 'https://github.com/christoomey/vim-tmux-navigator'
Plug 'https://github.com/airblade/vim-gitgutter'
Plug 'https://github.com/benmills/vimux'
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'
Plug 'https://github.com/moll/vim-bbye'
Plug 'https://github.com/jlanzarotta/bufexplorer'
" Plug 'kassio/neoterm'
Plug 'https://github.com/szw/vim-maximizer'
Plug 'ryanoasis/vim-devicons'

" colors
Plug 'https://github.com/altercation/vim-colors-solarized'
Plug 'https://github.com/vim-scripts/wombat256.vim'
Plug 'https://github.com/nanotech/jellybeans.vim'
Plug 'https://github.com/NLKNguyen/papercolor-theme'
Plug 'chriskempson/base16-vim'
Plug 'https://github.com/tyrannicaltoucan/vim-quantum'
Plug 'https://github.com/baskerville/bubblegum'
Plug 'https://github.com/chriskempson/vim-tomorrow-theme'
Plug 'rakr/vim-one'
Plug 'https://github.com/endel/vim-github-colorscheme'
Plug 'https://github.com/scheakur/vim-scheakur'
Plug 'https://github.com/tomasr/molokai'

" programming
Plug 'https://github.com/w0rp/ale'
" Plug 'https://github.com/honza/vim-snippets'
" Plug 'https://github.com/Yggdroot/indentLine'
Plug 'https://github.com/nathanaelkane/vim-indent-guides'
" Plug 'https://github.com/Raimondi/delimitMate'
Plug 'https://github.com/jiangmiao/auto-pairs'
Plug 'https://github.com/majutsushi/tagbar'
" Plug 'https://github.com/ervandew/supertab'
Plug 'https://github.com/SirVer/ultisnips'
Plug 'https://github.com/scrooloose/nerdcommenter'
" if has('nvim')
"     Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
" else
"     Plug 'Shougo/deoplete.nvim'
"     Plug 'roxma/nvim-yarp'
"     Plug 'roxma/vim-hug-neovim-rpc'
" endif
" Plug 'autozimu/LanguageClient-neovim', {
"     \ 'branch': 'next',
"     \ 'do': 'bash install.sh',
"     \ }

Plug 'https://github.com/lifepillar/vim-mucomplete'

Plug 'https://github.com/tpope/vim-surround'
Plug 'https://github.com/tpope/vim-repeat'

" ncm2 : autocomplete
" Plug 'ncm2/ncm2'
" Plug 'roxma/nvim-yarp'
"
" Plug 'ncm2/ncm2-bufword'
" Plug 'ncm2/ncm2-tmux'
" Plug 'ncm2/ncm2-path'

" if has('nvim')
"     Plug 'eed3si9n/LanguageClient-neovim', { 'do': ':UpdateRemotePlugins' }
" else
"     Plug 'autozimu/LanguageClient-neovim', {
"         \ 'branch': 'next',
"         \ 'do': 'bash install.sh',
"         \ }
" endif
" Plug 'prabirshrestha/async.vim'
" Plug 'prabirshrestha/vim-lsp'


" languages
" scala
if has('nvim')
    Plug 'ensime/ensime-vim', { 'do': ':UpdateRemotePlugins' }
else
    Plug 'ensime/ensime-vim'
endif

Plug 'https://github.com/derekwyatt/vim-scala'
Plug 'https://github.com/ktvoelker/sbt-vim'

" python
" Plug 'zchee/deoplete-jedi'

" html, css, javascript, json
Plug 'mattn/emmet-vim'
Plug 'pangloss/vim-javascript'
Plug 'mxw/vim-jsx'
Plug 'prettier/vim-prettier', {
  \ 'do': 'npm install',
  \ 'for': ['javascript', 'typescript', 'css', 'less', 'scss', 'json', 'graphql', 'markdown', 'vue', 'yaml', 'html'] }
" Plug 'prettier/vim-prettier', { 'do': 'npm install' }
" Plug 'prettier/vim-prettier'
Plug 'ternjs/tern_for_vim', { 'do': 'npm install'}
" Plug 'https://github.com/epilande/vim-react-snippets'
Plug 'https://github.com/mlaursen/vim-react-snippets'
Plug 'https://github.com/epilande/vim-es2015-snippets'
" Plug 'https://github.com/steelsojka/deoplete-flow'
" Plug 'carlitux/deoplete-ternjs'
" Plug 'https://github.com/flowtype/vim-flow'

" fish shell script
Plug 'https://github.com/dag/vim-fish'

" json
Plug 'https://github.com/elzr/vim-json'

" markdown
" Plug 'https://github.com/shime/vim-livedown'
" Plug 'https://github.com/suan/vim-instant-markdown'
" Plug 'https://github.com/mgor/vim-markdown-grip'
if has('nvim')
    Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() }}
else
    Plug 'https://github.com/iamcco/markdown-preview.vim'
endif

" database : postgresql,
Plug 'https://github.com/vim-scripts/dbext.vim'
Plug 'https://github.com/lifepillar/pgsql.vim'
Plug 'b4b4r07/vim-sqlfmt'
Plug 'https://github.com/vim-scripts/SQLUtilities'
Plug 'https://github.com/vim-scripts/Align'

call plug#end()
"  }}}

" VI 기본 설정                               {{{
""""""""""""""""""""""""""""""""""""""""""""""""

" This may or may not be needed
" set t_Co=256
set termguicolors

" colorscheme molokai
" colorscheme wombat256mod
" colorscheme solarized
" colorscheme jellybeans
" colorscheme bubblegum-256-light
" colorscheme Tomorrow
" colorscheme one
colorscheme PaperColor
set background=light
" set background=dark

" <leader> key를 ,로 변경
let mapleader=','

" <localmapleader>를 ;으로 변경
let maplocalleader=';'
" ;;를 ;로 매핑
nnoremap ;; ;

" <space>를 za로 바인딩 :
" nnoremap <Enter> za

" jk를 <ESC>로 바인딩. jk를 문자열을 입력하려면
" j 입력 후 1초 기다리면 됨
inoremap jk <ESC>

" 라인수를 표시해 줍니다
set number
set relativenumber

" 각 파일에 해당하는 문법(Syntax)를 적용시켜줍니다.
" C나 Java등 사용시 색상등..
syntax on
filetype plugin indent on

" 파일 편집시 undo 할수 있는 최대 횟수 설정
set history=100

" 함수 닫기표시
set showmatch

" 타이핑시 마우스 커서 감추기
set mousehide

" 최소한 2줄 이하로는 자동 스크롤
set scrolloff=2

" ESC키를 누르면 한글 모드가 해제
" 입력모드에서 이전 언어 설정 모드 유지
" ESC를 jk로 바인딩했기 때문에 의미 없음?
inoremap <ESC> <ESC>:set imdisable<CR>
nnoremap i :set noimd<CR>i
nnoremap I :set noimd<CR>I
nnoremap a :set noimd<CR>a
nnoremap A :set noimd<CR>A
nnoremap o :set noimd<CR>o
nnoremap O :set noimd<CR>O

" enable filetype detection, plus loading of filetype plugins
filetype plugin on

" Status Lines -> airline 사용
" set laststatus=2
" if has("statusline")
"  set statusline=%<%f\ %h%m%r%=[%{\"\".(&fenc==\"\"?&enc:&fenc).((exists(\"+bomb\")\ &&\ &bomb)?\",B\":\"\").\"\\"}:%y]%k\ %-14.(%l,%c/%L%)
"  set statusline=%<%f\ %h%m%r%=%{\"[\".(&fenc==\"\"?&enc:&fenc).((exists(\"+bomb\")\ &&\ &bomb)?\",B\":\"\").\"]\ \"}%y%k\ %-14.(%l,%c/%L%)
" endif

" 경고 소리와 경고 화면 깜빡임을 끈다.
" set visualbell
set noerrorbells visualbell t_vb=
augroup turn_off_visualbell
    autocmd!
    autocmd GUIEnter * set visualbell t_vb=
augroup END

" Automatically Quit Vim if Actual Files are Closed
function! CheckLeftBuffers()
  if tabpagenr('$') == 1
    let i = 1
    while i <= winnr('$')
      if getbufvar(winbufnr(i), '&buftype') ==? 'help' ||
          \ getbufvar(winbufnr(i), '&buftype') ==? 'quickfix' ||
          \ exists('t:NERDTreeBufName') &&
          \   bufname(winbufnr(i)) == t:NERDTreeBufName ||
          \ bufname(winbufnr(i)) ==? '__Tag_List__'
        let i += 1
      else
        break
      endif
    endwhile
    if i == winnr('$') + 1
      qall
    endif
    unlet i
  endif
endfunction
augroup close_vim
    autocmd!
    autocmd BufEnter * call CheckLeftBuffers()
augroup END

" }}}

" 기본키 매핑                               {{{
"""""""""""""""""""""""""""""""""""""""""""""""
" 윈도우 네비게이션 키 매핑
" vim-tmux-navigator 설정과 충돌함
noremap <C-h> <C-w>h
noremap <C-j> <C-w>j
noremap <C-k> <C-w>k
noremap <C-l> <C-w>l

" H, L 라인의 첫번째 컬럼, 마지막 컬럼
nnoremap H 0
nnoremap L $

" 대문자로 변경
inoremap <c-u> <esc>moviwU`oa
nnoremap <c-u> moviwU`o

" buffers
nnoremap <C-n> :bnext<CR>
nnoremap <C-p> :bprev<CR>

" match trailing spaces as Error
nnoremap <leader>w :match Error /\v +$/<cr>
nnoremap <leader>W :match none<cr>

" resizing window size
nnoremap + <C-w>+
nnoremap - <C-w>-
nnoremap <M-+> <C-w>>
nnoremap <M--> <C-w><

" tab navigation
nnoremap <leader>tn :tabnext<CR>
nnoremap <leader>tp :tabnext<CR>

" save
nnoremap <C-s><C-s> :w<CR>
inoremap <C-s><C-s> <ESC>:w<CR>
nnoremap <C-s><C-g> :Gwrite<CR>
inoremap <C-s><C-g> <ESC>:Gwrite<CR>

" copy & paste
vnoremap <leader>y "+y
nnoremap <leader>p o<ESC>"+p
nnoremap <leader>P O<ESC>"+P

" move lines
nnoremap <A-d> :m .+1<CR>==
nnoremap <A-u> :m .-2<CR>==
vnoremap <A-d> :m '>+1<CR>gv=gv
vnoremap <A-u> :m '<-2<CR>gv=gv

" omnifunc
inoremap <leader><leader> <C-x><C-o>

" toggle fold
nnoremap <Space><Space> za

" complete, completion
inoremap <C-k> <C-x><C-k>

" tabedit current buffer && close the current tab
" this setup is used instead of maximizing current
" splited window  -- <C-w> + |, <C-w> + _
nnoremap <Leader>te :tabedit %<CR>
nnoremap <Leader>tc :tabclose<CR>
nnoremap <Leader>tn :tabnew<CR>

" 
inoremap <C-f> <Esc>A
" }}}

" terminal realted setup                     {{{
" """"""""""""""""""""""""""""""""""""""""""""""
tnoremap <leader>jk <C-\><C-n>
tnoremap <C-h> <C-\><C-N><C-w>h
tnoremap <C-j> <C-\><C-N><C-w>j
tnoremap <C-k> <C-\><C-N><C-w>k
tnoremap <C-l> <C-\><C-N><C-w>l
tnoremap <A-m><A-m> <C-\><C-N>:MaximizerToggle<CR>a
"  }}}

" preview window setup                       {{{
" """"""""""""""""""""""""""""""""""""""""""""""
set previewheight=10
nnoremap <leader>x :pclose<CR>
" augroup completion_preview_close
"     autocmd!
"     autocmd CompleteDone * if !&previewwindow && &completeopt =~ 'preview' | silent! pclose | endif
" augroup END
"  }}}

" buffer realted setup                       {{{
" """"""""""""""""""""""""""""""""""""""""""""""
let g:bufExplorerDefaultHelp=1 " Show default help.
nnoremap <leader>bb :BufExplorer<cr>
nnoremap <leader>bw :Bwipeout<cr>
"  }}}

" search related setup                       {{{
" """"""""""""""""""""""""""""""""""""""""""""""
" search key mapping for search to use
" very magical regular expression
" nnoremap / :set hlsearch<cr>/
nnoremap / :set hlsearch<CR>/\v
onoremap / /\v
vnoremap / /\v
nnoremap ? :set hlsearch<CR>?\v
onoremap ? ?\v
vnoremap ? ?\v

" enable incsearch
set incsearch

" hlsearch key mappings
" nnoremap <leader>h :set hlsearch<cr>
" nnoremap <leader>H :set nohlsearch<cr>
nnoremap <silent><expr> <Leader>h (&hls && v:hlsearch ? ':nohlsearch' : ':set hlsearch')."\n"
"  }}}

" grep                                       {{{
" """"""""""""""""""""""""""""""""""""""""""""""
cnoremap grep AsyncRun grep -nH -R
" cnoremap grep AsyncRun grep -nH --exclude-dir=.{stack-work} -R
" nnoremap <leader>gw :execute 'AsyncRun grep -nH -R ' .
"     \ '--exclude-dir=.{stack-work} ' .
"     \ shellescape(expand("<cWORD>")) .
"     \ " ."<cr>:copen<cr>
" nnoremap <leader>g :set operatorfunc=GrepOperator<cr>g@
" vnoremap <leader>g :<c-u>call GrepOperator(visualmode())<cr>
"
" function! GrepOperator(type)
"     echom a:type
" endfunction
" }}}

" encoding                                   {{{
" """"""""""""""""""""""""""""""""""""""""""""""
" 기본 엔코딩 : utf-8
set encoding=utf-8
scriptencoding utf-8
set fileencodings=utf-8,cp949
" set langmenu=cp949
" set termencoding=euc-kr
" language messages en_US
" set langmenu=en_US.UTF-8
" language messages en_US.UTF-8

" set enc=utf-8
set fileencoding=utf-8
set fileencodings=ucs-bom,utf-8,cp949,latin1
set nobomb

" let $LANG = 'ko_KR.UTF-8'
" source $VIMRUNTIME/delmenu.vim
" source $VIMRUNTIME/menu.vim
" }}}

" vimrc 파일 & vimscript 관련 설정           {{{
" """"""""""""""""""""""""""""""""""""""""""""""
" Vimscript foldmethod : Vimscript 접기 설정
augroup filetype_vim
    autocmd!
    autocmd FileType vim setlocal foldmethod=marker
augroup END

" key binding and sourcing for opening vimrcfile
" vimrc 파일 열기 & 적용
if has('win32')
    if has('nvim')
        nnoremap <leader>ev :e ~/AppData/Local/nvim/init.vim<cr>
        nnoremap <leader>sv :source ~AppData/Local/nvim/init.vim<cr>
    else
        nnoremap <leader>ev :e ~/_vimrc<cr>
        nnoremap <leader>sv :source ~/_vimrc<cr>
    endif
else
    if has('nvim')
        nnoremap <leader>ev :e ~/.config/nvim/init.vim<cr>
        nnoremap <leader>sv :source ~/.config/nvim/init.vim<cr>
    else
        nnoremap <leader>ev :e ~/.vimrc<cr>
        nnoremap <leader>sv :source ~/.vimrc<cr>
    endif
endif

" }}}

" 들여쓰기, 탭 : indentation, Tab 설정       {{{
" """"""""""""""""""""""""""""""""""""""""""""""
" 자동 들여쓰기
set autoindent

" backspace 설정
" backspace over everything in insert mode
" set backspace=indent,eol,start
" backspace over indent in insert mode
set backspace=indent

" 들여쓰기 폭을 정합니다.
set shiftwidth=4

" 탭의 폭을 정합니다.
set tabstop=4

" tap을 누르면 스페이스 4개를 넣는다.
set softtabstop=4

" set shiftround

" 탭을 스페이스로 대체합니다.
set expandtab

" C의 구문에 맞게 들여쓰기 합니다
set cindent

" toggle cursorcolumn/cursorline
nnoremap <Space>cc :call ToggleCursorColumn()<CR>
nnoremap <Space>cl :call ToggleCursorColumn()<CR>
function! ToggleCursorColumn()
  if &cursorcolumn == 1
    set cursorcolumn!
    set cursorline!
    echo 'cursorcolumn/cursorline disabled'
  else
    set cursorcolumn
    set cursorline
    echo 'cursorcolumn/cursorline enabled'
  endif
endfunction
" }}}

" quickfix Window 설정                       {{{
" """"""""""""""""""""""""""""""""""""""""""""""
" Quickfix Window Toggle
nnoremap <leader>q :call QuickFixToggleC()<cr>

function! QuickFixToggleC()
    for l:i in range(1, winnr('$'))
        let l:bnum = winbufnr(l:i)
        if getbufvar(bnum, '&buftype') ==? 'quickfix'
            cclose
            return
        endif
    endfor

    copen
endfunction

" QuickFix Window Navigation 키 매핑
nnoremap <Space>j :cnext<cr>
nnoremap <Space>k :cprevious<cr>

" Winodws에서는 cp949를 utf-8로 바꿈
" Quickfix Window 매뉴얼을 참고함.
" function! QfMakeConv()
"     let qflist = getqflist()
"     echom &filetype
"    " for i in qflist
"    "    let i.text = iconv(i.text, "cp949", "&encoding")
"    " endfor
"    " call setqflist(qflist)
"     call setqflist([&filetyp])
" endfunction
"
" if has("win32")
"     augroup QfMakeConvForWindows
"         autocmd!
"         autocmd QuickfixCmdPost make call QfMakeConv()
"     augroup END
" endif
" }}}

"  외부 인터프린터 언어 인터페이스 설정       {{{
" """""""""""""""""""""""""""""""""""""""""""""""
if has('win32') && !has('nvim')
     " let &pythonthreedll=$HOME . '\scoop\apps\python\current\python37.dll'
set pythonthreedll=c:\Users\steel\scoop\apps\python\3.7.2\python37.dll
set pythondll=C:\Users\steel\scoop\apps\python27\2.7.16\python27.dll
"     let &rubydll=$HOME . '\vimfiles\interpreters\ruby2.2.6\bin\msvcrt-ruby220.dll'
"     let &luadll=$HOME . '\vimfiles\interpreters\lua5.3.3\lua53.dll'
endif
" }}}

" Menu, ScrollBar, ToolBar 설정              {{{
" """"""""""""""""""""""""""""""""""""""""""""""
" Menu, ScrollBar, ToolBar 모두 없앤다.
let &guioptions='g'

" Menu, ScrollBar, ToolBar 표시/숨기기 토글 함수
function! ToggleMenuScrollBarToolBar()
    if &guioptions ==# 'g'
        let &guioptions = 'gmrLtT'
    else
        let &guioptions = 'g'
    endif
endfunction
"}}}

" airline                                    {{{
" """"""""""""""""""""""""""""""""""""""""""""""
if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif
" let g:airline_left_sep = '▸'
" let g:airline_right_sep = '◂'
" let g:airline_right_sep = '◀'
let g:airline_left_sep = ''
let g:airline_left_alt_sep = ''
let g:airline_right_sep = ''
let g:airline_right_alt_sep = ''
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#fnamemod = ':t'
" let g:airline#extensions#tabline#left_sep = ' '
let g:airline#extensions#tabline#left_sep = ''
let g:airline#extensions#tabline#left_alt_sep = '|'

let g:airline_powerline_fonts = 1

" let g:airline_theme='wombat'
" let g:airline_theme='molokai'
" let g:airline_theme='papercolor'
" let g:airline_theme='sol'
let g:airline_theme='luna'
" let g:airline_theme='one'
" let g:airline_theme='base16'
" }}}

" vim maximizer setup                      {{{
" """"""""""""""""""""""""""""""""""""""""""""""
let g:maximizer_default_mapping_key = '<A-m><A-m>'
" }}}

" AsyncRun 설정                              {{{
" """"""""""""""""""""""""""""""""""""""""""""""
" cjk에서 텍스트가 깨지는 경우 아래를 설정
" let g:asyncrun_encs = 'gbk'
" }}}

"  NERDTree 설정                              {{{
" """""""""""""""""""""""""""""""""""""""""""""""
" NERTTree 토글 키 바인딩
nnoremap <leader>n :NERDTreeToggle<CR>
let NERDTreeAutoDeleteBuffer = 1
" autocmd vimenter * NERDTree
" }}}

"  mucomplete                               {{{
" """""""""""""""""""""""""""""""""""""""""""""""
inoremap <silent> <expr> <cr>
      \ mucomplete#ultisnips#expand_snippet("\<cr>")

let g:AutoPairsMapSpace = 0
imap <silent> <expr> <space> pumvisible()
    \ ? "<space>"
    \ : "<c-r>=AutoPairsSpace()<cr>"

" }}}

"  tmux / vimux 설정                          {{{
" """""""""""""""""""""""""""""""""""""""""""""""
" Repeat last command in the next tmux pane.
" nnoremap <Leader>r :call <SID>TmuxRepeat()<CR>
"
" function! s:TmuxRepeat()
" silent! exec "!tmux select-pane -l && tmux send up enter && tmux select-pane -l"
" redraw!
" endfunction
"
" inoremap <C-s> <Esc>:w<CR>:call <SID>TmuxRepeat()<CR>a
" noremap  <C-s> :w<CR>:call <SID>TmuxRepeat()<CR>

" Prompt for a command to run
nnoremap <Leader>vp :VimuxPromptCommand<CR>
nnoremap <C-s>c :VimuxPromptCommand<CR>

" Run last command executed by VimuxRunCommand
nnoremap <Leader>vl :call VimuxRunLastCommand()<CR>
nnoremap <C-s><C-v> :write<CR>:call VimuxRunLastCommand()<CR>
inoremap <C-s><C-v> <Esc>:write<CR>:call VimuxRunLastCommand()<CR>

" Inspect runner pane
nnoremap <Leader>vi :VimuxInspectRunner<CR>

" Close vim tmux runner opened by VimuxRunCommand
nnoremap <Leader>vq :VimuxCloseRunner<CR>

" Interrupt any command running in the runner pane
nnoremap <Leader>vx :VimuxInterruptRunner<CR>

" Zoom the runner pane (use <bind-key> z to restore runner pane)
nnoremap <Leader>vz :call VimuxZoomRunner()<CR>

" Run last command and zoom the runner pane
" inoremap <C-s> <Esc>:w<CR>:call VimuxRunLastCommand()<CR>:call VimuxZoomRunner()<CR>
" nnoremap <C-s><C-s> :w<CR>:call VimuxRunLastCommand()<CR>:call VimuxZoomRunner()<CR>

" If text is selected, save it in the v buffer and send that buffer it to tmux
function! VimuxSlime()
      call VimuxSendText(@v)
      call VimuxSendKeys('Enter')
endfunction

vnoremap <Leader>vs "vy :call VimuxSlime()<CR>
" vnoremap <Leader>vs "vy :call VimuxSlime()<CR>:call VimuxZoomRunner()<CR>

nnoremap <C-s>b vip"vy:call VimuxSlime()<CR>
nnoremap <C-s>f ggVG"vy:call VimuxSlime()<CR>

let g:VimuxHeight = '5'

let g:VimuxRunnerType = 'pane'
" let g:VimuxRunnerType = 'window'
" }}}

" LanguageClient : LanguageClient-neovim, vim-lsp 설정{{{
" """""""""""""""""""""""""""""""""""""""""""""""""""""""
" set signcolumn=yes
" if has('nvim')
" let g:LanguageClient_autoStart = 1
" let g:LanguageClient_serverCommands = {
"     \ 'javascript': ['flow-language-server', '--stdio'],
"     \ 'scala': ['node', expand('~/.bin/sbt-server-stdio.js')],
"     \ }
" let g:LanguageClient_serverCommands = {
"     \ 'javascript': ['javascript-typescript-stdio'],
"     \ 'scala': ['node', expand('~/.bin/sbt-server-stdio.js')],
"     \ }
" nnoremap <silent> gd :call LanguageClient_textDocument_definition()<CR>
" else
    " autocmd User lsp_setup call lsp#register_server({
    "                 \ 'name': 'scala',
    "                 \ 'cmd': {server_info->['sbt-server-stdio.js']},
    "                 \ 'whitelist': ['scala'],
    "                 \ })
    " let g:lsp_signs_enabled = 1         " enable signs
    " let g:lsp_diagnostics_echo_cursor = 1 " enable echo under cursor when in normal mode
    " let g:lsp_signs_error = {'text': '✗'}
    " let g:lsp_signs_warning = {'text': '‼', 'icon': '/path/to/some/icon'} " icons require GUI
    " let g:lsp_signs_hint = {'icon': '/path/to/some/other/icon'} " icons require GUI
" endif
" }}}

"  deoplete 설정                           {{{
" """""""""""""""""""""""""""""""""""""""""""""""
" Use deoplete.
" let g:deoplete#enable_at_startup = 1
" " let g:deoplete#omni#input_patterns.scala = ['[^. *\t0-9]\.\w*',': [A-Z]\w', '[\[\t\( ][A-Za-z]\w*']
" call deoplete#custom#option('sources', {
"     \ '_': ['buffer', 'omni', 'ultisnips', 'file'],
"     \ 'cpp': ['buffer', 'tag'],
" \})
" }}}

" supertab settings                          {{{
" """"""""""""""""""""""""""""""""""""""""""""""
" let g:SuperTabDefaultCompletionType = '<c-x><c-o>'
" let g:SuperTabDefaultCompletionType = '<c-x><c-n>'
" let g:SuperTabDefaultCompletionType = '<c-x><c-u>'
let g:SuperTabDefaultCompletionType = 'context'
let g:SuperTabContextDefaultCompletionType = '<c-x><c-o>'

" if has("gui_running")
"   imap <c-space> <c-r>=SuperTabAlternateCompletion("\<lt>c-x>\<lt>c-o>")<cr>
" else " no gui
"   if has("unix")
"     inoremap <Nul> <c-r>=SuperTabAlternateCompletion("\<lt>c-x>\<lt>c-o>")<cr>
"   endif
" endif
" }}}

" NERDCommenter 설정                         {{{
" """"""""""""""""""""""""""""""""""""""""""""""
" Add spaces after comment delimiters by default
let g:NERDSpaceDelims = 1

" Use compact syntax for prettified multi-line comments
let g:NERDCompactSexyComs = 1

" Align line-wise comment delimiters flush left instead of following code indentation
let g:NERDDefaultAlign = 'left'

" Set a language to use its alternate delimiters by default
let g:NERDAltDelims_java = 1

" Add your own custom formats or override the defaults
let g:NERDCustomDelimiters = { 'c': { 'left': '/**','right': '*/' } }

" Allow commenting and inverting empty lines (useful when commenting a region)
let g:NERDCommentEmptyLines = 1

" Enable trimming of trailing whitespace when uncommenting
let g:NERDTrimTrailingWhitespace = 1
" }}}

"  tagbar 설정                                {{{
" """""""""""""""""""""""""""""""""""""""""""""""
nnoremap <leader>tb :TagbarToggle<CR>
" }}}

" indentGuides                                {{{
" """""""""""""""""""""""""""""""""""""""""""""""
" let g:indent_guides_guide_size = 1
nnoremap <Space>ig :IndentGuidesToggle<cr>

" }}}

" delimitMate                                 {{{
" """""""""""""""""""""""""""""""""""""""""""""""
let g:delimitMate_expand_cr = 2
" }}}

" ale                                         {{{
" """""""""""""""""""""""""""""""""""""""""""""""
let g:ale_sign_error = '●' " Less aggressive than the default '>>'
let g:ale_sign_warning = '.'
let g:ale_lint_on_enter = 0 " Less distracting when opening a new file
" }}}

" java : eclim, gradle test                   {{{
" """""""""""""""""""""""""""""""""""""""""""""""
augroup filetype_java_eclim
    autocmd!
    autocmd FileType java nnoremap <buffer> <localleader>d :JavaSearch -s project -x declarations<CR>
    autocmd FileType java nnoremap <buffer> <localleader>r :JavaSearch -s project -x references<CR>
    autocmd FileType java nnoremap <buffer> <localleader>a :JavaSearch -s project -x all<CR>
    autocmd FileType java nnoremap <buffer> <localleader>i :JavaSearch -s project -x implementors<CR>
    autocmd FileType java nnoremap <buffer> <localleader>jf :%JavaFormat<CR>
    autocmd FileType java inoremap <buffer> jj <Esc>:%JavaFormat<CR>
    autocmd FileType java nnoremap <buffer> <localleader>jt :VimuxPromptCommand<CR>gradle test --info<CR>:call VimuxZoomRunner()<CR>
    autocmd FileType java nnoremap <buffer> <localleader>jc :VimuxPromptCommand<CR>gradle compileJava --info<CR>:call VimuxZoomRunner()<CR>
augroup END
" }}}

" scala                                       {{{
" """""""""""""""""""""""""""""""""""""""""""""""
augroup filetype_scala
    autocmd!
"     autocmd BufWritePost *.scala Neomake! sbt
    " autocmd FileType scala nnoremap <buffer> <C-s><C-f> mvgg=G4x`v:write<CR>
    autocmd FileType scala nnoremap <silent> <buffer> <C-s><C-f> :write<CR>:!ng scalafmt % --config ~/.scalafmt.conf<CR><CR>:edit!<CR>
    autocmd FileType scala inoremap <silent> <buffer> <C-s><C-f> <Esc>:write<CR>:!ng scalafmt % --config ~/.scalafmt.conf<CR><CR>:edit!<CR>
    autocmd BufEnter *.scala setl formatprg=scalafmt\ --config\ $HOME/.scalafmt.conf\ --stdin
    autocmd BufEnter *.scala setl equalprg=scalafmt\ --config\ $HOME/.scalafmt.conf\ --stdin
augroup END
" autocmd FileType scala setlocal omnifunc=LanguageClient#complete
" autocmd FileType scala setlocal completefunc=LanguageClient#complete
" autocmd FileType scala setlocal omnifunc=EnCompleteFunc
" }}}

" fzf                                         {{{
" """""""""""""""""""""""""""""""""""""""""""""""
nnoremap <Space>ff :Files<cr>
" nnoremap <M-f> :Files<cr>
" nnoremap <Space>l :Lines<cr>
" nnoremap <M-l> :Lines<cr>
nnoremap <Space>bb :Buffers<cr>
" nnoremap <M-b> :Buffers<cr>
" }}}

" python : jedi                               {{{
" """""""""""""""""""""""""""""""""""""""""""""""
augroup filetype_python
    autocmd!
    autocmd FileType python setlocal completeopt-=preview
augroup END
let g:ale_python_pylint_executable = 'pylint-3'
let g:jedi#force_py_version=3
" }}}

" html, css, javascript, json                 {{{
" """""""""""""""""""""""""""""""""""""""""""""""
augroup jsbeautify_group
    autocmd!
    autocmd FileType javascript nnoremap <buffer> <C-s><C-f> :Prettier<CR>:write<CR>
    autocmd FileType javascript inoremap <buffer> <C-s><C-f> <ESC>:Prettier<CR>:write<CR>
    autocmd FileType json nnoremap <buffer> <C-s><C-f> :Prettier<CR>:write<CR>
    autocmd FileType json inoremap <buffer> <C-s><C-f> <ESC>:Prettier<CR>:write<CR>
    autocmd FileType jsx vnoremap <buffer> <SPACE>ff :call RangeJsxBeautify()<cr>
    autocmd FileType jsx nnoremap <buffer> <SPACE>ff mvggVG:call RangeJsxBeautify()<cr>`v
    autocmd FileType html vnoremap <buffer> <SPACE>ff :call RangeHtmlBeautify()<cr>
    autocmd FileType html nnoremap <buffer> <SPACE>ff mvggVG:call RangeHtmlBeautify()<cr>`v
    autocmd FileType html nnoremap <buffer> <C-s><C-f> mvggVG:call RangeHtmlBeautify()<cr>`v:write<cr>
    autocmd FileType html inoremap <buffer> <C-s><C-f> <ESC>mvggVG:call RangeHtmlBeautify()<cr>`v:write<cr>
    autocmd FileType css vnoremap <buffer> <SPACE>ff :call RangeCSSBeautify()<cr>
    autocmd FileType css nnoremap <buffer> <SPACE>ff mvggVG:call RangeCSSBeautify()<cr>`v

    autocmd FileType javascript setlocal ts=2
    autocmd FileType javascript setlocal sw=2
    autocmd FileType javascript.jsx setlocal ts=2
    autocmd FileType javascript.jsx setlocal sw=2
augroup END

" print spaces between brackets
" Prettier default: true
let g:prettier#config#bracket_spacing = 'true'

" json conceal
augroup json_concealing
    autocmd InsertEnter *.json setlocal conceallevel=2 concealcursor=
    autocmd InsertLeave *.json setlocal conceallevel=2 concealcursor=inc
augroup END
" }}}

" fish script                                 {{{
" """""""""""""""""""""""""""""""""""""""""""""""
augroup fish_group
    autocmd!
    " autocmd FileType fish setlocal compiler fish
    autocmd FileType fish setlocal foldmethod=expr
augroup END

" }}}

" java script                                 {{{
" """""""""""""""""""""""""""""""""""""""""""""""
let g:user_emmet_settings = {
  \  'javascript.jsx' : {
    \      'extends' : 'jsx',
    \  },
  \}

" }}}

" markdown                                    {{{
" """""""""""""""""""""""""""""""""""""""""""""""
augroup markdown_key_bindings
    autocmd!
    autocmd FileType markdown nnoremap <buffer> <localleader>v :MarkdownPreview<CR>
    autocmd FileType markdown nnoremap <buffer> <localleader>c :MarkdownPreviewStop<CR>
augroup END
" }}}

"" sql                                         {{{
" """""""""""""""""""""""""""""""""""""""""""""""
let g:sqlfmt_command = 'sqlformat'
let g:sqlfmt_options = '-r -k upper'

augroup sql_key_bindings
    autocmd!
    autocmd FileType sql nnoremap <buffer> <CR><CR> :DBExecSQLUnderCursor<CR>
    autocmd FileType sql vnoremap <buffer> <CR><CR> :DBExecVisualSQL<CR>
    autocmd FileType sql nnoremap <buffer> <CR>% :DBExecRangeSQL<CR>

    autocmd FileType sql nnoremap <buffer> <C-s><C-f> :SQLFmt<CR>:write<CR>
    autocmd FileType sql inoremap <buffer> <C-s><C-f> <ESC>:SQLFmt<CR>:write<CR>
augroup END


" }}}
