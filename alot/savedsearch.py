# Copyright (C) 2014 Anton Khirnov <anton@khirnov.net>
# This file is released under the GNU GPL, version 3 or a later revision.
# For further details see the COPYING file

class SavedSearch(object):

    name  = None
    query = None

    def __init__(self, name, query = None):
        self.name  = name
        self.query = query
