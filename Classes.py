class Basic_pay:
    def __init__(self,basic_pay):
        self.basic_pay = basic_pay *12
    def display_BP(self):
        print("The basic pay I received in a year: ", self.basic_pay)
BP= Basic_pay(int(input("Enter basic pay in a month: ")))
BP.display_BP()

class Allowance:
    def init(self, basic_pay_allowances):
        self.basic_pay_allowances = basic_pay_allowances *12
    def display_Allowance(self):
        print("The basic pay allowance I received in a year: ", self.basic_pay_allowances)
A= Allowance(float(input("Enter basic pay allowance i received in a month in percentage: ")))
A.display_Allowance()