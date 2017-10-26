#Nicholas Marler
#This interpreter works by calling the B() function and passing in any string. It will print its result and return the bool value
#Example: B("((T))vF")
#Can test the code at the bottom.

#The main boolean statement to be evaluated
def B(s):
    if isEmpty(s): return print("Error. Incomplete Statement")
    answer, s = IT(s)
    if s[0] == '.':
        if len(s) == 1:
            print(answer)
            return answer
        if whiteSpace(s[1]): #Checks for being valid, but having spaces after the "."
            if removeAfterWhiteSpaces(s[1:]):
                print(answer)
                return answer
        return print("Error. Extra stuff after '.' ")
    return print("Error. Did not end statement with a '.'")

def IT(s):
    if isEmpty(s): print("Error. Incomplete Statement")
    answer, s = OT(s)
    return IT_TAIL(answer, s)

def IT_TAIL(answer, s):
    if isEmpty(s): return print("Error. Incomplete Statement")
    if whiteSpace(s[0]):
        return IT_TAIL(answer, s[1:])
    if s[0] in ".)":
        return answer, s
    if s[0] == "-":
        if s[1] == ">":
            new_answer, s = OT(s[2:])
            if answer == False:
                answer = True
            elif answer == True and new_answer == False:
                answer = False
            else:
                answer = True
            return IT_TAIL(answer, s)
        return print("Error. Must follow a '-' with a '>'")
    return print("Error. IT_TAIL")

def OT(s):
    if isEmpty(s): print("Error. Incomplete Statement")
    answer, s = AT(s)
    return OT_TAIL(answer, s)

def OT_TAIL(answer, s):
    if isEmpty(s): print("Error. Incomplete Statement")
    if whiteSpace(s[0]):
        return OT_TAIL(answer, s[1:])
    if s[0] in ".-)":
        return answer, s
    if s[0] == "v":
       new_answer, s = AT(s[1:])
       answer = new_answer or answer
       return OT_TAIL(answer, s)
    return print("Error. OT_TAIL")

def AT(s):
    if isEmpty(s): print("Error. Incomplete Statement")
    if whiteSpace(s[0]):
        return AT(s[1:])
    answer, s = L(s)
    return AT_TAIL(answer, s)
    
def AT_TAIL(answer, s):
    if isEmpty(s): print("Error. Incomplete Statement")
    if whiteSpace(s[0]):
        return AT_TAIL(answer, s[1:])
    if s[0] in ".v-)":
        return answer, s
    if s[0] == "^":
       new_answer, s = L(s[1:])
       answer = new_answer and answer
       return AT_TAIL(answer, s)
    return print("Error. OT_TAIL")

def L(s):
    if isEmpty(s): print("Error. Incomplete Statement")
    if whiteSpace(s[0]):
        return L(s[1:])
    if s[0] == "∼":
        answer, s = L(s[1:])
        return not answer, s  
    return A(s)

def A(s):
    if isEmpty(s): print("Error. Incomplete Statement")
    if whiteSpace(s[0]):
        return A(s[1:])
    if s[0] == "T":
        return True, s[1:]
    if s[0] == "F":
        return False, s[1:]
    if s[0] == "(":
        answer, s = IT(s[1:])
        if s[0] == ")":
            return answer, s[1:]
    return print("Error. A")

#Helper. Check for white space
def whiteSpace(s):
  return s == '\n' or s == '\r' or s == '\t' or s == ' '

#Helper. Check for Empty
def isEmpty(s):
  return len(s) == 0 

#Helper. Handles any white spaces after .
def removeAfterWhiteSpaces(s):
    if isEmpty(s): return True
    if whiteSpace(s[0]): return removeAfterWhiteSpaces(s[1:])
    return False

#You can type any statement here to test it
B("")