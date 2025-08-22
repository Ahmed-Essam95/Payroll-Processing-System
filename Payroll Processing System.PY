import pandas as pd
import numpy as np


# Generate 1000 unique employee names
employee_names = [f"Employee_{i+1}" for i in range(1, 1000)]

# Use departments in a round-robin way
departments = ["IT", "HR", "Finance", "Marketing", "Sales", "Customer Care", "Fraud", "Risk Management"]
employee_departments = [departments[i % len(departments)] for i in range(1, 1000)]

# Random-like ages between 22 and 60 (cyclic for demo purposes)
employee_ages = [22 + (i % 29) for i in range(1, 1000)]

# Years of experience (0 to 15)
employee_experience = [i % 15 for i in range(1,1000)]

# Base salary (cyclic pattern, could be random in real scenario)
base_salaries = [4000 + (i % 21) * 2000 for i in range(1, 1000)]


def generate_date():
    """Generate 1000 Random Joining Date"""

    year = str( np.random.randint(2007,2025+1) )
    month = str( np.random.randint(1,7+1) ).zfill(2)
    day = str( np.random.randint(1,28+1) ).zfill(2)

    return "-".join([year,month,day])

dates_list = [ generate_date() for one_date in range(1,1000)  ]


# Create DataFrame
df_employees = pd.DataFrame({
    "Name": employee_names,
    "Department": employee_departments,
    "Age": employee_ages,
    "Years_Experience": employee_experience,
    "Base_Salary": base_salaries ,
    "Joining_date": pd.to_datetime(dates_list) 
})

Sheet_path = r"path\Payroll Processing System.xlsx"
df_employees.to_excel(Sheet_path , index=False)

# ------------------------------------------------------------------------------------------------------------------------------------
Modified_df = df_employees.copy()



def subs(row):
    """Return the years of experience"""

    today = pd.to_datetime( pd.Timestamp.today() )

    all_years = str(   ( today - row["Joining_date"] )   // 365  )

    string_year = "".strip()

    for digit in all_years :
        if digit.lower() != "d" :
            string_year += digit 
        else:
            break

    return string_year 



# Task ( 7 )
# Overriding on Years Experience column to be calculated based on joining date
Modified_df["Years_Experience"] = Modified_df.apply( subs , axis=1 ).astype(int)


# Task ( 8 ) Alternative  Solution
# today = pd.to_datetime( pd.Timestamp.today() )
# Modified_df["Years_Experience"] = ( (today - Modified_df["Joining_date"]).dt.days // 365 ).astype(int)




# Task ( 2 )
def Department_Bonus(row_1) :
    """Calculate Bonus Before Salary Adjustment as the bonus is before salary increase"""

    if row_1["Department"] == "IT" :
        return row_1["Base_Salary"] * 0.10
    
    elif row_1["Department"] == "HR" :
        return row_1["Base_Salary"] * 0.07
    
    elif row_1["Department"] == "Finance" :
        return row_1["Base_Salary"] * 0.12
    
    else:
        return row_1["Base_Salary"] * 0.05


# Task ( 2 )
Modified_df["Department_Bonus"] = Modified_df.apply( Department_Bonus  , axis=1)


# Task ( 1 )
Modified_df["Adjusted_Salary"] = Modified_df.apply( lambda each_row : each_row["Base_Salary"] * 1.15 if each_row["Years_Experience"]  > 10  
                                                   else each_row["Base_Salary"] * 1.07 , axis=1 )


# Task ( 3 )
Modified_df["Career_Level"] = Modified_df["Age"].map( lambda age : "Junior" if age < 30 else ( "Mid-level"  if age >= 30 and age <= 40   else "Senior")  )


# Task ( 4 )
Modified_df["Employee_Code"] = Modified_df.apply( lambda by_row : f"{by_row["Name"][:3].upper()}-{by_row["Department"].upper()}"    ,  axis=1  )


# Task ( 5 )
Modified_df["Net Salary After Bonus"] = Modified_df.apply( lambda twice :  twice["Adjusted_Salary"] + twice["Department_Bonus"] , axis=1 )


# Task ( 6 )
Modified_df["Summary"] = Modified_df.apply( 
    lambda summarized_line : f"{summarized_line["Name"].capitalize()}  " 
                             f"({summarized_line["Department"].upper()}) "
                             f" earns $ {int(summarized_line["Adjusted_Salary"]+summarized_line["Department_Bonus"])}"
                             f"  After Bonus" , axis=1
      )



def Promotion(row) : 
    if row["Years_Experience"] < 5 : 
        return f"Not Eligible, Less than 5 years, next Promotion year after = { 5- row["Years_Experience"]}" 
    
    elif row["Years_Experience"] == 5 : 
        return f"Employee Eligibe for the fifth year cycle promotion, amount : {row["Base_Salary"] * 2}" 
    
    elif row["Years_Experience"] == 10 : 
        return f"Employee Eligibe for the fifth year cycle promotion, amount : {row["Base_Salary"] * 3}" 
    
    elif row["Years_Experience"] == 15 : 
        return f"Employee Eligibe for the fifth year cycle promotion, amount : {row["Base_Salary"] * 4}" 
    
    elif row["Years_Experience"] == 20 : 
        return f"Employee Eligibe for the fifth year cycle promotion, amount : {row["Base_Salary"] * 5}" 

    else : 
        return f"Not Eligible this year, fifth year cycle promotion after = { 5 - (row["Years_Experience"] % 5 )}"



# Task ( 8 )
# Next Promotion Date (Every 5 Years)
Modified_df["promotion"] = Modified_df.apply(  Promotion     , axis=1)



def Tax_brackets(row) :
    """Calc Tax % based on Salary Category"""

    if row["Adjusted_Salary"] <= 10000 :
        return row["Adjusted_Salary"] * 0.09
    
    elif row["Adjusted_Salary"] > 10000  and row["Adjusted_Salary"] <= 20000 :
        return row["Adjusted_Salary"] * 0.11

    elif row["Adjusted_Salary"] > 20000  and row["Adjusted_Salary"] <= 30000 :
        return row["Adjusted_Salary"] * 0.13

    elif row["Adjusted_Salary"] > 30000  and row["Adjusted_Salary"] <= 40000 :
        return row["Adjusted_Salary"] * 0.15

    elif row["Adjusted_Salary"] > 40000  and row["Adjusted_Salary"] <= 50000 :
        return row["Adjusted_Salary"] * 0.17

    else:
        return row["Adjusted_Salary"] * 0.19


# Tax Amount
Modified_df["Deducted Taxes"] = Modified_df.apply( Tax_brackets ,   axis=1)


# Medical Insurance
Modified_df["medical_insurance"] = Modified_df["Adjusted_Salary"] * 0.09


# Net Salary after deduct Taxes and insurance
Modified_df["Net Salary"] = (  

    Modified_df["Adjusted_Salary"]
      - ( Modified_df["Adjusted_Salary"] * 0.13)
        - Modified_df["Deducted Taxes"]  )



Sheet_path_2 = r"path\Modified_sheet.xlsx"
Modified_df.to_excel(Sheet_path_2 , index=False)

