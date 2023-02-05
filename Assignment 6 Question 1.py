import json
employee_data = [{"Name":"Sham","DOB":"11/09/1996","Height":"5'5","City":"Kakinada","State":"Andhra"}, 
                 {"Name":"Gousiya","DOB":"24/09/1996","Height":"5'2","City":"Gokak","State":"Karnataka"},
                 {"Name":"Lipsa","DOB":"01/08/1998","Height":"5'11","City":"Bargarh","State":"Odisha"},
                 {"Name":"Kaki","DOB":"11/09/2000","Height":"6","City":"Chennai","State":"Tamil Nadu"},
                 {"Name":"Vamsi","DOB":"25/03/1997","Height":"5'4","City":"Hyderabad","State":"Telangana"}]

with open("employee.json", "w") as f:
    json.dump(employee_data, f)

with open("employee.json", "r") as f:
    employee_data = json.load(f)

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def __repr__(self):
        return f"Name: {self.name}, DOB: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}"

employee_list = []
for employee in employee_data:
    emp = Employee(employee["Name"], employee["DOB"], employee["Height"], employee["City"], employee["State"])
    employee_list.append(emp)

print(employee_list)