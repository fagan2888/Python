# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: devices/v1beta1/DevicesService_Beta1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from services import ServiceStatus_pb2 as services_dot_ServiceStatus__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='devices/v1beta1/DevicesService_Beta1.proto',
  package='bloombox.schema.services.devices.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n*devices/v1beta1/DevicesService_Beta1.proto\x12(bloombox.schema.services.devices.v1beta1\x1a\x1cservices/ServiceStatus.proto\x1a\x1cgoogle/api/annotations.proto\"y\n\x10\x44\x65viceAssignment\x12\x0f\n\x07partner\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x42\n\x04role\x18\x03 \x01(\x0e\x32\x34.bloombox.schema.services.devices.v1beta1.DeviceRole\"\x82\x01\n\x10\x44\x65viceActivation\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12N\n\nassignment\x18\x03 \x01(\x0b\x32:.bloombox.schema.services.devices.v1beta1.DeviceAssignment\"\xf8\x01\n\x04Ping\x1a\t\n\x07Request\x1a\x43\n\x08Response\x12\x37\n\x06status\x18\x01 \x01(\x0e\x32\'.bloombox.schema.services.ServiceStatus\x1a\x9f\x01\n\tOperation\x12G\n\x07request\x18\x01 \x01(\x0b\x32\x36.bloombox.schema.services.devices.v1beta1.Ping.Request\x12I\n\x08response\x18\x02 \x01(\x0b\x32\x37.bloombox.schema.services.devices.v1beta1.Ping.Response\"\x9b\x03\n\nActivation\x1a.\n\x07Request\x12\x0e\n\x06serial\x18\x01 \x01(\t\x12\x13\n\x0b\x66ingerprint\x18\x02 \x01(\t\x1a\xae\x01\n\x08Response\x12\x0e\n\x06\x61\x63tive\x18\x01 \x01(\x08\x12\x44\n\x05\x65rror\x18\x02 \x01(\x0e\x32\x35.bloombox.schema.services.devices.v1beta1.DeviceError\x12L\n\x08manifest\x18\x03 \x01(\x0b\x32:.bloombox.schema.services.devices.v1beta1.DeviceActivation\x1a\xab\x01\n\tOperation\x12M\n\x07request\x18\x01 \x01(\x0b\x32<.bloombox.schema.services.devices.v1beta1.Activation.Request\x12O\n\x08response\x18\x02 \x01(\x0b\x32=.bloombox.schema.services.devices.v1beta1.Activation.Response*p\n\x0b\x44\x65viceError\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x12\n\x0eINVALID_SERIAL\x10\x01\x12\x14\n\x10\x44\x45VICE_NOT_FOUND\x10\x02\x12\x12\n\x0eINTERNAL_ERROR\x10\x03\x12\x15\n\x11\x44\x45VICE_UNASSIGNED\x10\x04*H\n\nDeviceRole\x12\x0e\n\nUNASSIGNED\x10\x00\x12\x08\n\x04MENU\x10\x01\x12\x0b\n\x07\x43HECKIN\x10\x02\x12\n\n\x06\x42\x45\x41\x43ON\x10\x03\x12\x07\n\x03POS\x10\x04\x32\xdf\x02\n\x07\x44\x65vices\x12\x96\x01\n\x04Ping\x12\x36.bloombox.schema.services.devices.v1beta1.Ping.Request\x1a\x37.bloombox.schema.services.devices.v1beta1.Ping.Response\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/devices/v1beta1/ping\x12\xba\x01\n\x08\x41\x63tivate\x12<.bloombox.schema.services.devices.v1beta1.Activation.Request\x1a=.bloombox.schema.services.devices.v1beta1.Activation.Response\"1\x82\xd3\xe4\x93\x02+\x12)/devices/v1beta1/{serial}/device:activateB7\n+io.bloombox.schema.services.devices.v1beta1H\x01P\x01\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[services_dot_ServiceStatus__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_DEVICEERROR = _descriptor.EnumDescriptor(
  name='DeviceError',
  full_name='bloombox.schema.services.devices.v1beta1.DeviceError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_ERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SERIAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_NOT_FOUND', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_UNASSIGNED', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1069,
  serialized_end=1181,
)
_sym_db.RegisterEnumDescriptor(_DEVICEERROR)

