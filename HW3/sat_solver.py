# TODO: Your name, Cornell NetID
# TODO: Your Partner's name, Cornell NetID

from helpers import *
from cnf_sat_solver import dpll

# DO NOT CHANGE SAT_solver 
# Convert to Conjunctive Normal Form (CNF)
"""
>>> to_cnf_gadget('~(B | C)')
(~B & ~C)
"""
def to_cnf_gadget(s):
    s = expr(s)
    if isinstance(s, str):
        s = expr(s)
    step1 = parse_iff_implies(s)  # Steps 1
    step2 = deMorgansLaw(step1)  # Step 2
    return distibutiveLaw(step2)  # Step 3

# ______________________________________________________________________________
# STEP1: if s has IFF or IMPLIES, parse them

# TODO: depending on whether the operator contains IMPLIES('==>') or IFF('<=>'),
# Change them into equivalent form with only &, |, and ~ as logical operators
# The return value should be an Expression (e.g. ~a | b )

# Hint: you may use the expr() helper function to help you parse a string into an Expr
# you may also use the is_symbol() helper function to determine if you have encountered a propositional symbol
def parse_iff_implies(s):
    # TODO: write your code here, change the return values accordingly
    new_str = str(s)
    #x = prop_symbols(s)
    #x = expr_handle_infix_ops(s)
    #print(s)

    #s = expr(s)

    # s = "(~(P ==> Q)) | (R ==> P)"

    # #s = "A <=> B"
    s = expr(s)
    #print(str(s.args[0]))
    #print(s.__repr__)

    # s = "A <=> B"

    # s = "(~(P ==> Q)) | (R ==> P)"
    # s = expr(s)

    # new_str = str(s)
    # print("Input: " + str(s))

    # print(s.args)



    def recursiveBoy(arg):
        # print(arg)
        if (arg.op == "<=>" ):
            term1 = Expr('~', arg.args[0])
            term2 = Expr('~', arg.args[1])

            term1 = Expr('|', term1,arg.args[1])
            term2 = Expr('|', term2,arg.args[0])

            return Expr('&', term1,term2)
        elif(arg.op == "==>"):
            term = Expr('~',arg.args[0])
            return Expr('|', term,arg.args[1])
        elif (arg.op == '~'):
            return Expr(arg.op, recursiveBoy(arg.args[0]))
        elif(arg.args==()):
            return arg
        elif (arg.args[0].args == () or arg.args[1].args == ()):#indexing out of range here
            if(arg.op=='~'):
                return Expr(arg.op, arg.args[0])
            else:
                return Expr(arg.op,arg.args[0],arg.args[1])
        else:
            if (len(arg.args)== 1): #Review this one too
                return Expr(arg.op, recursiveBoy(arg.args[0]))
            else:
                return Expr(arg.op,recursiveBoy(arg.args[0]), recursiveBoy(arg.args[1]))



    # exp_Array = recursiveBoy(s)
    # print(str(recursiveBoy(s)))
    # print("Original String: " + str(s))
    # print("val out:" + str(recursiveBoy(s)))
    return recursiveBoy(s)

    #return Expr(s.op, *args)

# ______________________________________________________________________________
# STEP2: if there is NOT(~), move it inside, change the operations accordingly.


# """ Example:
# >>> deMorgansLaw(~(A | B))
# (~A & ~B)
# """

# TODO: recursively apply deMorgansLaw if you encounter a negation('~')
# The return value should be an Expression (e.g. ~a | b )

# Hint: you may use the associate() helper function to help you flatten the expression
# you may also use the is_symbol() helper function to determine if you have encountered a propositional symbol
def deMorgansLaw(s):
    # TODO: write your code here, change the return values accordingly

    def recursiveBoy2ElectricBoogaloo(arg):
        if (is_symbol(str(arg)) == True):
            return arg
        else:
            if(arg.op=='~'):

                if(arg.args[0].args== ()):
                    return Expr('~',arg.args[0])
                elif(arg.args[0].op == '~'):
                    return recursiveBoy2ElectricBoogaloo(arg.args[0].args[0])
                elif(arg.args[0].op =='|' ):
                    return Expr('&', recursiveBoy2ElectricBoogaloo(Expr('~', arg.args[0].args[0])),  recursiveBoy2ElectricBoogaloo(Expr('~', arg.args[0].args[1])))
                elif (arg.args[0].op =='&' ):
                    return Expr('|', recursiveBoy2ElectricBoogaloo(Expr('~', arg.args[0].args[0])),
                                recursiveBoy2ElectricBoogaloo(Expr('~', arg.args[0].args[1])))
            else:
                return Expr(arg.op, recursiveBoy2ElectricBoogaloo(arg.args[0]), recursiveBoy2ElectricBoogaloo(arg.args[1]))


    # test = "(~(A&B) & (B|C) & ~(B&C))"
    test = "(~(A&B) & (B|C) & ~(B&C))"
    exp = s
    # print(str(exp.args))
    # print(s)

    op = exp.op
    args = exp.args
    # print(args)
    # V = str(associate(op, args))
    # print("original S: " + str(s))
    # print("associate v: "+V)
    # print("final output demorg: "+ str(recursiveBoy2ElectricBoogaloo(exp)))

    return recursiveBoy2ElectricBoogaloo(exp)

