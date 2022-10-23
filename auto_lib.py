from typing import Dict, Any

def getlines(src:str) -> int:
    r: int = 0
    with open(src, 'r') as f:
        for c in f.read():
            if c != '\n':
                continue
            else:
                r += 1
    return r

def str_format(src:str, env:Dict[str,Any]) -> str:
    inv: bool = False
    vnm: str = ""
    ret: str = ""
    for _, c in enumerate(src):
        if c == '<':
            if inv == False:
                inv = True
            if inv == True:
                continue
        elif c == '>':
            if inv == True:
                inv = False
                ret += str(env[vnm])
                vnm = ""
            if inv == False:
                continue
        else:
            if inv == True:
                vnm += c
            else:
                ret += c
    return ret