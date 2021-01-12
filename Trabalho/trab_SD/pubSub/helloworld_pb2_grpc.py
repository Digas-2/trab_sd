# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import helloworld_pb2 as helloworld__pb2


class GreeterStub(object):
    """The greeting service definition.
    Sends a greeting
    rpc SayHello (HelloRequest) returns (HelloReply) {}
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Pull = channel.unary_stream(
                '/helloworld.Greeter/Pull',
                request_serializer=helloworld__pb2.Identity.SerializeToString,
                response_deserializer=helloworld__pb2.Message.FromString,
                )
        self.PullOld = channel.unary_stream(
                '/helloworld.Greeter/PullOld',
                request_serializer=helloworld__pb2.Identity.SerializeToString,
                response_deserializer=helloworld__pb2.Message.FromString,
                )
        self.Publish = channel.unary_unary(
                '/helloworld.Greeter/Publish',
                request_serializer=helloworld__pb2.PublishRequest.SerializeToString,
                response_deserializer=helloworld__pb2.PublishResponse.FromString,
                )
        self.Unsubscribe = channel.unary_unary(
                '/helloworld.Greeter/Unsubscribe',
                request_serializer=helloworld__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=helloworld__pb2.Subscription.FromString,
                )
        self.Subscribe = channel.unary_unary(
                '/helloworld.Greeter/Subscribe',
                request_serializer=helloworld__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=helloworld__pb2.Subscription.FromString,
                )
        self.Authenticate = channel.unary_unary(
                '/helloworld.Greeter/Authenticate',
                request_serializer=helloworld__pb2.Identity.SerializeToString,
                response_deserializer=helloworld__pb2.ServerResponse.FromString,
                )
        self.Disconnect = channel.unary_unary(
                '/helloworld.Greeter/Disconnect',
                request_serializer=helloworld__pb2.Identity.SerializeToString,
                response_deserializer=helloworld__pb2.ServerResponse.FromString,
                )


class GreeterServicer(object):
    """The greeting service definition.
    Sends a greeting
    rpc SayHello (HelloRequest) returns (HelloReply) {}
    """

    def Pull(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PullOld(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Publish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unsubscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Authenticate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disconnect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Pull': grpc.unary_stream_rpc_method_handler(
                    servicer.Pull,
                    request_deserializer=helloworld__pb2.Identity.FromString,
                    response_serializer=helloworld__pb2.Message.SerializeToString,
            ),
            'PullOld': grpc.unary_stream_rpc_method_handler(
                    servicer.PullOld,
                    request_deserializer=helloworld__pb2.Identity.FromString,
                    response_serializer=helloworld__pb2.Message.SerializeToString,
            ),
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=helloworld__pb2.PublishRequest.FromString,
                    response_serializer=helloworld__pb2.PublishResponse.SerializeToString,
            ),
            'Unsubscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Unsubscribe,
                    request_deserializer=helloworld__pb2.SubscribeRequest.FromString,
                    response_serializer=helloworld__pb2.Subscription.SerializeToString,
            ),
            'Subscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=helloworld__pb2.SubscribeRequest.FromString,
                    response_serializer=helloworld__pb2.Subscription.SerializeToString,
            ),
            'Authenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.Authenticate,
                    request_deserializer=helloworld__pb2.Identity.FromString,
                    response_serializer=helloworld__pb2.ServerResponse.SerializeToString,
            ),
            'Disconnect': grpc.unary_unary_rpc_method_handler(
                    servicer.Disconnect,
                    request_deserializer=helloworld__pb2.Identity.FromString,
                    response_serializer=helloworld__pb2.ServerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.
    Sends a greeting
    rpc SayHello (HelloRequest) returns (HelloReply) {}
    """

    @staticmethod
    def Pull(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/helloworld.Greeter/Pull',
            helloworld__pb2.Identity.SerializeToString,
            helloworld__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PullOld(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/helloworld.Greeter/PullOld',
            helloworld__pb2.Identity.SerializeToString,
            helloworld__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/Publish',
            helloworld__pb2.PublishRequest.SerializeToString,
            helloworld__pb2.PublishResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unsubscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/Unsubscribe',
            helloworld__pb2.SubscribeRequest.SerializeToString,
            helloworld__pb2.Subscription.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/Subscribe',
            helloworld__pb2.SubscribeRequest.SerializeToString,
            helloworld__pb2.Subscription.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Authenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/Authenticate',
            helloworld__pb2.Identity.SerializeToString,
            helloworld__pb2.ServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disconnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/Disconnect',
            helloworld__pb2.Identity.SerializeToString,
            helloworld__pb2.ServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