# ______________________________________________________________________________
# STEP3: use Distibutive Law to distribute and('&') over or('|')

#
# """ Example:
# >>> distibutiveLaw((A & B) | C)
# ((A | C) & (B | C))
# """

# TODO: apply distibutiveLaw so as to return an equivalent expression in CNF form
# Hint: you may use the associate() helper function to help you flatten the expression
def distibutiveLaw(s):
    # TODO: write your code here, change the return values accordingly
    def recursiveBoy3ReturnOfTheFreed(arg):
        # print(arg)
        #Issue here where return a None for some reason
        if (is_symbol(str(arg)) == True):
            return arg
        else:
            if(arg.op == '&'):
                # print("and")
                if (arg.args[0].args == () and arg.args[1].args == ()): #Fix this one
                    return Expr('&', arg.args[0], arg.args[1])
                elif (arg.args[1].args == () and arg.args[0].args[0].args == () ): #Fix this one
                    if (arg.args[0].op == '|'):
                        secondArgsleft = arg.args[0].args[0]
                        secondArgsright = arg.args[0].args[1]
                        rightSide = arg.args[1]
                        exp1 = Expr('&', secondArgsleft, rightSide)
                        exp2 = Expr('&', secondArgsright, rightSide)
                        return Expr('|', exp1, exp2)
                    else:
                        return Expr(arg.op, arg.args[0], arg.args[1])
                elif (arg.args[0].args == () and arg.args[1].args[0].args == ()): #Fix this one
                    if (arg.args[1].op == '|'):
                        secondArgsleft = arg.args[1].args[0]
                        secondArgsright = arg.args[1].args[1]
                        rightSide = arg.args[0]
                        exp1 = Expr('&', rightSide, secondArgsleft)
                        exp2 = Expr('&', rightSide, secondArgsright)
                        return Expr('|', exp1, exp2)
                    else:
                        return Expr(arg.op, arg.args[0], arg.args[1])
                elif (arg.args[0].args == ()):
                    if (arg.args[1].op == '|'):
                        secondArgsleft = arg.args[0]
                        secondArgsright = arg.args[1].args
                        exp1 = Expr('&', secondArgsleft, secondArgsright[0])
                        exp2 = Expr('&', secondArgsleft, secondArgsright[1])
                        return Expr('|', exp1, recursiveBoy3ReturnOfTheFreed(exp2))
                    else:
                        return Expr(arg.op, arg.args[0], arg.args[1])

                elif (arg.args[1].args == ()):
                    if (arg.args[0].op == '|'):
                        secondArgsleft = arg.args[0].args
                        secondArgsright = arg.args[1]
                        exp1 = Expr('&', secondArgsleft[0], secondArgsright)
                        exp2 = Expr('&', secondArgsleft[1], secondArgsright)
                        return Expr('|', recursiveBoy3ReturnOfTheFreed(exp1), exp2)
                    else:
                        return Expr(arg.op, arg.args[0], arg.args[1])
                else:  # recurse more
                    # print("In the else")
                    return Expr('&', recursiveBoy3ReturnOfTheFreed(arg.args[0]),
                                recursiveBoy3ReturnOfTheFreed(arg.args[1]))
            elif (arg.op =='|'):
                # print("or")
                if (arg.args[0].args == () and arg.args[1].args == ()): #Fix this one
                    # print("entered1")
                    return Expr('|', arg.args[0], arg.args[1])
                elif ( arg.args[1].args == ()and arg.args[0].args[0].args == ()): #Fix this one
                    # print("here1")
                    if (arg.args[0].op == '&'):
                        secondArgsleft = arg.args[0].args[0]
                        secondArgsright = arg.args[0].args[1]
                        rightSide = arg.args[1]
                        exp1 = Expr('|', secondArgsleft, rightSide)
                        exp2 = Expr('|', secondArgsright, rightSide)
                        return Expr('&', exp1, exp2)
                    else:
                        return Expr(arg.op, arg.args[0], arg.args[1])
                elif (arg.args[0].args == () and arg.args[1].args[0].args == ()): #Fix this one
                    # print("here2")
                    if (arg.args[1].op == '&'):
                        secondArgsleft = arg.args[1].args[0]
                        secondArgsright = arg.args[1].args[1]
                        rightSide = arg.args[0]
                        exp1 = Expr('|', rightSide, secondArgsleft)
                        exp2 = Expr('|', rightSide, secondArgsright)
                        return Expr('&', exp1, exp2)
                    else:
                        return Expr(arg.op, arg.args[0], arg.args[1])
                elif (arg.args[0].args == ()):
                    # print("entered2")
                    if (arg.args[1].op == '&'):
                        secondArgsleft = arg.args[0]
                        secondArgsright = arg.args[1].args
                        exp1 = Expr('|',secondArgsleft,secondArgsright[0])
                        exp2 = Expr('|',secondArgsleft,secondArgsright[1])
                        return Expr('&', exp1, recursiveBoy3ReturnOfTheFreed(exp2))
                    else:
                        return Expr(arg.op, arg.args[0], arg.args[1])

                elif(arg.args[1].args == ()):
                    # print("3")
                    # print(str(arg.args[0].args[0]))
                    if (arg.args[0].op == '&'):
                        secondArgsleft = arg.args[0].args
                        secondArgsright = arg.args[1]
                        exp1 = Expr('|',secondArgsleft[0],secondArgsright)
                        exp2 = Expr('|',secondArgsleft[1],secondArgsright)
                        return Expr('&', recursiveBoy3ReturnOfTheFreed(exp1), exp2)
                    else:
                        return Expr(arg.op, arg.args[0], arg.args[1])


                else:  # recurse more
                    # print("4")
                    return Expr("|", recursiveBoy3ReturnOfTheFreed(arg.args[0]),
                                recursiveBoy3ReturnOfTheFreed(arg.args[1]))
            else: #recurse more
                # print("In the else")
                return Expr(arg.op,recursiveBoy3ReturnOfTheFreed(arg.args[0]))

    # print(str(recursiveBoy3ReturnOfTheFreed(expr(s))))

    # test = "((A | B) & C)"
    exp = expr(s)
    # print("Input here" + str(s))
    # print("Return val: " + str(recursiveBoy3ReturnOfTheFreed(exp)))
    return recursiveBoy3ReturnOfTheFreed(exp)


