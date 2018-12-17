
class Calculator:

    def add(self, value1=int, value2=int):
        #add the two numbers a user inputs then prints out the result
        print(value1 + value2)
    
    def divide(self, value1, value2):
        # divide two numbers a user inputs then prints the result
        print( value1 // value2 )
   
    def subtract(self, value1=int, value2=int):
        # subtract two numbers a user inputs then prints the result 
        print(value1  - value2)

    def multiply(self,value1=int, value2=int):
        # multiply the two numbers a users inputs then prints the results
        print( value1 * value2)
        


if __name__ == "__main__":

    new_calculator = Calculator()
    new_calculator.add(5,5)
    new_calculator.subtract(10, 5)
    new_calculator.divide(4,2)
    new_calculator.multiply(10,2)
    