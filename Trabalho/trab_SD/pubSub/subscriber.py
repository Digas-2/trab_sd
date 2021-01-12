

from __future__ import print_function
import logging
import time
import grpc
from signal import signal, SIGINT
from datetime import timezone
import datetime

import helloworld_pb2
import helloworld_pb2_grpc


def Authenticate(stub,username):
    response = stub.Authenticate(helloworld_pb2.Identity(
            name=username))
    if (response.message == "code_user_01"):
        print("Welcome")
    else:
        print("Welcome back")


def Subscribe(stub,identity,tag):
    response = stub.Subscribe(helloworld_pb2.SubscribeRequest(
        identity=helloworld_pb2.Identity(name=identity),
        subscription=helloworld_pb2.Subscription(key=tag) ))
    if(response.key != "sub_success"):
        print("Please insert an available tag.")
    return response.key
    
    
def Unsubscribe(stub,identity):
    response = stub.Unsubscribe(helloworld_pb2.SubscribeRequest(
        identity=helloworld_pb2.Identity(name=identity),
        subscription=helloworld_pb2.Subscription(key="tag") ))
    print("Successfully unsubscribed from " + response.key)
    print("Please log in again if you wish to Subscribe to a different tag")
    exit(0)

def PullOld(stub,identity,hours,current_tag):
    responses = stub.PullOld(helloworld_pb2.Identity(name=identity))
    for response in responses:
        if(response.tag == current_tag):
            date_time_obj = datetime.datetime.strptime(response.timestamp, '%Y-%m-%d %H:%M:%S.%f')
            timestamp = date_time_obj.replace(tzinfo=timezone.utc).timestamp()
            dif = time.time() - timestamp
            if(dif < hours * 3600):
                print(response)
        #print(dif)


def Pull(stub,identity):
    while(True):
        try:
            responses = stub.Pull(helloworld_pb2.Identity(name=identity))
            for response in responses:
                print(response)
        except KeyboardInterrupt:
            print("SIGINT or CTRL-C detected. Exiting gracefully")
            stub.Disconnect(helloworld_pb2.Identity(name=identity))
            time.sleep(1)
            exit(0)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        #Authentication process
        print("---------------Please insert user name-------------------")
        user_name = input()
        Authenticate(stub,user_name)

        print("---------------Do you wish to request the available tags?(y/n)-------------------")
        retrieve_tags = input()
        if(retrieve_tags == 'y' or retrieve_tags =='Y'):
            print("trial\nlicense\nsupport\nbug\n")
           #print("available tags")
        elif (retrieve_tags == 'n' or retrieve_tags == 'N'):
           print("Ok")
        else:
           print("please insert either y/n")

        print("---------------Subscribe(1)/Unsubscribe(2)-------------------")
        sub_unsub = input()
        #print(sub_unsub)
        if(int(sub_unsub) == 1):
            print("Please write the tag you wish to subscribe to")
            rep = ""
            while(rep != "sub_success"):
                tag = str(input())
                if tag:
                    pass
                else:
                    tag = "code_42"
                rep = Subscribe(stub,user_name,tag)
                #print(rep)
                if(rep == "sub_error_001" or rep == "sub_error_002"):
                    print("Please write an available tag")
                if(tag == "code_42"):
                    tag = rep
                    rep = "sub_success"

        else:
            Unsubscribe(stub,user_name)

        
        old = input('-------------Do you wish to pull old messages? (y/n)-------------')
        if(old == 'y' or old == 'Y'):
            hours = input('Insert the hours of previous messages you wish to get: ')
            PullOld(stub,user_name,int(hours),tag)

        time.sleep(1)

        print('-------------Pulling Subscribed data------------------------')
        Pull(stub,user_name)
        

def handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

if __name__ == '__main__':
    #signal(SIGINT, handler)
    logging.basicConfig()
    run()
