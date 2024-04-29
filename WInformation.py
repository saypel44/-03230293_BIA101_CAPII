class Information:
    def __init__(self, basic_pay, employment_type, sector, children, nppf, gis, basic_pay_allowances, fees_remuneration, bonus, commission, leave_encashment, shareofProfirreceived, consultancy_income, benefitsReceived):
        self.basic_pay = basic_pay* 12
        self.employment_type = employment_type
        self.sector = sector
        self.children = children
        self.nppf = nppf * 12/100
        self.gis = gis 
        self.basic_pay_allowances = basic_pay_allowances *15/100
        self.fees_remuneration = fees_remuneration
        self.bonus = bonus
        self.commission = commission
        self.leave_encashment = leave_encashment
        self.shareofProfirreceived = shareofProfirreceived
        self.consultancy_income = consultancy_income
        self.benefitsReceived = benefitsReceived

    def display_info(self):
        #Displays information of the employee
        print("Employee Information")
        print(f"Basic Pay: Nu.{self.basic_pay:.2f}")
        print(f"Employment Type: {self.employment_type}")
        print(f"Sector: {self.sector}")
        print(f"Number of Children: {self.children}")
        print(f"NPPF Contribution: Nu.{self.nppf:.2f}")
        print(f"GIS Contribution:  Nu.{self.gis:.2f}")
        print(f"Basic Pay Allowances: {self.basic_pay_allowances:.2%}")  # Display as percentage
        print(f"Fees Remuneration:  Nu.{self.fees_remuneration:.2f}")
        print(f"Bonus:  Nu.{self.bonus:.2f}")
        print(f"Commission:  Nu.{self.commission:.2f}")
        print(f"Leave Encashment:  Nu.{self.leave_encashment:.2f}")
        print(f"Share of Profit Received: Nu.{self.shareofProfirreceived:.2f}")
        print(f"Consultancy Income:  Nu.{self.consultancy_income:.2f}")
        print(f"Benefits Received:  Nu.{self.benefitsReceived:.2f}")

# Create an instance of the Information class
Info = Information(
    basic_pay=14675,  # Nu. (average salary can vary depending on profession and experience)
    employment_type="Permanent",  # "Regular" can also be used
    sector="Government",
    children=2,
    nppf=14675,  # Assuming 12% NPPF contribution (adjust based on actual rate)
    gis=300,  # Replace with a realistic GIS contribution (data available online)
    basic_pay_allowances=14675,  # 15% basic pay allowance (common but can vary)
    fees_remuneration=0,  # Assuming no fees received in this example
    bonus=5000,  # Nu. (bonus amounts can vary greatly)
    commission=0,  # Assuming no commission in this example
    leave_encashment=1225,  # Assuming no unused leave to encash
    shareofProfirreceived=0,  # Assuming no profit-sharing in this example
    consultancy_income=0,  # Assuming no consultancy income in this example
    benefitsReceived=3500  # Nu. House rent allowance
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

def calculate_deductions(self):
    """Calculates and returns the total annual deductions."""

    nppf = self.information.nppf  # Annual NPPF contribution
    gis = self.information.gis  # Annual GIS contribution

    # Additional deductions based on Bhutanese tax regulations (replace with actual rules)
    children_deduction = 0  # Replace with actual child deduction amount based on number of children
    medical_insurance_deduction = 0  # Replace with actual medical insurance premium paid

    total_deductions = nppf + gis + children_deduction + medical_insurance_deduction
    return total_deductions

class Income:
    def __init__(self, information):
        self.information = information

    def calculate_total_income(self):
        """Calculates and returns the total annual income."""

        # ... (same logic for calculating gross pay using GrossPay class)

        # Additional components
        bonus = self.information.bonus
        commission = self.information.commission
        leave_encashment = self.information.leave_encashment
        shareof_profit = self.information.shareofProfirreceived
        consultancy_income = self.information.consultancy_income

        # Calculate total income
        total_income_annual = (gross_pay) + bonus + commission + leave_encashment + shareof_profit + consultancy_income
        return total_income_annual

    def calculate_net_income(self):
        """Calculates and returns the net annual income (income minus deductions)."""
        total_income = self.calculate_total_income()
        deductions_obj = Deductions(self.information)  # Create Deductions object
        total_deductions = deductions_obj.calculate_deductions()
        net_income = total_income - total_deductions
        return net_income

class Deductions:
    def __init__(self, information):
        self.information = information

    def calculate_deductions(self):
        """Calculates and returns the total annual deductions."""
        return calculate_deductions(self)  # Call the dedicated function within the class

# ... (rest of the code creating Info object and possibly calculating gross pay)

income = Income(Info)
total_income = income.calculate_total_income()
net_income = income.calculate_net_income()

print(f"Total Income: Nu.{total_income:.2f}")
print(f"Net Income: Nu.{net_income:.2f}")
