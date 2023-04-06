#If we have an object which has both instance as well as class attr, who will get preference?
'''
Instance attribute will be prefered
'''
class Employee:
    company="abs"
    id=123
    salary=100
ankita=Employee()
riya=Employee()
mehak=Employee()
print(ankita.id)
print(riya.company)
print(mehak.salary)
Employee.company="df"
ankita.company="ak"
print(ankita.company)
'''
output:
123
abs
100
ak
'''  

#Create a class and make three object with different parameters and change the values when you retrive data from the class.
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Employee("Ankita",23)
r = Employee("Riya", 24)
m = Employee("Mehak", 22)
a.name = "Ankita Sharma"
a.age = 24
print(a.name,a.age)      
r.name = "Riya Singh"
print(r.name)       
m.age = 23
print(m.age)  

'''output
Ankita Sharma 24
Riya Singh
23
'''

#Define Super method and Class method
'''
super method are the method which is used to call the parent class of the subclass.
Class methods are methods that are called on the class itself, not on a specific object instance.
'''