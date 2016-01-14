# 測試腳本
2016/1/14 當天用來執行測試的腳本。內含姓名與學號的檔案都已經處理過，不一定符合腳本的輸入輸出。

## 目錄結構
* data:  經過預處理符合測試模型的arff資料。
* model:  準備用來測試的模型。
* result:  測試結果。

## 流程
1. ![init/groups.txt](https://github.com/Phate334/104NUkDataMiningWEKAtopic/blob/master/scripts/init/groups.txt)包含組員的姓名與學號，執行![init_team.py](https://github.com/Phate334/104NUkDataMiningWEKAtopic/blob/master/scripts/init/init_team.py)產生一個team.json檔，作為以下腳本的中繼資料。
2. ![algo.txt](https://github.com/Phate334/104NUkDataMiningWEKAtopic/blob/master/scripts/algo.txt)蒐集每個模型所使用的演算法名稱，包含完整package路徑。例:weka.classifiers.trees.J48
3. 執行![show.py](https://github.com/Phate334/104NUkDataMiningWEKAtopic/blob/master/scripts/show.py)將algo.txt中的演算法名稱加入team.json中，並產生"小組資訊.txt"檔案，包含組別資訊。
4. 執行![check_file.py](https://github.com/Phate334/104NUkDataMiningWEKAtopic/blob/master/scripts/check_file.py)檢查上傳的data和model是否符合規定，並在team.json中加入狀態資訊。上交檔案有缺失的組別會直接跳過後面的測試。
5. 執行![test_model.py](https://github.com/Phate334/104NUkDataMiningWEKAtopic/blob/master/scripts/test_model.py)開始測試繳交的model，所有結果放在result下存成txt檔。
6. 執行![rank.py](https://github.com/Phate334/104NUkDataMiningWEKAtopic/blob/master/scripts/rank.py)解析result中的結果，取出每份測試的F-Measure、ROC Area，並以總和作為排序標準。

## 測試結果
請上elearning教學平台查看。
