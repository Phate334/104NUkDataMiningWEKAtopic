# -*-coding:utf-8 -*-
from multiprocessing import Process, Manager, Lock

num_process = 10

data = []
with open("data.csv", "r") as f:  # 訓練資料
    data_tags = f.readline().strip().split(",")
    for line in f:
        line = line.strip().split(",")
        temp = dict(zip(data_tags,line))
        temp['age'] = int(temp['age'])
        data.append(temp)

test = []
with open("test-data.csv", "r") as f:  # 測試資料
    test_tags = f.readline().strip().split(",")
    for line in f:
        line = line.strip().split(",")
        temp = dict(zip(test_tags,line))
        temp['age'] = int(temp['age'])
        test.append(temp)

out_tags = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'year', 'class']
check_tags = ['workclass', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country', 'class']

def work(mod, output, counter, lock):
    for i,t in enumerate(test):  # 比較check_tags中的那幾個欄位，用符合最多欄那筆資料的hours-per-week
        if i%num_process != mod:
            continue
        flag = [-1, 0]  # index, 最大符合欄位
        for j,d in enumerate(data):
            temp_count = 0
            if d['age']+5 <= t['age'] and t['age'] < d['age']+5:
                temp_count += 1
            for c_tag in check_tags:
                if t[c_tag] == d[c_tag]:
                    temp_count += 1
            if temp_count > flag[1]:
                flag[0], flag[1] = (j, temp_count)
        # 檢查完所有訓練資料後，決定寫入值
        if flag[1] > 5:
            test[i]['hours-per-week'] = str(data[flag[0]]['hours-per-week'])
        else:
            test[i]['hours-per-week'] = str(-1)
        test[i]['age'] = str(test[i]['age'])
        temp = []
        for tag in out_tags:
            temp.append(test[i][tag])
        with lock:
            output.append(",".join(temp))
            counter.value += 1
            print("%d\r" % counter.value),

if __name__ == "__main__":
    lock = Lock()
    manager = Manager()
    output = manager.list()
    counter = manager.Value('l', 0)
    
    processes = []
    for i in range(num_process):
        t = Process(target=work, args=(i, output, counter, lock))
        t.daemon = True
        processes.append(t)
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    with open("output_multi.csv", "w") as f:
        f.write("%s\n" % ",".join(out_tags))
        f.write("\n".join(output))