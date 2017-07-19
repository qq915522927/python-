import re

s = 'sfdfsdfs 123-123143-34'
p = r'.*(\d+-\d+-\d+)'

r1 = re.match(p,s)
print(r1.group(1))
#结果为
# 3-123143-34
#贪婪模式 前面部分匹配 竟可能多的，保证 后面数字 至少有一位满足条件 即可
#用问号 关闭贪婪模式


p = r'.*?(\d+-\d+-\d+)'

r1 = re.match(p,s)
print(r1)


