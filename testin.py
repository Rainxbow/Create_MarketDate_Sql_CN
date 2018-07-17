#!/usr/bin/python3
 
import pymysql
f = open("./output.txt","r") 

db = pymysql.connect("localhost","test","1","TEST" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

line = f.readline()
while line:
	# 使用 execute() 方法执行 SQL，如果表存在则删除
	cursor = db.cursor()
	
	linename="T_"+line 

	sql = """INSERT INTO %s(EXCHANGEID,INSTRUMENTID,LASTPRICE,
		BIDPRICE1,BIDPRICE2,BIDPRICE3,BIDPRICE4,BIDPRICE5,
		BIDVOLUME1,BIDVOLUME2,BIDVOLUME3,BIDVOLUME4,BIDVOLUME5,
		ASKPRICE1,ASKPRICE2,ASKPRICE3,ASKPRICE4,ASKPRICE5,
		ASKVOLUME1,ASKVOLUME2,ASKVOLUME3,ASKVOLUME4,ASKVOLUME5,
		VOLUME,VOLUME_TODAY,VOLUME_TICK,OPENINTEREST,
		UPDATETIME_UPDATEMILLISEC,
		TRADINGDAY,
		OPENPRICE,HIGHESTPRICE,LOWESTPRICE,PRECLOSEPRICE,
		UPPERLIMITPRICE,LOWERLIMITPRICE)
		VALUES('0','0',0,
		0,0,0,0,0,
		0,0,0,0,0,
		0,0,0,0,0,
		0,0,0,0,0,
		0,0,0,0,
		'1000-01-01 00:00:00',
		'1000-01-01',
		0,0,0,0,0,0)""" %linename
	cursor.execute(sql)
	db.commit()
	
	linename = "K_1m_"+line
	sql="""INSERT INTO %s(SYMBOL,EXCHANGE,DATE,TIME,VOLUME,OPENINTEREST,
		OPENPRICE,HIGHPRICE,LOWPRICE,CLOSEPRICE,VOLUMEPERMIN)
		VALUES('0','0','1000-01-01','838:59:59',0,0,0,0,0,0,0
		)"""%linename
	cursor.execute(sql)
	db.commit()

	linename = "K_5m_"+line
	sql="""INSERT INTO %s(SYMBOL,EXCHANGE,DATE,TIME,VOLUME,OPENINTEREST,
		OPENPRICE,HIGHPRICE,LOWPRICE,CLOSEPRICE,VOLUMEPERMIN)
		VALUES('0','0','1000-01-01','838:59:59',0,0,0,0,0,0,0
		)"""%linename
	cursor.execute(sql)
	db.commit()

	linename = "K_15m_"+line
	sql="""INSERT INTO %s(SYMBOL,EXCHANGE,DATE,TIME,VOLUME,OPENINTEREST,
		OPENPRICE,HIGHPRICE,LOWPRICE,CLOSEPRICE,VOLUMEPERMIN)
		VALUES('0','0','1000-01-01','838:59:59',0,0,0,0,0,0,0
		)"""%linename
	cursor.execute(sql)
	db.commit()

	linename = "K_30m_"+line
	sql="""INSERT INTO %s(SYMBOL,EXCHANGE,DATE,TIME,VOLUME,OPENINTEREST,
		OPENPRICE,HIGHPRICE,LOWPRICE,CLOSEPRICE,VOLUMEPERMIN)
		VALUES('0','0','1000-01-01','838:59:59',0,0,0,0,0,0,0
		)"""%linename
	cursor.execute(sql)
	db.commit()

	linename = "K_1h_"+line
	sql="""INSERT INTO %s(SYMBOL,EXCHANGE,DATE,TIME,VOLUME,OPENINTEREST,
		OPENPRICE,HIGHPRICE,LOWPRICE,CLOSEPRICE,VOLUMEPERMIN)
		VALUES('0','0','1000-01-01','838:59:59',0,0,0,0,0,0,0
		)"""%linename
	cursor.execute(sql)
	db.commit()

	linename = "K_4h_"+line
	sql="""INSERT INTO %s(SYMBOL,EXCHANGE,DATE,TIME,VOLUME,OPENINTEREST,
		OPENPRICE,HIGHPRICE,LOWPRICE,CLOSEPRICE,VOLUMEPERMIN)
		VALUES('0','0','1000-01-01','838:59:59',0,0,0,0,0,0,0
		)"""%linename
	cursor.execute(sql)
	db.commit()

	linename = "K_1d_"+line
	sql="""INSERT INTO %s(SYMBOL,EXCHANGE,DATE,TIME,VOLUME,OPENINTEREST,
		OPENPRICE,HIGHPRICE,LOWPRICE,CLOSEPRICE,VOLUMEPERMIN)
		VALUES('0','0','1000-01-01','838:59:59',0,0,0,0,0,0,0
		)"""%linename
	cursor.execute(sql)
	db.commit()

	linename = "K_1w_"+line
	sql="""INSERT INTO %s(SYMBOL,EXCHANGE,DATE,TIME,VOLUME,OPENINTEREST,
		OPENPRICE,HIGHPRICE,LOWPRICE,CLOSEPRICE,VOLUMEPERMIN)
		VALUES('0','0','1000-01-01','838:59:59',0,0,0,0,0,0,0
		)"""%linename
	cursor.execute(sql)
	db.commit()
		
	line = f.readline()
f.close()
 
# 关闭数据库连接
db.close()
