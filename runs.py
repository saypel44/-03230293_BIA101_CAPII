class emploment_types:
    def  setemploment_types(self, emploment_types):
        self.emploment_types=emploment_types
    def getemploment_types(self):
        return self.emploment_types
    
Emp_types=emploment_types()
Emp_types.setemploment_types(input("Enter your employment type, if you are permanent or temporary: "))
print(Emp_types.getemploment_types())

class Sector:
    def  setSector(self, Sector):
        self.Sector=Sector
    def getSector(self):
        return self.Sector
    
Sector=Sector()
Sector.setSector(input("Enter your Sector, if you works under Government, private or cooperate: "))
print(Sector.getSector())



class BasicPay:
    def setBasicPay(self,BasicPay):
        self.BasicPay= BasicPay
    def getBasicPay(self):
        return self.BasicPay * 12

obj1 = BasicPay()
obj1.setBasicPay(float(input("Enter your basic pay: ")))
print(obj1.getBasicPay())


class Allowance:
    def __init__(self, allowance_percentage=0.0):
        self.allowance_percentage = allowance_percentage  # Convert to decimal

    def set_allowance_percentage(self, allowance_percentage):
        self.allowance_percentage = allowance_percentage / 100  # Convert to decimal

    def get_total_allowance(self, BasicPay):
        return self.allowance_percentage *BasicPay

obj2 = Allowance()
obj2.set_allowance_percentage(float(input("Enter your Allowance: ")))
print(obj2.get_total_allowance(obj1.getBasicPay())) 

class fees_remuneration:
    def __init__(self, fees_remuneration_percentage=0.0):
        self.fees_remuneration_percentage = fees_remuneration_percentage  # Convert to decimal

    def set_fees_remuneration_percentage(self,fees_remuneration_percentage):
        self.fees_remuneration_percentage =fees_remuneration_percentage / 100  # Convert to decimal

    def get_total_fees_remuneration_(self, BasicPay):
        return self.fees_remuneration_percentage *BasicPay 

obj3= fees_remuneration()
obj3.set_fees_remuneration_percentage(float(input("Enter your fees_remuneration_: ")))
print(obj3.get_total_fees_remuneration_(obj1.getBasicPay())) 

class commission:
    def __init__(self, commission_percentage=0.0):
        self.commission_percentage = commission_percentage  # Convert to decimal

    def set_commission_percentage(self,commission_percentage):
        self.commission_percentage =commission_percentage / 100  # Convert to decimal

    def get_total_commission(self, BasicPay):
        return self.commission_percentage *BasicPay 

obj4= commission()
obj4.set_commission_percentage(float(input("Enter your commission: ")))
print(obj4.get_total_commission(obj1.getBasicPay())) 

class leave_encashment:
    def __init__(self, leave_encashment_percentage=0.0):
        self.leave_encashment_percentage = leave_encashment_percentage # Convert to decimal

    def set_leave_encashment_percentage(self,leave_encashment_percentage):
        self.leave_encashment_percentage =leave_encashment_percentage / 100  # Convert to decimal

    def get_total_leave_encashment(self, BasicPay):
        return self.leave_encashment_percentage *BasicPay

obj5= leave_encashment()
obj5.set_leave_encashment_percentage(float(input("Enter your leave_encashment: ")))
print(obj5.get_total_leave_encashment(obj1.getBasicPay())) 

class shareofProfirreceived:
    def __init__(self, shareofProfirreceived_percentage=0.0):
        self.shareofProfirreceived_percentage = shareofProfirreceived_percentage  # Convert to decimal

    def set_shareofProfirreceived_percentage(self,shareofProfirreceived_percentage):
        self.shareofProfirreceived_percentage =shareofProfirreceived_percentage / 100  # Convert to decimal

    def get_total_shareofProfirreceived(self, BasicPay):
        return self.shareofProfirreceived_percentage *BasicPay 

obj6= shareofProfirreceived()
obj6.set_shareofProfirreceived_percentage(float(input("Enter your share of Profit received: ")))
print(obj6.get_total_shareofProfirreceived(obj1.getBasicPay()))

