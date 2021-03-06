from flask import Blueprint, Flask, redirect, render_template, request

from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository
from models.budget import Budget
import repositories.budget_repository as budget_repository

transactions_blueprint = Blueprint("transactions", __name__)

# INDEX
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()  
    transaction_total = 0
    for transaction in transactions:
        transaction_total += transaction.value
    return render_template("transactions/index_transactions.html", transactions=transactions, total=transaction_total)


# NEW
@transactions_blueprint.route("/transactions/new")
def new_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    budgets = budget_repository.select_all()
    return render_template("transactions/new_transactions.html", merchants=merchants, tags=tags, budgets=budgets)


# CREATE
@transactions_blueprint.route("/transactions", methods=["POST"])
def create_transaction():
    merchant_id = request.form["merchant_id"]
    tag_id = request.form["tag_id"]
    value = request.form["value"]
    budget = request.form["budget_id"]
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    new_transaction = Transaction(merchant, tag, value, budget)
    transaction_repository.save(new_transaction)
    
    return redirect("/transactions")


# EDIT
@transactions_blueprint.route("/transactions/<id>/edit")
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    budgets = budget_repository.select_all()
    return render_template('transactions/edit_transactions.html', transaction=transaction, merchants=merchants, tags=tags, budgets=budgets)


# UPDATE
@transactions_blueprint.route("/transactions/<id>", methods=["POST"])
def update_transaction(id):
    merchant_id = request.form["merchant_id"]
    tag_id = request.form["tag_id"]
    value = request.form["value"]
    budget_id = request.form["budget_id"]
    budget = budget_repository.select(budget_id)
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    transaction = Transaction(merchant, tag, value, budget, id)
    transaction_repository.update(transaction)
    return redirect("/transactions")

# SELECT AND SHOW
@transactions_blueprint.route("/transactions/<id>")
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template('transactions/show_transactions.html', transaction=transaction)


# DELETE
@transactions_blueprint.route("/transactions/<id>/delete", methods=["POST"])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")
