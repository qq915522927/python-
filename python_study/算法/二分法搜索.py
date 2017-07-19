#二分法查找
#假设查找序列为从小到大的有序序列
#取中间位置元素，如果是要查找数则结束，如果大于，则在左边再择中，直到正好取到，或者列表为空为止

#用递归方法实现，每次返回一个列表，从中间分开后取一个，作为整体再二分，直到找到，或者列表耗尽
def binary_search(alist,item):
    n = len(alist)
    if n == 0:
        #如果都没找到，列表长度为0,则返回false
        return False
    mid = n//2
    if alist[mid] > item:
        cur_list = alist[0:mid]
        return binary_search(cur_list,item) #将 最后返回的值一直返回 给最前面的函数
    elif alist[mid] < item:
        cur_list = alist[mid+1:]
        return binary_search(cur_list,item)
    else:
        #当找到事返回True
        return True

#使用循环，非嵌套，只操作同一个列表，同时可以返回元素的索引，不增加内存开销
def binary_search2(alist,item):
    n = len(alist)
    start = 0
    end = n-1

    while start < end:
        #循环开始
        mid = (start + end) // 2
        if alist[mid] > item:
            start = start
            end = mid
        elif alist[mid] < item:
            start = mid + 1
            end = end
        else:
            return mid
    return False

if __name__ == '__main__':
    l = [1,3,5,6,7,9,10]
    i = binary_search(l,11)
    print(i)

    g = binary_search2(l,5)
    print(g)