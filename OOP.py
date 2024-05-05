# 1. Basic Pay
class BasicPay:
    def __init__(self, BasicPay):
        self.BasicPay = BasicPay

    def getBasicPay(self):
        self.BasicPay = self.BasicPay* 12  # Calculate annual income here
        print("The annual basic pay I received: Nu. ", self.BasicPay )
        return self.BasicPay

BP = BasicPay(BasicPay=float(input("Enter basic pay in a month: ")))
BP.getBasicPay()

#2. Basic allowances
class allowances:
    def __init__(self, allowances):
        self.allowances = allowances

    def getallowances(self):
        self.allowances = allowances / 100 * BP.getallowances() * 12  # Calculate annual income here
        print("The aallowances pay I received: Nu. ", self.allowances )
        return self.allowances

BP = allowances(allowances=float(input("Enter basic pay in a month: ")))
BP.getallowances()