yearly_salary = float(input())

if yearly_salary <= 55867:
    federal_tax_bracket = 1
elif 55867 < yearly_salary <= 111733:
    federal_tax_bracket = 2
elif 111733 < yearly_salary <= 173205:
    federal_tax_bracket = 3
elif 173205 < yearly_salary <= 246752:
    federal_tax_bracket = 4
elif yearly_salary > 246752:
    federal_tax_bracket = 5

print(federal_tax_bracket)
