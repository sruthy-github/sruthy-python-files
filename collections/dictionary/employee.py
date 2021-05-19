employee={"id":"1000","name":"manu","designation":"Manager","salary":30000}
print(employee["name"])
print("company" in employee)
employee["company"]="luminar"
employee["salary"]+=5000
for i in employee:
    print(i,":",employee[i])
