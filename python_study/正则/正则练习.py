"""有一批网址：

http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
需要 正则后为：

http://www.interoem.com/
http://3995503.com/
http://lib.wzmc.edu.cn/
http://www.zy-ls.com/
http://www.fincm.com/"""
import re
s = """
http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
"""
#前面部分容易识别，后面需要替换的地方不易识别，可用sub 里传函数的方式，返回前面的部分
p = r'(http://.+?/).*'
r = re.sub(p,lambda x:x.group(1)+'\n',s)
# r = re.sub(p,'1',s)
print(r)

"""2. 找出单词

有一句英文如下：

hello world ha ha

查找所有的单词"""

s ='hello world ha ha'
#两种实现方案
#1.通过 分割完成
#2.通过字符特征
p1 = r' +'
r1 = re.split(p1,s)
print(r1)

p2 = r'\b[a-zA-Z]+\b'
r2 = re.findall(p2,s)
print(r)
