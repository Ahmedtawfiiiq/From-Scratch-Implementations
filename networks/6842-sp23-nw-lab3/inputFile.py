# 6,10
# u,v,2
# u,w,5
# u,x,1
# x,v,2
# v,w,3
# x,w,3
# w,y,1
# x,y,1
# w,z,5
# y,z,2


def takeInput():
    n, m = input().split(",")

    lines = []
    for _ in range(int(m)):
        lines.append(input())

    d = {}
    for line in lines:
        line = line.split(",")
        src = line[0]
        dst = line[1]
        weight = line[2]
        if src not in d:
            d[src] = {}
        d[src][dst] = weight

    # check if all nodes are present
    for line in lines:
        line = line.split(",")
        src = line[0]
        dst = line[1]
        if dst not in d:
            d[dst] = {}

    return d
