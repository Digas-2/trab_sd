

from __future__ import print_function
import logging
from datetime import datetime
import uuid
from numpy import random
import time


import grpc
from signal import signal, SIGINT

import helloworld_pb2
import helloworld_pb2_grpc
from pois import PoisTime




def Publish(stub, interal_id, tag, text_desciption):
    response = stub.Publish(helloworld_pb2.PublishRequest(
        internal_id=interal_id,
        messages=helloworld_pb2.Message(tag=tag, timestamp=str(datetime.now()), text_description=text_desciption)))
    print(response)


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        computer_id = uuid.uuid4().hex

        print("---------------Do you wish to request the available tags?(y/n)-------------------")
        retrieve_tags = input()
        if(retrieve_tags == 'y' or retrieve_tags =='Y'):
            print("\ntrial\nlicense\nsupport\nbug\n")
           #print("available tags")
        elif (retrieve_tags == 'n' or retrieve_tags == 'N'):
           print("Ok")
        else:
           print("please insert either y/n")

        print("Choose a tag to send:")
        tag = input()

        print("Insert description of your message:")
        text_desc = input()
        Publish(stub, computer_id, tag, text_desc)


        n_events = 12
        time_interval = 60
        while(True):
            next_event = PoisTime(n_events, time_interval)
            next_event_seconds = next_event / 0.016667

            while int(next_event_seconds):
                mins, secs = divmod(next_event_seconds, 60)
                #timer = '{:02d}:{:02d}'.format(mins, secs)
                time.sleep(1)
                next_event_seconds -= 1
            Publish(stub, computer_id, tag, text_desc)


def handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)


if __name__ == '__main__':
    signal(SIGINT, handler)
    logging.basicConfig()
    run()
