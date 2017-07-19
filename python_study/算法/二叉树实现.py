#二叉树
#二叉树，是有且只有只有两个分支的树结构

#节点类，与链表类似，有两个指针，指向分支节点
class Node(object):
    """节点类"""
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    '''二叉树'''
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        #要确定增加的节点的位置，需要遍历前面所有节点
        #广度遍历 tree，实现的方式 是 队列的形式，可用队列的形式完成
        queue =[]
        queue.append(self.root)
        while True:
            #弹出第一个节点
            cur_node = queue.pop(0)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            else:
                cur_node.lchild = node
                return
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
            else:
                cur_node.rchild = node
                return
    #先序遍历，还有中序排列，后序排列
    def preorder(self,root):
        #传入跟节点
        # if root is None:
        #     return
        print(root.elem)

        if root.lchild is not None:
            self.preorder(root.lchild)
        else:
            pass
        if root.rchild is not None:
            self.preorder(root.rchild)
        else:
            pass


if __name__=='__main__':
    t = Tree()
    t.add(5)
    t.add(10)
    t.add(33)
    t.add(13)
    t.add(15)
    t.add(13)
    t.add(16)
    t.preorder(t.root)
