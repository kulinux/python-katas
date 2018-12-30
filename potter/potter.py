

def remove_dif(books):
    diff = []
    res = []
    res.extend(books)

    for book in books:
        if book not in diff:
           diff.append(book)
           res.remove(book)
    return diff, res


def naive_price(books):
    if len(books) == 5: return 8 * 5 * 0.75
    if len(books) == 4: return 8 * 4 * 0.80
    if len(books) == 3: return 8 * 3 * 0.90
    if len(books) == 2: return 8 * 2 * 0.95
    if len(books) == 1: return 8 * 1
    return 0


def price(books):
    diff, res = remove_dif(books)
    total = naive_price(diff)
    while len(res) > 0:
        total = total + naive_price(diff)
        diff, res = remove_dif(res)

    return total




