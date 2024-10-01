from collections import Counter

def can_be_poly(val: str) -> bool:
    counts = Counter(val)
    odd_count = len(list(filter(lambda x: x % 2, counts.values())))
    return odd_count < 2

print(can_be_poly('otto'))