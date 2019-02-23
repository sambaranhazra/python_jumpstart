#!/usr/bin/python

def main():
    text = input('Hey how is going?')
    while text != 'Stop Copying Me':
        print(text)
        text = input()

    print('Ugh fine! You won!!!')


if __name__ == '__main__':
    main()
