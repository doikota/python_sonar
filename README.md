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

### nosetests/pynoseの実行
```
nosetests --with-xunit tests.test_mymodule
pynose --with-xunit tests.test_mymodule
```

###　pylintをインストール
```
pip install pylint
```

### pylintの実行
```
pylint mypackage -r n --msg-template="{path}:{line}: [{msg?id}({symbol}) ,{obj}] {msg} " > ./pylint-result.txt
```

### SonarLintの適用
C:\Users\<user>\AppData\Roaming\Code\User\settings.jsonに以下を追記
```
  "sonarlint.connectedMode.connections.sonarqube": [
    {
      "serverUrl": "http://localhost:9000",
      "token": "<your token>",
    }
  ]
```
