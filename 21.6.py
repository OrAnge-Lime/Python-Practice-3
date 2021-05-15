wb_tree = []

def tree(t):
    black = []
    white = []
    white.append(t)
    white.append(t)
    black.append(white)
    black.append(white)
    black.append(white)
    tree(black)


tree(wb_tree)