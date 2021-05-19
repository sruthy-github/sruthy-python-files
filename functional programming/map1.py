employees=[
    {"id":1000,"name":"ajay","salary":25000,"designation":"developer"},
     {"id": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
     {"id": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
     {"id": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
     {"id": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]
emp_name=list(map(lambda emp:emp["name"],employees))
print(emp_name)