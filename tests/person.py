class Person(object):
    '''
    creating class person as the superclass for the fellow and
    staff sub-classes to inehrit properties such
    as first_name, last_name and person type to inherit.
    '''

    def __init__(self, person_name, person_type, wants_accomodation='N'):
        self.person_name = person_name
        self.person_type = person_type
        """The id() function returns unique integer(identity)
         of the object person"""
        self.person_id = id(self)
        self.wants_accomodation = wants_accomodation


class Fellow(Person):
    """Creating class fellow which inherits its
    methods and properties from the superclass person"""
    def __init__(self, person_name, wants_accomodation):
        super(Fellow, self).__init__(
            person_name, person_type='Fellow',
            wants_accomodation=wants_accomodation)


class Staff(Person):
    """Creating class staff which inherits its
    methods and properties from the superclass person"""
    def __init__(self, person_name, wants_accomodation):
        super(Staff, self).__init__(
            person_name, person_type='Staff',
            wants_accomodation=wants_accomodation)
