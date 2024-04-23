class Information:
    def __init__(self, basic_pay, employment_type, sector, children, nppf, gis, basic_pay_allowances, fees_remuneration, bonus, commission, leave_encashment, shareofProfirreceived, consultancy_income, benefitsReceived):
        self.basic_pay = basic_pay
        self.employment_type = employment_type
        self.sector = sector
        self.children = children
        self.nppf = nppf
        self.gis = gis
        self.basic_pay_allowances= basic_pay_allowances
        self.fees_remuneration=fees_remuneration
        self.bonus=bonus
        self.commission=commission
        self.leave_encashment=leave_encashment
        self.shareofProfirreceived=shareofProfirreceived
        self.consultancy_income=consultancy_income
        self.benefitsReceived=benefitsReceived

Info = Information (basic_pay= 14507 ,
        employment_type = "Regular",
        sector = "Government",
        children= 0,
        nppf = 300,
        gis =300,
        basic_pay_allowances= (10//100),
        fees_remuneration=150,
        bonus=1600,
        commission=500,
        leave_encashment= 0,
        shareofProfirreceived=0,
        consultancy_income=0,
        benefitsReceived=0)

print("Information: ", Info)