# -*- coding:utf-8 -*-
# 初始化使用者目錄
import os
import json
import uniout

groups = []
with open("groups.txt","r") as f:
    for line in f:
        line = line.strip().split(" ")
        groups.append(line)

teams = []
for ind, meb in enumerate(groups):
    temp = {}
    temp['num'] = ind
    temp['member'] = [meb[0], meb[1]]
    temp['member_id'] = [meb[2].upper(), meb[3].upper()]
    temp['team_id'] = str(hash("".join(temp['member_id'])))
    teams.append(temp)

with open("team.json","w") as f:
    f.write(json.dumps(teams))
