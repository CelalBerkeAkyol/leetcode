
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# | salary      | int     |
# +-------------+---------+
# employee_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the employee ID, employee name, and salary.
 

# Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

# Return the result table ordered by employee_id.

import pandas as pd

# way - 1 
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees[(employees["name"].str[ :1] != 'M' ) & (employees["employee_id"] % 2 == 1)][["salary"]]
    employees["bonus"].fillna(0, inplace=True)
    return employees[ [ "employee_id" , "bonus"]].sort_values(by ="employee_id", ascending=True)

# way - 2 
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
   
    # bonus = employees[(employees['employee_id']%2 == 1) & (employees['name'][0] != 'M')]
    
    # calculate bonus 
    employees.loc[(employees['employee_id']%2 == 1) & (~employees['name'].str.startswith('M')), 'bonus']= employees['salary']


    return employees[['employee_id','bonus']].sort_values('employee_id')