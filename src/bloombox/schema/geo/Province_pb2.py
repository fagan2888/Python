# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: geo/Province.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from geo import USState_pb2 as geo_dot_USState__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='geo/Province.proto',
  package='opencannabis.geo',
  syntax='proto3',
  serialized_pb=_b('\n\x12geo/Province.proto\x12\x10opencannabis.geo\x1a\x11geo/USState.proto\"V\n\x08Province\x12.\n\x05state\x18\x01 \x01(\x0e\x32\x1d.opencannabis.geo.usa.USStateH\x00\x12\x12\n\x08province\x18\x02 \x01(\tH\x00\x42\x06\n\x04specB \n\x1aio.opencannabis.schema.geoH\x01P\x01\x62\x06proto3')
  ,
  dependencies=[geo_dot_USState__pb2.DESCRIPTOR,])




_PROVINCE = _descriptor.Descriptor(
  name='Province',
  full_name='opencannabis.geo.Province',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='opencannabis.geo.Province.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='province', full_name='opencannabis.geo.Province.province', index=1,
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
    _descriptor.OneofDescriptor(
      name='spec', full_name='opencannabis.geo.Province.spec',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=59,
  serialized_end=145,
)

_PROVINCE.fields_by_name['state'].enum_type = geo_dot_USState__pb2._USSTATE
_PROVINCE.oneofs_by_name['spec'].fields.append(
  _PROVINCE.fields_by_name['state'])
_PROVINCE.fields_by_name['state'].containing_oneof = _PROVINCE.oneofs_by_name['spec']
_PROVINCE.oneofs_by_name['spec'].fields.append(
  _PROVINCE.fields_by_name['province'])
_PROVINCE.fields_by_name['province'].containing_oneof = _PROVINCE.oneofs_by_name['spec']
DESCRIPTOR.message_types_by_name['Province'] = _PROVINCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Province = _reflection.GeneratedProtocolMessageType('Province', (_message.Message,), dict(
  DESCRIPTOR = _PROVINCE,
  __module__ = 'geo.Province_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.geo.Province)
  ))
_sym_db.RegisterMessage(Province)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032io.opencannabis.schema.geoH\001P\001'))
# @@protoc_insertion_point(module_scope)