class BasicPay:
    def __init__(self, basic_pay):
        self.basic_pay = basic_pay

    def calculate_annual_basicpay(self):
        self.annual_income = self.basic_pay * 12  # Calculate annual income here

    def display_BP(self):
        self.calculate_annual_basicpay()  # Call the calculation method before displaying
        print(f"The annual basic pay I received: Nu.{self.calculate_annual_basicpay:}")

BP = BasicPay(basic_pay=int(input("Enter basic pay in a month: ")))
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

class AddBPA:
    def getaddBPA(self):
        print("Total basic pay received in a year is: ", BP.annual_income + A.annual_allowance)
add=AddBPA()
add.getaddBPA()

class income:
    def __init__(self,Annual_bonus, fees_remuneration):
        self.Annual_bonus = Annual_bonus
        self.fees_remuneration = fees_remuneration  # Nu.
        self.bonus_yearly = bonus # Nu.
        self.commission = commission  # Nu.
        self.leave_encashment= leave_encashment  # Nu.
        self.shareofProfirreceived_yearly = shareofProfirreceived # Nu.
        self.consultancy_income_yearly = consultancy_income  # Nu.
        self.benefitsReceived_monthly = benefitsReceived  # Nu.

    def calculate_annual_income(self):
        # Calculate annual income here
        self.Annual_bonus = Annual_bonus
        self.fees_remuneration = fees_remuneration *12  # Nu.
        self.bonus_yearly = bonus # Nu.
        self.commission = commission  # Nu.
        self.leave_encashment= leave_encashment  # Nu.
        self.shareofProfirreceived_yearly = shareofProfirreceived # Nu.
        self.consultancy_income_yearly = consultancy_income  # Nu.
        self.benefitsReceived_monthly = benefitsReceived*12

    def display_Income(self):
        self.calculate_annual_income()  # Call the calculation method before displaying
        print(f"The annual basic pay I received: Nu.{self.annual_income:}")