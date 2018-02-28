import random


def print_header():
    print('#################################################')
    print('       Practice FDP common equivalents           ')
    print('#################################################')
    print(' Rules: Answer questions, Type \'exit\' to EXIT  ')
    print('        Type percents truncated to 1 or 2 digits ')
    print('        i.e. 10.0 for 10% or  16.67 for 16.6666  ')
    print('#################################################')


def create_fdp_dict():
    keys = ['1/100', '1/50', '1/25', '1/20', '1/11', '1/10', '1/9', '1/8',
            '1/6', '1/5', '1/4', '3/10', '1/3', '3/8', '2/5', '1/2', '3/5',
            '5/8', '2/3', '7/10', '3/4', '4/5', '5/6', '7/8', '9/10', '1/1',
            '5/4', '4/3', '3/2', '7/4']
    values = [f'{round(eval(i)*100, 2)}%' for i in keys]
    fdp_dict = dict(zip(keys, values))
    return fdp_dict


def mine_fdp_dict(kv_list):
    return (random.choice(kv_list))


def user_interface(fdp_dict):
    keys_list = list(fdp_dict.keys())
    values_list = list(fdp_dict.values())
    kv_list = keys_list + values_list
    fdp_dict_rev = {v: k for k, v in fdp_dict.items()}

    for i in range(100):
        mined = mine_fdp_dict(kv_list)
        result = input(f"\nWhat is the FDP equivalent of: {mined}   ")
        if mined in keys_list:
            if f'{result}%' == fdp_dict[mined]:
                print('Yes!')
            elif result == 'exit':
                break
            else:
                print(f'No! Answer is : {fdp_dict[mined]}')
        else:
            if result == fdp_dict_rev[mined]:
                print('Yes!')
            elif result == 'exit':
                break
            else:
                print(f'No! Answer is : {fdp_dict_rev[mined]}')


def main():
    print_header()
    fdp_dict = create_fdp_dict()
    user_interface(fdp_dict)


if __name__ == '__main__':
    main()