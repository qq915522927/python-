# coding=utf8
def fb_list(n,l=[]):
    count = len(l)
    if count == n:
        return l
    if not count:
        l.append(0)
        l.append(1)
    l.append(l[-1] + l[-2])
    return fb_list(n,l)

if __name__ == '__main__':
    print fb_list(10)