# coding=utf8

def qiick_sorting(l):
    if len(l) <= 1:
        return l
    mid = [i for i in l if i == l[0]]
    less = [i for i in l if i < l[0]]
    more = [i for i in l if i > l[0]]
    return qiick_sorting(less)+ mid+ qiick_sorting(more)

def insert_sorting(l):
    ordered = []
    while True:
        if len(l)>=1:
            current = l.pop(0)
            ordered.append(current)
            for i in range(len(ordered)-1,0,-1):
                if ordered[i] < ordered[i-1]:
                    ordered[i],ordered[i-1] =ordered[i-1], ordered[i]
        else:
            break
    return ordered

def select_sorting(l):
    ordered = []
    for i in range(len(l)):
        min = float('inf')
        for item in l:
            if item < min:
                min = item
        ordered.append(min)
        l.remove(min)
    return ordered

if __name__ == '__main__':
    l = [4,2,6,2,7,9,6,55,55]
    l2 = insert_sorting(l)
    print l2