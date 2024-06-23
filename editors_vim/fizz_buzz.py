"""Three scenarios
1. If the number is divisible by 3, output 
2. If the number is divisible by 5, output buzz.
3. If the number is divisible by 15, output the number itself.
"""

def fizz_buzz(limit):
    for i in range(1, limit + 1):
        if (i % 3 == 0) & (i % 5 == 0):
            print("fizz buzz") 
            continue
        if i % 3 == 0:
            print('fizz')
            continue
        if i % 5 == 0:
            print('buzz')
            continue 
        else:
            print(i)

def main():
    fizz_buzz(int(input()))

if __name__ == '__main__':
    main()
