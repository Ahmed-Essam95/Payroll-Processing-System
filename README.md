# Payroll-Processing-System
This project is a Payroll Processing System built with Python, Pandas, and NumPy. It simulates payroll data for 1,000 employees and performs various HR &amp; Finance operations such as salary adjustments, bonuses, promotions, tax deductions, and net salary calculations.  The final results are exported to Excel for reporting and analysis.


🚀 Features

✔ Employee Data Simulation
Generates 1,000 employee records with:
Name
Department (IT, HR, Finance, Marketing, Sales, Customer Care, Fraud, Risk Management)
Age
Years of Experience (calculated from joining date)
Base Salary
Joining Date

✔ Salary & Bonus Adjustments
Salary adjusted based on years of experience:
+15% for > 10 years of experience
+7% otherwise
Department-specific bonuses:
IT → 10%
HR → 7%
Finance → 12%
Others → 5%

✔ Career Level Classification
Junior → Age < 30
Mid-level → Age 30–40
Senior → Age > 40

✔ Employee Code Generator
Code format: EMP-{DEPARTMENT}

✔ Promotion Eligibility
Every 5 years of experience → Promotion with bonus multipliers on base salary.

✔ Tax Brackets
Salary ≤ 10K → 9% tax
10K–20K → 11% tax
20K–30K → 13% tax
30K–40K → 15% tax
40K–50K → 17% tax
50K → 19% tax

✔ Deductions & Net Salary
Tax deductions (progressive brackets)
Medical insurance: 9% of adjusted salary
Final net salary after all deductions

✔ Excel Export

Raw Employee Data → Payroll Processing System.xlsx
Modified Payroll with Calculations → Modified_df Test.xlsx

🛠️ Tech Stack

Python 3.9+
Pandas (data processing)
NumPy (random data generation)

## Author ##
Ahmed EssamEldeen
