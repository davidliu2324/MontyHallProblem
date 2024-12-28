import random
#This simple math problem was brought up to me by a client of the gym I work at. Premise of the Monty Hall problem is simple:
#"Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?"

#We are told that if we switch our choice, our odds are better, namely by Savant. Our odds are set to increase from 1/3 to 2/3. I will run tests to see which method, over many trials, is better.

#Let method 1 be the method where we don't switch
#Let method 2 be the method where we do switch

doors = [0, 1, 2]

def method2(revealedGoatDoor, selectedDoor):
    switchedDoor = 0
    for i in range(len(doors)):
        if i != selectedDoor and i != revealedGoatDoor:
            switchedDoor = i
    return switchedDoor

#Running 100 tests
def hundredTests():
    method1CorrectGuesses = 0
    method2CorrectGuesses = 0
    for i in range(100):
        selectedDoor = random.randint(0,2)
        doorWithCar = random.randint(0,2)
        revealedGoatDoor = 0
    
        for j in range(len(doors)):
            if j != selectedDoor and j != doorWithCar:
                revealedGoatDoor = j
                break

        #Method 1
        if selectedDoor == doorWithCar:
            method1CorrectGuesses += 1
        
        #Method 2
        switchedDoor = method2(revealedGoatDoor, selectedDoor)
        if switchedDoor == doorWithCar:
            method2CorrectGuesses +=1
    
    method1SuccessRate = method1CorrectGuesses/100
    method2SuccessRate = method2CorrectGuesses/100

    print("If we dont switch the door, for 100 tests, we get a ", method1SuccessRate," success rate. If we switch the door, for 100 tests, we get a ", method2SuccessRate, " success rate.") 

#Running 10 000 tests
def tenThousandTests():
    method1CorrectGuesses = 0
    method2CorrectGuesses = 0
    for i in range(10000):
        selectedDoor = random.randint(0,2)
        doorWithCar = random.randint(0,2)
        revealedGoatDoor = -1
    
        for j in range(len(doors)):
            if j != selectedDoor and j != doorWithCar:
                revealedGoatDoor = j
                break

        #Method 1
        if selectedDoor == doorWithCar:
            method1CorrectGuesses += 1
        
        #Method 2
        switchedDoor = method2(revealedGoatDoor, selectedDoor)
        if switchedDoor == doorWithCar:
            method2CorrectGuesses +=1
    
    method1SuccessRate = method1CorrectGuesses/10000
    method2SuccessRate = method2CorrectGuesses/10000

    print("If we dont switch the door, for 10 000 tests, we get a ", method1SuccessRate," success rate. If we switch the door, for 10 000 tests, we get a ", method2SuccessRate, " success rate.") 

def millionTests():
    method1CorrectGuesses = 0
    method2CorrectGuesses = 0
    for i in range(1000000):
        selectedDoor = random.randint(0,2)
        doorWithCar = random.randint(0,2)
        revealedGoatDoor = -1
    
        for j in range(len(doors)):
            if j != selectedDoor and j != doorWithCar:
                revealedGoatDoor = j
                break

        #Method 1
        if selectedDoor == doorWithCar:
            method1CorrectGuesses += 1
        
        #Method 2
        switchedDoor = method2(revealedGoatDoor, selectedDoor)
        if switchedDoor == doorWithCar:
            method2CorrectGuesses +=1
    
    method1SuccessRate = method1CorrectGuesses/1000000
    method2SuccessRate = method2CorrectGuesses/1000000

    print("If we dont switch the door, for 1 000 000 tests, we get a ", method1SuccessRate," success rate. If we switch the door, for 1 000 000 tests, we get a ", method2SuccessRate, " success rate.") 

hundredTests()
tenThousandTests()
millionTests()