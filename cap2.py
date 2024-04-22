#10th May

#whiteboarding - easy and medium - Tuesdaay 

class Taxpayer:
  def __init__(self, basic_pay, employment_type, sector, children, nppf, gis):
    self.basic_pay = basic_pay
    self.employment_type = employment_type
    self.sector = sector
    self.children = children
    self.nppf = nppf
    self.gis = gis

Detail= Taxpayer(basic_pay=14675, employment_type= "Regular", sector= "government", children= 3, nppf=0,  gis=300 )
# Accessing attributes and calling methods
# print("basic_pay:", Detail.basic_pay, "Employment type: ", Detail.employment_type, "Sector: ", Detail.sector, "Children: ", Detail.children, "nppf:",  Detail.nppf, "gis:", Detail.gis)
# print(Detail.basic_pay-Detail.nppf-  Detail.gis)

class Income:
    def __init__(self, basic_pay_allowances, fees_remuneration, bonus, commission, leave_encashment, shareofProfirreceived, consultancy_income, benefitsReceived):
      self.basic_pay_allowances= basic_pay_allowances
      self.fees_remuneration=fees_remuneration
      self.bonus=bonus
      self.commission=commission
      self.leave_encashment=leave_encashment
      self.shareofProfirreceived=shareofProfirreceived
      self.consultancy_income=consultancy_income
      self.benefitsReceived=benefitsReceived
      

class PIT_Tax_Rates:
   def __init__(self, Income):
      self.Income= Detail.basic_pay()
    #   self.
print(Detail.basic_pay)
# 1	Up to Nu. 300,000	0%
# 2	Nu.300,001 to Nu. 400,000	10%
# 3	Nu. 400,001 to Nu. 650,000	15%
# 4	Nu. 650,001 to Nu. 1,000,000	20%
# 5	Nu. 1,000,001 to Nu. 1,500,000	25%
# 6	Nu. 1,500,001 and up	30%
# Surcharge at the rate of 10% shall be levied on (PIT)	Personal Income Tax, if the annual Personal Income Tax	is equal to or more than Nu. 1,000,000.
# Property

class TaxCalculator:
  """
  This class calculates income tax based on provided income and tax brackets.
  """
  def __init__(self):
    self.brackets = [
      (0, 300000, 0),
      (300001, 400000, 0.1),
      (400001, 650000, 0.15),
      (650001, 1000000, 0.2),
      (1000001, 1500000, 0.25),
      (1500001, float('inf'), 0.3)
    ]
    self.surcharge_rate = 0.1

  def calculate_tax(self, income):
    """
    Calculates income tax for a given income amount.

    Args:
      income: The income amount for which to calculate tax.

    Returns:
      The total income tax amount.
    """
    tax = 0
    for lower_limit, upper_limit, rate in self.brackets:
      if income <= lower_limit:
        continue
      elif income <= upper_limit:
        tax += (income - lower_limit) * rate
        break
      else:
        tax += (upper_limit - lower_limit) * rate
        income -= upper_limit

    # Apply surcharge if income tax is equal to or more than 1,000,000 Nu
    if tax >= 1000000:
      tax += tax * self.surcharge_rate

    return tax

# Example usage
calculator = TaxCalculator()
income = 800000
tax = calculator.calculate_tax(income)
print(f"Income tax for Nu. {income:,.2f} is Nu. {tax:,.2f}")
