#选择排序
#将列表 视为两部分，前部分用于存放有序序列，后部分每次遍历，选取最小值，加入到有序序列的前面

def select_sort(alist):
    n = len(alist)
    #外部循环，每次寻找一个，需要找n-1次
    for j in range(n-1):
        #内部循环，遍历后部分，将最小值的索引储存，便利完后与第一个元素交换
        min_index = j
        for i in range(j,n):
            if alist[min_index] > alist[i]:
                min_index = i
        #一次遍历后，将选择的元素与最右边元素 换位，即添加到了有序序列里
        alist[j],alist[min_index] = alist[min_index],alist[j]


if __name__ == '__main__':
    l = [3423,53453,57467,56352,2565,9]
    print(l)
    select_sort(l)
    print(l)