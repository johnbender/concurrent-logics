def order(start, finish):
    return range(start, finish + 1)

def optimal_fences(orders):
    if len(orders) == 0:
        return []

    heaviest = None
    weights = {}

    # find the heaviest edge, that is the edge that appears most frequently
    # in all the orders under consideration. proceed pairwise
    for key in orders:
        current = orders[key]

        for num in current:
            if not num + 1 in current:
                continue

            edge = (num, num + 1)

            if not heaviest:
                heaviest = edge

            if edge in weights:
                weights[edge] += 1
            else:
                weights[edge] = 1

            if weights[edge] > weights[heaviest]:
                heaviest = edge

    start, end = heaviest
    unfenced = {}

    # only retain those orders unfenced at the heaviest edge
    for key in orders:
        current = orders[key]
        if not start in current or not end in current:
            unfenced[key] = current

    # recursively handle the unfenced edges
    result = [heaviest]
    result.extend(optimal_fences(unfenced))
    return result

def main():
    # a -> c -> b | k -> e | g -> f -> d | h -> l  i -> j
    orders = {
        "a -> b": order(1,3),
        "c -> d": order(2,6),
        "e -> f": order(4,5),
        "g -> h": order(4,6),
        "i -> j": order(8,9),
        "k -> l": order(3,7)
    }

    print optimal_fences(orders)

if __name__ == "__main__":
    main()
