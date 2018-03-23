#!/usr/bin/python3


import os
import datetime
from pathlib import Path
home = str(Path.home())


def get_backup_list():
    with open('./dotfileslist.txt') as f:
        _srcs = []
        _dsts = []
        for line in f.readlines():
            _line = line.strip()
            if not _line.startswith('#') and len(_line) != 0:
                _src,_dst = _line.split()
                if _src.upper() != 'NONE' :
                    _src = _src.replace('$HOME', '~')
                    _src = (_src.replace('~', home) if _src.startswith('~/') 
                            else os.path.abspath(_src))
                else:
                    _src = 'None'
                _dst = _dst.replace('$HOME', '~')
                _dst = (_dst.replace('~', home) if _dst.startswith('~/')
                        else os.path.abspath(_dst))
                _srcs.append(_src)
                _dsts.append(_dst)
    return _srcs,_dsts


def modification_time(filename):
    print(filename)
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


import shutil
import subprocess


def copy_and_git_add(srcs,dsts):
    for _src,_dst in zip(srcs,dsts):
        if _src != 'None':
            if not os.path.isdir('/'.join(_dst.split('/')[:-1])):
                subprocess.call(['mkdir', '-p', '/'.join(_dst.split('/')[:-1])])
            _src_time = modification_time(_src)
            _dst_time = (modification_time(_dst) if os.path.exists(_dst)
                    else datetime.datetime(1,1,1,1))
            if (_src_time > _dst_time):
                print('Coping ' + _src + " to " + _dst + ' ...')
            shutil.copy(_src, _dst)
        subprocess.call(['git', 'add', _dst])

def git_rm(dsts):
    _files_in_git = subprocess.check_output(
                    ['git', 'ls-tree', '-r', 'master', '--name-only']).decode('utf-8').split()
    for f in _files_in_git:
        if os.path.abspath(f) not in dsts:
            print('Deleting ' + f + '...')
            subprocess.call(['git', 'rm', f])


def git_commit():
    subprocess.call(['git', 'commit', '-m', str(datetime.datetime.now())])


def git_commit1():
    return subprocess.check_output( ['git', 'commit', '-m', str(datetime.datetime.now())] ).decode('utf-8')


def git_push():
    subprocess.call(['git', 'push', 'origin', 'master'])

if __name__ == '__main__':
    print("Starting...")
    srcs,dsts = get_backup_list()
    copy_and_git_add(srcs, dsts)
    git_rm(dsts)
    if '커밋할 사항 없음' not in git_commit1():
        git_push()
    print("Ending...")
