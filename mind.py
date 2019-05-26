#!/usr/bin/env python3

"""Represents the mental state of Eva"""

import logging
import memory
import perception
import id
import ego

class Mind:

    def __init__(self, name, id_state, ego_state):
        self.return_state = 0
        self.Name = name
        self.is_active = True
        self.entries = []
        self.responses = []
        self.id_state = id_state
        self.ego_state = ego_state
        self.default_responses = {"what's your name?" : "My name is " + self.Name,
                                "whats your name?"  : "My name is " + self.Name}

        return

    def ProcessEntry(self, entry):
        original_entry = entry
        entry = entry.lower().strip()
        response = ''

        if entry in self.default_responses.keys():
            response = self.default_responses[entry]
        elif entry == "how are you doing?":
            response = "My levels are:\nHappines=" + str(self.id_state.Happiness) + "\n" \
                        + "Angryness=" + str(self.id_state.Angryness) + "\n" \
                        + "Anxiousness=" + str(self.id_state.Anxiousness)
        elif entry == "go to sleep":
            response = "Ok. Bye."
            self.is_active = False
        else:
            response = "Sorry, but I don't understand.\n" \
                        + "[" + original_entry + "]\n" \
                        + "What do you mean?"
        
        if response != '':
            logging.debug('Creating response: ' + response)
            self.responses.append(response)

        return

    def Process(self, memory_state, perception_state):
        for entry in self.entries:
            self.ProcessEntry(entry)
            memory_state.entries.append(entry)
            logging.debug('Transfers entry from mind to memory: ' + entry)

        self.entries.clear()

        return
