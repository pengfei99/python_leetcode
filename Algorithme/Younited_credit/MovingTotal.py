"""
The append method allows you to add element into the list. Then the contains can return a bool value, if the sum
of any 3 consecutive numbers in the list equals to the given input, then return true, else return false

The easiest way is to test all the possibilities, but this will has O(n power n ) exponential time complexity
Can you find out a way to solve the question in polynomial time complexity
"""


class MovingTotal:
    def __init__(self):
        self.data = []

    def fac(self, i):
        (3 / 2) * (self.data[i] + self.data[i + 2])

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        for item in numbers:
            self.data.append(item)

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        mid = total / 3
        for i in range(0, len(self.data) - 2):
            current = self.data[i] + self.data[i + 1] + self.data[i + 2]
            if current == total:
                return True
        return False


if __name__ == "__main__":
    movingtotal = MovingTotal()

    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))

    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
