#! /usr/bin/python3

import sys

f_input = sys.argv[1]
f_output = sys.argv[2]

dic_genre = {}
with open(f_input, "rt") as fp:
    genres = []
    for line in fp:
        line = line.replace("\n", "")
        genres = ( line.split('::')[2] ).split('|')  
        for genre in genres:
            if genre in dic_genre:
                dic_genre[genre] += 1
            else:
                dic_genre[genre] = 1

with open(f_output, "wt") as fp:
    for genre in dic_genre:
        fp.write("{} {}\n".format(genre, dic_genre[genre]))
