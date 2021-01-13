def tratarINT(y):
    while True:
        try:
            x = int(input({y}))
        except(ValueError, TypeError):
            print('\033[31mErro: please, input a intenger number.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUser preferred not to enter this number.\033[m')
            return 0
        else:
            return x

def tratarFLOAT(y):
    while True:
        try:
            x = float(input({y}))
        except(ValueError, TypeError):
            print('\033[31mErro: please, input a intenger number.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUser preferred not to enter this number.\033[m')
            return 0
        else:
            return x





