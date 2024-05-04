# 1. Basic Pay
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

#2. Basic allowances
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

#3. Fees remuneration
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

#4.Commission
class commisiion:
    def __init__(self, commisiion):
        self.commisiion = commisiion / 100  # Convert percentage to decimal

    def calculate_commisiion(self, basic_pay):
        self.commisiion = basic_pay * self.commisiion * 12

    def display_commisiion(self, addfees_remuneration):
        self.calculate_commisiion(addfees_remuneration)  # Calculate allowance based on basic pay
        print(f"The commission I received: Nu.{self.commisiion:}")

com = commisiion(commisiion=float(input("Enter commission I received in a month in percentage: ")))
com.display_commisiion(Add.Addfees_remuneration) 

class Addcom:
    def calculate_Addcom(self,annual_basicPay, annual_allowance,commission):
        self.Addcom =annual_basicPay + annual_allowance + commission

    def display_Addcom(self,annual_basicPay, annual_allowance, commission ):
        self.calculate_Addcom(annual_basicPay, annual_allowance, commission)  # Calculate allowance based on basic pay
        print(f"The added commission I received: Nu.{self.Addcom:}")

Add= Addcom()
Add.display_Addcom(BP.annual_basicPay, A.annual_allowance,com.commisiion )

# 5.Leave encashment
class leave_encashment:
    def __init__(self, leave_encashment):
        self.leave_encashment = leave_encashment / 100  # Convert percentage to decimal

    def calculate_leave_encashment(self, basic_pay):
        self.leave_encashment = basic_pay * self.leave_encashment * 12

    def display_leave_encashment(self, Addcom):
        self.calculate_leave_encashment(Addcom)  # Calculate allowance based on basic pay
        print(f"The leave encashment I received: Nu.{self.leave_encashment:}")

lc = leave_encashment(leave_encashment=float(input("Enter leave encashment I received in a month in percentage: ")))
lc.display_leave_encashment(Add.Addcom)

class Addlc:
    def calculate_Addlc(self,annual_basicPay, annual_allowance,commission, leave_encashment ):
        self.Addlc =annual_basicPay + annual_allowance + commission + leave_encashment

    def display_Addlc(self,annual_basicPay, annual_allowance, commission, leave_encashment ):
        self.calculate_Addlc(annual_basicPay, annual_allowance, commission, leave_encashment)  # Calculate allowance based on basic pay
        print(f"The added commission I received: Nu.{self.Addlc:}")

Add= Addlc()
Add.display_Addlc(BP.annual_basicPay, A.annual_allowance, com.commisiion, lc.leave_encashment )

#6.share of profit
class shareofProfirreceived:
    def __init__(self,shareofProfirreceived):
        self.shareofProfirreceived = shareofProfirreceived/ 100  # Convert percentage to decimal

    def calculate_shareofProfirreceived(self, basic_pay):
        self.shareofProfirreceived= basic_pay * self.shareofProfirreceived * 12

    def display_shareofProfirreceived(self, Addlc):
        self.calculate_shareofProfirreceived(Addlc)  # Calculate allowance based on basic pay
        print(f"The leave encashment I received: Nu.{self.shareofProfirreceived:}")

SOP = shareofProfirreceived(shareofProfirreceived=float(input("Enter share of Profit received I received in a month in percentage: ")))
SOP.display_shareofProfirreceived(Add.Addlc)

class AddSoP:
    def calculate_AddSoP(self,annual_basicPay, annual_allowance,commission, leave_encashment, shareofProfirreceived  ):
        self.AddSoP =annual_basicPay + annual_allowance + commission + leave_encashment+ shareofProfirreceived

    def display_AddSoP(self,annual_basicPay, annual_allowance, commission, leave_encashment, shareofProfirreceived ):
        self.calculate_AddSoP(annual_basicPay, annual_allowance, commission, leave_encashment, shareofProfirreceived)  # Calculate allowance based on basic pay
        print(f"The added commission I received: Nu.{self.AddSoP:}")

Add= AddSoP()
Add.display_AddSoP(BP.annual_basicPay, A.annual_allowance, com.commisiion, lc.leave_encashment, SOP.shareofProfirreceived )

