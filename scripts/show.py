# -*- coding:utf-8 -*-
import os
import json
with open("team.json", "r") as f:
    teams = json.loads(f.read())

algo = []
with open("algo.txt", "r") as f:
    for line in f:
        line = line.strip().split()[-2:]
        for index, team in enumerate(teams):
            if line[0] in team["member_id"]:
                teams[index]["algo"] = line[1]
with open("team.json", "w") as f:
    f.write(json.dumps(teams))


with open(u"小組資訊.txt", "w") as f:
    f.write("組別\t組員\t\t\t\t學號\t\t\t\t演算法\n")
    f.write("="*75 + "\n")
    for team in teams:
        f.write("%d\t%-20s\t\t%s\t%s\n" % (team["num"], ",".join([m.encode("utf-8") for m in team["member"]]), ",".join([m.encode("utf-8") for m in team["member_id"]]), team["algo"]))

with open("team.json", "w") as f:
    f.write(json.dumps(teams))
