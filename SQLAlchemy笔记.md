# SQLAlchemy学习笔记
记录一些容易忘的点


* 直接执行SQL语句:
>db.session.execute('.......')

* SELECT数据去重: 1.直接在sqlalchemy上面执行sql语句; 2.使用session.query+filter+distinct实现;
>uv=db.session.query(UrlCounter.ipaddr).filter(UrlCounter.url==target_url).distinct().count()

* 查询介于日期的
>UrlCounter.query.filter_by(url='xxxxxxxxxxxxxx').filter(UrlCounter.time.between('2017-10-13','2017-10-14'))

* 查询最小值
>db.session.query(db.func.min(UrlCounter.time)).filter(UrlCounter.url=='xxxxxxxxxxxxxxxx')

