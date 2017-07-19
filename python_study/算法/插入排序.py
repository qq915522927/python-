#插入排序
#同样将序列分为两部分，前部分为有序，后部分为无序，每次取后部分的第一个元素，与有序列表中
#的元素比较，若符合排序规则，则退出循环，若不符合则交换，同时向前与前一元素比较，直到插入到正确位置

def insert_sort(alist):
     n = len(alist)
     #操作发生在有序的部分
     #外部循环，第一个元素默认插入，后还需要插入n-1个，循环n-1次
     for j in range(1,n):
          i = j
     #内部循环，取到元素，与前一元素比较
          # while i > 0:
          #     if alist[i] < alist[i-1]:
          #          alist[i],alist[i-1] = alist[i-1],alist[i]
          #          i -=1
          #     else:
          #         #因为左边是有序的，只要最后满足，就可直接退出，表示插入成功
          #          break

          for i in range(j,0,-1):
              if alist[i] < alist[i-1]:
                  alist[i],alist[i-1] = alist[i-1],alist[i]
                  i -=1
              else:
                  #因为左边是有序的，只要最后满足，就可直接退出，表示插入成功
                  print('提前退出')
                  break




if __name__ == '__main__':
    l = [1,2,3,4,5]
    print(l)
    insert_sort(l)
    print(l)
