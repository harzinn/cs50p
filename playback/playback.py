def main():
    #Take user input
    user = input('Please enter prompt: ')

    #Print out the slowed down version of the input
    print(slowdown(user))

def slowdown(user): # Function that replaces spaces with ...
    convert = user.replace(' ', '...')
    return convert

main()