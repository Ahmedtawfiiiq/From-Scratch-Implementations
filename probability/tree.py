def tree_probability(transitions, cur, t, tosses):
    if tosses == 0:
        return cur == t
    p_target = 0
    for nxt, p in transitions[cur]:
        p_target += p * tree_probability(transitions, nxt, t, tosses - 1)
    return p_target


# transitions = {
#     0: [(0, 0.6), (1, 0.4)],
#     1: [(0, 0.3), (1, 0.7)],
# }

transitions = {
    0: [(0, 0.2), (1, 0.8)],
    1: [(0, 0.4), (1, 0.6)],
}

print(tree_probability(transitions, cur=0, t=1, tosses=2))
