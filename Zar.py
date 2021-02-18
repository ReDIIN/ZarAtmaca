import random
min = 1

max = 6

roll_again = "evet"

while roll_again == "evet" or roll_again == "Evet" or roll_again == "e" or roll_again == "E":
    print("Zarlar Atılıyor...")
    print("sonuç: ")
    print(random.randint(min,max))
    print(random.randint(min,max))

    roll_again = input("Bir daha zar atmak ister misin? ")


else:
    print("Yine Bekleriz Efendim ;) ")

