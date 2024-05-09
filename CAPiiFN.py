#Employee employment type
class Emploment_Types:
    def  setEmploment_Types(self, emploment_types): 
        self.emploment_types=emploment_types
    def getEmploment_Types(self):
        return self.emploment_types   
Emp_types=Emploment_Types()
Emp_types.setEmploment_Types(input("Enter your employment type; permanent or contract:  "))
print(Emp_types.getEmploment_Types())

#Employee sector
class Sector:
    def  setSector(self, Sector):
        self.Sector=Sector
    def getSector(self):
        return self.Sector   
Sector=Sector()
Sector.setSector(input("Enter your Sector; Government, private or cooperate: "))
print(Sector.getSector())

#employee basic pay
class BasicPay:
    def setBasicPay(self,BasicPay):
        self.BasicPay= BasicPay
    def getBasicPay(self):
        return  self.BasicPay * 12  # returns Annual basic
obj1 = BasicPay()
obj1.setBasicPay(float(input("Enter your monthly basic pay: ")))
print(obj1.getBasicPay())

#employee recieving only allowances
class Allowance:
    def __init__(self, allowance_percentage=0.0):
        self.allowance_percentage = allowance_percentage  

    def set_allowance_percentage(self, allowance_percentage):
        self.allowance_percentage = allowance_percentage / 100  # Convert to decimal

    def get_total_allowance(self, BasicPay):
        return self.allowance_percentage *BasicPay #Annual allowances received on basic pay
obj2 = Allowance()
obj2.set_allowance_percentage(float(input("Enter your Allowance receive in percentage: ")))
print(obj2.get_total_allowance(obj1.getBasicPay())) 

#Employee receiving fees remuneration
class fees_remuneration:
    def __init__(self, fees_remuneration_percentage=0.0):
        self.fees_remuneration_percentage = fees_remuneration_percentage  

    def set_fees_remuneration_percentage(self,fees_remuneration_percentage):
        self.fees_remuneration_percentage =fees_remuneration_percentage / 100  # Convert to decimal

    def get_total_fees_remuneration_(self, BasicPay):
        return self.fees_remuneration_percentage *BasicPay #returns Annual amount
obj3= fees_remuneration()
obj3.set_fees_remuneration_percentage(float(input("Enter your fees remuneration receive in percentage: ")))
print(obj3.get_total_fees_remuneration_(obj1.getBasicPay())) 

#Employee receiving commision 
class commission:
    def __init__(self, commission_percentage=0.0):
        self.commission_percentage = commission_percentage  
    def set_commission_percentage(self,commission_percentage):
        self.commission_percentage =commission_percentage / 100  # Convert to decimal

    def get_total_commission(self, BasicPay):
        return self.commission_percentage *BasicPay  #returns Annual amount
obj4= commission()
obj4.set_commission_percentage(float(input("Enter your commission receive in percentage: ")))
print(obj4.get_total_commission(obj1.getBasicPay())) 

#Employee receiving leanve encasment
class leave_encashment:
    def __init__(self, leave_encashment_percentage=0.0):
        self.leave_encashment_percentage = leave_encashment_percentage 

    def set_leave_encashment_percentage(self,leave_encashment_percentage):
        self.leave_encashment_percentage =leave_encashment_percentage / 100  # Convert to decimal

    def get_total_leave_encashment(self, BasicPay):
        return self.leave_encashment_percentage *BasicPay #returns Annual amount
obj5= leave_encashment()
obj5.set_leave_encashment_percentage(float(input("Enter your leave_encashment receive in percentage: ")))
print(obj5.get_total_leave_encashment(obj1.getBasicPay())) 

#Employee receiving share of profit
class shareofProfirreceived:
    def __init__(self, shareofProfirreceived_percentage=0.0):
        self.shareofProfirreceived_percentage = shareofProfirreceived_percentage  

    def set_shareofProfirreceived_percentage(self,shareofProfirreceived_percentage):
        self.shareofProfirreceived_percentage =shareofProfirreceived_percentage / 100  # Convert to decimal

    def get_total_shareofProfirreceived(self, BasicPay):
        return self.shareofProfirreceived_percentage *BasicPay #returns Annual amount 
obj6= shareofProfirreceived()
obj6.set_shareofProfirreceived_percentage(float(input("Enter your share of Profit receive in percentage: ")))
print(obj6.get_total_shareofProfirreceived(obj1.getBasicPay()))


