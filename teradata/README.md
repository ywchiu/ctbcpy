## 設定環境變數

### 安裝 teradata for python
```
wget https://files.pythonhosted.org/packages/cd/44/1395c22a4358486a572881cfd21cd1ea8a11101c35bb676c0e9466520ca5/teradata-15.10.0.21.tar.gz
pip install teradata-15.10.0.21.tar.gz

```

### 在 ~/.bashrc 或 ~/.bash_profile 中鍵入

```
export ODBCINI=/opt/teradata/client/16.20/odbc_64/odbc.ini
export ODBCINST=/opt/teradata/client/16.20/odbc_64/odbcinst.ini
export LD_LIBRARY_PATH=/opt/teradata/client/16.20/lib
```

##本地端測試 ODBC

### 在shell 下建入tdxodbc64

- $ tdxodbc64

```
Enter Data Source Name: testdsn
Enter UserID: dbc
Enter Password: dbc 

select * from dbc.dbcinfo;
```

