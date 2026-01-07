def min_max_avg(lst):
    if len(lst) == 0:
        return None, None, None
    (
        lst_min,
        lst_max,
    ) = lst[0], lst[0]
    lst_sum, lst_count = 0, len(lst)

    ## Min Number
    for i in lst:
        if i < lst_min:
            lst_min = i

    ## Max Number
    for i in lst:
        if i > lst_max:
            lst_max = i

    ## Avg Number
    for i in lst:
        lst_sum += i

    lst_avg = lst_sum / lst_count

    return lst_min, lst_max, lst_avg


def prime_freq(lst) -> int:
    def is_prime(num) -> bool:
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    prime_lst = []
    for num in lst:
        if is_prime(num):
            prime_lst.append(num)

    return len(prime_lst)


def odd_even_freq(lst):
    odd_count, even_count = 0, 0

    for num in lst:
        if num % 2 == 0:
            even_count += 1
        elif num % 2 != 0:
            odd_count += 1
    return odd_count, even_count


def number_analyzer(lst):
    lst_min, lst_max, lst_avg = min_max_avg(lst)
    lst_prime_count = prime_freq(lst)
    lst_odd_count, lst_even_count = odd_even_freq(lst)
    
    print("=================")
    print("List Analysis")
    print("=================")
    print(f"Min: {lst_min}, Max: {lst_max}, Average: {lst_avg}")
    print(f"The list has {lst_prime_count} Prime Number.")
    print(
        f"The list has {lst_odd_count} Odd number, and {lst_even_count} Even Numbers."
    )


lst = [1, 2, 3, 4, 5, 6, 7, 8, 10, 34]
number_analyzer(lst)
