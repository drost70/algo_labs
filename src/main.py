import math


def minEatingSpeed(piles, h):
    def canEatAll(piles, k, h):
        hours_required = 0
        for pile in piles:
            hours_required += math.ceil(pile / k)
        return hours_required <= h

    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2
        if canEatAll(piles, mid, h):
            right = mid
        else:
            left = mid + 1

    return left


piles1 = [3, 6, 7, 11]
h1 = 8
print(minEatingSpeed(piles1, h1))

piles2 = [30, 11, 23, 4, 20]
h2 = 5
print(minEatingSpeed(piles2, h2))

piles3 = [30, 11, 23, 4, 20]
h3 = 6
print(minEatingSpeed(piles3, h3))