#7. Consultancy income
class consultancyIncome:
    def __init__(self,consultancyIncome):
        self.consultancyIncome= consultancyIncome/ 100  # Convert percentage to decimal

    def calculate_consultancyIncome(self, basic_pay):
        self.consultancyIncome= basic_pay * self.consultancyIncome * 12

    def display_consultancyIncome(self, AddSoP):
        self.calculate_consultancyIncome(AddSoP)  # Calculate allowance based on basic pay
        print(f"The consultancy Income I received: Nu.{self.consultancyIncome:}")

CI= consultancyIncome(consultancyIncome=float(input("Enter share of Profit received I received in a month in percentage: ")))
CI.display_consultancyIncome(Add.AddSoP)

class AddCI:
    def calculate_AddCI(self,annual_basicPay, annual_allowance,commission, leave_encashment, shareofProfirreceived, consultancyIncome  ):
        self.AddCI =annual_basicPay + annual_allowance + commission + leave_encashment+ shareofProfirreceived + consultancyIncome

    def display_AddCI(self,annual_basicPay, annual_allowance, commission, leave_encashment, shareofProfirreceived, consultancyIncome ):
        self.calculate_AddCI(annual_basicPay, annual_allowance, commission, leave_encashment, shareofProfirreceived, consultancyIncome)  # Calculate allowance based on basic pay
        print(f"The added consultancy Income I received: Nu.{self.AddCI:}")

Add= AddCI()
Add.display_AddCI(BP.annual_basicPay, A.annual_allowance, com.commisiion, lc.leave_encashment, SOP.shareofProfirreceived, CI.consultancyIncome )

# 8. other benefited received
class Other_benefits:
    def __init__(self, HouseRentAllowances, MobileAllowances, ConveyanceAllowances, LTC, AnyotherAllowances):
        self.HouseRentAllowances= HouseRentAllowances / 100  # Convert percentage to decimal
        self.MobileAllowances= MobileAllowances / 100
        self.ConveyanceAllowances= ConveyanceAllowances / 100
        self.LTC= LTC / 100
        self.AnyotherAllowances= AnyotherAllowances / 100

    # 1. Basic Pay
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

#2. Basic allowances
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

#3. Fees remuneration
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

#4.Commission
class commisiion:
    def __init__(self, commisiion):
        self.commisiion = commisiion / 100  # Convert percentage to decimal

    def calculate_commisiion(self, basic_pay):
        self.commisiion = basic_pay * self.commisiion * 12

    def display_commisiion(self, addfees_remuneration):
        self.calculate_commisiion(addfees_remuneration)  # Calculate allowance based on basic pay
        print(f"The commission I received: Nu.{self.commisiion:}")

com = commisiion(commisiion=float(input("Enter commission I received in a month in percentage: ")))
com.display_commisiion(Add.Addfees_remuneration) 

class Addcom:
    def calculate_Addcom(self,annual_basicPay, annual_allowance,commission):
        self.Addcom =annual_basicPay + annual_allowance + commission

    def display_Addcom(self,annual_basicPay, annual_allowance, commission ):
        self.calculate_Addcom(annual_basicPay, annual_allowance, commission)  # Calculate allowance based on basic pay
        print(f"The added commission I received: Nu.{self.Addcom:}")

Add= Addcom()
Add.display_Addcom(BP.annual_basicPay, A.annual_allowance,com.commisiion )

# 5.Leave encashment
class leave_encashment:
    def __init__(self, leave_encashment):
        self.leave_encashment = leave_encashment / 100  # Convert percentage to decimal

    def calculate_leave_encashment(self, basic_pay):
        self.leave_encashment = basic_pay * self.leave_encashment * 12

    def display_leave_encashment(self, Addcom):
        self.calculate_leave_encashment(Addcom)  # Calculate allowance based on basic pay
        print(f"The leave encashment I received: Nu.{self.leave_encashment:}")

lc = leave_encashment(leave_encashment=float(input("Enter leave encashment I received in a month in percentage: ")))
lc.display_leave_encashment(Add.Addcom)

class Addlc:
    def calculate_Addlc(self,annual_basicPay, annual_allowance,commission, leave_encashment ):
        self.Addlc =annual_basicPay + annual_allowance + commission + leave_encashment

    def display_Addlc(self,annual_basicPay, annual_allowance, commission, leave_encashment ):
        self.calculate_Addlc(annual_basicPay, annual_allowance, commission, leave_encashment)  # Calculate allowance based on basic pay
        print(f"The added commission I received: Nu.{self.Addlc:}")