# ______________________________________________________________________________

# DO NOT CHANGE SAT_solver 
# Check satisfiability of an arbitrary looking Boolean Expression.
# It returns a satisfying assignment(Non-deterministic, non exhaustive) when it succeeds.
# returns False if the formula is unsatisfiable
# Don't need to care about the heuristic part


# """ Example:
# >>> SAT_solver(A |'<=>'| B) == {A: True, B: True}
# True
# """
#
# """ unsatisfiable example:
# >>> SAT_solver(A & ~A )
# False
# """
def SAT_solver(s, heuristic=no_heuristic):
    return dpll(conjuncts(to_cnf_gadget(s)), prop_symbols(s), {}, heuristic)


if __name__ == "__main__":

# Initialization
    A, B, C, D, E, F = expr('A, B, C, D, E, F')
    P, Q, R = expr('P, Q, R')

# Shows alternative ways to write your expression
    assert SAT_solver(A | '<=>' | B) == {A: True, B: True}
    assert SAT_solver(expr('A <=> B')) == {A: True, B: True}

# Some unsatisfiable examples
    assert SAT_solver(P & ~P) is False
    # The whole expression below is essentially just (A&~A)
    assert SAT_solver((A | B | C) & (A | B | ~C) & (A | ~B | C) & (A | ~B | ~C) & (
        ~A | B | C) & (~A | B | ~C) & (~A | ~B | C) & (~A | ~B | ~C)) is False

# This is the same example in the instructions.
    # Notice that SAT_solver's return value  is *Non-deterministic*, and *Non-exhaustive* when the expression is satisfiable,
    # meaning that it will only return *a* satisfying assignment when it succeeds.
    # If you run the same instruction multiple times, you may see different returns, but they should all be satisfying ones.
    result = SAT_solver((~(P | '==>' | Q)) | (R | '==>' | P))
    assert pl_true((~(P | '==>' | Q)) | (R | '==>' | P), result)

    assert pl_true((~(P | '==>' | Q)) | (R | '==>' | P), {P: True})
    assert pl_true((~(P | '==>' | Q)) | (R | '==>' | P), {Q: False, R: False})
    assert pl_true((~(P | '==>' | Q)) | (R | '==>' | P), {R: False})

# Some Boolean expressions has unique satisfying solutions
    assert SAT_solver(A & ~B & C & (A | ~D) & (~E | ~D) & (C | ~D) & (~A | ~F) & (E | ~F) & (~D | ~F) &
                      (B | ~C | D) & (A | ~E | F) & (~A | E | D)) == \
        {B: False, C: True, A: True, F: False, D: True, E: False}
    assert SAT_solver(A & B & ~C & D) == {C: False, A: True, D: True, B: True}
    assert SAT_solver((A | (B & C)) | '<=>' | ((A | B) & (A | C))) == {
        C: True, A: True} or {C: True, B: True}
    assert SAT_solver(A & ~B) == {A: True, B: False}

# The order in which the satisfying variable assignments get returned doen't matter.
    assert {A: True, B: False} == {B: False, A: True}
    print("No assertion errors found so far")
