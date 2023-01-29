import itertools

def pairsum(vals, target):
    return sorted([(a, b) for a, b in itertools.combinations(vals, 2) if a + b == target])

if __name__ == "__main__":
    vals= [3, 2, 6, 1, 5, 4]
    target = 7
    print(pairsum(vals, target))