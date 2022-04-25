from flask import Blueprint, Flask, redirect, render_template, request

from models.tag import Tag
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

tags_blueprint = Blueprint("tags", __name__)

# INDEX
@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index_tags.html", tags=tags)

# NEW
@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("tags/new_tags.html")


# CREATE
@tags_blueprint.route("/tags", methods=["POST"])
def create_tag():
    name = request.form["name"]
    new_tag = Tag(name)
    tag_repository.save(new_tag)
    return redirect("/tags")


# EDIT
@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('tags/edit_tags.html', tag=tag)


# UPDATE
@tags_blueprint.route("/tags/<id>", methods=["POST"])
def update_tag(id):
    name = request.form["name"]
    tag = Tag(name, id)
    tag_repository.update(tag)
    return redirect("/tags")


# DELETE
@tags_blueprint.route("/tags/<id>/delete", methods=["POST"])
def delete_tag(id):
    tag_repository.delete(id)
    return redirect("/tags")
