#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
from itertools import permutations

# decoration
print(stylize("\n---- | All permutations of a string | ----\n", fg("red")))

# class
class Permutations:
    def __init__(self, string):
        self.string = string

    # output magic method
    def __repr__(self):
        output = self.permutations(self.string)

        print(stylize(f"\nAll possible permutations of \"{self.string}\":", fg("green")))
        for i in output:
            print(i)

        return ""

    # methods
    def permutations(self, string):
        all_permutations = ["".join(p) for p in permutations(string)]
        return all_permutations

# main execution
if __name__ == "__main__":
    # user interaction
    string = input("Text: ")

    print(Permutations(string))
