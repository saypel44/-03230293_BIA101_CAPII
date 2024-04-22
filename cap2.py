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
      self.
print(Detail.basic_pay)
# 1	Up to Nu. 300,000	0%
# 2	Nu.300,001 to Nu. 400,000	10%
# 3	Nu. 400,001 to Nu. 650,000	15%
# 4	Nu. 650,001 to Nu. 1,000,000	20%
# 5	Nu. 1,000,001 to Nu. 1,500,000	25%
# 6	Nu. 1,500,001 and up	30%
# Surcharge at the rate of 10% shall be levied on (PIT)	Personal Income Tax, if the annual Personal Income Tax	is equal to or more than Nu. 1,000,000.
# Property