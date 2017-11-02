from Config import Configuration


class Room(Configuration):
    def __init__(self):
        Configuration.__init__(self)

    def __del__(self):
        Configuration.__del__(self)

    def create_room(self, room_type, room_name):
        try:
            room_name = room_name.lower()
            room_type = room_type.lower()
            article = 'A'
            self.assertIn(room_type, list(self.configs['space_config'].keys()),
                          msg="Invalid Room Type : {}".format(room_type))
            self.assertNotIn(room_name, list(self.configs['available_spaces'].keys()),
                             msg="{} {} {} already exists!".format(article, room_type, room_name))

            self.configs.get('available_spaces', {}).setdefault(room_name, {
                'type': room_type,
                'allocated': []
            })
            if room_type[0] in ['a', 'e', 'i', 'o', 'u']:
                article = 'An'
            print("{} {} called {} has been successfully created!".format(article, room_type, room_name))
        except Exception as e:
            print("{}".format(e))
