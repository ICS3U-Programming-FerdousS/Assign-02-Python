#!/usr/bin/env python3
# Created by: Ferdous Sediqi
# Created on: March 1st, 2022
# This program asks the user for the radius and
# height of the Cylinder. then, calculates and displays
# the total volume and surface area of the Cylinder.

import math


def main():

    # input

    radius = float(input("Enter the radius is cm: "))
    height = float(input("Enter the height is cm: "))
    print("")

    # clculate

    volume = math.pi * radius * radius * height
    area_fourmula1 = 2 * math.pi * radius * height
    area_fourmula2 = 2 * math.pi * radius * radius
    total_area = area_fourmula1 + area_fourmula2

    # output the answer
    print("The volume of the Cylinder is = {:.2f}" .format(volume), "cm")
    print("")
    print("The total surface area of the Cylinder is = {:.2f}"
          .format(total_area), "cm^2")


if __name__ == "__main__":
    main()
