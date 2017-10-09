## 笔记  
0.进入mysql：直接运行mysql的话可能会提示 `ERROR 1045 (28000): Access denied for user 'ODBC'@'localhost' (using password: NO)` ,这时候输入 `mysql -u root -p`再输出密码就能登录了~
1.查询内容去重:  SELECT **DISTINCT** *[CONDITION]* FROM *[CONDITION]*;
2.使用.sql文件: 在mysql命令行里输入source *[path]* 就可以运行这个sql文件了。
