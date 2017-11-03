import unittest
import os
import json


class Configuration(unittest.TestCase):
    '''
    Sets the configuration information for the room assignment
    '''

    config_file = os.path.abspath('database.db')
    configs = dict(
        space_config=dict(
            office={"max": 6, 'name': 'Office'},
            livingspace={"max": 4, 'name': 'Living Space'}
        ),
        allocation_config=dict(
            staff=['office'],
            fellow=['office', 'livingspace']
        ),
        available_spaces={})

    def __init__(self):
        self.read_config()

    def __del__(self):
        self.write_config()

    def read_config(self):
        try:
            self.assertTrue(os.path.exists(self.config_file), msg="Config file does not exist!")
            with open(self.config_file) as fh:
                self.configs = json.load(fh)
        except Exception as e:
            print("{}".format(e))

    def write_config(self):
        try:
            with open(self.config_file, 'w') as fh:
                json.dump(self.configs, fh, sort_keys=True, indent=4, ensure_ascii=False)

        except Exception as e:
            print("Error while saving configurations! : {}".format(e))
