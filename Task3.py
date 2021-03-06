# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

# первый вариант, сделал его до того как проходил тест
range_list = [x for x in range(1, 11)]
squared_list = [x ** 2 for x in range(1, 11)]
final_list = [(range_list[x], squared_list[x]) for x in range(0, 10)]
print(final_list)

# второй вариант, более компактный
second_final_list = [(y, y ** 2) for y in range(1, 11)]
print(second_final_list)
