from db.run_sql import run_sql
from models.budget import Budget
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository 

def save(input_value):
    sql = "INSERT INTO budgets (value) VALUES (%s) RETURNING id"
    values = [input_value.value]
    results = run_sql(sql, values)
    id = results[0]['id']
    input_value.id = id

def select_all():
    budgets = []
    sql = "SELECT * FROM budgets"
    results = run_sql(sql)
    for result in results:
        budget = Budget(result["value"], result["id"])
        budgets.append(budget)
    return budgets

def select(id):
    sql = "SELECT * FROM budgets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    budget = Budget(result["value"], result["id"])
    return budget

def delete_all():
    sql = "DELETE FROM budgets"
    run_sql(sql)

def update(budget):
    sql = "UPDATE budgets SET value = %s WHERE id = %s"
    values = [budget.value, budget.id]
    run_sql(sql, values)

