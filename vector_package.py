#my personal, handrolled vector package
#design principles drawn from SICP chapter 2

#level 1
def cons_vec(*args):
    new_vec = {}
    for index, arg in enumerate(args):
        new_vec[index] = arg
    return new_vec

def sel_vec(vec, index):
    try:
        return vec[index]
    except:
        print("no value at that index")

def mut_vec(vec, index, val):
    vec[index] = val
    return vec

#ABSTRACTION LAYER

#level 2
def add_vec:

def sub_vec:

def mul_vec:

def div_vec:
