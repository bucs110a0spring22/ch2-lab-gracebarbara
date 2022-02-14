
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week, type(cost_per_week))
classes_per_week = 3
print("Classes per week:", classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class, type(cost_per_class))

#Part B
import random
my_list = (7,5.0,85,3.0,"11")
assortment = (my_list)
random.choice(assortment)
my_random_output = (random.choice(assortment))
print(my_random_output)
