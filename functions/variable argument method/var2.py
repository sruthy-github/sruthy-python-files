employees={
    1000:{"id":1000,"name":"ajay","salary":25000,"designation":"developer"},
    1001: {"id": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    1002: {"id": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    1003: {"id": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    1004: {"id": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

}

def print_employee(**kwargs):
    id=kwargs["id"]
    prop=kwargs["prop"]
    if id in employees:
        print(employees[id]["name"])
        print(employees[id][prop])
    else:
        print("invalid id")


   # print(kwargs)
print_employee(id=1000,prop="salary")