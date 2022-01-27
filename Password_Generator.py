import random



#list of possible charaters  
char = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","@","#","$","%","^","&","*","1","2","3","4","5","6","7","8","9","0"]

i = 1


#assigns the charters 
char1 = (random.choice(char))
char2 = (random.choice(char))
char3 = (random.choice(char))
char4 = (random.choice(char))
char5 = (random.choice(char))
char6 = (random.choice(char))
char7 = (random.choice(char))
char8 = (random.choice(char))
char9 = (random.choice(char))
char10 = (random.choice(char))
char11 = (random.choice(char))
char12 = (random.choice(char))
char13 = (random.choice(char))
char14 = (random.choice(char))
char15 = (random.choice(char))
char16 = (random.choice(char))
char17 = (random.choice(char))
char18 = (random.choice(char))
char19 = (random.choice(char))
char20 = (random.choice(char))








while i == 1: 

    #asks for amout of charters 
    que = input("how long do you want your password to be Max 20: ")

#Gives Password
    #1
    if que == str(1):
        print("Your password is: " + char1)
        i = 2
    #2
    elif que == str(2):
        print("Your password is: " + char1+char2)
        i = 2
    #3
    elif que == str(3):
        print("Your password is: " + char1+char2+char3)
        i = 2
    #4
    elif que == str(4):
        print("Your password is: " + char1+char2+char3+char4)
        i = 2
    #5
    elif que == str(5):
        print("Your password is: " + char1+char2+char3+char4+char5)
        i = 2
    #6
    elif que == str(6):
        print("Your password is: " + char1+char2+char3+char4+char5+char6)
        i = 2
    #7
    elif que == str(7):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7)
        i = 2
    #8
    elif que == str(8):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7+char8)
        i = 2
    #9
    elif que == str(9):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7+char8+char9)
        i = 2
    #10
    elif que == str(10):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10)
        i = 2
    #11
    elif que == str(11):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11)
        i = 2
    #12
    elif que == str(12):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12)
        i = 2
    #13
    elif que == str(13):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13)
        i = 2
    #14
    elif que == str(14):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14)
        i = 2
    #15
    elif que == str(15):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14+char15)
        i = 2
    #16
    elif que == str(16):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14+char15+char16)
        i = 2
    #17
    elif que == str(17):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14+char15+char16+char17)
        i = 2
    #18
    elif que == str(18):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14+char15+char16+char17+char18)
        i = 2
    #19
    elif que == str(19):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14+char15+char16+char17+char18+char19)
        i = 2
    #20
    elif que == str(20):
        print("Your password is: " + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14+char15+char16+char17+char18+char19+char20)
        i = 2

        
    #if not a number 1-20
    else:
        print("Pick a number 1-20")

quit()
