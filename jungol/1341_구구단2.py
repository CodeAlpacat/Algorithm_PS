a, b = map(int, input().split())

if 2 <= a <= 9 and 2 <= b <= 9:
    if a <= b:
        for x in range(a, b+1):
            for i in range(1, 10):
                if i % 3 == 1:
                    print()
                if x * i < 10:
                    print(f'{x} * {i} =  {x*i}', end='   ')
                else:
                    print(f'{x} * {i} = {x*i}', end='   ')
            print()
                    
    else:
        for x in range(a, b-1, -1):
            for i in range(1, 10):
                if i % 3 == 1:
                    print()
                if x * i < 10:
                    print(f'{x} * {i} =  {x*i}', end='   ')
                else:
                    print(f'{x} * {i} = {x*i}', end='   ')
            print()