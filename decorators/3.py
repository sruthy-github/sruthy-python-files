def check_condition(func):
    def wrapper(**kwargs):
        age = kwargs["age"]
        health = kwargs["health"]
        if age >= 65 or health == True:
            return func(**kwargs)
        else:
            raise Exception("You are not eligible for VACCINATION")
    return wrapper
@check_condition
def vaccination(**kwargs):
    print("****COVID VACCINATION****")
    print("You are eligible for VACCINATION")
    print("*************************")

vaccination(name="Anu", age=28, place="Ernakulam", health=True)



