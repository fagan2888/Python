# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bq_table.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bq_table.proto',
  package='gen_bq_schema',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x62q_table.proto\x12\rgen_bq_schema\x1a google/protobuf/descriptor.proto:4\n\ntable_name\x12\x1f.google.protobuf.MessageOptions\x18\xfd\x07 \x01(\t:;\n\x11table_description\x12\x1f.google.protobuf.MessageOptions\x18\x82\x08 \x01(\tB\x08Z\x06protosb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


TABLE_NAME_FIELD_NUMBER = 1021
table_name = _descriptor.FieldDescriptor(
  name='table_name', full_name='gen_bq_schema.table_name', index=0,
  number=1021, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
TABLE_DESCRIPTION_FIELD_NUMBER = 1026
table_description = _descriptor.FieldDescriptor(
  name='table_description', full_name='gen_bq_schema.table_description', index=1,
  number=1026, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)

DESCRIPTOR.extensions_by_name['table_name'] = table_name
DESCRIPTOR.extensions_by_name['table_description'] = table_description
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(table_name)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(table_description)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\006protos'))
# @@protoc_insertion_point(module_scope)
