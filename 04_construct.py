class employee:
    language = "Python" #This is class attribute 
    salary = 10000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am writing a Python program")

    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")

    @staticmethod
    def greet():
        print("Hello, good morning!")

mudasir = employee("mudasir",10000,"python")
#mudasir.name = "Mudasir"
print(mudasir.name,mudasir.salary,mudasir.language)


