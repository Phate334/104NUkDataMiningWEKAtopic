# -*- coding:utf-8 -*-
import os
import json
with open("team.json", "r") as f:
    teams = json.loads(f.read())

def classer_result(result_file):
    with open(result_file, "r") as f:
        flag = False
        for line in f:
            if "Error on test data" in line:
                flag = True
            if flag and "Weighted Avg." in line:
                line = line.strip().split()[-2:]
                f_measure, ROC = line
    return (float(f_measure), float(ROC))

rank_data = []
for team in teams:
    if team["status"] == "error":
        continue
    temp = {}
    temp["num"] = team["num"]
    temp["member"] = team["member"]
    temp["miss"] = classer_result("result\\%d_miss.txt" % team["num"])
    temp["no_miss"] = classer_result("result\\%d_no_miss.txt" % team["num"])
    temp["total"] = temp["miss"][0] + temp["miss"][1] + temp["no_miss"][0] + temp["no_miss"][1]
    rank_data.append(temp)

print(u"開獎囉~~")
print("F-Measure + ROC")
print("="*60)
print(u"組別\t缺漏\t\t無缺漏\t\t\t總和")
print("="*60)
for team in sorted(rank_data, key=lambda x:x["total"], reverse=True):
    num = team["num"]
    print(u"第%2d組\t%.3f|%.3f\t%.3f|%.3f\t\t%.3f" % (num,
    team["miss"][0], team["miss"][1], team["no_miss"][0], team["no_miss"][1], team["total"]))
    print("%-10s\t%s\n" % (team["member"][0], team["member"][1]))
