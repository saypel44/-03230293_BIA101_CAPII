class Bonus:
    def __init__(self, bonus_percentage):
        self.bonus_percentage = bonus_percentage / 100

    def calculate_annual_bonus (self, add.getaddBPA):
        self.annual_bonus = add.getaddBPA * self.bonus_percentage * 12
        return self.annual_bonus  # Return calculated annual bonus

    def display_annual_bonus(self, add.getaddBPA):
        annual_bonus = self.calculate_annual_bonus(add.getaddBPA)
        print(f"The annual bonus I received: Nu.{annual_bonus:}")

A = Bonus(bonus_percentage=int(input("Enter bonus I received in a month: ")))
A.display_annual_bonus(add.getaddBPA)