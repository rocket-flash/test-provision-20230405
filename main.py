#! /usr/bin/env python

import hashlib

hasher = hashlib.sha1()
hasher.update(b"trololol")

print(hasher.hexdigest())
