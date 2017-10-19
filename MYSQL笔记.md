## 笔记  


* 进入mysql：直接运行mysql的话可能会提示 `ERROR 1045 (28000): Access denied for user 'ODBC'@'localhost' (using password: NO)` ,这时候输入 `mysql -u root -p`再输出密码就能登录了~  

* 安装了MYSQL5.0，可是用其他机器访问我的数据库服务器的时候，老是报10060错误，上网查看了一下，原来是windows防火墙将MYSQL的端口3306给拦截了，具体的打开方法如下：开始-设置-控制面板-Windows防火墙,找到mysql, 打开端口就行了~

* 查询内容去重:  `SELECT DISTINCT <CONDITION> FROM <CONDITION>; `
* 使用.sql文件: 在mysql命令行里输入`source <path> `就可以运行这个sql文件了。  
* 自动递增重新计数:`ALTER TABLE <tablename> AUTO_INCREMENT=1;`
