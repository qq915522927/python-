# coding=utf8
def fb_list(n,l=[]):
    count = len(l)
    if count == n: #基线条件 （和一般的递归条件有点不一样） 有点不像递归，更像是循环
        return l
    if not count:
        l.append(0)
        l.append(1)
    l.append(l[-1] + l[-2])
    return fb_list(n,l)

def fb_list2(n): #这个才更像递归
    if n == 1:
        return [0]
    l = fb_list2(n-1)
    return l.append(l[-1]+l[-2])



if __name__ == '__main__':
    print fb_list(10)
    print '************'
    print fb_list(10)