import pandas as pd
import operator
import sys

ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.div,
        '%' : operator.mod,
        '^' : operator.xor,
        '**': operator.pow
        }


def evaluate(x):
    return getattr(sys.modules[__name__],x)

def dict(index_list, A_list, B_list, C_list):
    d = {
            'A' : pd.Series( A_list, index = index_list ),
            'B' : pd.Series( B_list, index = index_list ),
            'C' : pd.Series( C_list, index = index_list )
        }
    return d

def entry(input):
    input_list = input.split(' = ')
    input_list = [input_list[0][0], int(input_list[0][1:]) - 1, input_list[1]]
    #print input_list

    evaluate(input_list[0])[input_list[1]] = int(input_list[2])

    d = dict(indexes, A, B, C)
    df = pd.DataFrame(d)
    return df

def set_expression(input):

    input_list = input.split(' ')
    #print input_list
    input_list = [input_list[0][0], int(input_list[0][1:]) - 1, input_list[1], input_list[2][0], int(input_list[2][1:]) - 1, input_list[3], input_list[4][0], int(input_list[4][1:]) - 1]
    #print input_list

    evaluate(input_list[6])[input_list[7]] = ops[input_list[2]](int(evaluate(input_list[0])[input_list[1]]),int(evaluate(input_list[3])[input_list[4]]))

    d = dict(indexes, A, B, C)
    df = pd.DataFrame(d)#, index=[1, 2, 3], columns=['A', 'B', 'C'])
    print df

indexes = [1, 2, 3]
A = [0] * len(indexes)
B = [0] * len(indexes)
C = [0] * len(indexes)
d = dict(indexes, A, B, C)
df = pd.DataFrame(d)
print df

while True:
    main_input = str(raw_input("Action List: \n 1) Set Value \n 2) Set Expression \n 3) Exit \nEnter your action choice:\t"))
    if main_input == '1':
        input_1 = str(raw_input("Enter Set Value Command \t"))
        #input_1 = "C1 = 11"
        print entry(input_1)
    if main_input == '2':
        input_2 = str(raw_input("Enter Set Expression Command \t"))
        print set_expression(input_2)
    if main_input == '3':
        print "Bye!"
        exit()
    else:
        print "Please enter 1 or 2 or 3 as per the actions listed"
