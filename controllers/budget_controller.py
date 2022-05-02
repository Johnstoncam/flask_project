from flask import Blueprint, Flask, redirect, render_template, request

from models.budget import Budget
import repositories.budget_repository as budget_repository
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository


budgets_blueprint = Blueprint("budgets", __name__)

# INDEX
@budgets_blueprint.route("/budgets")
def budgets():
    budgets = budget_repository.select_all()
    return render_template("budgets/index_budgets.html", budgets=budgets)

# NEW
@budgets_blueprint.route("/budgets/new")
def new_budget():
    return render_template("budgets/new_budgets.html")


# CREATE
@budgets_blueprint.route("/budgets", methods=["POST"])
def create_budget():
    value = request.form["value"]
    name = request.form["name"]
    new_budget = Budget(value, name)
    budget_repository.save(new_budget)
    return redirect("/budgets")


# EDIT
@budgets_blueprint.route("/budgets/<id>/edit")
def edit_budget(id):
    budget = budget_repository.select(id)
    return render_template('/budgets/edit_budgets.html', budget=budget)


# UPDATE
@budgets_blueprint.route("/budgets/<id>", methods=["POST"])
def update_budget(id):
    value = request.form["value"]
    name = request.form["name"]
    budget = Budget(value, name, id)
    budget_repository.update(budget)
    return redirect("/budgets")

# SELECT AND SHOW
@budgets_blueprint.route("/budgets/<id>")
def show_budgets():
    budgets = budget_repository.select_all()
    return render_template("budgets/index_merchants.html", budgets=budgets)

# DELETE
@budgets_blueprint.route("/budgets/<id>/delete", methods=["POST"])
def delete_budget(id):
    budget_repository.delete(id)
    return redirect("/budgets")


