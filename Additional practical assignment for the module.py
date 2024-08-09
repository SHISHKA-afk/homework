grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = list(students)
students_sort.sort()
sum_graders = list(map(sum,grades))
quantity_graders = list(map(len,grades))
average_graders = [sum_graders[i] / quantity_graders[i] for i in range(len(quantity_graders))]
dictionary = dict(zip(students_sort, average_graders))
print(dictionary)