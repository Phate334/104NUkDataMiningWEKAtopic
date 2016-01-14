# -*- coding:utf-8 -*-
import os
import subprocess
import json

miss_cmd = "java %s -l model\\%d.model -T data\\%d_miss.arff -i > result\\%d_miss.txt"
no_miss_cmd = "java %s -l model\\%d.model -T data\\%d_no_miss.arff -i > result\\%d_no_miss.txt"

with open("team.json", "r") as f:
    teams = json.loads(f.read())

print(u"開始測試.....")
print("="*60)
print(u"組別\t執行結果(缺漏資料、無缺漏資料)")
print("="*60)
for team in teams:
    num = team["num"]
    if team["status"] == "error":
        print(u"第%-2d組\tERROR" % num)
        continue
    miss_retcode = subprocess.call(miss_cmd % (team["algo"], num, num, num), shell=True)
    miss_retcode = "Done" if miss_retcode == 0 else "error"
    no_miss_retcode = subprocess.call(no_miss_cmd % (team["algo"], num, num, num), shell=True)
    no_miss_retcode = "Done" if no_miss_retcode == 0 else "error"
    print(u"第%2d組\t%-5s\t%-5s" % (num, miss_retcode, no_miss_retcode))