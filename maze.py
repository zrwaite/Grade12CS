from random import shuffle, randrange
 
def make_maze(w = 16, h = 8):
    vis=[] #Empty array for something idk
    cols=[] #Array for vertical columns
    rows=[] #Array for horizontal rows
    for i in range(h):
        vis.append([0] * w + [1])
        cols.append(["|  "] * w + ['|'])
        rows.append(["+--"] * w + ['+'])
    vis.append([1] * (w + 1))
    cols.append([])
    rows.append(["+--"] * w + ['+'])
    for i in range(len(cols)):
        for b in range(len(rows[i])):
            print(rows[i][b], end="")
        print("")
        for b in range(len(cols[i])):
            print(cols[i][b], end="")
        print("")
    def walk(x, y):
        vis[y][x] = 1
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: rows[max(y, yy)][x] = "+  "
            if yy == y: cols[y][max(x, xx)] = "   "
            walk(xx, yy)
    walk(randrange(w), randrange(h))
 
    s = ""
    for (a, b) in zip(rows, cols):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s
 
if __name__ == '__main__':
    print(make_maze())