# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: geo/Country.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='geo/Country.proto',
  package='opencannabis.geo',
  syntax='proto3',
  serialized_pb=_b('\n\x11geo/Country.proto\x12\x10opencannabis.geo\"\x17\n\x07\x43ountry\x12\x0c\n\x04\x63ode\x18\x01 \x01(\tB \n\x1aio.opencannabis.schema.geoH\x01P\x01\x62\x06proto3')
)




_COUNTRY = _descriptor.Descriptor(
  name='Country',
  full_name='opencannabis.geo.Country',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='opencannabis.geo.Country.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=39,
  serialized_end=62,
)

DESCRIPTOR.message_types_by_name['Country'] = _COUNTRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Country = _reflection.GeneratedProtocolMessageType('Country', (_message.Message,), dict(
  DESCRIPTOR = _COUNTRY,
  __module__ = 'geo.Country_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.geo.Country)
  ))
_sym_db.RegisterMessage(Country)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032io.opencannabis.schema.geoH\001P\001'))
# @@protoc_insertion_point(module_scope)