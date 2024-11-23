min_val = float('inf')
count = [0]

def dfs(root, max_sofar):
    if not root:
        return 
    
    if root.val >= max_sofar:
        count[0] += 1
    max_sofar = max(max_sofar, root.val)

    dfs(root.left, max_sofar)
    dfs(root.right, max_sofar)

    

print(count[0], min_val)
    
    
