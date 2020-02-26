# -*- coding: utf-8 -*-


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    w='Weird'
    nw='Not Weird'

    if n in range(1,101):
        if((2<=n<=5)&(n%2==0)):
            print(nw)
        elif((6<=n<=20)&(n%2==0)):
            print(w)
        elif((n>20)&(n%2==0)):
            print(nw)
        elif(n%2!=0):
            print(w)
    