DeviceError = enum_type_wrapper.EnumTypeWrapper(_DEVICEERROR)
_DEVICEROLE = _descriptor.EnumDescriptor(
  name='DeviceRole',
  full_name='bloombox.schema.services.devices.v1beta1.DeviceRole',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNASSIGNED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MENU', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECKIN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEACON', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POS', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1183,
  serialized_end=1255,
)
_sym_db.RegisterEnumDescriptor(_DEVICEROLE)

DeviceRole = enum_type_wrapper.EnumTypeWrapper(_DEVICEROLE)
NO_ERROR = 0
INVALID_SERIAL = 1
DEVICE_NOT_FOUND = 2
INTERNAL_ERROR = 3
DEVICE_UNASSIGNED = 4
UNASSIGNED = 0
MENU = 1
CHECKIN = 2
BEACON = 3
POS = 4



_DEVICEASSIGNMENT = _descriptor.Descriptor(
  name='DeviceAssignment',
  full_name='bloombox.schema.services.devices.v1beta1.DeviceAssignment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partner', full_name='bloombox.schema.services.devices.v1beta1.DeviceAssignment.partner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='bloombox.schema.services.devices.v1beta1.DeviceAssignment.location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='bloombox.schema.services.devices.v1beta1.DeviceAssignment.role', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=269,
)


_DEVICEACTIVATION = _descriptor.Descriptor(
  name='DeviceActivation',
  full_name='bloombox.schema.services.devices.v1beta1.DeviceActivation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='bloombox.schema.services.devices.v1beta1.DeviceActivation.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='bloombox.schema.services.devices.v1beta1.DeviceActivation.hostname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assignment', full_name='bloombox.schema.services.devices.v1beta1.DeviceActivation.assignment', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=402,
)


_PING_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bloombox.schema.services.devices.v1beta1.Ping.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=422,
)

_PING_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='bloombox.schema.services.devices.v1beta1.Ping.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bloombox.schema.services.devices.v1beta1.Ping.Response.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=424,
  serialized_end=491,
)

_PING_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='bloombox.schema.services.devices.v1beta1.Ping.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='bloombox.schema.services.devices.v1beta1.Ping.Operation.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='bloombox.schema.services.devices.v1beta1.Ping.Operation.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=494,
  serialized_end=653,
)

_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='bloombox.schema.services.devices.v1beta1.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_PING_REQUEST, _PING_RESPONSE, _PING_OPERATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=405,
  serialized_end=653,
)


_ACTIVATION_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bloombox.schema.services.devices.v1beta1.Activation.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serial', full_name='bloombox.schema.services.devices.v1beta1.Activation.Request.serial', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fingerprint', full_name='bloombox.schema.services.devices.v1beta1.Activation.Request.fingerprint', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=670,
  serialized_end=716,
)

_ACTIVATION_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='bloombox.schema.services.devices.v1beta1.Activation.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='active', full_name='bloombox.schema.services.devices.v1beta1.Activation.Response.active', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='bloombox.schema.services.devices.v1beta1.Activation.Response.error', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manifest', full_name='bloombox.schema.services.devices.v1beta1.Activation.Response.manifest', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=719,
  serialized_end=893,
)

_ACTIVATION_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='bloombox.schema.services.devices.v1beta1.Activation.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='bloombox.schema.services.devices.v1beta1.Activation.Operation.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='bloombox.schema.services.devices.v1beta1.Activation.Operation.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=896,
  serialized_end=1067,
)

_ACTIVATION = _descriptor.Descriptor(
  name='Activation',
  full_name='bloombox.schema.services.devices.v1beta1.Activation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_ACTIVATION_REQUEST, _ACTIVATION_RESPONSE, _ACTIVATION_OPERATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=656,
  serialized_end=1067,
)

