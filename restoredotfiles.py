#!/usr/bin/env python3
# This app require 'pyfunctional' package
# You need 'pip3 install pyfunctional --user'


import os
import datetime
from pathlib import Path
home = str(Path.home())
from functional import seq
import shutil
import subprocess


def absolute_path(s):
    if s.upper() != 'NONE':
        _s = s.replace('$HOME', '~')
        _s = _s.replace('~', home) \
                if _s.startswith('~/') \
                else os.path.abspath(_s)
    else:
        _s = 'None'
    return _s


def get_backup_list():
    return tuple( zip( \
            *(seq.open('./dotfileslist.txt') \
            .map(lambda l: l.strip()) \
            .filter(lambda l: not l.startswith('#') and len(l) != 0) \
            .map(lambda l: l.split('#')[0].strip().split()) \
            .map(lambda ss: (absolute_path(ss[0]), absolute_path(ss[1])))
            ) ) )
            
def make_dir_if_not_exist(filepath):
    _d = '/'.join(filepath.split('/')[:-1])
    if not os.path.isdir(_d):
        subprocess.call(['mkdir', '-p', _d])

def restore_dotfiles(srcs,dsts):
    for _src,_dst in zip(srcs,dsts):
        if _src != 'None':
            print('Coping ' + _dst + " to " + _src + ' ...')
            make_dir_if_not_exist(_src)
            shutil.copy(_dst, _src)

def do_restore():
    print("Starting restore...")
    srcs,dsts = get_backup_list()
    restore_dotfiles(srcs, dsts)
    print("Ending...")

if __name__ == '__main__':
    do_restore()
