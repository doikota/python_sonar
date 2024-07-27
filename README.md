# PythonでSonarQubeを使う

### Pythonは3.12.4に刷新し、coverageをインストール
```
> python --version
Python 3.12.4

> pip install coverage

> coverage --version
Coverage.py, version 7.6.0 with C extension
Full documentation is at https://coverage.readthedocs.io/en/7.6.0
```

### coverageの実行
```
coverage run -m unittest tests.test_mymodule
```

### pynoseをインストール
Python3.12ではnoseがサポートされていないので、pynoseをインストールする
```
pip install pynose
pynose -V
pynose version 1.5.2
nosetests -V
nosetests version 1.5.2
```

### nosetestsの実行
```
nosetests --with-xunit tests.test_mymodule
```
