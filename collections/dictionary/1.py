#dictionary
#dic={}
#keyvalue players
dic={"name":"luminar","location":"Kakkanad","course":"python","mark":120,"data":10.5}
print(dic["location"])
dic["mark"]+=30
print(dic)
#delete
dic.pop("data")
#del dic["data"]
print(dic)
print("name" in dic)