#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(min(len(my_list_1), len(my_list_2), list_length)):
        try:
            # Attempt division
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    return result_list
