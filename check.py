#!/usr/bin/env python3
import os

with open("names.txt") as f:
    name = f.readline();
    if os.path.isfile("./images/{}.jpg".format(name)):
        pass
    else:
        print(name)
