import random
count=0

a=random.randint(0,10)

def process_abc(abc):
    global count
    match abc:
        case abc if abc<a:
            print('You Guessed Too Low ')
            count=count+1
            return 'continue'
        case abc if abc>a:
            print('You Guessed Too High')
            count=count+1
            return 'continue'
        case abc if abc==a:
            print('Your Guess Is Right ')
            count=count+1
            print(f'You Won And It Took You {count} Gusses')
            return 'exit'
        case 'exit':return 'exit'


def inp():
    abc=int(input('Enter Your Number '))
    xyz=process_abc(abc)
    if(xyz=='continue'):
        inp()
    if(xyz=='exit'):
        exit

inp()