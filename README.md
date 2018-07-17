python + mysql
小demo一个

根据name文件夹下的所有csv文件名（中国主要期货交易所对应合约的合约名）以及对应合约交易所生成对应行情数据的Mysql数据库表

具体的表包括：所有合约的tick表、K线表（包括一分钟、五分钟、三十分钟、一小时、一天、一周的）

具体文件功能：
testlist.py 根据name文件夹下的.csv文件生成output.txt。具体内容为，对应合约名_交易所缩写
test.py 根据output.txt文件内容生成对应数据库表
testlist.py 向生成数据库中插入默认数据。
output.txt 缓存合约名以及交易所代码

数据库名请设置为TEST，管理员为test，密码为1
