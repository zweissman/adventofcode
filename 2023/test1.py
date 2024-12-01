# map, filter, zip, decorator, closure, lambda, list comprehension, pep 8, monkey patching
# @property, @staticmethod, @classmethod, @dataclass
# operator , functools, ABC


def get_large(numbers, n):
    # numbers.sort()

    return sorted(numbers[-n:])


nums = [2, 3, 4, 1, 34, 123, 321, 1]

print(nums)
largest = get_large(nums, 2)
print(nums)
