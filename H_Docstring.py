class Account:
    """Account Blueprint"""


    def __init__(self, number, name, surname):
        self.number = number
        self.name = name
        self.surname = surname


    def set_balance(self, balance):
        """Setter method.
            Args:
                balance: Pass value of savings account balance.
            Returns:
                None
        """
        self.balance = balance
