import pdb
import itertools as iter

def intersection(left, right):
    return set(left).intersection(right)

def order(start, finish):
    return range(start, finish + 1)

def heavier(weights, pairs):
    for pair in pairs:
        if pair in weights:
            weights[pair] += 1
        else:
            weights[pair] = 1

    return weights

def pairs(l):
    l = list(l)
    result = []
    for i in l:
        try:
            result.append((i, l[l.index(i)+1]))
        except:
            pass

    return result

def print_dict(title, dictionary):
    print "%(title)s ===" % locals()
    for key in dictionary:
        print key, dictionary[key]
    print


# a -> c -> b | k -> e | g -> f -> d | h -> l  i -> j

orders = {
    "a -> b": order(1,3),
    "c -> d": order(2,6),
    "e -> f": order(4,5),
    "g -> h": order(4,6),
    "i -> j": order(8,9),
    "k -> l": order(3,7)
}

def main():
    solo = []
    candidates = {}

    for fst, snd in iter.combinations(orders, 2):
        fst_order, snd_order = orders[fst], orders[snd]
        overlap = intersection(fst_order, snd_order)

        if len(overlap) > 1:
            # track the two edges involved and the overlapping nodes
            candidates[(fst, snd)] = overlap

    # retain so that they can be cut after overlapping edges are dealt with
    # TODO get the non overlapped edges

    print_dict("Candidates", candidates)

    weighted_cuts = {}
    for fst, snd in iter.combinations(candidates, 2):
        fst_overlap = candidates[fst]
        snd_overlap = candidates[snd]
        overlap = intersection(fst_overlap, snd_overlap)

        print fst, snd, overlap

        if len(overlap) > 1:
            # take the pairs of the overlaping nodes and increase weights
            weighted_cuts = heavier(weighted_cuts, pairs(overlap))

    print_dict("Weighted Fences", weighted_cuts)


if __name__ == "__main__":
    main()
