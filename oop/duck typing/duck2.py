class Pycharm:
    def compile(self):
        print("compile using pycharm")
    def execute(self):
        print("execute using pycharm")
    def debug(self):
        print("debug using pycharm")
class Vscode:
    def compile(self):
        print("compile using vscode")
    def execute(self):
        print("execute using vscode")
    def debug(self):
        print("debug using vscode")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()
p=Programmer()
pyc=Pycharm()
p.coding(pyc)