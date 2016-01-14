# -*- coding:utf-8 -*-
import random

test = []
with open("output_multi.csv", "r") as f:  # 測試資料
    test_tags = f.readline().strip().split(",")
    for line in f:
        line = line.strip().split(",")
        test.append(line)

work_class = test_tags.index("workclass")
occupation = test_tags.index("occupation")

miss_data = [d_id for d_id, t in enumerate(test) if t[work_class] == "?" and t[occupation] == "?"]
print(len(miss_data))
remove_id = random.sample(miss_data, 59318)  # 總共有七萬筆33%缺漏值，只要留下6%

data = [t for d_id, t in enumerate(test) if d_id not in remove_id]


test_no = []
with open("output_no_miss.csv", "r") as f:  # 測試資料
    test_tags = f.readline().strip().split(",")
    for line in f:
        line = line.strip().split(",")
        test_no.append(line)

with open("test_miss.csv", "w") as f:
    f.write("%s\n" % ",".join(test_tags))
    for raw in random.sample(data,5000):
        f.write("%s\n" % ",".join(raw))
        
with open("test_no_miss.csv", "w") as f:
    f.write("%s\n" % ",".join(test_tags))
    for raw in random.sample(test_no, 5000):
        f.write("%s\n" % ",".join(raw))