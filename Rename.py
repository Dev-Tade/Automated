import sys
import os

dirn = sys.argv[1]
os.chdir(dirn)

old = os.listdir(".")
old_ext = []
new = "{}-{}.{}"

for n in range(len(old)):
    ext = old[n].split(".")[1]
    old_ext.append(ext)

for n in range(len(old)):
    os.rename(old[n], new.format(dirn,n,old_ext[n]))
