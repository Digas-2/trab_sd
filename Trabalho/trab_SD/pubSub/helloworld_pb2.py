# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='helloworld.proto',
  package='helloworld',
  syntax='proto3',
  serialized_options=b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10helloworld.proto\x12\nhelloworld\"!\n\x0eServerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x18\n\x08Identity\x12\x0c\n\x04name\x18\x01 \x01(\t\"C\n\x07Message\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\t\x12\x18\n\x10text_description\x18\x03 \x01(\t\"L\n\x0ePublishRequest\x12\x13\n\x0binternal_id\x18\x01 \x01(\t\x12%\n\x08messages\x18\x02 \x01(\x0b\x32\x13.helloworld.Message\"&\n\x0fPublishResponse\x12\x13\n\x0bmessage_ids\x18\x01 \x01(\t\"j\n\x10SubscribeRequest\x12&\n\x08identity\x18\x01 \x01(\x0b\x32\x14.helloworld.Identity\x12.\n\x0csubscription\x18\x02 \x01(\x0b\x32\x18.helloworld.Subscription\"\x1b\n\x0cSubscription\x12\x0b\n\x03key\x18\x01 \x01(\t2\xd6\x03\n\x07Greeter\x12\x35\n\x04Pull\x12\x14.helloworld.Identity\x1a\x13.helloworld.Message\"\x00\x30\x01\x12\x38\n\x07PullOld\x12\x14.helloworld.Identity\x1a\x13.helloworld.Message\"\x00\x30\x01\x12\x44\n\x07Publish\x12\x1a.helloworld.PublishRequest\x1a\x1b.helloworld.PublishResponse\"\x00\x12G\n\x0bUnsubscribe\x12\x1c.helloworld.SubscribeRequest\x1a\x18.helloworld.Subscription\"\x00\x12\x45\n\tSubscribe\x12\x1c.helloworld.SubscribeRequest\x1a\x18.helloworld.Subscription\"\x00\x12\x42\n\x0c\x41uthenticate\x12\x14.helloworld.Identity\x1a\x1a.helloworld.ServerResponse\"\x00\x12@\n\nDisconnect\x12\x14.helloworld.Identity\x1a\x1a.helloworld.ServerResponse\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3'
)




_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='helloworld.ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='helloworld.ServerResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=65,
)


_IDENTITY = _descriptor.Descriptor(
  name='Identity',
  full_name='helloworld.Identity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='helloworld.Identity.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=91,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='helloworld.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='helloworld.Message.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='helloworld.Message.timestamp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text_description', full_name='helloworld.Message.text_description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=160,
)


_PUBLISHREQUEST = _descriptor.Descriptor(
  name='PublishRequest',
  full_name='helloworld.PublishRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='internal_id', full_name='helloworld.PublishRequest.internal_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='messages', full_name='helloworld.PublishRequest.messages', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=238,
)


_PUBLISHRESPONSE = _descriptor.Descriptor(
  name='PublishResponse',
  full_name='helloworld.PublishResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_ids', full_name='helloworld.PublishResponse.message_ids', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=278,
)


_SUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='helloworld.SubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity', full_name='helloworld.SubscribeRequest.identity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subscription', full_name='helloworld.SubscribeRequest.subscription', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=386,
)


_SUBSCRIPTION = _descriptor.Descriptor(
  name='Subscription',
  full_name='helloworld.Subscription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='helloworld.Subscription.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=388,
  serialized_end=415,
)

_PUBLISHREQUEST.fields_by_name['messages'].message_type = _MESSAGE
_SUBSCRIBEREQUEST.fields_by_name['identity'].message_type = _IDENTITY
_SUBSCRIBEREQUEST.fields_by_name['subscription'].message_type = _SUBSCRIPTION
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE
DESCRIPTOR.message_types_by_name['Identity'] = _IDENTITY
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['PublishRequest'] = _PUBLISHREQUEST
DESCRIPTOR.message_types_by_name['PublishResponse'] = _PUBLISHRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['Subscription'] = _SUBSCRIPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERRESPONSE,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.ServerResponse)
  })
_sym_db.RegisterMessage(ServerResponse)

Identity = _reflection.GeneratedProtocolMessageType('Identity', (_message.Message,), {
  'DESCRIPTOR' : _IDENTITY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Identity)
  })
_sym_db.RegisterMessage(Identity)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Message)
  })
_sym_db.RegisterMessage(Message)

PublishRequest = _reflection.GeneratedProtocolMessageType('PublishRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.PublishRequest)
  })
_sym_db.RegisterMessage(PublishRequest)

PublishResponse = _reflection.GeneratedProtocolMessageType('PublishResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHRESPONSE,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.PublishResponse)
  })
_sym_db.RegisterMessage(PublishResponse)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.SubscribeRequest)
  })
_sym_db.RegisterMessage(SubscribeRequest)

Subscription = _reflection.GeneratedProtocolMessageType('Subscription', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTION,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Subscription)
  })
_sym_db.RegisterMessage(Subscription)


DESCRIPTOR._options = None

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='helloworld.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=418,
  serialized_end=888,
  methods=[
  _descriptor.MethodDescriptor(
    name='Pull',
    full_name='helloworld.Greeter.Pull',
    index=0,
    containing_service=None,
    input_type=_IDENTITY,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PullOld',
    full_name='helloworld.Greeter.PullOld',
    index=1,
    containing_service=None,
    input_type=_IDENTITY,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Publish',
    full_name='helloworld.Greeter.Publish',
    index=2,
    containing_service=None,
    input_type=_PUBLISHREQUEST,
    output_type=_PUBLISHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Unsubscribe',
    full_name='helloworld.Greeter.Unsubscribe',
    index=3,
    containing_service=None,
    input_type=_SUBSCRIBEREQUEST,
    output_type=_SUBSCRIPTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='helloworld.Greeter.Subscribe',
    index=4,
    containing_service=None,
    input_type=_SUBSCRIBEREQUEST,
    output_type=_SUBSCRIPTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Authenticate',
    full_name='helloworld.Greeter.Authenticate',
    index=5,
    containing_service=None,
    input_type=_IDENTITY,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Disconnect',
    full_name='helloworld.Greeter.Disconnect',
    index=6,
    containing_service=None,
    input_type=_IDENTITY,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
