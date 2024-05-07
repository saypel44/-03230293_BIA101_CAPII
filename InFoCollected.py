class InFoCollected:
    def __init__(self, basic_pay, employment_type, sector, children, nppf, gis, basic_pay_allowances, fees_remuneration, bonus, commission, leave_encashment, shareofProfirreceived, consultancy_income, benefitsReceived):
        self.basic_pay = basic_pay * 12
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
Info = InFoCollected(
    basic_pay=int(input("BP: ")),  # Nu. (average salary can vary depending on profession and experience)
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