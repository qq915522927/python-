#表示一常量的特定集合
from enum import Enum

m = Enum('Mouth',('一月','二月','三月'))

print(m['一月'])
print(m.一月)
for name,member in m.__members__.items():
    print(name +'*****'+str(member)+'*******'+str(member.value))
    # 一月*****Mouth.一月*******1
    # 二月*****Mouth.二月*******2
    # 三月*****Mouth.三月*******3
