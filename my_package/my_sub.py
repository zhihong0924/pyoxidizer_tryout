
import sys
import typer

def do_something():
    print('running my_sub')
    print(f'current python version is {sys.version}')
    print(f'typer is installed: {typer.Typer()}')

if __name__ == '__main__':
    do_something()