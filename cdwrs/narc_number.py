import timeit

def check_zeros(lst: list) -> list:
    for idx, value in enumerate(lst):
        if value == 0:
            lst.pop(idx)
        else: break
        
    return lst

def narcissistic_number(value: int) -> int:
    value_lst = [int(x) for x in str(value)]
    value_lst_wz = check_zeros(value_lst)
    len_value_lst_wz = len(value_lst_wz)
    value_lst_power = [value ** len_value_lst_wz for value in value_lst_wz]

    return sum(value_lst_power)

if __name__ == '__main__':
    numb = int(input("Enter a number: "))
    timer_1 = timeit.Timer(lambda: narcissistic_number(numb))
    elasped_time_1 = timer_1.timeit(1)

    print(f"The narcissistic_number function took: {elasped_time_1}")


