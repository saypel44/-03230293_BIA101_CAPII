class BasicPay:
    def __init__(self, basic_pay):
        self.basic_pay = basic_pay

    def calculate_annual_basicpay(self):
        self.annual_basicPay = self.basic_pay * 12  # Calculate annual income here

    def display_BP(self):
        self.calculate_annual_basicpay()  # Call the calculation method before displaying
        print(f"The annual basic pay I received: Nu.{ self.annual_basicPay:}")

BP = BasicPay(basic_pay=float(input("Enter basic pay in a month: ")))
BP.display_BP()  # Call the display method to show the result

class Allowance:
    def __init__(self, allowance_percentage):
        self.allowance_percentage = allowance_percentage / 100  # Convert percentage to decimal

    def calculate_annual_allowance(self, basic_pay):
        self.annual_allowance = basic_pay * self.allowance_percentage * 12

    def display_Allowance(self, basic_pay):
        self.calculate_annual_allowance(basic_pay)  # Calculate allowance based on basic pay
        print(f"The annual basic pay allowance I received: Nu.{self.annual_allowance:}")

A = Allowance(allowance_percentage=float(input("Enter basic pay allowance I received in a month in percentage: ")))
A.display_Allowance(BP.basic_pay)  # Pass basic pay object's basic_pay for calculation

# class AddBPA:
#     def getaddBPA(self):
#         print("Total basic pay received in a year is: ", BP.annual_income + A.annual_allowance)
# add=AddBPA()
# add.getaddBPA()

class AddBPA:
    def calculate_AddBPA(self,annual_basicPay, annual_allowance):
        self.AddBPA =annual_basicPay + annual_allowance

    def display_AddBPA(self,annual_basicPay, annual_allowance ):
        self.calculate_AddBPA(annual_basicPay, annual_allowance)  # Calculate allowance based on basic pay
        print(f"The added I received: Nu.{self.AddBPA:}")

Add= AddBPA()
Add.display_AddBPA(BP.annual_basicPay, A.annual_allowance)

class fees_remuneration:
    def __init__(self, fees_remuneration):
        self.fees_remuneration = fees_remuneration / 100  # Convert percentage to decimal

    def calculate_fees_remuneration(self, basic_pay):
        self.fees_remuneration = basic_pay * self.fees_remuneration * 12

    def display_fees_remuneration(self, AddBPA):
        self.calculate_fees_remuneration(AddBPA)  # Calculate allowance based on basic pay
        print(f"The annual fees remuneration allowance I received: Nu.{self.fees_remuneration:}")

remu = fees_remuneration(fees_remuneration=int(input("Enter fees_remuneration I received in a month in percentage: ")))
remu.display_fees_remuneration(Add.AddBPA) 

class Addfees_remuneration:
    def calculate_Addfees_remuneration(self,annual_basicPay, annual_allowance,fees_remuneration):
        self.Addfees_remuneration =annual_basicPay + annual_allowance +fees_remuneration

    def display_Addfees_remuneration(self,annual_basicPay, annual_allowance,fees_remuneration ):
        self.calculate_Addfees_remuneration(annual_basicPay, annual_allowance, fees_remuneration)  # Calculate allowance based on basic pay
        print(f"The added fees remuneration  I received: Nu.{self.Addfees_remuneration:}")

Add= Addfees_remuneration()
Add.display_Addfees_remuneration(BP.annual_basicPay, A.annual_allowance, remu.fees_remuneration)

class commisiion:
    def __init__(self, commisiion):
        self.commisiion = commisiion / 100  # Convert percentage to decimal

    def calculate_commisiion(self, basic_pay):
        self.commisiion = basic_pay * self.commisiion * 12

    def display_commisiion(self, addfees_remuneration):
        self.calculate_commisiion(addfees_remuneration)  # Calculate allowance based on basic pay
        print(f"The commission I received: Nu.{self.commisiion:}")

com = commisiion(commisiion=float(input("Enter commission I received in a month in percentage: ")))
com.display_commisiion(fees_remuneration) 

class Addcom:
    def calculate_Addcom(self,annual_basicPay, annual_allowance,commission):
        self.AddBPA =annual_basicPay + annual_allowance + commission

    def display_Addcom(self,annual_basicPay, annual_allowance, commission ):
        self.calculate_AddBPA(annual_basicPay, annual_allowance, commission)  # Calculate allowance based on basic pay
        print(f"The added commission I received: Nu.{self.Addcom:}")

Add= Addcom()
Add.display_AddBPA(BP.annual_basicPay, A.annual_allowance,com.commisiion )










