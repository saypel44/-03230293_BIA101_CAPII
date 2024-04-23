class Income:
  """
  This class represents an individual's income for PIT calculations.
  """

  def __init__(self, basic_pay, employment_type, sector, children, nppf, gis, basic_pay_allowances, 
               fees_remuneration, bonus, commission, leave_encashment, shareofProfirreceived, 
               consultancy_income, benefitsReceived):
    self.basic_pay = basic_pay
    self.employment_type = employment_type
    self.sector = sector
    self.children = children
    self.nppf = nppf
    self.gis = gis
    self.basic_pay_allowances = basic_pay_allowances
    self.fees_remuneration = fees_remuneration
    self.bonus = bonus
    self.commission = commission
    self.leave_encashment = leave_encashment
    self.shareofProfirreceived = shareofProfirreceived
    self.consultancy_income = consultancy_income
    self.benefitsReceived = benefitsReceived

  def calculate_taxable_income(self):
    """
    Calculates the taxable income based on the income object's attributes.

    Returns:
        A float representing the taxable income.
    """

    gross_income = (self.basic_pay + self.basic_pay_allowances + self.fees_remuneration + 
                    self.bonus + self.commission + self.leave_encashment + 
                    self.shareofProfirreceived + self.consultancy_income)

    # Handle GIS (Gross Interest Income) based on your tax regulations
    # Here, we assume GIS might be taxable income
    taxable_income = gross_income + self.gis

    # Subtract deductible contributions (e.g., NPPF)
    taxable_income -= self.nppf

    # Consider potential deduction for children (replace with actual logic)
    # Here, we assume a hypothetical deduction of $100 per child for simplicity.
    children_deduction = self.children * 100  # Hypothetical deduction (Replace with actual logic)
    taxable_income -= children_deduction

    # Handle benefitsReceived based on your tax regulations
    # Here, we assume benefits are not included in taxable income (replace with actual logic)
    # taxable_income += self.benefitsReceived  # Uncomment if benefits are taxable

    print(taxable_income)
    return taxable_income  # Return the calculated taxable income

# Example usage
my_income = Income(basic_pay=15890,
                   employment_type="Regular",
                   sector="Government",
                   children=2,
                   nppf=300,
                   gis=300,
                   basic_pay_allowances=0,
                   fees_remuneration=400,
                   bonus=500,
                   commission=500,
                   leave_encashment=0,
                   shareofProfirreceived=0,
                   consultancy_income=0,
                   benefitsReceived=0)

taxable_income = my_income.calculate_taxable_income()
print("Taxable Income:", taxable_income)
