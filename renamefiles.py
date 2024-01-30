"""
Rename multiple files in directory
"""
import os

for dpath, dnames, fnames in os.walk('./'):
    for f in fnames:
        os.chdir(dpath)
        if f.startswith('currentname'):
            os.rename(f, f.replace('newname', 'u'))
