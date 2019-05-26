#!/usr/bin/env python3

"""Represents the perception of outer world of the consciousness"""

import os
import mind
import logging

class Perception:

    def __init__(self):
        self.default_folder = 'entries/'
        pass

    def GetNextFile(self):
        for file in os.listdir(self.default_folder):
            f = open(os.path.join(self.default_folder, file), 'r')
            content = f.read()
            f.close()
            os.remove(os.path.join(self.default_folder, file))
            return content

        return ''

    def Process(self, mind_state):
        while True:
            last_message = self.GetNextFile()

            if last_message != '':
                logging.debug(last_message)
                mind_state.entries.append(last_message)
            else:
                return