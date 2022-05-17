import random

#Retorna un numero random ENTERO entre el rango que elegí, o sea, entre 1 y 10
random_int = random.randint(1,10)

print(random_int)

#Retorna un numero random FLOAT entre 0.0 y 0.9
random_float = random.random()

print(random_float)

#Si quiero entre otro rango lo multplico. Si lo multiplico * 5 me va a dar un random entre 0.0 y 4.9
new_random = random_float * 5

print(new_random)

#Random score
love_score = random.randint(1,100)
print(f"Your love score is {love_score}%")