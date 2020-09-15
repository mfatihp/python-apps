"""
Author : Muhammet Fatih POLAT
Date   : 2020-09-14


anagram():
    A function takes two input from console and compare them if they are anagram or not.

    Argument list:
        Takes no argument
    
    Output:
        Prints comparison results

        Return -> None

"""


def anagram():
    
    # Taking inputs
    first = input("a: ")
    second = input("b: ")

    # Creating combined text
    combined = first + second
    charset = sorted(set(combined))
    
    # Creating character lists
    first_list = [i for i in first]
    second_list = [i for i in second]
    
    # Creating dictionary for characters and characters' count
    first_dict = {}

    for i in charset:
        count = first_list.count(i)
        first_dict[i] = count

    second_dict = {}

    for i in charset:
        count = second_list.count(i)
        second_dict[i] = count
    
    # Finding minimum difference for first text
    f_diff_s = 0

    # Iterating over for each key in dictionary
    for k in first_dict.keys():
        if first_dict[k] > second_dict[k]:
            diff_f = first_dict[k] - second_dict[k]
            f_diff_s += diff_f

    # Finding minimum difference for second text
    s_diff_f = 0

    # Iterating over for each key in dictionary
    for k in second_dict.keys():
        if first_dict[k] < second_dict[k]:
            diff_s = second_dict[k] - first_dict[k]
            s_diff_f += diff_s
    
    # Checking differences, if both differences is zero print text below 
    if (f_diff_s == 0) and (s_diff_f == 0):
        print("they are anagrams")
    # If not equal zero, print formatted text below
    else:
        print(f"remove {f_diff_s} characters from '{first}' and {s_diff_f} characters from '{second}'")
        
    


anagram()

    
