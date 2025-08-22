class employee:
    language = "Python" #This is class attribute 
    salary = 10000

    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")

    def greet(self):
        print("Hello, good morning!")

mudasir = employee()
#mudasir.language = "Javascript" #This is an instance attribute 
mudasir.getInfo()
mudasir.greet()
print(mudasir.language, mudasir.salary)

