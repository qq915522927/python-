#希尔算法
#希尔算法是插入算法的一个升级优化，插入算法实际是步长为一的希尔
#希尔算法 利用步长 将序列分为多个部分， 相隔一定步长的元素 为一组，每组内部都进行插入排序
#全部组排序完成后，缩小步长，直到步长为一，最终完成，所有元素的排序
#希尔算法实际是 插入算法的 步长变为 n的形式，左边为有序序列，右部分为 无序部分
#希尔算法的插入 之插入到一步长为关系 的 组中

def shell_sort(alist):
    n = len(alist)
    step = 4
    while step >=1:
    #外部循环 需要循环 n-step 次
        for j in range(step,n):
            i = j
            #内部循环实际为插入排序
            while i-step >= 0:
                if alist[i] < alist[i-step]:
                    alist[i],alist[i-step] = alist[i-step],alist[i]
                    i -= step
                else:
                    break

        step //= 2


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5,34,645,34,234,6476,345]
    print(l)
    shell_sort(l)
    print(l)