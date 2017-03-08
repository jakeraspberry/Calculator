#Calculator10.py
#Jacob Laframboise March 6, 2017
#A calculator which can take an expression involving addition, subtraction, multiplication, division, exponents, and brackets with positive and negative numbers

#Code to quickly run program with a constant input instead of getting user input
#input1='(-17)+(44/6*11^2)-999'
#input1='44/6*11^2'
#inputList=list(input1)

#print('Original input: ', inputList)





def itemsToString(list1): #A function to make every item in a list a string
    list2=[]
    for i in list1:
        list2.append(str(i))
    return list2

def isNum(s): #function to determine whether an item is a number
    try:
        float(s)
        return True
    except ValueError:
        return False
    except IndexError:
        return False




#operation funtions:

def doExponents(inpList):
    for i in inpList:
        
        place=inpList.index(i)

        if i == '^':
            inpList[inpList.index(i)] = float((inpList[inpList.index(i)-1]))**(float(inpList[inpList.index(i)+1])) #multiplies two items on either side of a '*' symbol
            inpList.pop(place+1)#removes item after '*'
            inpList.pop(place-1)#removes item before '*'
            #print(' = ',''.join(itemsToString(inpList))) #shows work
    return inpList

def doMultiply(inpList):
    for i in inpList:
            
        place=inpList.index(i)

        if i == '*':
            inpList[inpList.index(i)] = float(inpList[inpList.index(i)-1])*(float(inpList[inpList.index(i)+1]))
            inpList.pop(place+1)
            inpList.pop(place-1)
            #print(' = ',''.join(itemsToString(inpList))) #shows work
    return inpList


def doDivide(inpList):
    try: 
        for i in inpList:
                
            place=inpList.index(i)    
            if i == '/':
                inpList[inpList.index(i)] = float((inpList[inpList.index(i)-1]))/(float(inpList[inpList.index(i)+1]))
                inpList.pop(place+1)
                inpList.pop(place-1)
                #print(' = ',''.join(itemsToString(inpList))) #shows work
        return inpList
    except ZeroDivisionError:
        print('Cannot divide by zero, your answer is undefined.')
        inpList=[]

def doAdd(inpList):
    for i in inpList:
        
        place=inpList.index(i)    
        if i == '+':

            inpList[inpList.index(i)] = float(inpList[inpList.index(i)-1])+(float(inpList[inpList.index(i)+1]))
            inpList.pop(place+1)
            inpList.pop(place-1)
            #print(' = ',''.join(itemsToString(inpList))) #shows work
    return inpList


def doSubtract(inpList):
    for i in inpList:
            
        place=inpList.index(i)    
        if i == '-':
            inpList[inpList.index(i)] = float(inpList[inpList.index(i)-1])-(float(inpList[inpList.index(i)+1]))
            inpList.pop(place+1)
            inpList.pop(place-1)
            #print(' = ',''.join(itemsToString(inpList))) #shows work
    return inpList


#A function to run through order of operations on a selected list
def compute(expressionList):
    computedList = doExponents(expressionList)
    computedList = doMultiply(expressionList)
    computedList = doDivide(expressionList)
    computedList = doAdd(expressionList)
    computedList = doSubtract(expressionList)
    return computedList





#A function to group multidigit numbers together into one item

def digitGroup(inpList):
    reLoop=True

    while reLoop:

            reLoop=False #has to be false, will be set true if something is done
            posiCount=0
            for i in inpList:
                #double digit combine:
                place=inpList.index(i)

                try:
                    if i != inpList[-1] or inpList[-1]==inpList[-2]: #guarantees it wont check the one after the last item in the string
                        
                        if i=='-' and inpList[posiCount-1]=='(' : #code to deal with negative numbers, comments in this if statement were for debugging
                            #print('combining: ',inpList[posiCount], ' and ', inpList[posiCount+1]) 
                            inpList[posiCount]=str(inpList[posiCount]) + inpList[posiCount+1]
                            #print('inpList after combining: ', inpList)
                            #print('Going to pop ', inpList[posiCount+1])
                            inpList.pop(posiCount+1)
                            #print('inpList after popping: ', inpList)
                            reLoop=True

                        if isNum(i) and isNum(inpList[place+1]): #checks for see if the next two items are digits
                            
                            inpList[place]=inpList[place]+inpList[place+1] #combines digits into place of first digit
                            inpList.pop(place+1) #removes sole second digit item
                            #print(inpList) #shows multidigit number grouping steps
                            reLoop=True
                except IndexError: #prevents break apon just one numerical input
                    print("Your number is still ", input1, ", try giving me some actual expressions :)")
                posiCount+=1
    return(inpList)







#The main function, will call all other functions

def solve(inputList):
    inStringOrg=inputList#save original input
    print('Original input: ', inputList) #print original input
    inputList=list(inputList)
    #print('Original input: ', inputList) #print original input as string
    inputList=digitGroup(inputList) #group digits and merge negative signs
    reScan=True
    currentAnswer=7777777 #initializing
    
    while reScan==True:
        #print(' = ',''.join(itemsToString(inputList))) #shows each step of calculation, can be commented out for cleanliness
        
        reScan=False
        oBrackets=[] #store positions of open brackets
        smallestDiff=823745619 #initializing
        cBrackets=[]
        posiCount=0 #to zero index and initialize, variable stores current position in list

        for i in inputList: #scans for brackets and makes lists of positions
            if i=='(':
                #print('Found: ',i, ' as: ( in position: ', posiCount)
                oBrackets.append(posiCount)                
                #reScan=True #disabled to prevent infinite loop potential, done on close bracket only
            elif i ==')':
                #print('Found: ',i, ' as: ) in position: ', posiCount)
                cBrackets.append(posiCount)
                reScan=True
            posiCount+=1 #increase position

        for i in oBrackets: #function determines which open bracket is closest to the first close bracket, and the far it is to get the correct slice inside the bracket set
            if (smallestDiff==823745619 and oBrackets!=[] and cBrackets!=[]) or (cBrackets[0]-i < smallestDiff and cBrackets[0]-i > 0):
                smallestDiff=cBrackets[0]-i

        #print(smallestDiff)
        if smallestDiff != 823745619:    #if it has been set something else because it found a bracket set   
            toSolveList = inputList[cBrackets[0]-smallestDiff+1:cBrackets[0]]
        else:
            toSolveList=inputList


        '''
        #following 5 lines just print out to the user what the calculator is doing, can be commented out for cleaniness    
        print('Going to solve: ', toSolveList)
        if smallestDiff != 823745619:
            print('Replacing: ',inputList[cBrackets[0]-smallestDiff:cBrackets[0]+1],' with: ', compute(toSolveList))
        else:
            print('Replacing: ',inputList,' with: ', compute(toSolveList))
        '''

        #calls the compute function on either the slice between the brackets or the whole list when brackets are not present
        if smallestDiff != 823745619:
            inputList[cBrackets[0]-smallestDiff:cBrackets[0]+1]=compute(toSolveList)
        else:
            inputList=compute(toSolveList)
            
        

        if currentAnswer==inputList: #checks to see if anything was done on last loop
            finalAnswer=currentAnswer
            #reScan=False
        
        currentAnswer=inputList
        

    #make a nice final answer to output    
    finalAnswer=''.join(itemsToString(inputList))
    return(finalAnswer)


#print(solve(inputList))


#loop to get input from user and return an answer, then ask again until the user exits
cont=True #keep loop going
while cont==True:
    expression=input("Input your expression here: ")
    if expression=='exit':
        cont=False
    else:
        print(' = ',solve(expression))



