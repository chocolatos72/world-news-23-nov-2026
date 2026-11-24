#!/usr/bin/env python3
"""Berita 23 — v36 KORAN KLASIK, entry program (Python 3.13, stdlib only).

The image is entry.png beside this file, and the program copies it to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png when that is set).
The image itself is one 1024x1024 newspaper page summing up Monday
23 November 2026: the COP31 collapse as the lead, five pictured stories
(2-6), and the rest of the world's news (7-30) in four columns, with a
world map, a KEY NUMBERS box, a UTC strip and a DATE CHECK box.
The pictured five are the warship Merkury sinking, the Dymer strike,
the Hodeidah telecom strike, the Gaza toxic wasteland, and Nvidia's
CEO reinstatement; Hormuz and Liverpool head the ranked list below.
"""
import os
import shutil

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "entry.png")
dst = os.path.join(out, "entry.png")
shutil.copyfile(src, dst)
# the copied file must be the whole image, byte for byte
assert os.path.getsize(dst) == os.path.getsize(src)
