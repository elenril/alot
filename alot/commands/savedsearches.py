# -*- coding: utf-8 -*-

# Copyright (C) 2011-2012  Patrick Totzke <patricktotzke@gmail.com>
# This file is released under the GNU GPL, version 3 or a later revision.
# For further details see the COPYING file

import logging
import argparse

from alot.commands import Command, registerCommand
from alot.commands.globals import MoveCommand
from alot import buffers

MODE = 'savedsearches'


@registerCommand(MODE, 'open', help='open saved search')
class OpenSavedsearchCommand(Command):
    def apply(self, ui):
        buf = ui.current_buffer
        ss = buf.get_current_ss()
        query = ss.query
        logging.debug("Opening search buffer for '%s'", query)
        open_searches = ui.get_buffers_of_type(buffers.SearchBuffer)
        to_be_focused = None
        for sb in open_searches:
            if sb.querystring == query:
                to_be_focused = sb
        if to_be_focused:
            if ui.current_buffer != to_be_focused:
                ui.buffer_focus(to_be_focused)
            else:
                # refresh an already displayed search
                ui.current_buffer.rebuild()
                ui.update()
        else:
            ui.buffer_open(buffers.SearchBuffer(ui, query))

@registerCommand(MODE, 'open_unread', help='open saved search, unread only')
class OpenSavedsearchUnreadCommand(Command):
    def apply(self, ui):
        buf = ui.current_buffer
        ss = buf.get_current_ss()
        query = '( %s ) AND tag:unread' % ss.query
        logging.debug("Opening search buffer for '%s'", query)
        open_searches = ui.get_buffers_of_type(buffers.SearchBuffer)
        to_be_focused = None
        for sb in open_searches:
            if sb.querystring == query:
                to_be_focused = sb
        if to_be_focused:
            if ui.current_buffer != to_be_focused:
                ui.buffer_focus(to_be_focused)
            else:
                # refresh an already displayed search
                ui.current_buffer.rebuild()
                ui.update()
        else:
            ui.buffer_open(buffers.SearchBuffer(ui, query))


@registerCommand(MODE, 'move', help='move focus in saved searches buffer',
                 arguments=[(['movement'], {
                     'nargs': argparse.REMAINDER,
                     'help': 'last'})])
class MoveFocusCommand(MoveCommand):

    def apply(self, ui):
        logging.debug(self.movement)
        MoveCommand.apply(self, ui)
        #ui.update()
        #ui.current_buffer.refresh()
