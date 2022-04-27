from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository


merchant_repository.delete_all()
tag_repository.delete_all()
transaction_repository.delete_all()


merchant_1 = Merchant("Halfords")
merchant_repository.save(merchant_1)

merchant_2 = Merchant("Aldi")
merchant_repository.save(merchant_2)

merchant_3 = Merchant("Scotrail")
merchant_repository.save(merchant_3)

tag_1 = Tag("Maintenance")
tag_repository.save(tag_1)

tag_2 = Tag("Groceries")
tag_repository.save(tag_2)

tag_3 = Tag("Transport")
tag_repository.save(tag_3)
