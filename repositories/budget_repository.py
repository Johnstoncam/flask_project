from db.run_sql import run_sql
from models.budget import Budget
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository 

def save(budget):
    sql = "INSERT INTO budgets (value, name) VALUES (%s, %s) RETURNING id"
    values = [budget.value, budget.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    budget.id = id

def select_all():
    budgets = []
    sql = "SELECT * FROM budgets"
    results = run_sql(sql)
    for result in results:
        budget = Budget(result["value"], result["name"], result["id"])
        budgets.append(budget)
    return budgets

def select(id):
    sql = "SELECT * FROM budgets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    budget = Budget(result["value"], result["name"], result["id"])
    return budget

def delete_all():
    sql = "DELETE FROM budgets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM budgets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(budget):
    sql = "UPDATE budgets SET value = %s, name = %s WHERE id = %s"
    values = [budget.value, budget.name, budget.id]
    run_sql(sql, values)

def get_difference(id):
    sql = "SELECT SUM(t.value)-b.value as budget_difference FROM transactions as t INNER JOIN budgets as b ON b.id = t.budget_id WHERE b.name = %s GROUP BY b.name, b.value"
    values = [id]
    run_sql(sql, values)



