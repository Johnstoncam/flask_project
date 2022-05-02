from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository
from models.tag import Tag
import repositories.tag_repository as tag_repository
from models.budget import Budget
import repositories.budget_repository as budget_repository

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, tag_id, value, budget_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.merchant.id, transaction.tag.id, transaction.value, transaction.budget]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id


def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for result in results:
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        budget = budget_repository.select(result["budget_id"])
        transaction = Transaction(merchant, tag, result["value"], budget, result["id"])
        transactions.append(transaction)
    return transactions


def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    merchant = merchant_repository.select(result["merchant_id"])
    tag = tag_repository.select(result["tag_id"])
    budget = budget_repository.select(result["budget_id"])
    transaction = Transaction(merchant, tag, result["value"], budget, result["id"])
    return transaction


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(transaction):
    sql = "UPDATE transactions SET (merchant_id, tag_id, value, budget_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [transaction.merchant.id, transaction.tag.id, transaction.value, transaction.budget.id, transaction.id]
    run_sql(sql, values)
    return transaction

def select_transaction(id):
    transactions = []
    sql = "SELECT merchants.* FROM merchants INNER JOIN transactions ON transactions.merchant_id = merchant.id WHERE transactions.tag_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        merchant = Merchant(result["name"])
        transactions.append(merchant)
    return transactions