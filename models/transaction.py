class Transaction:

    def __init__(self, merchant, tag, value, id=None):
        self.merchant = merchant
        self.tag = tag
        self.value = value
        self.id = id

        