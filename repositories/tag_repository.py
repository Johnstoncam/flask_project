from db.run_sql import run_sql
from models.merchant import Merchant
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name) VALUES (%s) RETURNING id"
    values = [tag.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id


def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for result in results:
        tag = Tag(result["name"], result["id"])
        tags.append(tag)
    return tags


def select(id):
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    tag = Tag(result["name"], result["id"])
    return tag


def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(tag):
    sql = "UPDATE tags SET (name) = (%s) WHERE id = %s"
    values = [tag.name, tag.id]
    run_sql(sql, values)


