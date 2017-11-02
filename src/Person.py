from Config import Configuration


class Person(Configuration):
    def __init__(self):
        Configuration.__init__(self)

    def __del__(self):
        Configuration.__del__(self)

    def add_person(self, person_name, person_type, accommodation=False):
        person_type = person_type.lower()
        person_name = person_name.lower()
        try:
            self.assertIn(person_type, list(self.configs.get('allocation_config', {}).keys()),
                          msg="Invalid person type : [{}]!".format(person_type))
            self.assertNotIn(person_name, list(self.configs.get('all_people', {}).keys()),
                             msg="Person {} already exists!")
        except Exception as e:
            print(e)
