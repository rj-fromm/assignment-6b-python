#!/usr/bin/env python3

# Created by: RJ Fromm
# Created on: november 2019
# This show two functions
import math

def calculate_area(radius):
    # process
    area = (radius ** 2 * math.pi)/2
    print("The area is {0}".format(area))


def main():
    while True:
        radius_of_circle = input("Enter the radius of the circle: ")
        try:
            radius_user_int = int(radius_of_circle)

            calculate_area(radius_user_int)
            break
        except Exception:
            print("that is not a number")


if __name__ == "__main__":
    main()
