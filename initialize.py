import numpy as np
import generators as ge
import nbformat as nbf
from IPython.core.getipython import get_ipython
from IPython import get_ipython

ip = get_ipython()
hm=ip.history_manager


def question(n):
    return f'{n}. ' + ge.QHA[f'q{n}']

def answer(n):
    return ge.QHA[f'a{n}']

def hint(n):
    return ge.QHA[f'h{n}']

def draw(attempts):
    shell = get_ipython()
    payload = dict(
            source='set_next_input',
            text=f'_guesser(answer,1,{attempts})\n\n',
            replace=False,
        )

    shell.payload_manager.write_payload(payload, single=True)

def get_current_session_id():
    return hm.get_last_session_id()

def output_session_history(current_session):
    return [i for i in hm.get_range()]

def output_question(n):
    print(f'{question(n)}')

def _guesser(answer,n,attempts):
    if attempts == 2:
        print(f'the answer is: {answer(n)}')
        return 

    current_session = get_current_session_id()
    session_history = output_session_history(current_session)
    guess = session_history[2][2].split('\n')[2]

    if guess == answer(n):
        print(f'good job')
        return 

    if attempts < 2:
        print(hint(n) + '\n')
        attempts += 1
        draw(attempts)


def guesser(answer,n,attempts,limit):
    #attempss,limit = 0,2
    current_session = get_current_session_id()
    session_history = output_session_history(current_session)
    guess = session_history[2][2].split('\n')[2]


    while True:
        guess = session_history[2][2].split('\n')[2]
        #print(attempts, guess)

        if guess == answer(n):
            print('good job')
            break

        if attempts < limit:
            print(hint(n) + '\n')
            attempts += 1
            draw(attempts)

        else:
            print(f'the answer is: {answer(n)}')
            break


def pick():
    n = np.random.randint(1,2)
    attempts,limit = 0,2
    current_session = get_current_session_id()
    session_history = output_session_history(current_session)
    #print(f'{question(n)}')''

    output_question(n)
    draw(0)
    
    
    

