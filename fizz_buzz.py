def f_b(a):
    arr = list(range(int(a.split(' ')[0]), int(a.split(' ')[1])+1))
    rez = []
    for i in arr:
        if i%3 == 0 and i%5 != 0:
            rez.append('Fizz')
        elif i%3 != 0 and i%5 == 0:
            rez.append('Buzz')
        elif i%3 == 0 and i%5 == 0:
            rez.append('FizzBuzz')
        else:
            rez.append(i)
    return [print(i) for i in rez]


a = input()

f_b(a)