# coding=utf8

'''
迪克斯特拉算法用于解决加权图的最小路径问题，适用于有向无环图
总体分为4步
1. 找出最便宜的节点
2. 计算该节点的各个邻居的开销
3. 重复第一步找出最便宜的节点
4. 重复第二部更新该节点邻居的开销
'''
'''
具体实现步骤：
1.首先需要三个散列表
第一个表用来储存图结构
{'start':{'A':6,'B':2},'A':{'end':1},'B':{'A':3,'end':5},'end':{}}
每一个键值对的值表示该节点下邻居节点以及开销。

第二个表用来存放到各个节点的总开销
costs = {'A':6,'B':2,'end':float('inf')}

第三个表用来记录各个节点的父节点，以记录完整路径



结构如下：
'''

graph = {'start':{'A':6,'B':2},'A':{'end':1},'B':{'A':3,'end':5},'end':{}}
costs = {'A':6,'B':2,'end':float('inf')}
parents = {'A':'start','B':'start','end':''}

#处理过的节点列表
processed = []

def find_lowest_node(l):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in l:
        cost = l[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_node(costs)
while node:
    #该节点的开销
    cost = costs[node]
    #该节点的邻居
    neighbors = graph[node]
    for n in neighbors.keys():
        #邻居节点的新开销
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]: #判断新的开销是否更小，是的化跟新对应节点的costs，同时跟新parents
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)

    #找出接下来要处理的节点
    node = find_lowest_node(costs)

route_list = []

def get_route(l,parent):
    pre = l.get(parent,None)

    if pre:
        route_list.append(pre)
        get_route(l, pre)
    else:
        return



get_route(parents,'end')
route = '-'.join(route_list[::-1])

print '到达终点最少开销为{}，路径为{}'.format(costs['end'],route)