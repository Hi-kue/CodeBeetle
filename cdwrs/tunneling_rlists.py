"""
file: tunneling_rlists.py
author: @Hi-kue
description:
    - Given a list (of most likely integers), reverse the list using recursion.
    - The list can also be nested lists, which would require tunneling of the sublists.
    - For each sublist within the list, reverse the sublist using recursion as well.
"""
def reverse_list(lst: list) -> list:
    if not isinstance(lst, list):
        return lst

    reversed_elem = []
    for item in lst[::-1]:
        if isinstance(item, list):
            reversed_elem.append(reverse_list(item))
        else:
            reversed_elem.append(item)

    return reversed_elem

def tunneling_rlists(lst: list) -> list:
    if not isinstance(lst, list):
        return lst
    return [tunneling_rlists(sublist) for sublist in lst[::-1]]

if __name__ == "__main__":
    lst = [1, 2, 3, [4, 5, [6, 7]]]
    print(tunneling_rlists(lst=lst))
    print(reverse_list(lst=lst))
