import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2, -100, 100]
print(heapq.nlargest(2, nums))
print(heapq.nsmallest(1, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print("cheap 1, 2, 3")
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['price'])
print("expensive No1")
print(expensive)

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2, -100, 100]
heap = list(nums)
print("1:", heap)
heapq.heapify(heap)
print("2:", heap)