Add= Addlc()
Add.display_Addlc(BP.annual_basicPay, A.annual_allowance, com.commisiion, lc.leave_encashment )

#6.share of profit
class shareofProfirreceived:
    def __init__(self,shareofProfirreceived):
        self.shareofProfirreceived = shareofProfirreceived/ 100  # Convert percentage to decimal

    def calculate_shareofProfirreceived(self, basic_pay):
        self.shareofProfirreceived= basic_pay * self.shareofProfirreceived * 12

    def display_shareofProfirreceived(self, Addlc):
        self.calculate_shareofProfirreceived(Addlc)  # Calculate allowance based on basic pay
        print(f"The leave encashment I received: Nu.{self.shareofProfirreceived:}")

SOP = shareofProfirreceived(shareofProfirreceived=float(input("Enter share of Profit received I received in a month in percentage: ")))
SOP.display_shareofProfirreceived(Add.Addlc)

class AddSoP:
    def calculate_AddSoP(self,annual_basicPay, annual_allowance,commission, leave_encashment, shareofProfirreceived  ):
        self.AddSoP =annual_basicPay + annual_allowance + commission + leave_encashment+ shareofProfirreceived

    def display_AddSoP(self,annual_basicPay, annual_allowance, commission, leave_encashment, shareofProfirreceived ):
        self.calculate_AddSoP(annual_basicPay, annual_allowance, commission, leave_encashment, shareofProfirreceived)  # Calculate allowance based on basic pay
        print(f"The added commission I received: Nu.{self.AddSoP:}")

Add= AddSoP()
Add.display_AddSoP(BP.annual_basicPay, A.annual_allowance, com.commisiion, lc.leave_encashment, SOP.shareofProfirreceived )

#7. Consultancy income
class consultancyIncome:
    def __init__(self,consultancyIncome):
        self.consultancyIncome= consultancyIncome/ 100  # Convert percentage to decimal

    def calculate_consultancyIncome(self, basic_pay):
        self.consultancyIncome= basic_pay * self.consultancyIncome * 12

    def display_consultancyIncome(self, AddSoP):
        self.calculate_consultancyIncome(AddSoP)  # Calculate allowance based on basic pay
        print(f"The consultancy Income I received: Nu.{self.consultancyIncome:}")

CI= consultancyIncome(consultancyIncome=float(input("Enter share of Profit received I received in a month in percentage: ")))
CI.display_consultancyIncome(Add.AddSoP)

class AddCI:
    def calculate_AddCI(self,annual_basicPay, annual_allowance,commission, leave_encashment, shareofProfirreceived, consultancyIncome  ):
        self.AddCI =annual_basicPay + annual_allowance + commission + leave_encashment+ shareofProfirreceived + consultancyIncome

    def display_AddCI(self,annual_basicPay, annual_allowance, commission, leave_encashment, shareofProfirreceived, consultancyIncome ):
        self.calculate_AddCI(annual_basicPay, annual_allowance, commission, leave_encashment, shareofProfirreceived, consultancyIncome)  # Calculate allowance based on basic pay
        print(f"The added consultancy Income I received: Nu.{self.AddCI:}")

Add= AddCI()
Add.display_AddCI(BP.annual_basicPay, A.annual_allowance, com.commisiion, lc.leave_encashment, SOP.shareofProfirreceived, CI.consultancyIncome )


class OtherBenefits:
    def __init__(self, house_rent_allowances, mobile_allowances, conveyance_allowances, ltc, anyother_allowances):
        self.house_rent_allowances = house_rent_allowances / 100
        self.mobile_allowances = mobile_allowances / 100
        self.conveyance_allowances = conveyance_allowances / 100
        self.ltc = ltc / 100
        self.anyother_allowances = anyother_allowances / 100

    def calculate_total_other_benefits(self, basic_pay):
        self.house_rent_allowances = basic_pay * self.house_rent_allowances * 12 
        self.mobile_allowances = basic_pay * self.mobile_allowances * 12
        self.conveyance_allowances = basic_pay * self.conveyance_allowances * 12
        self.ltc = basic_pay * self.ltc * 12
        self.anyother_allowances = basic_pay * self.anyother_allowances * 12
        total_other_benefits=self.house_rent_allowances+self.mobile_allowances+ self.conveyance_allowances+self.ltc+ self.anyother_allowances 

