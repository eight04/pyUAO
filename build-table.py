import requests
import json
import pathlib

r = requests.get("https://unpkg.com/uao-js@1.0.1/table/u2b.json")
data = r.json()
with pathlib.Path("uao/u2b.py").open("w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write("u2b_table={")
    for i, (key, value) in enumerate(data.items()):
        if i != 0:
            f.write(",")
        f.write("u{!r}:{!r}".format(key, value.encode("latin-1")))
    f.write("}")
    
r = requests.get("https://unpkg.com/uao-js@1.0.1/table/b2u.json")
data = r.json()
with pathlib.Path("uao/b2u.py").open("w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write("b2u_table={")
    for i, (key, value) in enumerate(data.items()):
        if i != 0:
            f.write(",")
        key = key.encode("latin-1")
        f.write("{!r}:u{!r}".format(key[0] * 0x100 + key[1], value))
    f.write("}")
