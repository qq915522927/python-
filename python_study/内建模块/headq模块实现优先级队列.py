# coding=utf8
import heapq
print heapq.__name__
class ProrityQueeue(object):
    def __init__(self):
        self._index = 0 #用来维护优先级一样的item的排序
        self._queuue = []
    def push(self,prority,item):
        #  heapq.heappush 以堆结构的方式插入，保证堆顶为最小元素
        # 为了方便以优先级比较，将每一个子项 设置为一个元组，优先级相同时按照插入的顺序排列
        heapq.heappush(self._queuue,(-prority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queuue)[2]

if __name__ == '__main__':

    pq = ProrityQueeue()
    pq.push(5,'5')
    pq.push(3,'4')
    pq.push(6,'6')
    pq.push(7,'9')
    pq.push(7,'7')
    pq.push(8,'8')

    for i in range(6):
        print pq.pop()

