#!/usr/bin/python3
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
    return list( zip( \
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


def modification_time(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


def src_updated(src, dst):
    _src_t = modification_time(src)
    _dst_t = modification_time(dst) \
            if os.path.exists(dst) \
            else datetime.datetime(1,1,1,1)
    return _src_t > _dst_t
    

def copy_dotfile_if_updated(src, dst):
    if src_updated(src, dst):
        print('Coping ' + src + " to " + dst + ' ...')
        shutil.copy(src, dst)


def copy_dotfiles(srcs,dsts):
    for _src,_dst in zip(srcs,dsts):
        if _src != 'None':
            make_dir_if_not_exist(_dst)
            copy_dotfile_if_updated(_src, _dst)


def git_add(dsts):
    for _dst in dsts:
        subprocess.call(['git', 'add', _dst])


def git_rm_not_in(dsts):
    _dsts = set(dsts)
    _files_in_git_repo = subprocess.check_output( \
            ['git', 'ls-tree', '-r', 'master', '--name-only'] ) \
            .decode('utf-8').split()
    for f in _files_in_git_repo:
        if os.path.abspath(f) not in _dsts:
            print('Deleting ' + f + '...')
            subprocess.call(['git', 'rm', f])


def git_commit():
    return not subprocess.call( \
            ['git', 'commit', '-m', str(datetime.datetime.now())] )


def git_push():
    subprocess.call(['git', 'push', 'origin', 'master'])


def do_backup():
    print("Starting backup...")
    srcs,dsts = get_backup_list()
    copy_dotfiles(srcs, dsts)
    git_add(dsts)
    git_rm_not_in(dsts)
    if git_commit():
        git_push()
    print("Ending...")


if __name__ == '__main__':
    do_backup()
