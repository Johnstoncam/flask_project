from flask import Blueprint, Flask, redirect, render_template, request

from models.tag import Tag
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

tags_blueprint = Blueprint("categories", __name__)

# INDEX
@tags_blueprint.route("/merchants")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index_tags.html", tags=tags)

