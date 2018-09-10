# https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm

maps = {0:[2, 3], 1:[0], 2:[1], 3:[4], 4:[]}
maps = {1:[2],2:[1,5],3:[4],4:[3,5],5:[6],6:[7],7:[8],8:[6,9],9:[]}
maps = {1:[3, 2], 2:[4], 3:[4, 5], 4:[6, 1], 5:[6]}

index = {} # numbers the nodes consecutively in the order in which they are discovered.(named index)
lowlink = {} # represents the smallest index of any node known to be reached from v(v means the current node) # Therefore v must be left on the stack if v.lowlink < v.index
stack = []

def tarjan(v):
    index[v] = len(index)
    lowlink[v] = len(lowlink)
    stack.append(v)
    
    if v in maps:
        for u in maps[v]:
            if u not in index:
                tarjan(u)
                lowlink[v] = min(lowlink[v], lowlink[u])
            elif u in stack:
                lowlink[v] = min(lowlink[v], index[u])#Note that v.lowlink := min(v.lowlink, w.index) is the correct way to update v.lowlink if w is on stack. Because w is on the stack already, (v, w) is a back-edge in the DFS tree and therefore w is not in the subtree of v. Because v.lowlink takes into account nodes reachable only through the nodes in the subtree of v we must stop at w and use w.index instead of w.lowlink.

        if index[v] == lowlink[v]:
            scc = [] # strongly connected component
            while True:
                head =  stack.pop()
                scc.append(head)
                if head == v:
                    break 

            print(scc)

for k in maps:
    if k not in index:
        tarjan(k)
