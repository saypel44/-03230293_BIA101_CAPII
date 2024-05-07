


class AnnualBasicPay:
    def setBasicPay(self,BasicPay):
        self.BasicPay= BasicPay
    def getBasicPay(self):
        return self.BasicPay * 12

obj1 = AnnualBasicPay()
obj1.setBasicPay(float(input("Enter your basic pay: ")))
print(obj1.getBasicPay())

# class Allowance:
#     def setAllowance(self, Allowance ):
#         self.Allowance= (Allowance/100) 
#     def getAllowance(self, BasicPay, obj1.AnnualBasicPay):
#         return (self.Allowance * BasicPay * 12 ) + obj1.AnnualBasicPay

class Allowance:
    def __init__(self, allowance_percentage=0.0):
        self.allowance_percentage = allowance_percentage / 100  # Convert to decimal

    def set_allowance_percentage(self, allowance_percentage):
        self.allowance_percentage = allowance_percentage / 100  # Convert to decimal

    def get_total_allowance(self, BasicPay):
        return self.allowance_percentage *BasicPay* 12 

obj2 = Allowance()
obj2.set_allowance_percentage(float(input("Enter your Allowance: ")))
print(obj2.get_total_allowance(obj1.getBasicPay())) 

class fees_remuneration:
    def __init__(self, fees_remuneration_percentage=0.0):
        self.fees_remuneration_percentage = fees_remuneration_percentage / 100  # Convert to decimal

    def set_fees_remuneration_percentage(self,fees_remuneration_percentage):
        self.fees_remuneration_percentage =fees_remuneration_percentage / 100  # Convert to decimal

    def get_total_fees_remuneration_(self, BasicPay):
        return self.fees_remuneration_percentage *BasicPay* 12 

obj3= fees_remuneration()
obj3.set_fees_remuneration_percentage(float(input("Enter your fees_remuneration_: ")))
print(obj3.get_total_fees_remuneration_(obj1.getBasicPay())) 

class commission:
    def __init__(self, commission_percentage=0.0):
        self.commission_percentage = commission_percentage / 100  # Convert to decimal

    def set_commission_percentage(self,commission_percentage):
        self.commission_percentage =commission_percentage / 100  # Convert to decimal

    def get_total_commission(self, BasicPay):
        return self.commission_percentage *BasicPay* 12 

obj4= commission()
obj4.set_commission_percentage(float(input("Enter your commission: ")))
print(obj4.get_total_commission(obj1.getBasicPay())) 

class leave_encashment:
    def __init__(self, leave_encashment_percentage=0.0):
        self.leave_encashment_percentage = leave_encashment_percentage / 100  # Convert to decimal

    def set_leave_encashment_percentage(self,leave_encashment_percentage):
        self.leave_encashment_percentage =leave_encashment_percentage / 100  # Convert to decimal

    def get_total_leave_encashment(self, BasicPay):
        return self.leave_encashment_percentage *BasicPay* 12 

obj5= leave_encashment()
obj5.set_leave_encashment_percentage(float(input("Enter your leave_encashment: ")))
print(obj5.get_total_leave_encashment(obj1.getBasicPay())) 

class shareofProfirreceived:
    def __init__(self, shareofProfirreceived_percentage=0.0):
        self.shareofProfirreceived_percentage = shareofProfirreceived_percentage / 100  # Convert to decimal

    def set_shareofProfirreceived_percentage(self,shareofProfirreceived_percentage):
        self.shareofProfirreceived_percentage =shareofProfirreceived_percentage / 100  # Convert to decimal

    def get_total_shareofProfirreceived(self, BasicPay):
        return self.shareofProfirreceived_percentage *BasicPay* 12 

obj6= shareofProfirreceived()
obj6.set_shareofProfirreceived_percentage(float(input("Enter your share of Profit received: ")))
print(obj6.get_total_shareofProfirreceived(obj1.getBasicPay()))

class consultancyIncome:
    def __init__(self, consultancyIncome_percentage=0.0):
        self.consultancyIncome_percentage = consultancyIncome_percentage / 100  # Convert to decimal

    def set_consultancyIncome_percentage(self,consultancyIncome_percentage):
        self.consultancyIncome_percentage =consultancyIncome_percentage / 100  # Convert to decimal

    def get_total_consultancyIncome(self, BasicPay):
        return self.consultancyIncome_percentage *BasicPay* 12 

obj7= consultancyIncome()
obj7.set_consultancyIncome_percentage(float(input("Enter your consultancy Income received: ")))
print(obj7.get_total_consultancyIncome(obj1.getBasicPay()))
    
class Other_HouseRentAllowances:
    def __init__(self, HouseRentAllowances_percentage=0.0):
        self.HouseRentAllowances_percentage = HouseRentAllowances_percentage / 100  # Convert to decimal

    def set_HouseRentAllowances_percentage(self,HouseRentAllowances_percentage):
        self.HouseRentAllowances_percentage =HouseRentAllowances_percentage / 100  # Convert to decimal

    def get_total_HouseRentAllowances(self, BasicPay):
        return self.HouseRentAllowances_percentage *BasicPay* 12 