class consultancyIncome:
    def __init__(self, consultancyIncome_percentage=0.0):
        self.consultancyIncome_percentage = consultancyIncome_percentage # Convert to decimal

    def set_consultancyIncome_percentage(self,consultancyIncome_percentage):
        self.consultancyIncome_percentage =consultancyIncome_percentage / 100  # Convert to decimal

    def get_total_consultancyIncome(self, BasicPay):
        return self.consultancyIncome_percentage *BasicPay

obj7= consultancyIncome()
obj7.set_consultancyIncome_percentage(float(input("Enter your consultancy Income received: ")))
print(obj7.get_total_consultancyIncome(obj1.getBasicPay()))
    
class Other_HouseRentAllowances:
    def __init__(self, HouseRentAllowances_percentage=0.0):
        self.HouseRentAllowances_percentage = HouseRentAllowances_percentage  # Convert to decimal

    def set_HouseRentAllowances_percentage(self,HouseRentAllowances_percentage):
        self.HouseRentAllowances_percentage =HouseRentAllowances_percentage / 100  # Convert to decimal

    def get_total_HouseRentAllowances(self, BasicPay):
        return self.HouseRentAllowances_percentage *BasicPay 

obj8= Other_HouseRentAllowances()
obj8.set_HouseRentAllowances_percentage(float(input("Enter your other allowances that is house rent house rent  Income received: ")))
print(obj8.get_total_HouseRentAllowances(obj1.getBasicPay()))


class Other_mobile_allowances:
    def __init__(self, mobile_allowances_percentage=0.0):
        self.mobile_allowances_percentage = mobile_allowances_percentage  # Convert to decimal

    def set_mobile_allowances_percentage(self,mobile_allowances_percentage):
        self.mobile_allowances_percentage =mobile_allowances_percentage / 100  # Convert to decimal

    def get_total_mobile_allowances(self, BasicPay):
        return self.mobile_allowances_percentage *BasicPay

obj9= Other_mobile_allowances()
obj9.set_mobile_allowances_percentage(float(input("Enter your other allowances that is mobile_allowances received: ")))
print(obj9.get_total_mobile_allowances(obj1.getBasicPay()))

class Other_conveyance_allowances:
    def __init__(self, conveyance_allowances_percentage=0.0):
        self.conveyance_allowances_percentage = conveyance_allowances_percentage  # Convert to decimal

    def set_conveyance_allowances_percentage(self,conveyance_allowances_percentage):
        self.conveyance_allowances_percentage =conveyance_allowances_percentage / 100  # Convert to decimal

    def get_total_conveyance_allowances(self, BasicPay):
        return self.conveyance_allowances_percentage *BasicPay

obj10= Other_conveyance_allowances()
obj10.set_conveyance_allowances_percentage(float(input("Enter your other allowances that is conveyance_allowances received: ")))
print(obj10.get_total_conveyance_allowances(obj1.getBasicPay()))

class Other_ltc:
    def __init__(self, ltc_percentage=0.0):
        self.ltc_percentage =ltc_percentage  # Convert to decimal

    def set_ltc_percentage(self,ltc_percentage):
        self.ltc_percentage =ltc_percentage / 100  # Convert to decimal

    def get_total_ltc(self, BasicPay):
        return self.ltc_percentage *BasicPay

obj11= Other_ltc()
obj11.set_ltc_percentage(float(input("Enter your other allowances that is ltc received: ")))
print(obj11.get_total_ltc(obj1.getBasicPay()))

class Other_anyother_allowances:
    def __init__(self, anyother_allowances_percentage=0.0):
        self.anyother_allowances_percentage =anyother_allowances_percentage  # Convert to decimal

    def set_anyother_allowances_percentage(self,anyother_allowances_percentage):
        self.anyother_allowances_percentage =anyother_allowances_percentage / 100  # Convert to decimal

    def get_total_anyother_allowances(self, BasicPay):
        return self.anyother_allowances_percentage *BasicPay

obj12= Other_anyother_allowances()
obj12.set_anyother_allowances_percentage(float(input("Enter your other allowances that is anyother_allowances received: ")))
print(obj12.get_total_anyother_allowances(obj1.getBasicPay()))

# class NPPF:
#     def __init__(self, NPPF_percentage=0.0):
#         self.NPPF_percentage =NPPF_percentage # Convert to decimal

#     def set_NPPF_percentage(self,NPPF_percentage):
#         self.NPPF_percentage =NPPF_percentage / 100  # Convert to decimal

