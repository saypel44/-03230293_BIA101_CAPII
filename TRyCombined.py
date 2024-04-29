class Information:
    def __init__(self,basic_pay, employment_type, sector, children, nppf, gis, basic_pay_allowances, fees_remuneration, bonus, commission, leave_encashment, shareofProfirreceived, consultancy_income, benefitsReceived):
        self.basic_pay = basic_pay *12  # Nu.
        self.employment_type = employment_type
        self.sector = sector
        self.children = children
        self.nppf= nppf *12 # Decimal value (e.g., 0.12 for 12%)
        self.gis = gis *12  # Nu.
        self.basic_pay_allowances = basic_pay_allowances *12 # Decimal value (e.g., 0.15 for 15%)
        self.fees_remuneration = fees_remuneration *12  # Nu.
        self.bonus_yearly = bonus # Nu.
        self.commission = commission  # Nu.
        self.leave_encashment= leave_encashment  # Nu.
        self.shareofProfirreceived_yearly = shareofProfirreceived # Nu.
        self.consultancy_income_yearly = consultancy_income  # Nu.
        self.benefitsReceived_monthly = benefitsReceived*12  # Nu.


    def display_info(self):
        """Displays all information about the Information class in a user-friendly format, including annual income."""

        print("Employee Information")
        print(f"Basic Pay: Nu.{self.basic_pay:.2f}")
        print(f"Employment Type: {self.employment_type}")
        print(f"Sector: {self.sector}")
        print(f"Number of Children: {self.children}")
        print(f"NPPF Amount: {self.nppf:.2f}")
        print(f"GIS Contribution : Nu.{self.gis:.2f}")
        print(f"Basic Pay Allowances: {self.basic_pay_allowances:.2f}")
        print(f"Fees Remuneration : Nu.{self.fees_remuneration:.2f}")
        print(f"Bonus: Nu.{self.bonus_yearly:.2f}")
        print(f"Commission: Nu.{self.commission:.2f}")
        print(f"Leave Encashment: Nu.{self.leave_encashment:.2f}")
        print(f"Share of Profit Received: Nu.{self.shareofProfirreceived_yearly:.2f}")
        print(f"Consultancy Income: Nu.{self.consultancy_income_yearly:.2f}")
        print(f"Benefits Received: Nu.{self.benefitsReceived_monthly:.2f}")
        

# Create an instance of the Information class with assumed Bhutanese values
Info = Information (
    basic_pay=14675,  # Nu. (average salary can vary depending on profession and experience)
    employment_type="Permanent",  # "Regular" can also be used
    sector="Government",
    children=2,
    nppf=14675* 12/100,  # Assuming 12% NPPF contribution (adjust based on actual rate)
    gis=300,  # Replace with a realistic GIS contribution (data available onlinebasic_pay_allowances=(15/100)*14675,  # 15% basic pay allowance (common but can vary)
    basic_pay_allowances=(15/100)*14675,
    fees_remuneration=0,  # Assuming no fees received in this example
    bonus=5000,  # Nu. (bonus amounts can vary greatly)
    commission=0,  # Assuming no commission in this example
    leave_encashment=1225,  # Assuming no unused leave to encash
    shareofProfirreceived=0,  # Assuming no profit-sharing in this example
    consultancy_income=0,  # Assuming no consultancy income in this example
    benefitsReceived=3500    
)
# Call the display_info method to print the information
Info.display_info()


class GrossPay:
  def __init__(self, information):
    self.information = information

  def calculate_gross_pay(self):
    """Calculates and returns the gross pay (monthly)."""
    gross_pay = (
        self.information.basic_pay +
        self.information.basic_pay_allowances +
        self.information.fees_remuneration
    )
    return gross_pay

# Create a GrossPay object using the Information object
gross_pay = GrossPay(Info)

# Calculate and potentially display gross pay
gross_pay = gross_pay.calculate_gross_pay()
print(f"Gross Pay: Nu.{gross_pay:.2f}")


class Income:
  def __init__(self, information):
    self.information = information

  def calculate_total_income(self):
    """Calculates and returns the total annual income."""
    # Basic components
    gross_pay = GrossPay(Info)
    gross_pay = gross_pay.calculate_gross_pay()

    # Additional components (modify based on your needs)
    bonus = self.information.bonus_yearly
    commission = self.information.commission
    leave_encashment = self.information.leave_encashment
    shareof_profit = self.information.shareofProfirreceived_yearly
    consultancy_income = self.information.consultancy_income_yearly

    # Calculate total income
    total_income_annual = (gross_pay) + bonus + commission + leave_encashment + shareof_profit + consultancy_income
    return total_income_annual
Income = Income(Info)

# Calculate and potentially display gross pay
IncomeEarned= Income.calculate_total_income()
print(f"Income : Nu.{IncomeEarned:.2f}")


# class deductions:
#   def __init__(self, information):
#     self.information = information

#   def calculate_deductions(self):
#     """Calculates and returns the total annual income."""
#     # Basic components
#     deductions = deductions(Info)
#     deductions = deductions.calculate_deductions()

#     # Additional components (modify based on your needs)
#     nppf = self.information.nppf # Decimal value (e.g., 0.12 for 12%)
#     gis=  self.information.gis

#     # Calculate total income
#     total_deductions = nppf+gis
#     return  total_deductions
#     total_deductions = deductions.calculate_deductions()
#     print("Total deductions:", total_deductions)


# # deductions = deductions(Info)

# # Calculate and potentially display gross pay
# # Dec= deductions.calculate_deductions()
# # print(f"Income : Nu.{Dec:.2f}")