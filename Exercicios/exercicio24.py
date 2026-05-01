par = 0

while par <= 100:

    par +=1

    if (par %2) != 0:

        print('Eu não mostro números ímpares')

        continue

    print(par)

    if par == 100:

        print('Acabou')

        break