class AnnualBasicPay:
    def setBasicPay(self,BasicPay):
        self.BasicPay= BasicPay
    def getBasicPay(self):
        return self.BasicPay * 12

obj1 = AnnualBasicPay()
obj1.setBasicPay(float(input("Enter your basic pay: ")))
print(obj1.getBasicPay())
        
class Other_Allowance:
  def __init__(self, allowance_percentage=0.0):
    self.allowance_percentage = allowance_percentage / 100  # Convert to decimal

  def get_total_allowance(self, BasicPay):
    return self.allowance_percentage * BasicPay

class HouseRentAllowance(Other_Allowance):
  pass  # Inherits everything from Allowance

class MobileAllowance(Other_Allowance):
  pass  # Inherits everything from Allowance

class ConveyanceAllowance(Other_Allowance):
  pass  # Inherits everything from Allowance

class LTCAllowance(Other_Allowance):
  pass  # Inherits everything from Allowance

class any_otherallowances(Other_Allowance):
  pass
  

class OtherAllowances:
  def __init__(self, house_rent=0.0, mobile=0.0, conveyance=0.0, ltc=0.0, anyotherallowances=0.0):
    self.house_rent_allowance = HouseRentAllowance(house_rent)(float(input("Enter house rent allowance percentage: ")))
    self.mobile_allowance = MobileAllowance(mobile)
    self.conveyance_allowance = ConveyanceAllowance(conveyance)
    self.ltc_allowance = LTCAllowance(ltc)
    self.anyother_allowances=any_otherallowances(anyotherallowances)

  def get_total_other_allowances(self,BasicPay):
    total_allowance = 0
    total_allowance += self.house_rent_allowance.get_total_allowance(BasicPay)*BasicPay
    total_allowance += self.mobile_allowance.get_total_allowance(BasicPay)*BasicPay
    total_allowance += self.conveyance_allowance.get_total_allowance(BasicPay)*BasicPay
    total_allowance += self.ltc_allowance.get_total_allowance(BasicPay)*BasicPay
    total_allowance+=self.anyother_allowances.get_total_allowance(BasicPay)*BasicPay            
    return total_allowance

# Usage
# basic_pay = float(input("Enter your basic pay: "))

# # other_allowances = OtherAllowances(
# #     house_rent=float(input("Enter house rent allowance percentage: ")),
# #     mobile=float(input("Enter mobile allowance percentage: ")),
# #     conveyance=float(input("Enter conveyance allowance percentage: ")),
# #     ltc=float(input("Enter LTC allowance percentage: ")),
# #     anyotherallowances=float(input("Enter any other  allowance percentage: "))
# )

total_other_allowances = other_allowances.get_total_other_allowances(obj1.getBasicPay())
print(f"Total Other Allowances: {total_other_allowances:.2f}")

class total:
  def getTotal(self,AnnualBasicPay, OtherAllowances):
        return AnnualBasicPay +OtherAllowances

T = total()
# T.setBasicPay(float(input("Enter your basic pay: ")))
print(T.getTotal(obj1.getBasicPay(), other_allowances.get_total_other_allowances(obj1.getBasicPay())))
        