
def check_pesel(to_check):
    check_list = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    num_sum = 0
    for i in range(len(check_list)):
        print('i is', i)
        tmp = int(to_check[i]) * check_list[i]
        if tmp >= 9:
            tmp = str(tmp)[-1]
            print('digit: ', tmp)
        num_sum += int(tmp)
        print('end: ', num_sum)
    if num_sum >= 9:
        num_sum = str(num_sum)[-1]
    control_number = 10 - int(num_sum)

    print('control_number: ', control_number)
    print('to_check: ', to_check)

    if str(control_number) == to_check[-1]:
        result = True
    else:
        result = False


    return result



if __name__ == '__main__':
    to_check = '56021720676'
    print(f'Is control conmber proper?  {check_pesel(to_check)}')