def overlap(left, right):
    return len(intersection(left, right)) > 0

def intersection(left, right):
    return set(left).intersection(right)

def order(start, finish):
    return range(start, finish + 1)

def heavier_all(weighted_cut, pairs):
    new_weights = []
    edges, nodes, weights = weighted_cut

    for pair in pairs:
        new_weight = 1
        for (nodes, weight) in weights:
            if pair == nodes:
                new_weight = weight+1
                pairs.remove(pair)
                new_weights.append((pair, new_weight))

    # left overs
    for pair in pairs:
        new_weights.append((pair, 1))

    return (edges, nodes, new_weights)

def heavier(weighted_cut):
    edges, nodes, weight = weighted_cut
    return (edges, nodes, weight + 1)

def pairs(l):
    l = list(l)
    result = []
    for i in l:
        try:
            result.append((i, l[l.index(i)+1]))
        except:
            pass

    return result

# a -> c -> b -> e -> f -> d  i -> j

orders = [
    ("a -> b", order(1,3)),
    ("c -> d", order(2,6)),
    ("e -> f", order(4,5)),
    ("g -> h", order(4,6)),
    ("i -> j", order(8,9))
]

def main():
    overlapping = set([])
    considered_pairs = []
    names = []
    candidates = []
    for (name, order) in orders:
        names.append(name)

        for (oth_name, cmpr) in orders:
            edges = [name, oth_name]
            index = None

            # check to see if the inverted pair is already in the set
            try:
                index = considered_pairs.index([oth_name, name])
            except ValueError:
                pass

            # skip id comparisons, or when the current pairs twin has been considered
            if order == cmpr or index != None:
                continue
            elif overlap(order, cmpr):
                # track the names of overlapping orders
                overlapping = overlapping.union(set([name, oth_name]))

                # track when a pair of edges has been considered so that the
                # reversed twin can be ignored
                considered_pairs.append(edges)

                # track the two edges involved and the overlapping nodes
                candidates.append((edges, intersection(order, cmpr)))

    # retain so that they can be cut after overlapping edges are dealt with
    solo = set(names).difference(overlapping)

    weighted_cuts = []
    for (edges, nodes) in candidates:
        weighted = (edges, nodes, [])

        for (oth_edges, cmpr) in candidates:

            # if the compared candidates are the same but "permuted"
            if len(set(edges).intersection(set(oth_edges))) > 1:
                continue
            elif overlap(nodes, cmpr):
                # when there's overlap increment
                # TODO pair the weight with the overlap portion
                weighted = heavier_all(weighted, pairs(intersection(nodes,cmpr)))

        weighted_cuts.append(weighted)

    for cut in weighted_cuts:
        print cut


if __name__ == "__main__":
    main()
