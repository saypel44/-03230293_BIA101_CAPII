# 1. Basic Pay
class BasicPay:
  def __init__(self, basic_pay):
    self.basic_pay = basic_pay  # Store monthly basic pay

  def get_basic_pay(self):
    self.annual_basic_pay = self.basic_pay * 12  # Calculate annual pay
    print(f"The annual basic pay I received: Nu.{self.annual_basic_pay:.2f}")  # Format to 2 decimals
    return self.annual_basic_pay  # Return the calculated value

# ... (rest of the code)

BP = BasicPay(basic_pay=int(input("Enter basic pay in a month: ")))
BP.get_basic_pay()  # Call the method to calculate and print annual pay

class OtherBenefits:
  def __init__(self):
    self.HouseRentAllowances = None  # Initialize allowances to None
    self.mobile_allowances = None
    self.conveyance_allowances = None
    self.ltc = None
    self.anyother_allowances = None

  def setBenefits(self, house_rent_allowance, mobile_allowance, conveyance_allowance, ltc, anyother_allowance):
    self.HouseRentAllowances = house_rent_allowance
    self.mobile_allowances = mobile_allowance
    self.conveyance_allowances = conveyance_allowance
    self.ltc = ltc
    self.anyother_allowances = anyother_allowance

  def getBenefits(self):
    return (self.HouseRentAllowances * BP.get_basic_pay(),  # Use BP.get_basic_pay()
            self.mobile_allowances * BP.get_basic_pay(),
            # ... (rest of calculations)
            self.conveyance_allowances * BP.get_basic_pay(),
            self.ltc * BP.get_basic_pay(),
            self.anyother_allowances *BP.get_basic_pay())

# class OtherBenefits:
#   def __init__(self):
#     self.HouseRentAllowances = None  # Initialize allowances to None
#     self.mobile_allowances = None
#     self.conveyance_allowances = None
#     self.ltc = None
#     self.anyother_allowances = None

#   def setBenefits(self, house_rent_allowance, mobile_allowance, conveyance_allowance, ltc, anyother_allowance):
#     self.HouseRentAllowances = house_rent_allowance
#     self.mobile_allowances = mobile_allowance
#     self.conveyance_allowances = conveyance_allowance
#     self.ltc = ltc
#     self.anyother_allowances = anyother_allowance

#   def getBenefits(self):
#     return (self.HouseRentAllowances * BP.get_basic_pay(),  # Use BP.get_basic_pay()
#             self.mobile_allowances * BP.get_basic_pay(),
#             self.conveyance_allowances * BP.get_basic_pay(),
#             self.ltc * BP.get_basic_pay(),
#             self.anyother_allowances *BP.get_basic_pay())

# Example usage
OB = OtherBenefits()

# Get user input for allowances (assuming they're percentages)
house_rent_allowance = float(input("Enter House Rent Allowance I received in a month (in percentage): "))
mobile_allowance = float(input("Enter Mobile Allowance I received in a month (in percentage): "))
conveyance_allowance = float(input("Enter Conveyance Allowance I received in a month (in percentage): "))
ltc = float(input("Enter LTC Allowance I received in a month (in percentage): "))
anyother_allowance = float(input("Enter Any Other Allowance I received in a month (in percentage): "))

# Set benefits using individual allowance values
OB.setBenefits(house_rent_allowance / 100, mobile_allowance / 100, conveyance_allowance / 100, ltc / 100, anyother_allowance / 100)

# Get and print all benefits as a tuple

print(OB.getBenefits())


