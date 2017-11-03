from Room import Room
from random import choice


class LivingSpace(Room):
    __key = 'available_spaces'
    __space_key = 'space_config'
    __room = None
    __max_occupants = 0
    allocations = dict(free=[], occupied=[])

    def __init__(self):
        Room.__init__(self)
        self.__get_occupation_info()
        self.__get_allocations()

    def __get_occupation_info(self):
        self.__room = self.__class__.__name__.lower()
        try:
            self.assertTrue(self.__space_key in self.configs and self.configs.get(self.__space_key),
                            msg="Allocation information could not be retrieved!")
            self.__max_occupants = self.configs[self.__space_key].get(self.__room, {'max': 0}).get('max', 0)
            self.allocations.update({
                'max_occupants': self.__max_occupants
            })
        except Exception as e:
            print("Getting Occupation Information {}".format(e))

    def __get_allocations(self):
        try:
            self.assertTrue(self.__key in self.configs and self.configs.get(self.__key),
                            msg="No {} have been enrolled".format(self.__room))
            for room in self.configs.get(self.__key):
                room_details = self.configs.get(self.__key).get(room)
                if room_details.get('type') == self.__room:
                    status = 'free'
                    if len(room_details.get('allocated')) >= self.__max_occupants:
                        status = 'occupied'
                    self.allocations[status].append({
                        'name': room,
                        'occupants': room_details.get('allocated')
                    })

        except Exception as e:
            print("{}".format(e))

    def select_room(self, optional=False):
        if not optional:
            self.__get_allocations()
            try:
                self.assertTrue(self.allocations.get('free'), msg="All rooms are fully occupied!")
                return choice(self.allocations.get('free')).get('name')
            except Exception as e:
                print("Unable to allocate room [{}] : {}".format(self.__room, e))