#Employee receiving consultancy income
class consultancyIncome:
    def __init__(self, consultancyIncome_percentage=0.0):
        self.consultancyIncome_percentage = consultancyIncome_percentage

    def set_consultancyIncome_percentage(self,consultancyIncome_percentage):
        self.consultancyIncome_percentage =consultancyIncome_percentage / 100  # Convert to decimal

    def get_total_consultancyIncome(self, BasicPay):
        return self.consultancyIncome_percentage *BasicPay #returns Annual amount
obj7= consultancyIncome()
obj7.set_consultancyIncome_percentage(float(input("Enter your consultancy Income receive in percentage: ")))
print(obj7.get_total_consultancyIncome(obj1.getBasicPay()))

#Employee receiving other allowances that are house rent, mobile, conyevance, ltc and other allowances     
class Other_HouseRentAllowances:
    def __init__(self, HouseRentAllowances_percentage=0.0):
        self.HouseRentAllowances_percentage = HouseRentAllowances_percentage 

    def set_HouseRentAllowances_percentage(self,HouseRentAllowances_percentage):
        self.HouseRentAllowances_percentage =HouseRentAllowances_percentage / 100  # Convert to decimal

    def get_total_HouseRentAllowances(self, BasicPay):
        return self.HouseRentAllowances_percentage *BasicPay  #returns Annual amount 
obj8= Other_HouseRentAllowances()
obj8.set_HouseRentAllowances_percentage(float(input("Enter your other allowances that is house rent house rent  Income receive in percentage: ")))
print(obj8.get_total_HouseRentAllowances(obj1.getBasicPay()))


class Other_mobile_allowances:
    def __init__(self, mobile_allowances_percentage=0.0):
        self.mobile_allowances_percentage = mobile_allowances_percentage  

    def set_mobile_allowances_percentage(self,mobile_allowances_percentage):
        self.mobile_allowances_percentage =mobile_allowances_percentage / 100  # Convert to decimal

    def get_total_mobile_allowances(self, BasicPay):
        return self.mobile_allowances_percentage *BasicPay  #returns Annual amount
obj9= Other_mobile_allowances()
obj9.set_mobile_allowances_percentage(float(input("Enter your other allowances that is mobile_allowances receive in percentage: ")))
print(obj9.get_total_mobile_allowances(obj1.getBasicPay()))

class Other_conveyance_allowances:
    def __init__(self, conveyance_allowances_percentage=0.0):
        self.conveyance_allowances_percentage = conveyance_allowances_percentage  

    def set_conveyance_allowances_percentage(self,conveyance_allowances_percentage):
        self.conveyance_allowances_percentage =conveyance_allowances_percentage / 100  # Convert to decimal

    def get_total_conveyance_allowances(self, BasicPay):
        return self.conveyance_allowances_percentage *BasicPay  #returns Annual amount
obj10= Other_conveyance_allowances()
obj10.set_conveyance_allowances_percentage(float(input("Enter your other allowances that is conveyance_allowances receive in percentage: ")))
print(obj10.get_total_conveyance_allowances(obj1.getBasicPay()))

class Other_ltc:
    def __init__(self, ltc_percentage=0.0):
        self.ltc_percentage =ltc_percentage  

    def set_ltc_percentage(self,ltc_percentage):
        self.ltc_percentage =ltc_percentage / 100  # Convert to decimal

    def get_total_ltc(self, BasicPay):
        return self.ltc_percentage *BasicPay #returns Annual amount
obj11= Other_ltc()
obj11.set_ltc_percentage(float(input("Enter your other allowances that is ltc receive in percentage: ")))
print(obj11.get_total_ltc(obj1.getBasicPay()))

class Other_anyother_allowances:
    def __init__(self, anyother_allowances_percentage=0.0):
        self.anyother_allowances_percentage =anyother_allowances_percentage  

    def set_anyother_allowances_percentage(self,anyother_allowances_percentage):
        self.anyother_allowances_percentage =anyother_allowances_percentage / 100  # Convert to decimal

    def get_total_anyother_allowances(self, BasicPay):
        return self.anyother_allowances_percentage *BasicPay #returns Annual amount
obj12= Other_anyother_allowances()
obj12.set_anyother_allowances_percentage(float(input("Enter your other allowances that is anyother_allowances receive in percentage: ")))
print(obj12.get_total_anyother_allowances(obj1.getBasicPay()))


