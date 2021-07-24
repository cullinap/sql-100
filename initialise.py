import numpy as np
import gene as ge

def question(n):
    print(f'{n}. ' + ge.QHA[f'q{n}'])

def sqlquestion(n):
    print(f'{n}. ' + ge.SQLQHA[f'q{n}'])

def answer(n):
    print(ge.QHA[f'a{n}'])

def hint(n):
    print(ge.QHA[f'h{n}'])

def print_dataset(i):
    print(ge.QHA[f'd{i}'])
    print('\n')

def pick():
    n = np.random.randint(1,21)

    if 1 <= n <= 20:
        i = 1
        print_dataset(i)
        question(n)
        return 

    if 43 <= n <= 38:
        i = 2
        print_dataset(i)
        question(n)
        return 

    if 50 <= n <= 44:
        i = 3
        print_dataset(i)
        question(n)
        return 

    if 55 <= n <= 51:
        i = 4
        print_dataset(i)
        question(n)
        return 

    else:
        question(n)
        return

def intializeSQL():
    from sqlalchemy import create_engine
    engine = create_engine('sqlite://', echo=False)
    import pandas as pd
    from pandas.io import sql

def pickSQL():
    # fix hint and answer functions specific to sql
    n = np.random.randint(1,7)
    sqlquestion(n)










