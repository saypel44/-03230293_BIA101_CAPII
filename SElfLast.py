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
Info = Information(
    basic_pay=int(input("enter basic pay: ")), # Nu. (average salary can vary depending on profession and experience)
    employment_type="Permanent",  # "Regular" can also be used
    sector="Government",
    children=2,
    nppf=14675* 12/100,  # Assuming 12% NPPF contribution (adjust based on actual rate)
    gis=300,  # Replace with a realistic GIS contribution (data available online)
    basic_pay_allowances=(15/100)*14675,  # 15% basic pay allowance (common but can vary)
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


class Net_income: 
  def getincome(self):
    print(f"Total Annual Income: Nu.{Info.basic_pay + Info.basic_pay_allowances + Info.bonus_yearly + Info.leave_encashment + Info.benefitsReceived_monthly- Info.nppf -Info.gis :.2f}")

I=Net_income()
I.getincome()

#CReate each class and then input them and calculate
