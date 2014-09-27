# Copyright (C) 2014 Anton Khirnov <anton@khirnov.net>
# This file is released under the GNU GPL, version 3 or a later revision.
# For further details see the COPYING file

import urwid

from ..settings import settings


class SavedSearchWidget(urwid.WidgetWrap):

    _dbman   = None
    _ss      = None
    _attrmap = None

    def __init__(self, dbman, saved_search):
        self._dbman = dbman
        self._ss    = saved_search

        attr = settings.get_theming_attribute('savedsearches', 'normal')
        focus_attr = settings.get_theming_attribute('savedsearches', 'focus')
        self._attrmap = urwid.AttrMap(None, attr, focus_attr)
        urwid.WidgetWrap.__init__(self, self._attrmap)
        self.rebuild()

    def rebuild(self):
        count = self._dbman.count_messages(self._ss.query)
        count_unread = self._dbman.count_messages('( %s ) AND tag:unread' % self._ss.query)
        count_widget = urwid.Text('{0:>7} {1:7}'.format(count, '({0})'.format(count_unread)))

        name_widget = urwid.Text(self._ss.name)

        self._attrmap.original_widget = urwid.Columns((count_widget, name_widget), dividechars = 1)

    def selectable(self):
        return True

    def keypress(self, size, key):
        return key
