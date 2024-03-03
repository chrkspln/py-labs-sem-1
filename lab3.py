# завдання 1.28
def finding_an_element(user_list):
    left_i = 0
    right_i = -1
    left_sum, right_sum = 0, 0
    while right_i > left_i:
        left_sum += user_list[left_i]
        right_sum += user_list[right_i]
        left_i += 1
        right_i -= 1
        if left_sum == right_sum:
            print("індекс елемента N з ідентичними сумами по обидва боки списку: ", left_i, '\n',
                  "сума елементів: ", left_sum)
            exit()
    print("елемента з ідентичними сумами по обидва боки списку від нього не знайшлось: ", -1)


input_list = [5, 6, 56, 7, 0, 89, 8, 6, 11, 1]
finding_an_element(input_list)
