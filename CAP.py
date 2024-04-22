# : 02908728_BIA101_CAPII

class Taxpayer:
  def __init__(self, basic_pay, employment_type, sector, children, nppf, gis):
    self.basic_pay = basic_pay
    self.employment_type = employment_type
    self.sector = sector
    self.children = children
    self.nppf = nppf
    self.gis = gis

  # ... other methods for deductions, taxable income, and tax calculation

Detail= Taxpayer(basic_pay=14675, employment_type= "Regular", sector= "government", children= 3, nppf=0,  gis=300 )
# Accessing attributes and calling methods
print("basic_pay:", Detail.basic_pay, "Employment type: ", Detail.employment_type, "Sector: ", Detail.sector, "Children: ", Detail.children, "nppf:",  Detail.nppf, "gis:", Detail.gis)
print(Detail.basic_pay-Detail.nppf-  Detail.gis)