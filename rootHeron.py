"""
Compute square roots using Heron of Alexandria method

Argument: 
    x: The number for which the square root is to be computed

Return: 
    The square root of x    
"""
def sqrt (x):
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x/guess) / 2.0
        i += 1
    return guess    


def main():
    print(sqrt(9))
    print(sqrt(2))


if __name__ == '__main__':
    main()
