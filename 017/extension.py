import os
# print(os.path.splitext("a/b/c/de.txt")[1]) # passvand ra barmigardand
# print(os.path.dirname("a/b/c/de.txt")) # dom ra barmigardanad
# print(os.path.basename("a/b/c/de.txt")[-4:]) # name khod file hamrah pasvand barmigardand

import pathlib
print(pathlib.Path("a/b/c/de.txt").suffix) # yadet nere P bozorg    pasvand barmigardanad
print(pathlib.Path("a/b/c/de.txt.mp4.jpg.zip").suffixes)