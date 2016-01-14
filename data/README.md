# 訓練、測試資料

## 訓練資料
資料來源: ![UCI adult](https://archive.ics.uci.edu/ml/datasets/Adult)
只使用![adult.data](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data)作為訓練資料集，共 32561 筆記錄。

![attr.py](https://github.com/Phate334/104NUkDataMiningWEKAtopic/blob/master/data/train/attr.py)用來將adult.data及adult.names和合併成CSV檔。

其中帶有缺漏值的資料如下:
* workclass: 1836(6%)
* occupation: 1843(6%)
* native-country: 583(2%)

WEKA重新評估模型的功能只支援![arff格式](https://weka.wikispaces.com/ARFF+%28stable+version%29)的資料。![CSV2ARFF](http://ikuz.eu/csv2arff/)

## 測試資料
資料來源: ![Census-Income (KDD) Data Set](https://archive.ics.uci.edu/ml/datasets/Census-Income+%28KDD%29)使用census-income.data及census-income.test兩份資料作為候選資料集。

