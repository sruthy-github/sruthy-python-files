def admin_required(func):
    def wrapper(user,pin):
        if user!="admin":
            raise Exception("You are not allowed")
        else:
            return func(user,pin)
    return wrapper
@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_required
def delete_account(user,acno):
    return str(acno)+"deleted"
try:
    print(change_pin("user1", 1000))


except Exception as e:
    print(e.args)
