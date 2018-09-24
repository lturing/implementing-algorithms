# https://en.wikipedia.org/wiki/K-d_tree

import random 
import numpy as np 
import matplotlib.pyplot as plt 

class Node:
    def __init__(self):
        self.val = 0
        self.split_idx = 0 
        self.right = None
        self.left = None

        # bounding box 
        self.bottom_left_x = 0 
        self.bottom_left_y = 0 
        self.top_right_x = 0 
        self.top_right_y = 0 

        self.points = []

def generate_kd_tree(dataset):

    def plot(root):
        stack = [root]
        stride = 2
        if root:
            # draw global bounding box 
            b_x = root.bottom_left_x 
            b_y = root.bottom_left_y
            t_x = root.top_right_x 
            t_y = root.top_right_y

            '''
            y = [i for i in np.linspace(b_y, t_y, stride)]
            x = [b_x for i in np.linspace(b_y, t_y, stride)]
            plt.plot(x, y, 'black')
            x = [t_x for i in np.linspace(b_y, t_y, stride)]
            plt.plot(x, y, 'black')
            x = [i for i in np.linspace(b_x, t_x, stride)]
            y = [b_y for i in np.linspace(b_x, t_x, stride)]
            plt.plot(x, y, 'black')
            y = [t_y for i in np.linspace(b_x, t_x, stride)]
            plt.plot(x, y, 'black')
            '''

            plt.xlim(b_x, t_x)
            plt.ylim(b_y, t_y)
            plt.tick_params(labelsize=15)

        plt.title('kd tree', fontsize=20, fontweight=80, loc='center')

        while stack:
            son = []
            while stack:
                head = stack.pop()
                if head != None:
                    if head.split_idx == 0:
                        y = [i for i in np.linspace(head.bottom_left_y, head.top_right_y, stride)]
                        x = [head.val for i in np.linspace(head.bottom_left_y, head.top_right_y, stride)]
                    else:
                        x = [i for i in np.linspace(head.bottom_left_x, head.top_right_x, stride)]
                        y = [head.val for i in np.linspace(head.bottom_left_x, head.top_right_x, stride)]
                    plt.plot(x, y)
                    if head.points:
                        x = [point[0] for point in head.points]
                        y = [point[1] for point in head.points]
                        plt.scatter(x, y, c='black', marker='.', s=80)
                    if head.left:
                        son.append(head.left)
                    if head.right:
                        son.append(head.right)

            stack = son 

        plt.show()

    def generate(split_idx, dataset, root, bbox, feat_len):
        split_idx = split_idx % feat_len 
        dataset = sorted(dataset, key=lambda asd:asd[split_idx])
        d_len = len(dataset)
        median = dataset[d_len//2][split_idx] if d_len % 2 == 1 else (dataset[d_len//2-1][split_idx]+dataset[d_len//2][split_idx])/2
        left = []
        right = []

        for item in dataset:
            if item[split_idx] < median:
                left.append(item)
            elif item[split_idx] > median:
                right.append(item)
            else:
                root.points.append(item)

        root.val = median 
        root.split_idx = split_idx 
        root.bottom_left_x = bbox[0]
        root.bottom_left_y = bbox[1]
        root.top_right_x = bbox[2]
        root.top_right_y = bbox[3]

        if left:
            root.left = Node()
            if split_idx == 0:
                new_bbox = [bbox[0], bbox[1], median, bbox[3]]
            else:
                new_bbox = [bbox[0], bbox[1], bbox[2], median]
            generate(split_idx+1, left, root.left, new_bbox, feat_len)

        if right:
            root.right = Node()
            if split_idx == 0:
                new_bbox = [median, bbox[1], bbox[2], bbox[3]]
            else:
                new_bbox = [bbox[0], median, bbox[2], bbox[3]]
            generate(split_idx+1, right, root.right, new_bbox, feat_len)

    boundbox = [] # bottom_left_x, bottom_left_y, top_right_x, top_right_y
    func = [min, max]
    for i in range(4):
        boundbox.append(func[i//2%2]([dataset[j][i%2] for j in range(len(dataset))]))

    delta = 0.1
    for i in range(2):
        add = (boundbox[i+2]-boundbox[i])*delta
        add = 1 if add < 1 else int(add)
        boundbox[i] = boundbox[i] - add 
        boundbox[i+2] = boundbox[i+2] + add 

    root = Node()
    feat_len = len(dataset[0])
    generate(0, dataset, root, boundbox, feat_len)
    plot(root)


dataset = [(random.randint(1, 30), random.randint(1, 30)) for i in range(50)]
generate_kd_tree(dataset)
