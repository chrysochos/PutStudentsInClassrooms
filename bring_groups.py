


class BringGroups(object):
    """
    This class is used to bring groups of a certain type to a certain
    location.  It is used by the BringGroupsBehavior.
    """

    def __init__(self, group_type, location):
        """
        Constructor.

        @param group_type: The type of group to bring.
        @type  group_type: L{str}

        @param location: The location to bring the groups to.
        @type  location: L{Location}
        """

        self.group_type = group_type
        self.location = location


    def __str__(self):
        """
        @return: A string representation of this object.
        @rtype:  L{str}
        """

        return "BringGroups(%s, %s)" % (self.group_type, self.location) 
    





