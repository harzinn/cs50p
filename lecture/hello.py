def main():
    name = input('What is your name? ')
    hello(name)


def hello(name='world'):
    name = name.strip().capitalize()
    print(f'Hello {name}')

main()