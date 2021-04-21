# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:37:17 2021.
Author: Evan Jones

Estimates pi using a pretty standard monte carlo algorithm:
Randomly generates a point in a unit square, the proportion within a radius of
1 from the origin to the total gives one quarter of pi

    pi = 4 * Nin / Ntotal

It then compares a pure python way to a numpy way, which is much faster as it
uses C compiled code.
"""
import random
import numpy as np
from time import perf_counter as timer


def pi_estimate_python(Ntotal):
    Nin = 0
    for i in range(Ntotal):
        x = random.random()
        y = random.random()

        if x*x + y*y < 1:
            Nin += 1

    return 4 * Nin / Ntotal


def pi_estimate_numpy(Ntotal):
    x, y = np.random.random((2, Ntotal))
    rsquared = x*x + y*y
    Nin = np.count_nonzero(rsquared < 1)
    return 4 * Nin / Ntotal


def main():
    niter = 1_000_000

    start = timer()
    iterative = pi_estimate_python(niter)
    stop = timer()
    print(f"pi = {iterative} for {niter} iterations. This took {stop-start} seconds")

    start = timer()
    vectorised = pi_estimate_numpy(niter)
    stop = timer()
    print(f"pi = {vectorised} for {niter} iterations. This took {stop-start} seconds")


if __name__ == "__main__":
    main()
