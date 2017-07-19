#conding='utf8'

#冒泡算法

#依次比较相邻的数，如果符合条件怎将两值调换位置，直到不可交换为止

def bubble_sort(alist=[]):
    n = len(alist)
    #外部循环，每执行依次，就提取处一个最大值，一共要执行n-1次
    #采用 倒叙的方式 使 i 的值 与内部循环的次数一致
    #记录交换的次数
    count = 0
    for i in range(n-1,0,-1):
        #内部循环，需要依次比较相邻位置的值，直到最后，最开始执行n-1次，每次循环的次数减1
        #j为游标，即前一个元素的位置
        #为了优化 当传入的列表正好是符合顺序排列的时候 [1,2,3,4,5],第一次遍历完后，若无发生交换，则直接退出

        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                count += 1
        if  count == 0:
            print('无需再排列')
            return




l = [342,23,546,676,3542,65]
bubble_sort(l)
print(l)

l = [1,2,3,4,5]
bubble_sort(l)
print(l)

