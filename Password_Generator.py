import random



#list of possible charaters  
char = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","@","#","$","%","^","&","*","1","2","3","4","5","6","7","8","9","0"]

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

#asks for amout of charters 
que = input("how long do you want your password to be Max 20: ")


#gives Password 
#1
if que == str(1):
    print("Your password is:" + char1)
#2
elif que == str(2):
    print("Your password is:" + char1+char2)
#3
elif que == str(3):
    print("Your password is:" + char1+char2+char3)
#4
elif que == str(4):
    print("Your password is:" + char1+char2+char3+char4)
#5
elif que == str(5):
    print("Your password is:" + char1+char2+char3+char4+char5)
#6
elif que == str(6):
    print("Your password is:" + char1+char2+char3+char4+char5+char6)
#7
elif que == str(7):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7)
#8
elif que == str(8):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7+char8)
#9
elif que == str(9):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7+char8+char9)
#10
elif que == str(10):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10)
#11
elif que == str(11):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11)
#12
elif que == str(12):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12)
#13
elif que == str(13):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13)
#14
elif que == str(14):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14)
#15
elif que == str(15):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14+char15)
#16
elif que == str(16):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14+char15+char16)
#17
elif que == str(17):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14+char15+char16+char17)
#18
elif que == str(18):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14+char15+char16+char17+char18)
#19
elif que == str(19):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14+char15+char16+char17+char18+char19)
#20
elif que == str(20):
    print("Your password is:" + char1+char2+char3+char4+char5+char6+char7+char8+char9+char10+char11+char12+char13+char14+char15+char16+char17+char18+char19+char20)
#if not a number 1-20
else:
    print("Pick a number 1-20")
    quit()
