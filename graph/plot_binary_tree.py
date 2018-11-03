import random 
import matplotlib.pyplot as plt 
import math 

class leaf:
    def __init__(self):
        self.weight = None
        self.left = None
        self.right = None 

def build(l, r, k, tree):
    while k >= len(tree):
        tree.append(leaf())

    tree[k].left = l 
    tree[k].right = r 

    if l == r:
        tree[k].weight = random.randint(1, 20)
        return 

    mid = (l+r) // 2 
    build(l, mid, 2 * k + 1, tree)
    build(mid + 1, r, 2 * k + 2, tree)

    tree[k].weight = tree[2 * k + 1].weight + tree[2 * k + 2].weight

def get_tree_depth(tree):
    return int(math.log2(len(tree))+1)

def plotNode(axl, nodeTxt, parentPt, centerPt, nodeType=dict(pad=0, fc="0.7", lw=0.01), arrowprops=dict(arrowstyle="-")):
    axl.annotate(nodeTxt, xy=parentPt, xytext= centerPt, bbox=nodeType, arrowprops=arrowprops, xycoords='axes fraction', textcoords='axes fraction', va="center", ha="center") 

def plot_tree_by_layer(tree):
    if len(tree) == 0:
        print('there is not leaf to plot.')
        return 

    depth = get_tree_depth(tree)
    low_height = 0.02 
    upper_height = 1.02
    left_width = 0.02
    right_width = 1.03

    verticle = (upper_height - low_height) / depth

    size = 20 
    fig = plt.figure(figsize=(size, size)) 
    fig.clf() 
    #plot_tree.axl = plt.subplot()
    axl = plt.subplot()

    stack = [0]
    cur_depth = 1
    while stack:
        son = []
        total = len(stack)
        plot = []
        cnt = 0

        while stack:
            k = stack.pop(0)

            left = 2 * k + 1
            right = 2 * k + 2

            flag = 0 
            if left < len(tree) and tree[left].weight != None:
                son.append(left)
                flag = 1
                cnt += 1

            if right < len(tree) and tree[right].weight != None:
                son.append(right)
                flag = 1
                cnt += 1

            if flag == 0:
                plot.append((k, k))
            else:
                plot.append((k, left, right))

        cur_width = (right_width - left_width) / (total+1)
        cur_height = verticle * (cur_depth - 1) + low_height

        nex_height = verticle * cur_depth + low_height 

        if cnt > 0:
            nex_width = (right_width - left_width) / (cnt + 1)

        cur = 1
        for i in range(len(plot)):
            k = plot[i][0]
            cur_x = cur_width * (i + 1)
            if len(plot[i]) == 2:
                plotNode(axl, '{0},{1}\n{2}'.format(tree[k].left, tree[k].right, tree[k].weight), (cur_x, cur_height), (cur_x, cur_height))
            else:
                nex_x = nex_width * cur
                cur += 1
                plotNode(axl, '{0},{1}\n{2}'.format(tree[k].left, tree[k].right, tree[k].weight), (nex_x, nex_height), (cur_x, cur_height))
                
                nex_x = nex_width * cur 
                cur += 1
                plotNode(axl, '{0},{1}\n{2}'.format(tree[k].left, tree[k].right, tree[k].weight), (nex_x, nex_height), (cur_x, cur_height))

        stack = son 
        cur_depth += 1

    plt.show()

if __name__ == '__main__':
    l = 2
    r = 30
    k = 0
    tree = []
    build(l, r, k, tree)
    plot_tree_by_layer(tree)
    


