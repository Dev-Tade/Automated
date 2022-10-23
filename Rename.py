#!usr/bin/env python3

from datetime   import datetime
from os         import listdir, rename, path
from typing     import List
from auto_lib   import getlines, str_format
from sys        import argv, stderr, stdout

def show_help():
    stdout.write(
    f"""
    Usage: rename.py <ext> <pattern>
    Example: rename.py .txt text-<i>
    Formating: <ID>
               <date>   -> current date time (DD_MM_YY@HH_MM)
               <ext>    -> current file extension (used internally)
               <ln>     -> lines inside the file
               <i>      -> current file index
    """)

def clear_undotted(l: List[str]) -> None:
    for i, n in enumerate(l):
        if not '.' in n:
            l.pop(i)

def clear_unmatching(l: List[str], s: str) -> None:
    if not s == ".*":
        for i, n in enumerate(l):
            if s in n:
                continue
            else:
                l.pop(i)
    else:
        ...

def main(args: List[str]) -> None:
    if not len(args) >= 1:
        stderr.write(f"Error: Not enough arguments. Try -h")
        exit(1)

    if '-h' in args or '--help' in args:
        show_help()
    else:
        rep_ext: str = args[0]
        pattern: str = args[1]+".<ext>"

        old = listdir('.')
        old_ext = []

        clear_undotted(old)
        clear_unmatching(old, rep_ext)

        for n in old:
            old_ext.append(n.split('.')[1])

        for i, n in enumerate(old):
            rename(n, str_format(
                pattern,{
                    "i":i,
                    "ln":str(getlines(n))+"l",
                    "ext":old_ext[i],
                    "date":datetime.now().strftime("%d_%m_%y@%H_%M")
                    }
                ))

if __name__ == '__main__':
    main(argv[1:])