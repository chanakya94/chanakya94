import random
def rps():
    user = input ( "enter your action :" )  # Asking user to enter their choice
    action = [ 'r','p' , 's' ]
    computer = random.choice ( action )  # system selecting choice randomly
    print ( "computer's choice:" , computer )  # printing system's random choice

    if user == computer :  # checking if user's and system's choices are same
        return print ( "it's a tie" )
    if not winnercheck ( user , computer ) :  #checking if user has won
        if winnercheck(user,computer) != True: #checking if system has won
            return print("computer has won" )
        return
    return print("you have won" )

def winnercheck(user,computer): #defining the function winnercheck
    if(user=='r' and computer=='s') or (user=='p' and computer=='s') or (user=='p' and computer=='r'): #checking for all possibilities of winning
        return True
rps() #calling the function