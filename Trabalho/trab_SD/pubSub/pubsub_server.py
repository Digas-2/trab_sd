from concurrent import futures
import logging

import grpc
import csv
from signal import signal, SIGINT
from sys import exit
from enum import Enum

import helloworld_pb2
import helloworld_pb2_grpc

class SubscriberData:
  def __init__(self, tag,connection_status):
    self.tag = tag
    self.connection_status = False
    self.list_of_pending_messages = []
    self.list_of_old_messages = []

class TagData:
    def __init__(self,tag,timestamp,description,internal_numerator):
        self.tag = tag
        self.timestamp = timestamp
        self.description = description
        self.numeric_id = internal_numerator

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    dict_of_subs = {"":SubscriberData}
    set_of_avabilable_tags = {'trial','license','support','bug'}

    internal_numerator = 0

    def RegisterSubscriber(self,identity):
        if (identity in self.dict_of_subs.keys()):
            return False
        self.dict_of_subs[identity] = SubscriberData("null",False)
        return True

    def Authenticate (self,request,context):        
        if (self.RegisterSubscriber(request.name)):
            self.dict_of_subs[request.name].connection_status = True
            return helloworld_pb2.ServerResponse(message="code_user_01")
        else:
            return helloworld_pb2.ServerResponse(message="code_user_02")

    def checkClient(self,sub_client):
        if (sub_client in self.dict_of_subs.keys()):
            return True,sub_client
        return False,"null"


    def Subscribe(self, request,context):
        k,current_subscription = self.checkClient(request.identity.name)
        if(k):
            if(request.subscription.key == "code_42"):
                if(self.dict_of_subs[request.identity.name].tag == "null"):
                    return helloworld_pb2.Subscription(key="sub_error_001")          
                elif(self.dict_of_subs[request.identity.name].tag in self.set_of_avabilable_tags):
                    print(request.identity.name + " subscribed to the tag " + self.dict_of_subs[request.identity.name].tag)
                    return helloworld_pb2.Subscription(key=self.dict_of_subs[request.identity.name].tag)
            elif(request.subscription.key in self.set_of_avabilable_tags):
                self.dict_of_subs[request.identity.name].connection_status = True
                self.dict_of_subs[request.identity.name].tag = request.subscription.key
                print(request.identity.name + " subscribed to the tag " + self.dict_of_subs[request.identity.name].tag)
                return helloworld_pb2.Subscription(key="sub_success")
            elif(not request.subscription.key in self.set_of_avabilable_tags):
                return helloworld_pb2.Subscription(key="sub_error_002")
        else:
            return helloworld_pb2.Subscription(key="user_error_001")

    def Disconnect(self,request,context):
        self.dict_of_subs[request.name].connection_status = False
        print(request.name + " disconnected")
        return helloworld_pb2.ServerResponse(message="dc_s")

    def Unsubscribe(self,request,context):
        resp_tag = self.dict_of_subs[request.identity.name].tag
        #if(self.dict_of_subs[request.identity.name].connection_status):
        self.dict_of_subs[request.identity.name].tag = "null"
        #self.Disconnect(request.identity.name)
        print(request.identity.name + " unsubscribed from " + resp_tag)
        return helloworld_pb2.Subscription(key=resp_tag)

    def Publish(self,request,context):
        k = TagData(request.messages.tag,request.messages.timestamp,request.messages.text_description,self.internal_numerator)
        self.internal_numerator += 1
        for subs in self.dict_of_subs:
            if(not subs == ""):
                if(self.dict_of_subs[subs].tag == request.messages.tag and self.dict_of_subs[subs].connection_status == True ):
                    self.dict_of_subs[subs].list_of_pending_messages.append(k)
                elif(self.dict_of_subs[subs].connection_status == False):
                    self.dict_of_subs[subs].list_of_old_messages.append(k)
        print(request.internal_id + " " + str(self.internal_numerator))
        return helloworld_pb2.PublishResponse(message_ids="success")

    def PullOld(self,request,context):
        if(not self.dict_of_subs[request.name].list_of_old_messages):
            pass
            #print("No old messages")
        else:
            #print("old messages detected")
            if(self.dict_of_subs[request.name].list_of_old_messages):
                #print("There are old messages\n")
                for i in self.dict_of_subs[request.name].list_of_old_messages:
                    temp_message_o = i
                    #print(temp_message)
                    time_stamp = temp_message_o.timestamp
                    text_desc = temp_message_o.description
                    self.dict_of_subs[request.name].list_of_old_messages.remove(i)
                    yield helloworld_pb2.Message(tag=self.dict_of_subs[request.name].tag,timestamp=time_stamp,text_description=text_desc)
        
    def Pull(self,request,context):
        #print(request.name)
        if(not self.dict_of_subs[request.name].list_of_pending_messages):
            pass
            #print("No pending messages")
        else:
            for i in self.dict_of_subs[request.name].list_of_pending_messages:
                temp_message = i
                #print(temp_message)
                time_stamp = temp_message.timestamp
                text_desc = temp_message.description
                self.dict_of_subs[request.name].list_of_pending_messages.remove(i)
                yield helloworld_pb2.Message(tag=self.dict_of_subs[request.name].tag,timestamp=time_stamp,text_description=text_desc)




def handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    signal(SIGINT, handler)
    logging.basicConfig()
    serve()
