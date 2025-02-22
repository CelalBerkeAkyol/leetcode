
# Table: Customers

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID and name of a customer.
 

# Table: Orders

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | customerId  | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# customerId is a foreign key (reference columns) of the ID from the Customers table.
# Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
 

# Write a solution to find all customers who never order anything.

# Return the result table in any order.
import pandas as pd
# We can solve this with a few methods. First we can concat two table in to one table. We can list all user ID and we compare CustomerID and id for find customers who never order anything
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders,  how='left', right_on='customerId', left_on='id')
    return df[df.customerId.isnull()].rename(columns = {"name": "Customers"})[["Customers"]]