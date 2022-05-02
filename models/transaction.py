class Transaction:

    def __init__(self, merchant, tag, value, budget, id=None):
        self.merchant = merchant
        self.tag = tag
        self.value = value
        self.budget = budget
        self.id = id