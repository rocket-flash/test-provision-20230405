#! /usr/bin/env python

import hashlib

hasher = hashlib.sha1()
hasher.update(b"TROLOLOL")

print(hasher.hexdigest())
