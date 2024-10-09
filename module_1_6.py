
#словари
my_dict = {'Brito':18,'Castelanos':20,'Hidalgo':18,'Nunez':17.5}
print("Dict:",my_dict)
driver_1 = my_dict['Brito']
print("Driver_exist:",driver_1)
print("Driver_not_exist:",my_dict.get('Payan'))
my_dict.update({'Salnave':18,
                'Victor':21})
drop_driver = my_dict.pop('Nunez')
print("Deleted_value:",drop_driver)
print("Modified_dict:",my_dict)

print("------------------------------------------")

#множества
my_set = {1,2,3,4,'Банан',25.55,1,2,4}
print("Set:",my_set)
my_set.update([10,7])
my_set.remove('Банан')
print("Modified set:",my_set)