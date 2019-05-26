#!/usr/bin/env python3

"""Eva"""

import os
import logging
import mind
import time
import id
import ego
import memory
import perception
import interface

TIME_CYCLE = 1

def main():

    logging.basicConfig(level=logging.DEBUG)

    eva_id = id.Id()
    eva_ego = ego.Ego()
    eva_perception = perception.Perception()
    eva_memory = memory.Memory()
    eva_interface = interface.Interface()

    eva_mind = mind.Mind('Eva', eva_id, eva_ego)

    timer_control = time.time()

    while eva_mind.is_active:

        if timer_control + TIME_CYCLE > time.time():
            continue

        eva_id.Process(eva_mind)
        eva_ego.Process(eva_mind)
        eva_perception.Process(eva_mind)
        eva_mind.Process(eva_memory, eva_perception)

        for response in eva_mind.responses:
            eva_interface.PrintResponse(response)

        eva_mind.responses.clear()

        timer_control = time.time()

    return eva_mind.return_state

if __name__ == '__main__':
    main()