import random
elemanlar="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parola_l=input(int("parola uzunluğu gir"))
for i in range(parola_l):
    x=random.choice(elemanlar)
    print(x)
