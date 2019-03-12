# venvはpython3で、仮想環境を作成するコマンド
基本的にpip installは、仮想環境で行うべき。

# venvの環境を作成する ( python -m venv 環境の名前 )
python -m venv 環境名

# 仮想環境に入る
source ./環境名/bin/activate

# 仮想環境から出る
deactivate

# メモ  
エイリアスを作成しておくと便利  
「~/.bash_profileファイル」に下記コード記入  
```
alias エイリアス名="source /Users/名前/このスクリプトのPATH/venv/環境名/bin/activate"
```

## 変更内容の適用  
```
source ~/.bash_profile  
```
