class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        parents = set()
        graph = defaultdict(list)

        for par, child, isLeft in descriptions:
            parents.add(par)
            children.add(child)
            graph[par].append((child, isLeft))

        #find root
        rootVal = None
        for p in parents:
            if p not in children:
                rootVal = p
                break

        #node cache
        nodes = {}
        nodes[rootVal] = TreeNode(rootVal)

        q = deque([nodes[rootVal]])

        while q:
            par = q.popleft()

            for childVal, isLeft in graph.get(par.val, []):
                if childVal not in nodes:
                    nodes[childVal] = TreeNode(childVal)

                child = nodes[childVal]
                if isLeft:
                    par.left = child
                else:
                    par.right = child

                q.append(child)

        return nodes[rootVal]