obj8= Other_HouseRentAllowances()
obj8.set_HouseRentAllowances_percentage(float(input("Enter your other allowances that is house rent house rent  Income received: ")))
print(obj8.get_total_HouseRentAllowances(obj1.getBasicPay()))


class Other_mobile_allowances:
    def __init__(self, mobile_allowances_percentage=0.0):
        self.mobile_allowances_percentage = mobile_allowances_percentage / 100  # Convert to decimal

    def set_mobile_allowances_percentage(self,mobile_allowances_percentage):
        self.mobile_allowances_percentage =mobile_allowances_percentage / 100  # Convert to decimal

    def get_total_mobile_allowances(self, BasicPay):
        return self.mobile_allowances_percentage *BasicPay* 12 

obj9= Other_mobile_allowances()
obj9.set_mobile_allowances_percentage(float(input("Enter your other allowances that is mobile_allowances received: ")))
print(obj9.get_total_mobile_allowances(obj1.getBasicPay()))

class Other_conveyance_allowances:
    def __init__(self, conveyance_allowances_percentage=0.0):
        self.conveyance_allowances_percentage = conveyance_allowances_percentage / 100  # Convert to decimal

    def set_conveyance_allowances_percentage(self,conveyance_allowances_percentage):
        self.conveyance_allowances_percentage =conveyance_allowances_percentage / 100  # Convert to decimal

    def get_total_conveyance_allowances(self, BasicPay):
        return self.conveyance_allowances_percentage *BasicPay* 12 

obj10= Other_conveyance_allowances()
obj10.set_conveyance_allowances_percentage(float(input("Enter your other allowances that is conveyance_allowances received: ")))
print(obj10.get_total_conveyance_allowances(obj1.getBasicPay()))

class Other_ltc:
    def __init__(self, ltc_percentage=0.0):
        self.ltc_percentage =ltc_percentage / 100  # Convert to decimal

    def set_ltc_percentage(self,ltc_percentage):
        self.ltc_percentage =ltc_percentage / 100  # Convert to decimal

    def get_total_ltc(self, BasicPay):
        return self.ltc_percentage *BasicPay* 12 

obj11= Other_ltc()
obj11.set_ltc_percentage(float(input("Enter your other allowances that is ltc received: ")))
print(obj11.get_total_ltc(obj1.getBasicPay()))

class Other_anyother_allowances:
    def __init__(self, anyother_allowances_percentage=0.0):
        self.anyother_allowances_percentage =anyother_allowances_percentage / 100  # Convert to decimal

    def set_anyother_allowances_percentage(self,anyother_allowances_percentage):
        self.anyother_allowances_percentage =anyother_allowances_percentage / 100  # Convert to decimal

    def get_total_anyother_allowances(self, BasicPay):
        return self.anyother_allowances_percentage *BasicPay* 12 

obj12= Other_anyother_allowances()
obj12.set_anyother_allowances_percentage(float(input("Enter your other allowances that is anyother_allowances received: ")))
print(obj12.get_total_anyother_allowances(obj1.getBasicPay()))








class Netincome:
    def get_total_income(self, 
                         AnnualBasicPay, 
                         Allowance, 
                         fees_remuneration,
                         commission, 
                         leave_encashment, 
                         consultancyIncome , 
                         Other_HouseRentAllowances, 
                         Other_mobile_allowances,
                         Other_conveyance_allowances,
                         Other_ltc,
                        Other_anyother_allowances
                         
                         ):
        return (AnnualBasicPay 
                + Allowance+fees_remuneration
                +commission 
                +leave_encashment
                +consultancyIncome
                +Other_HouseRentAllowances
                +Other_mobile_allowances
                +Other_conveyance_allowances
                +Other_ltc,
                + Other_anyother_allowances
        )
    
obj40=Netincome()
print(obj40.get_total_income(obj1.getBasicPay(), 
    obj2.get_total_allowance(obj1.getBasicPay()),
    obj3.get_total_fees_remuneration_(obj1.getBasicPay()),
    obj4.get_total_commission(obj1.getBasicPay()), 
    obj5.get_total_leave_encashment(obj1.getBasicPay()), 
    obj7.get_total_consultancyIncome(obj1.getBasicPay()) , 
    obj8.get_total_HouseRentAllowances(obj1.getBasicPay()),
    obj9.get_total_mobile_allowances(obj1.getBasicPay()),
    obj10.get_total_conveyance_allowances(obj1.getBasicPay()),
    obj11.get_total_ltc(obj1.getBasicPay()),
    obj12.get_total_anyother_allowances(obj1.getBasicPay())
    
    ))
