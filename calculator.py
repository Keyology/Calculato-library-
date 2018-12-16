
class Calculator:
    
    def __init__(self):
        self.value1 = int(input("enter a number"))
        self.value2 = int(input("enter a number"))

    def add(self):
        #add the two numbers a user inputs then prints out the result
        print(self.value1 + self.value2)
    
    def divide(self):
        # divide two numbers a user inputs then prints the result 
        print(self.value1 // self.value2) 
    def subtract(self):
        # subtract two numbers a user inputs then prints the result 
        print(self.value1 - self.value2)
        

    def multiply(self):
        # multiply the two numbers a users inputs then prints the results
        print(self.value1 * self.value2) 
        


if __name__ == "__main__":

    new_calculator = Calculator()
    new_calculator.add()
    new_calculator.subtract()
    new_calculator.divide()
    new_calculator.multiply()
    