class RetailItem:

    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price

    def set_discription(self, description):
        self.__description = description

    def set_units(self, units):
        self.__units = units 

    def set_price(self, price):
        self.__price = price

    def get_description(self, description):
        return self.__description

    def get_units(self, units):
        return self.__units

    def get_price(self, price):
        return self.__price

    def __str__(self):
        return (
        'Description: '
        + str(self.__description)
        + '\n'
        + 'Units in Inventory: '
        + str(self.__units)
        +'\n'
        +'Price: $'
        + str(self.__price)
        )
