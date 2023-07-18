import random


def check_sum(to_check):

    check_list = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    num_sum = 0
    for i in range(len(check_list)):
        # print('i is:', i)
        tmp = int(to_check[i]) * check_list[i]
        if tmp >= 9:
            tmp = str(tmp)[-1]
            # print('digit: ', tmp)
        num_sum += int(tmp)
        # print('end num_sum: ', num_sum)
    if num_sum >= 9:
        num_sum = str(num_sum)[-1]
    control_sum = 10 - int(num_sum)

    return control_sum


def check_pesel(to_check):
    control_sum = check_sum(to_check)
    last_digit = to_check[-1]
    if str(control_sum) == last_digit:
        result = True
    else:
        result = False

    print(f'** CONTROL_NUMBER: {control_sum} = LAST DIGIT OF PESEL: {last_digit} **')
    print('to_check: ', to_check)
    return result


def randomize_string():
    ran_str = ''
    for j in range(3):
        element = str(random.randint(0, 9))
        ran_str += element
    # print(ran_str)
    return ran_str


def generate_pesel(sex, day, month, year):

    day = str(day)
    month = str(month)
    year = str(year)
    sex = str(sex)
    m_list = [1, 3, 5, 7, 9]
    f_list = [0, 2, 4, 6, 8]

    if len(day) == 1:
        day = '0'+day
        print(day)
    if len(month) == 1:
        month = '0' + month
        print(month)
    year = year[-3:-1]
    print(year)
    if sex == 'M':
        sex_num = random.choice(m_list)
    if sex == 'F':
        sex_num = random.choice(f_list)
    print(sex_num)
    print(type(day))
    result = ''
    while len(result) != 11:
        print('** begining of while loop **')
        pesel_num = year + month + day + randomize_string() + str(sex_num)
        result = pesel_num + str(check_sum(pesel_num))
    return result


if __name__ == '__main__':
    to_check = '02070803628'
    print(f'Check sum is:  {check_sum(to_check)}')
    print(f'Is PESEL number proper?  {check_pesel(to_check)}')
    print(f'Generated PESEL number is:  {generate_pesel(sex="M", day=3, month=11, year=2000)}')
