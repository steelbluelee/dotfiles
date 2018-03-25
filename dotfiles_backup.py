#!/usr/bin/python3


import os
import datetime
from pathlib import Path
home = str(Path.home())
from functional import seq
import shutil
import subprocess


def unzip(s):
    _ls = []
    _rs = []
    for l,r in s:
        _ls.append(l)
        _rs.append(r)
    return (_ls, _rs)


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
    return unzip( \
            seq.open('./dotfileslist.txt') \
            .map(lambda l: l.strip()) \
            .filter(lambda l: not l.startswith('#') and len(l) != 0) \
            .map(lambda l: l.split()) \
            .map(lambda ss: (absolute_path(ss[0]), absolute_path(ss[1])))
            )


def modification_time(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


def make_dir_if_not_exist(filepath):
    _d = '/'.join(filepath.split('/'))[:-1]
    if not os.path.isdir(_d):
        subprocess.call(['mkdir', '-p', _d])


def srcupdated(src, dst):
    _src_t = modification_time(_src)
    _dst_t = modification_time(_dst) \
            if os.path.exists(_dst) \
            else datetime.datetime(1,1,1,1)
    return _src_t > _dst_t
    
def copy_dotfiles(srcs,dsts):
    for _src,_dst in zip(srcs,dsts):
        if _src != 'None':
            make_dir_if_not_exist(_dst)
            _src_time = modification_time(_src)
            _dst_time = (modification_time(_dst) if os.path.exists(_dst)
                    else datetime.datetime(1,1,1,1))
            if (_src_time > _dst_time):
                print('Coping ' + _src + " to " + _dst + ' ...')
                shutil.copy(_src, _dst)



def git_add(dsts):
    for _dst in dsts:
        subprocess.call(['git', 'add', _dst])


def git_rm(dsts):
    _files_in_git = subprocess.check_output( \
            ['git', 'ls-tree', '-r', 'master', '--name-only'] ) \
            .decode('utf-8').split()
    for f in _files_in_git:
        if os.path.abspath(f) not in dsts:
            print('Deleting ' + f + '...')
            subprocess.call(['git', 'rm', f])


def git_commit():
    return not subprocess.call( \
            ['git', 'commit', '-m', str(datetime.datetime.now())] )


def git_push():
    subprocess.call(['git', 'push', 'origin', 'master'])


if __name__ == '__main__':
    print("Starting...")
    srcs,dsts = get_backup_list()
    copy_dotfiles(srcs, dsts)
    git_add(dsts)
    git_rm(set(dsts))
    if git_commit():
        git_push()
    print("Ending...")
