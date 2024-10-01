import matplotlib.pyplot as plt
import numpy as np 
import time
from tkinter import *
from tkinter import ttk


# np.random.seed(123)
n = 8
rq, cq = n, n
x_start = np.arange(1, rq + 1, 1, dtype=np.int16)
a = np.random.random((rq, cq))

b = a @ x_start

ir = [i for i in range(rq)]
ic = [i for i in range(cq)]


def get_row_max_el(exc=[]):
    res_i, res_max = 0, 0
    for k, i in enumerate(ir):
        if k in exc:
            continue
        
        j = 0
        while a[i][j] == 0:
            j += 1

        if abs(a[i][j]) > res_max:
            res_max = abs(a[i][j])
            res_i = k

    return res_i


def get_col_max_el(exc=[]):
    res_i, res_max = 0, 0
    for k, i in enumerate(ic):
        if k in exc:
            continue
        
        j = 0
        while a[j][i] == 0:
            j += 1

        if abs(a[j][i]) > res_max:
            res_max = abs(a[j][i])
            res_i = k

    return res_i


def swap_rows(i, j):
    ir[i], ir[j] = ir[j], ir[i]


def swap_cols(i, j):
    ic[i], ic[j] = ic[j], ic[i]


def to_tringle(swp='c'):
    exclusion = []
    if swp == 'r':
        for i in range(rq):
            j = get_row_max_el(exc=exclusion)
            exclusion.append(i)
            swap_rows(i, j)
            b[ir[i]] = b[ir[i]] / a[ir[i]][i]
            a[ir[i]] = a[ir[i]] / a[ir[i]][i]


            for k in range(i + 1, rq):
                # print('bb', b[ir[k]], b[ir[i]], k, i)
                b[ir[k]] = b[ir[k]] - b[ir[i]] * a[ir[k]][i]
                a[ir[k]] = a[ir[k]] - a[ir[i]] * a[ir[k]][i]
    elif swp == 'c':
        for i in range(cq):
            j = get_col_max_el(exc=exclusion)
            exclusion.append(i)
            swap_cols(i, j)
            b[ir[i]] = b[ir[i]] / a[ir[i]][i]
            a[ir[i]] = a[ir[i]] / a[ir[i]][i]


            for k in range(i + 1, cq):
                b[ir[k]] = b[ir[k]] - b[ir[i]] * a[ir[k]][i]
                a[ir[k]] = a[ir[k]] - a[ir[i]] * a[ir[k]][i]
    else:
        for i in range(cq):
            b[ir[i]] = b[ir[i]] / a[ir[i]][i]
            a[ir[i]] = a[ir[i]] / a[ir[i]][i]

            for k in range(i + 1, cq):
                b[ir[k]] = b[ir[k]] - b[ir[i]] * a[ir[k]][i]
                a[ir[k]] = a[ir[k]] - a[ir[i]] * a[ir[k]][i]


def get_ans(start_order=True):
    res = np.zeros(rq, dtype=np.float16)
    for k, i in enumerate(ir[::-1]):
        res[rq - k - 1] = b[i] - a[i] @ res

    return res


to_tringle(swp='c')
print(get_ans())