#     def get_total_NPPF(self, BasicPay):
#         return self.NPPF_percentage *BasicPay

# obj13= NPPF()
# obj13.set_NPPF_percentage(float(input("Enter NPPF deduction: ")))
# print(obj13.get_total_NPPF(obj1.getBasicPay()))


# class GIS:
#     def __init__(self, GIS_percentage=0.0):
#         self.GIS_percentage =GIS_percentage # Convert to decimal

#     def set_GIS_percentage(self,GIS_percentage):
#         self.GIS_percentage =GIS_percentage / 100  # Convert to decimal

#     def get_total_GIS(self, BasicPay):
#         return self.GIS_percentage *BasicPay

# obj14= GIS()
# obj14.set_GIS_percentage(float(input("Enter GIS deduction: ")))
# print(obj14.get_total_GIS(obj1.getBasicPay()))

# class children:
#     def __init__(self, children):
#         self.children =children # Convert to decimal

#     def set_children(self,children):
#         self.children=children # Convert to decimal

#     def get_children(self):
#         return self.children

class children:
    def set_children(self, children):
        self.children=children
    def getchildren(self):
        return self.children  
children=children()
children.set_children(int(input("Enter the number of children you have: ")))
print(children.getchildren())


class Kids_tax:
        def set_Kids_tax(self, children):
            self.Kids_tax= children* 85

        def get_Kids_tax(self):
            return self.Kids_tax 
childrenTax=Kids_tax()
childrenTax.set_Kids_tax(children.getchildren())
print(childrenTax.get_Kids_tax())

class income:

    def get_total_income(self, 
                         BasicPay, 
                         Allowance, 
                         fees_remuneration,
                         commission, 
                         leave_encashment, 
                         consultancyIncome , 
                         shareofProfirreceived,
                         Other_HouseRentAllowances, 
                         Other_mobile_allowances,
                         Other_conveyance_allowances,
                         Other_ltc,
                         Other_anyother_allowances,
                        #  NPPF,
                        #  GIS
       
                         ):
        
        return (BasicPay 
                + Allowance
                +fees_remuneration
                +commission 
                +leave_encashment
                +consultancyIncome
                +shareofProfirreceived
                +Other_HouseRentAllowances
                +Other_mobile_allowances
                +Other_conveyance_allowances
                +Other_ltc
                + Other_anyother_allowances
                # -NPPF
                # -GIS
        )
    
obj40=income()
# print(obj40.get_total_income(obj1.getBasicPay(), 
print(obj40.get_total_income(
    obj1.getBasicPay(),
    obj2.get_total_allowance(obj1.getBasicPay()),
    obj3.get_total_fees_remuneration_(obj1.getBasicPay()),
    obj4.get_total_commission(obj1.getBasicPay()), 
    obj5.get_total_leave_encashment(obj1.getBasicPay()), 
    obj6.get_total_shareofProfirreceived(obj1.getBasicPay()),
    obj7.get_total_consultancyIncome(obj1.getBasicPay()) , 
    obj8.get_total_HouseRentAllowances(obj1.getBasicPay()),
    obj9.get_total_mobile_allowances(obj1.getBasicPay()),
    obj10.get_total_conveyance_allowances(obj1.getBasicPay()),
    obj11.get_total_ltc(obj1.getBasicPay()),
    obj12.get_total_anyother_allowances(obj1.getBasicPay()),
    # obj13.get_total_NPPF(obj1.getBasicPay()),
    # obj14.get_total_GIS(obj1.getBasicPay())
))


class Deduction:
    def __init__(self, percentage):
        self.percentage = percentage / 100  # Convert to decimal

    def set_deduction_percentage(self, percentage):
        self.percentage = percentage / 100

    def get_deduction(self, base_pay):
        return self.percentage * base_pay

class NPPF(Deduction):
    pass

class GIS(Deduction):
    pass

deductions = [
    NPPF(float(input("Enter NPPF deduction percentage: "))),
    GIS(float(input("Enter GIS deduction percentage: "))),
]

