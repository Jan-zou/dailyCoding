'''
coding: utf-8
Conversion of Infix Expression to Postfix Expression
Created 2014-09-23
ZouJingLin <zjl_717@sina.com>
'''

from stack import Stack


def infixToPostfix(infixexpr):
    """
    Create an empty stack opStack for keep operators.
    Create an empty list for postfix expression.
    Split infix expression get evert token.
    Scan the token list to get postfix expression.
        - if the token is an number or char ,append it to the postfix list.
        - if the token is an operators or left parenthesis, push it on the stack.
        - if the token is an right parenthesis, pop the stack until the left parenthesis is removed.

    """
    prec = {"(":1, "+":2, "-":2, "*":3, "/":3}
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    aList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sList = aList.lower()
    nList = "0123456789"

    for token in tokenList:
        if token in aList or token in sList or token in nList:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return ' '.join(postfixList)


if __name__ == "__main__":
    print(infixToPostfix("a * B + C * D"))

