# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: security/IdentityToken.proto

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




DESCRIPTOR = _descriptor.FileDescriptor(
  name='security/IdentityToken.proto',
  package='bloombox.schema.security',
  syntax='proto3',
  serialized_pb=_b('\n\x1csecurity/IdentityToken.proto\x12\x18\x62loombox.schema.security\"l\n\rIdentityToken\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0f\n\x07\x65ncoded\x18\x02 \x01(\t\x12=\n\x06issuer\x18\x03 \x01(\x0e\x32-.bloombox.schema.security.IdentityTokenIssuer*H\n\x13IdentityTokenIssuer\x12\x0c\n\x08INTERNAL\x10\x00\x12\x0c\n\x08\x46IREBASE\x10\x01\x12\t\n\x05\x41UTH0\x10\x02\x12\n\n\x06GOOGLE\x10\x03\x42\'\n\x1bio.bloombox.schema.securityH\x01P\x01\xa2\x02\x03\x42\x42Sb\x06proto3')
)

_IDENTITYTOKENISSUER = _descriptor.EnumDescriptor(
  name='IdentityTokenIssuer',
  full_name='bloombox.schema.security.IdentityTokenIssuer',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INTERNAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIREBASE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH0', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=168,
  serialized_end=240,
)
_sym_db.RegisterEnumDescriptor(_IDENTITYTOKENISSUER)

IdentityTokenIssuer = enum_type_wrapper.EnumTypeWrapper(_IDENTITYTOKENISSUER)
INTERNAL = 0
FIREBASE = 1
AUTH0 = 2
GOOGLE = 3



_IDENTITYTOKEN = _descriptor.Descriptor(
  name='IdentityToken',
  full_name='bloombox.schema.security.IdentityToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='bloombox.schema.security.IdentityToken.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoded', full_name='bloombox.schema.security.IdentityToken.encoded', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issuer', full_name='bloombox.schema.security.IdentityToken.issuer', index=2,
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
  serialized_start=58,
  serialized_end=166,
)

_IDENTITYTOKEN.fields_by_name['issuer'].enum_type = _IDENTITYTOKENISSUER
DESCRIPTOR.message_types_by_name['IdentityToken'] = _IDENTITYTOKEN
DESCRIPTOR.enum_types_by_name['IdentityTokenIssuer'] = _IDENTITYTOKENISSUER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IdentityToken = _reflection.GeneratedProtocolMessageType('IdentityToken', (_message.Message,), dict(
  DESCRIPTOR = _IDENTITYTOKEN,
  __module__ = 'security.IdentityToken_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.security.IdentityToken)
  ))
_sym_db.RegisterMessage(IdentityToken)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.bloombox.schema.securityH\001P\001\242\002\003BBS'))
# @@protoc_insertion_point(module_scope)
