class deductions:
  def __init__(self, information):
    self.information = information

  def calculate_deductions(self, Info):
    """Calculates and returns the total annual income."""
    # Basic components
    deductions = deductions(Info)
    deductions = deductions.calculate_deductions()

    # Additional components (modify based on your needs)
    nppf = self.information.nppf # Decimal value (e.g., 0.12 for 12%)
    gis=  self.information.gis

    # Calculate total income
    total_deductions = nppf+gis
    return  total_deductions
# deductions = deductions(Info)

# Calculate and potentially display gross pay
additonDec= deductions.calculate_deductions()
print(f"Income : Nu.{additonDec:.2f}")

