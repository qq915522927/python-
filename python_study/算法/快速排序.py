#快速排序
#快速排序，是先去第一个元素，存放在中间值里，然后从两头分别用两个游标向中间靠拢，分别为low 和 high
#low游标左边全是比，中间值小的元素，high 右边全是比中间值大的元素，当low所指元素比中间值大时
#就将这个值给high，然后high同时向左移动，重复同样的判断。最后high和low游标重合，即确定了
#插入中间值元素的位置，赋值
#此时序列 被分为了 两部分，两部分都要继续重复进行，游标夹逼，确定中间值的过程，直到序列的元素只有
#一个为止
#×××××××××××××××××××××××××××
#重点：考虑到这种重复进行的过程，使用递归完成后续的重复操作
#要使用递归，需要提炼出每次调用函数的共同特点，动态的传入参数

def quick_sort(alist,start,end):
    #退出情况：并不只是start=end，当第一个元素就是mid位置时，会造成start>end
    if start >= end:
        return
    low = start#首游标
    high = end #尾游标

    mid = alist[low]

    while low < high:
        #先考虑内部的循环

        #先从high游标开始，因为low游标所指位置为空了（没有意义了）
        while low < high and alist[high] >= mid:#一旦粮油表重合立马退出循环
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid

    #经过第一次分割后，序列变为两段，左右两段都要再进行一次这样的选位置插入，可以考虑递归
    #要对同一个列表进行操作，同时要区分开两段，（切片不可取，切片生成新的列表），可以传入列表的同时，传入起始位置

    quick_sort(alist,start,low-1)#左边部分
    quick_sort(alist,low+1,end)#右边部分

if __name__ == '__main__':
    l = [3, 2, 3, 4, 5,56,34,564,234,56]
    print(l)
    quick_sort(l,0,len(l)-1)
    print(l)