class Information:
    def __init__(self,basic_pay_monthly, employment_type, sector, children, nppf, gis_monthly, basic_pay_allowances, fees_remuneration_monthly, bonus_yearly, commission_yearly, leave_encashment_yearly, shareofProfirreceived_yearly, consultancy_income_yearly, benefitsReceived_monthly):
        self.basic_pay_monthly = basic_pay_monthly *12  # Nu.
        self.employment_type = employment_type
        self.sector = sector
        self.children = children
        self.nppf= nppf *12 # Decimal value (e.g., 0.12 for 12%)
        self.gis_monthly = gis_monthly *12  # Nu.
        self.basic_pay_allowances = basic_pay_allowances *12 # Decimal value (e.g., 0.15 for 15%)
        self.fees_remuneration_monthly = fees_remuneration_monthly *12  # Nu.
        self.bonus_yearly = bonus_yearly  # Nu.
        self.commission_yearly = commission_yearly  # Nu.
        self.leave_encashment_yearly = leave_encashment_yearly  # Nu.
        self.shareofProfirreceived_yearly = shareofProfirreceived_yearly  # Nu.
        self.consultancy_income_yearly = consultancy_income_yearly  # Nu.
        self.benefitsReceived_monthly = benefitsReceived_monthly *12  # Nu.


    def display_info(self):
        """Displays all information about the Information class in a user-friendly format, including annual income."""

        print("Employee Information")
        print(f"Basic Pay (Monthly): Nu.{self.basic_pay_monthly:.2f}")
        print(f"Employment Type: {self.employment_type}")
        print(f"Sector: {self.sector}")
        print(f"Number of Children: {self.children}")
        print(f"NPPF Rate: {self.nppf:.0f}")
        print(f"GIS Contribution (Monthly): Nu.{self.gis_monthly:.2f}")
        print(f"Basic Pay Allowances: {self.basic_pay_allowances:.2f}")
        print(f"Fees Remuneration (Monthly): Nu.{self.fees_remuneration_monthly:.2f}")
        print(f"Bonus (Yearly): Nu.{self.bonus_yearly:.2f}")
        print(f"Commission (Yearly): Nu.{self.commission_yearly:.2f}")
        print(f"Leave Encashment (Yearly): Nu.{self.leave_encashment_yearly:.2f}")
        print(f"Share of Profit Received (Yearly): Nu.{self.shareofProfirreceived_yearly:.2f}")
        print(f"Consultancy Income (Yearly): Nu.{self.consultancy_income_yearly:.2f}")
        print(f"Benefits Received (Monthly): Nu.{self.benefitsReceived_monthly:.2f}")
        

# Create an instance of the Information class with assumed Bhutanese values
Info = Information(
    basic_pay_monthly=14675,  # Nu. (average salary can vary depending on profession and experience)
    employment_type="Permanent",  # "Regular" can also be used
    sector="Government",
    children=2,
    nppf=14675* 12/100,  # Assuming 12% NPPF contribution (adjust based on actual rate)
    gis_monthly=300,  # Replace with a realistic GIS contribution (data available online)
    basic_pay_allowances=(15/100)*14675,  # 15% basic pay allowance (common but can vary)
    fees_remuneration_monthly=0,  # Assuming no fees received in this example
    bonus_yearly=5000,  # Nu. (bonus amounts can vary greatly)
    commission_yearly=0,  # Assuming no commission in this example
    leave_encashment_yearly=1225,  # Assuming no unused leave to encash
    shareofProfirreceived_yearly=0,  # Assuming no profit-sharing in this example
    consultancy_income_yearly=0,  # Assuming no consultancy income in this example
    benefitsReceived_monthly=3500  # Nu. House rent allowance
)
# Call the display_info method to print the information
Info.display_info()

