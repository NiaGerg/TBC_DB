from employee import Employee
from db import conn

# Define a list of employee data
employees_data = [
    {"name": "buba", "surname": "guga", "age": 25},
    {"name": "boba", "surname": "gaga", "age": 35},
    {"name": "baba", "surname": "goga", "age": 30},
    {"name": "Tsotne", "surname": "tso", "age": 90}
]


for data in employees_data:
    employee = Employee(**data)
    employee.save()


first_user = Employee.get(1)


if first_user is None:
    first_user = Employee("Tsotne", "Tsotnidze", 105)
    first_user.save()

# Update the name of the first employee
first_user.name = "Tornike"
first_user.save()

# Print details of the first user
print("First User:", first_user)

# Retrieve a list of employees with the name "Tsotne"
employees_with_name_tsotne = Employee.get_list(name='Tsotne')
print("Employees with name Tsotne:", employees_with_name_tsotne)


first_user.delete()
print("First user deleted.")


conn.commit()
conn.close()
