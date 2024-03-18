#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    a = arr[::-1]
    for j in range(len(a)):
        print(a[j], end=' ')