class NetIncome:
    def calculate_net_income(income, Deduction):
        total_income = (obj40.get_total_income(
    obj1.getBasicPay(),
    obj2.get_total_allowance(obj1.getBasicPay()),
    obj3.get_total_fees_remuneration_(obj1.getBasicPay()),
    obj4.get_total_commission(obj1.getBasicPay()), 
    obj5.get_total_leave_encashment(obj1.getBasicPay()), 
    obj6.get_total_shareofProfirreceived(obj1.getBasicPay()),
    obj7.get_total_consultancyIncome(obj1.getBasicPay()) , 
    obj8.get_total_HouseRentAllowances(obj1.getBasicPay()),
    obj9.get_total_mobile_allowances(obj1.getBasicPay()),
    obj10.get_total_conveyance_allowances(obj1.getBasicPay()),
    obj11.get_total_ltc(obj1.getBasicPay()),
    obj12.get_total_anyother_allowances(obj1.getBasicPay()),
    # obj13.get_total_NPPF(obj1.getBasicPay()),
    # obj14.get_total_GIS(obj1.getBasicPay())
))

    # Subtract deductions
        for deduction in Deduction:
            total_income -= deduction.get_deduction(BasicPay)

            return total_income

NI=NetIncome()
print(NI(income, Deduction))


# class taxBreaks:
#     def getCalculateTB ( Netincome):
#     # def taxBreaks(Netincome):
#         if Netincome() <= 300000:
#             print(" 0% on NetIncome")
#             TB1= (0/100)*Netincome
#             print("Your income charge no tax rate" , TB1)

#         elif 300001<Netincome <400000:
#             print(" 10% on NetIncome")
#             TB2= (10/100)*Netincome
#             print("You have to pay" , TB2)

#         elif 400001<Netincome <650000:
#             print(" 15% on NetIncome")
#             TB3= (15/100)*Netincome
#             print("You have to pay" , TB3)

#         elif 650001<Netincome <1000000:
#             print(" 20% on NetIncome")
#             TB4= (20/100)*Netincome
#             print("You have to pay" , TB4)
    
#         elif 1000001<Netincome <1500000:
#             print(" 25% on NetIncome")
#             TB5= (25/100)*Netincome
#             print("You have to pay" , TB5)

#         else:
#             print(" 30% on NetIncome")
#             TB6= (30/100)*Netincome
#             print("You have to pay" , TB6)

# objTB= taxBreaks()
# # objTB.set_GIS_percentage(float(input("Enter GIS deduction: ")))
# print(objTB.getCalculateTB(obj40.get_total_income(BasicPay, 
#                          Allowance, 
#                          fees_remuneration,
#                          commission, 
#                          leave_encashment, 
#                          consultancyIncome , 
#                          shareofProfirreceived,
#                          Other_HouseRentAllowances, 
#                          Other_mobile_allowances,
#                          Other_conveyance_allowances,
#                          Other_ltc,
#                          Other_anyother_allowances,
#                          NPPF,
#                          GIS)))
#     # obj1.getBasicPay(),
# #     obj2.get_total_allowance(obj1.getBasicPay()),
# #     obj3.get_total_fees_remuneration_(obj1.getBasicPay()),
# #     obj4.get_total_commission(obj1.getBasicPay()), 
# #     obj5.get_total_leave_encashment(obj1.getBasicPay()), 
# #     obj6.get_total_shareofProfirreceived(obj1.getBasicPay()),
# #     obj7.get_total_consultancyIncome(obj1.getBasicPay()) , 
# #     obj8.get_total_HouseRentAllowances(obj1.getBasicPay()),
# #     obj9.get_total_mobile_allowances(obj1.getBasicPay()),
# #     obj10.get_total_conveyance_allowances(obj1.getBasicPay()),
# #     obj11.get_total_ltc(obj1.getBasicPay()),
# #     obj12.get_total_anyother_allowances(obj1.getBasicPay()),
# #     obj13.get_total_NPPF(obj1.getBasicPay()),
# #     obj14.get_total_GIS(obj1.getBasicPay()))
# # ))



# # print(objTB.getTB(obj40.get_total_income(BasicPay, 
# #                          Allowance, 
# #                          fees_remuneration,
# #                          commission, 
# #                          leave_encashment, 
# #                          consultancyIncome , 
# #                          shareofProfirreceived,
# #                          Other_HouseRentAllowances, 
# #                          Other_mobile_allowances,
# #                          Other_conveyance_allowances,
# #                          Other_ltc,
# #                          Other_anyother_allowances,
# #                          NPPF,
# #                          GIS)))