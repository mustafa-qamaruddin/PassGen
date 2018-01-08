from custom import CHARSLIST
import networkx as nx

def customgen(password):
    vecs = []
    for chr in password:
        if chr == "?":
            vecs.append(CHARSLIST)
        else:
            vecs.append([chr])

    glossary = {}
    nodes = {}

    nodes[0] = [0]
    glossary[0] = ""

    for i in range(1, len(password)+1):
        nodes[i] = []

    idx = 1
    l = 1
    for vec in vecs:
        for node in vec:
            nodes[l].append(idx)
            glossary[idx] = node
            idx += 1
        l += 1

    elist = []
    for i in range(0, l):
        if i < l-1:
            for p in nodes[i]:
                for c in nodes[i+1]:
                    elist.append((p, c))

    G = nx.DiGraph()
    G.add_edges_from(elist)
    print(G.adj)
    return