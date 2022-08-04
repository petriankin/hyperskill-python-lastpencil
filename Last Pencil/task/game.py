def switch_name(name_to_switch):
    if name_to_switch == 'John':
        return 'Jack'
    else:
        return 'John'


def check_initial(input_param):
    try:
        int(input_param)
    except ValueError:
        print('The number of pencils should be numeric')
        return False
    if int(input_param) <= 0:
        print('The number of pencils should be positive')
        return False
    else:
        return True


print('How many pencils would you like to use:')
initial_input = ''
# initialCheckPassed = False
while True:
    initial_input = input()
    if check_initial(initial_input):
        break

amount = int(initial_input)

# jack is bot
print("Who will be the first (John, Jack):")
name = ''
while True:
    name = input()
    if name in ['Jack', 'John']:
        break
    else:
        print("Choose between 'John' and 'Jack'")

to_subtract = 0
possible_values = ["1", "2", "3"]


def jacks_turn(left_pencils):
    remainder = left_pencils % 4
    if remainder == 0:
        return 3
    elif remainder == 3:
        return 2
    elif remainder == 2:
        return 1
    else:
        return 1


while amount > 0:
    print('|' * amount)
    print(name + "'s turn:")
    if name == 'Jack':
        to_subtract = jacks_turn(amount)
        print(to_subtract)
    else:
        to_subtract_input = ''
        while True:
            to_subtract_input = input()
            if to_subtract_input not in possible_values:
                print("Possible values: '1', '2' or '3'")
            elif amount < int(to_subtract_input):
                print('Too many pencils were taken')
            else:
                to_subtract = int(to_subtract_input)
                break

    name = switch_name(name)
    amount -= to_subtract

print(name + ' won!')
