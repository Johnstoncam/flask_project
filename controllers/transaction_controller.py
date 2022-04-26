from flask import Blueprint, Flask, redirect, render_template, request

from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

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
    return render_template("transactions/new_transactions.html", merchants=merchants, tags=tags)


# CREATE
@transactions_blueprint.route("/transactions", methods=["POST"])
def create_transaction():
    merchant_id = request.form["merchant_id"]
    tag_id = request.form["tag_id"]
    value = request.form["value"]
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    new_transaction = Transaction(merchant, tag, value)
    transaction_repository.save(new_transaction)
    return redirect("/transactions")


# EDIT
@transactions_blueprint.route("/transactions/<id>/edit")
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template('transactions/edit_transactions.html', transaction=transaction, merchants=merchants, tags=tags)


# UPDATE
@transactions_blueprint.route("/transactions/<id>", methods=["POST"])
def update_transaction(id):
    merchant_id = request.form["merchant_id"]
    tag_id = request.form["tag_id"]
    value = request.form["value"]
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    print("this is the merchant")
    print(merchant.__dict__)
    print("this is the tag")
    print(tag.__dict__)
    print("this is the value")
    print(value)
    transaction = Transaction(merchant, tag, value, id)
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