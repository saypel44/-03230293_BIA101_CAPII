class AnnualBasicPay:
    def setBasicPay(self,BasicPay):
        self.BasicPay= BasicPay
    def getBasicPay(self):
        return self.BasicPay * 12

obj1 = AnnualBasicPay()
obj1.setBasicPay(float(input("Enter your basic pay: ")))
print(obj1.getBasicPay())
# Call the method to calculate and print annual pay

# class Other_benefits:
#  # attribute and method of the parent class
#     name = "" 
#     def Other_benefits(self):
#         print("Other_benefits: ")

#         self.HouseRentAllowances=None 
#         self.mobile_allowances=None 
#         self.conveyance_allowances=None 
#         self.ltc=None 
#         self.anyother_allowances=None 

# inherit from Animal
class Allowance:
  """
  This class represents a generic allowance with basic functionalities.
  """
  def __init__(self, allowance_percentage, allowance_name):
    self.allowance_percentage = allowance_percentage / 100  # Convert percentage to decimal
    self.allowance_name = allowance_name

  def set_allowance_percentage(self, allowance_percentage):
    self.allowance_percentage = allowance_percentage / 100  # Convert to decimal

  def get_allowance_percentage(self):
    return self.allowance_percentage

  def get_total_allowance(self, BasicPay):
    return self.allowance_percentage * BasicPay * 12

class HouseRentAllowances(Allowance):
  """
  This class inherits from Allowance and specifically represents House Rent Allowances.
  """
  def __init__(self, allowance_percentage):
    super().__init__(allowance_percentage, "House Rent Allowance")  # Call base class constructor with name

class MobileAllowances(Allowance):
  """
  This class inherits from Allowance and specifically represents Mobile Allowances.
  """
  def __init__(self, allowance_percentage):
    super().__init__(allowance_percentage, "Mobile Allowance")  # Call base class constructor with name

# Similar classes for conveyance_allowances, ltc, and AnyOtherAllowances

class TotalAllowances:
  """
  This class calculates the total allowance by combining all other allowances.
  """
  def __init__(self, allowances):
    self.allowances = allowances

  def calculate_total_allowance(self):
    total_allowance = 0
    for allowance in self.allowances:
      total_allowance += allowance.get_total_allowance()  # Assuming basic_pay is set globally
    return total_allowance

  def display_total_allowance(self):
    total_allowance = self.calculate_total_allowance()
    print(f"The Total Allowances I received: Nu.{total_allowance:.2f}")

# Example usage
# basic_pay = 10000  # Assuming basic_pay is set here

HA = HouseRentAllowances(float(input("Enter House rent Allowances received in a month in percentage: ")))
MA = MobileAllowances(float(input("Enter Mobile Allowances received in a month in percentage: ")))

# You can create similar objects for conveyance_allowances, ltc, and anyother_allowances

allowances = [HA, MA]  #    List of allowance objects

total_allowances = TotalAllowances(allowances)
total_allowances.display_total_allowance(obj1.getBasicPay())