_DEVICEASSIGNMENT.fields_by_name['role'].enum_type = _DEVICEROLE
_DEVICEACTIVATION.fields_by_name['assignment'].message_type = _DEVICEASSIGNMENT
_PING_REQUEST.containing_type = _PING
_PING_RESPONSE.fields_by_name['status'].enum_type = services_dot_ServiceStatus__pb2._SERVICESTATUS
_PING_RESPONSE.containing_type = _PING
_PING_OPERATION.fields_by_name['request'].message_type = _PING_REQUEST
_PING_OPERATION.fields_by_name['response'].message_type = _PING_RESPONSE
_PING_OPERATION.containing_type = _PING
_ACTIVATION_REQUEST.containing_type = _ACTIVATION
_ACTIVATION_RESPONSE.fields_by_name['error'].enum_type = _DEVICEERROR
_ACTIVATION_RESPONSE.fields_by_name['manifest'].message_type = _DEVICEACTIVATION
_ACTIVATION_RESPONSE.containing_type = _ACTIVATION
_ACTIVATION_OPERATION.fields_by_name['request'].message_type = _ACTIVATION_REQUEST
_ACTIVATION_OPERATION.fields_by_name['response'].message_type = _ACTIVATION_RESPONSE
_ACTIVATION_OPERATION.containing_type = _ACTIVATION
DESCRIPTOR.message_types_by_name['DeviceAssignment'] = _DEVICEASSIGNMENT
DESCRIPTOR.message_types_by_name['DeviceActivation'] = _DEVICEACTIVATION
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Activation'] = _ACTIVATION
DESCRIPTOR.enum_types_by_name['DeviceError'] = _DEVICEERROR
DESCRIPTOR.enum_types_by_name['DeviceRole'] = _DEVICEROLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceAssignment = _reflection.GeneratedProtocolMessageType('DeviceAssignment', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEASSIGNMENT,
  __module__ = 'devices.v1beta1.DevicesService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.devices.v1beta1.DeviceAssignment)
  ))
_sym_db.RegisterMessage(DeviceAssignment)

DeviceActivation = _reflection.GeneratedProtocolMessageType('DeviceActivation', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEACTIVATION,
  __module__ = 'devices.v1beta1.DevicesService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.devices.v1beta1.DeviceActivation)
  ))
_sym_db.RegisterMessage(DeviceActivation)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _PING_REQUEST,
    __module__ = 'devices.v1beta1.DevicesService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.devices.v1beta1.Ping.Request)
    ))
  ,

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _PING_RESPONSE,
    __module__ = 'devices.v1beta1.DevicesService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.devices.v1beta1.Ping.Response)
    ))
  ,

  Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(
    DESCRIPTOR = _PING_OPERATION,
    __module__ = 'devices.v1beta1.DevicesService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.devices.v1beta1.Ping.Operation)
    ))
  ,
  DESCRIPTOR = _PING,
  __module__ = 'devices.v1beta1.DevicesService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.devices.v1beta1.Ping)
  ))
_sym_db.RegisterMessage(Ping)
_sym_db.RegisterMessage(Ping.Request)
_sym_db.RegisterMessage(Ping.Response)
_sym_db.RegisterMessage(Ping.Operation)

Activation = _reflection.GeneratedProtocolMessageType('Activation', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _ACTIVATION_REQUEST,
    __module__ = 'devices.v1beta1.DevicesService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.devices.v1beta1.Activation.Request)
    ))
  ,

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _ACTIVATION_RESPONSE,
    __module__ = 'devices.v1beta1.DevicesService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.devices.v1beta1.Activation.Response)
    ))
  ,

  Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(
    DESCRIPTOR = _ACTIVATION_OPERATION,
    __module__ = 'devices.v1beta1.DevicesService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.devices.v1beta1.Activation.Operation)
    ))
  ,
  DESCRIPTOR = _ACTIVATION,
  __module__ = 'devices.v1beta1.DevicesService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.devices.v1beta1.Activation)
  ))
_sym_db.RegisterMessage(Activation)
_sym_db.RegisterMessage(Activation.Request)
_sym_db.RegisterMessage(Activation.Response)
_sym_db.RegisterMessage(Activation.Operation)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n+io.bloombox.schema.services.devices.v1beta1H\001P\001\242\002\003BBS'))

_DEVICES = _descriptor.ServiceDescriptor(
  name='Devices',
  full_name='bloombox.schema.services.devices.v1beta1.Devices',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1258,
  serialized_end=1609,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='bloombox.schema.services.devices.v1beta1.Devices.Ping',
    index=0,
    containing_service=None,
    input_type=_PING_REQUEST,
    output_type=_PING_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\027\022\025/devices/v1beta1/ping')),
  ),
  _descriptor.MethodDescriptor(
    name='Activate',
    full_name='bloombox.schema.services.devices.v1beta1.Devices.Activate',
    index=1,
    containing_service=None,
    input_type=_ACTIVATION_REQUEST,
    output_type=_ACTIVATION_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002+\022)/devices/v1beta1/{serial}/device:activate')),
  ),
])
_sym_db.RegisterServiceDescriptor(_DEVICES)

DESCRIPTOR.services_by_name['Devices'] = _DEVICES

# @@protoc_insertion_point(module_scope)
