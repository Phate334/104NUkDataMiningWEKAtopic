# -*- coding:utf-8 -*-
import os
import json
with open("team.json", "r") as f:
    teams = json.loads(f.read())

def find_file(num):
    if os.path.isfile("model\\%d.model"%num):
        model_sta = "OK"
    else:
        model_sta = "error"
    if os.path.isfile("data\\%d_miss.arff"%num):
        miss_sta = "OK"
    else:
        miss_sta = "error"
    if os.path.isfile("data\\%d_no_miss.arff"%num):
        no_miss_sta = "OK"
    else:
        no_miss_sta = "error"

    return "%-5s\t%-5s\t%-5s\t" % (model_sta, miss_sta, no_miss_sta)

print(u"檔案上傳狀況")
print("="*60)
print(u"組別\tmodel\tmiss\tno_miss")
print("="*60)
for index, team in enumerate(teams):
    num = team["num"]
    status = find_file(num)
    if "error" in status:
        teams[index]["status"] = "error"
    else:
        teams[index]["status"] = "OK"
    print(u"第%-2d組\t%s" % (num, status))

with open("team.json", "w") as f:
    f.write(json.dumps(teams))