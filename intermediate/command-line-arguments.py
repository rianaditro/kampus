import argparse

"""
Handling command line arguments in Python
It adds flexibility, improves automation, and
enhances the scalability and usability of your scripts. 

It easier to work with your scripts if we can pass parameters dynamically rather than
needing to change the code each time.
"""

# simple example
def sum_numbers(a, b):
    print(a + b)


if __name__ == "__main__":
    # example of running normally
    # sum_numbers(1, 2)

    # what if we need to see if the program will return same output with different parameters
    # we can use argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--num1", type=int, )
    parser.add_argument("--num2", type=int)
    args = parser.parse_args()

    num1 = args.num1
    num2 = args.num2
    sum_numbers(args.num1, args.num2)