#Employee deduction NPPF 
class NPPF:
    def __init__(self, NPPF_percentage=0.0):
        self.NPPF_percentage =NPPF_percentage 

    def set_NPPF_percentage(self,NPPF_percentage):
        self.NPPF_percentage =NPPF_percentage / 100  # Convert to decimal

    def get_total_NPPF(self, BasicPay):
        return self.NPPF_percentage *BasicPay #returns Annual amount
obj13= NPPF()
obj13.set_NPPF_percentage(float(input("Enter NPPF deduction in percentage: ")))
print(obj13.get_total_NPPF(obj1.getBasicPay()))


#Employee deduction GIS
class GIS:
    def __init__(self, GIS_percentage=0.0):
        self.GIS_percentage =GIS_percentage 

    def set_GIS_percentage(self,GIS_percentage):
        self.GIS_percentage =GIS_percentage / 100  # Convert to decimal

    def get_total_GIS(self, BasicPay):
        return self.GIS_percentage *BasicPay #returns Annual amount
obj14= GIS()
obj14.set_GIS_percentage(float(input("Enter GIS deduction in percentage: ")))
print(obj14.get_total_GIS(obj1.getBasicPay()))


#Employee having child or not 
class children:
    def set_children(self, children):
        self.children=children
    def getchildren(self):
        return self.children   #returns the number children employee has
children=children()
children.set_children(int(input("Enter the number of children going school: ")))
print(children.getchildren())

class Kidsallowances:
    def set_Kidsallowances(self, Kidsallowances):
        self.Kidsallowances=Kidsallowances 
    def getKidsallowances(self):
        return self.Kidsallowances   #REturns the amount of education allowances employee recievd in a year
Kidsallowances=Kidsallowances()
Kidsallowances.set_Kidsallowances(int(input("Enter the amount of allowances you received for children going school per head in a year which should be less than or equal to Nu.350,000: ")))
print(Kidsallowances.getKidsallowances())


# if have kids, tax on it
class Kids_tax:
        def set_Kids_tax(self, children, Kidsallowances):
            self.Kids_tax= children * Kidsallowances #Calculates the education allowances receied based on number of kids going school

        def get_Kids_tax(self):
            return self.Kids_tax 
childrenTax=Kids_tax()
childrenTax.set_Kids_tax(children.getchildren(), Kidsallowances.getKidsallowances())
print(childrenTax.get_Kids_tax())

#Employee NetIncome after adding incomes and deduct the NPPF and GIS and even education allowances on kids
class Netincome:
    def setnetincome(self,  BasicPay, 
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
                         NPPF,
                         GIS,
                         Kids_tax):
        self.netincome=( BasicPay 
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
                -NPPF
                -GIS
                -Kids_tax)
        
    def getnetincome(self):
        return self.netincome
    
NetIncome=Netincome()
NetIncome.setnetincome(
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
    obj13.get_total_NPPF(obj1.getBasicPay()),
    obj14.get_total_GIS(obj1.getBasicPay()),
    childrenTax.get_Kids_tax())
print(NetIncome.getnetincome())


#implication of tax breaks based on emploees netincome            
class tax_break:
  def __init__(self): 
    self.tax_info = None

  def calculate_tax_breaks(self, Netincome):
    if Netincome <= 300000:
      print("0% on NetIncome,so, No Tax should be paid")
    
    elif 300001 < Netincome <= 400000:
      print("10% on NetIncome")
      Tax = Netincome * 0.1 #10% is implemented on taxable income 
      print("You have to pay", Tax)

    elif 400001 < Netincome <= 650000:
        print("15% on NetIncome")
        Tax=(Netincome * 0.15) #15% is implemented on taxable income
        print("You have to pay", Tax)

        
    elif 650001 < Netincome <= 1000000:
        print("20% on NetIncome")
        Tax=(Netincome * 0.2) #20% is implemented on taxable income
        print("You have to pay",Tax)
        
    elif 1000001 < Netincome < 1500000:  
        print("25% on NetIncome")
        Tax=(Netincome * 0.25) #25% is implemented on taxable income
        print("You have to pay", Tax)

    else:
      print("30% on NetIncome")
      Tax=(Netincome * 0.30) #30% is implemented on taxable income
      print("You have to pay", Tax)
    self.tax_info = "Tax calculation completed."  # Update after calculations

  def get_tax_breaks(self):
    return self.tax_info  # Return the stored tax info

TB = tax_break()
TB.calculate_tax_breaks(NetIncome.getnetincome())
tax_info = TB.get_tax_breaks()
print(tax_info)


