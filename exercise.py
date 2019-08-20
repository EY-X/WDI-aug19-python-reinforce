class Location:
    
    def __init__(self, name):
        self.name = name

toronto = Location('Toronto')
ottawa = Location('Ottawa')
montreal = Location('Montreal')
quebec_city = Location('Quebec City')
halifax = Location('Halifax')
st_john = Location('St. John\'s')
# print(toronto.name)

class Trip:

    destinations = []
    
    @classmethod
    def add_stop(cls, location):
        cls.destinations.append(location.name)

    @classmethod
    def show_destinations(cls):
        location_stop = cls.destinations
        print('Begin Trip')
        for x in range(len(location_stop)-1):
            print(f'''
            Travelled from {location_stop[x]} to {location_stop[x+1]}.
            ''')
        print('Ended Trip')
            

trip1 = Trip()
trip1.add_stop(toronto)
trip1.add_stop(ottawa)
trip1.add_stop(montreal)
trip1.add_stop(quebec_city)
trip1.add_stop(st_john)
trip1.add_stop(halifax)



# print(trip1.destinations)
trip1.show_destinations()

# "Began trip."
# "Travelled from Toronto to Ottawa."
# "Travelled from Ottawa to Montreal."
# "Travelled from Montreal to Quebec City."
# "Travelled from Quebec City to Halifax."
# "Travelled from Halifax to St. John's."
# "Ended trip."