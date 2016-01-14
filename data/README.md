# 訓練、測試資料

## 訓練資料
資料來源: ![UCI adult](https://archive.ics.uci.edu/ml/datasets/Adult)
只使用![adult.data](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data)作為訓練資料集，共 32561 筆記錄。

其中帶有缺漏值的資料如下:
* workclass: 1836(6%)
* occupation: 1843(6%)
* native-country: 583(2%)

WEKA重新評估模型的功能只支援![arff格式](https://weka.wikispaces.com/ARFF+%28stable+version%29)的資料。![CSV2ARFF](http://ikuz.eu/csv2arff/)

