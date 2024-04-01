
import sys
from my_sub import do_something

# def main():
#     print('running my_main')
#     do_something()

# main()

def main(arg):
    print(f'running my_main: {arg}')
    do_something()

if __name__ == '__main__':
    main(sys.argv[1])