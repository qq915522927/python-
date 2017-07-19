import contextlib
from urllib.request import urlopen

with contextlib.closing(urlopen('http://wwww.baidu.com')) as f:
    print(f.readline())
print(urlopen('http://wwww.baidu.com'))
print(contextlib.closing(urlopen('http://wwww.baidu.com')) )