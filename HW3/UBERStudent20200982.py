#! /usr/bin/python3

import sys
from datetime import datetime, date

f_input = sys.argv[1]
f_output = sys.argv[2]

Weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

dic_uber = {}
with open(f_input, "rt") as fp:
    for line in fp:
        line = line.replace("\n", "")
        uber = line.split(',')
        u_date = datetime.strptime(uber[1], '%m/%d/%Y')
        uber[1] = Weekday[u_date.weekday()]        
        
        if uber[0] not in dic_uber:
            dic_uber[uber[0]] = {}
        if uber[1] not in dic_uber[uber[0]]:
            dic_uber[uber[0]][uber[1]] = {}
            dic_uber[uber[0]][uber[1]]['vehicles'] = int(uber[2])
            dic_uber[uber[0]][uber[1]]['trips'] = int(uber[3])
        else:   
            dic_uber[uber[0]][uber[1]]['vehicles'] += int(uber[2])
            dic_uber[uber[0]][uber[1]]['trips'] += int(uber[3])
            
with open(f_output, "wt") as fp:
    for region in dic_uber:
        for day in dic_uber[region]:
            fp.write("{},{}\t{},{}\n".format(region, day, dic_uber[region][day]['vehicles'], dic_uber[region][day]['trips']))            
