import random
import telebot

balance = 100
finale = ""



slot1 = ['❤️','🎆','☎️','☀️','7']
slot2 = ['❤️','🎆','☎️','☀️','7']
slot3 = ['❤️','🎆','☎️','☀️','7']

result1 = (random.choice(slot1))
result2 = (random.choice(slot2))
result3 = (random.choice(slot3))


def Slotroll():
    if result1 == result2 == result3:  
        finale = "YOU WIN"
    else:
        finale = "YOU LOSE"
    result = (result1 + result2 + result3)
    end = (finale + result)
    return end

        
    


        
