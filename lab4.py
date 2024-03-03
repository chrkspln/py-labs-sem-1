# варіант 56
class Hotel:
    # __init__ defines default values for an object if none were initiated by user
    def __init__(self, customers=3400, name='Grand Kharkiv', rooms=134,
                 location_str='Independence Ave', location_num=2):
        self.__customers_number_in_a_year = customers
        self.__hotel_name = name
        self.__room_number = rooms
        self.street_name = location_str
        self.street_num = location_num

    def __str__(self):
        return (f'Hotel name is {self.get_name()} and '
                f'the number of rooms here is {self.get_rooms()} '
                f'for {self.get_customers()} in a year. '
                f'Hotel location is {self.street_name} {self.street_num}')

    def __repr__(self):
        return (f'Hotel(\'{self.get_name()}\', {self.get_rooms()}, '
                f'{self.get_customers()}, {self.street_name}, {self.street_num})')

    def get_customers(self):
        return self.__customers_number_in_a_year

    def get_name(self):
        return self.__hotel_name

    def get_rooms(self):
        return self.__room_number

    def display_info(self):
        print("Hotel name is: ", self.get_name(),
              ", number of customers in a year is: ", self.get_customers(),
              ", number of rooms in a hotel is: ", self.get_rooms())

    def __del__(self):
        print(f'Destructor is invoked, \'{self.get_name()}\' deleted.')


hotel_default = Hotel()
hotel_1 = Hotel(4440, 'Lviv', 89, 'Rynok Sq.', 1)
hotel_2 = Hotel(8892, 'Mriya', 69, 'Shevchenka', 34)
print(str(hotel_default))
print(repr(hotel_default))
print(str(hotel_1))
print(repr(hotel_1))
print(str(hotel_2))
print(repr(hotel_2))
