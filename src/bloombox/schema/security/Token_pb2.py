# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: security/Token.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from oauth import AuthorizationScope_pb2 as oauth_dot_AuthorizationScope__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='security/Token.proto',
  package='bloombox.schema.security',
  syntax='proto3',
  serialized_pb=_b('\n\x14security/Token.proto\x12\x18\x62loombox.schema.security\x1a\x1eoauth/AuthorizationScope.proto\"h\n\x0eIDTokenPayload\x12\r\n\x05token\x18\x01 \x01(\t\x12\x12\n\nexpiration\x18\x02 \x01(\x04\x12\x10\n\x08issuance\x18\x03 \x01(\x04\x12\x0f\n\x07subject\x18\x04 \x01(\t\x12\x10\n\x08\x61udience\x18\x05 \x01(\t\"a\n\x07IDToken\x12\x11\n\x07\x65ncoded\x18\x01 \x01(\tH\x00\x12\x38\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32(.bloombox.schema.security.IDTokenPayloadH\x00\x42\t\n\x07payload\"z\n\x0cTokenPayload\x12\r\n\x05token\x18\x01 \x01(\t\x12\x12\n\nexpiration\x18\x02 \x01(\x04\x12\x10\n\x08issuance\x18\x03 \x01(\x04\x12\x35\n\x05scope\x18\x04 \x03(\x0b\x32&.opencannabis.oauth.AuthorizationScope\"c\n\tAuthToken\x12\x11\n\x07\x65ncoded\x18\x01 \x01(\tH\x00\x12\x38\n\x06ticket\x18\x02 \x01(\x0b\x32&.bloombox.schema.security.TokenPayloadH\x00\x42\t\n\x07payload\"o\n\x0b\x41uthPayload\x12-\n\x02id\x18\x01 \x01(\x0b\x32!.bloombox.schema.security.IDToken\x12\x31\n\x04\x61uth\x18\x02 \x01(\x0b\x32#.bloombox.schema.security.AuthTokenB\'\n\x1bio.bloombox.schema.securityH\x01P\x01\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[oauth_dot_AuthorizationScope__pb2.DESCRIPTOR,])




_IDTOKENPAYLOAD = _descriptor.Descriptor(
  name='IDTokenPayload',
  full_name='bloombox.schema.security.IDTokenPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='bloombox.schema.security.IDTokenPayload.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='bloombox.schema.security.IDTokenPayload.expiration', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issuance', full_name='bloombox.schema.security.IDTokenPayload.issuance', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subject', full_name='bloombox.schema.security.IDTokenPayload.subject', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audience', full_name='bloombox.schema.security.IDTokenPayload.audience', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=82,
  serialized_end=186,
)


_IDTOKEN = _descriptor.Descriptor(
  name='IDToken',
  full_name='bloombox.schema.security.IDToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encoded', full_name='bloombox.schema.security.IDToken.encoded', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='bloombox.schema.security.IDToken.data', index=1,
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='bloombox.schema.security.IDToken.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=188,
  serialized_end=285,
)


_TOKENPAYLOAD = _descriptor.Descriptor(
  name='TokenPayload',
  full_name='bloombox.schema.security.TokenPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='bloombox.schema.security.TokenPayload.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='bloombox.schema.security.TokenPayload.expiration', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issuance', full_name='bloombox.schema.security.TokenPayload.issuance', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scope', full_name='bloombox.schema.security.TokenPayload.scope', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=287,
  serialized_end=409,
)


_AUTHTOKEN = _descriptor.Descriptor(
  name='AuthToken',
  full_name='bloombox.schema.security.AuthToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encoded', full_name='bloombox.schema.security.AuthToken.encoded', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ticket', full_name='bloombox.schema.security.AuthToken.ticket', index=1,
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='bloombox.schema.security.AuthToken.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=411,
  serialized_end=510,
)


_AUTHPAYLOAD = _descriptor.Descriptor(
  name='AuthPayload',
  full_name='bloombox.schema.security.AuthPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bloombox.schema.security.AuthPayload.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth', full_name='bloombox.schema.security.AuthPayload.auth', index=1,
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
  serialized_start=512,
  serialized_end=623,
)

_IDTOKEN.fields_by_name['data'].message_type = _IDTOKENPAYLOAD
_IDTOKEN.oneofs_by_name['payload'].fields.append(
  _IDTOKEN.fields_by_name['encoded'])
_IDTOKEN.fields_by_name['encoded'].containing_oneof = _IDTOKEN.oneofs_by_name['payload']
_IDTOKEN.oneofs_by_name['payload'].fields.append(
  _IDTOKEN.fields_by_name['data'])
_IDTOKEN.fields_by_name['data'].containing_oneof = _IDTOKEN.oneofs_by_name['payload']
_TOKENPAYLOAD.fields_by_name['scope'].message_type = oauth_dot_AuthorizationScope__pb2._AUTHORIZATIONSCOPE
_AUTHTOKEN.fields_by_name['ticket'].message_type = _TOKENPAYLOAD
_AUTHTOKEN.oneofs_by_name['payload'].fields.append(
  _AUTHTOKEN.fields_by_name['encoded'])
_AUTHTOKEN.fields_by_name['encoded'].containing_oneof = _AUTHTOKEN.oneofs_by_name['payload']
_AUTHTOKEN.oneofs_by_name['payload'].fields.append(
  _AUTHTOKEN.fields_by_name['ticket'])
_AUTHTOKEN.fields_by_name['ticket'].containing_oneof = _AUTHTOKEN.oneofs_by_name['payload']
_AUTHPAYLOAD.fields_by_name['id'].message_type = _IDTOKEN
_AUTHPAYLOAD.fields_by_name['auth'].message_type = _AUTHTOKEN
DESCRIPTOR.message_types_by_name['IDTokenPayload'] = _IDTOKENPAYLOAD
DESCRIPTOR.message_types_by_name['IDToken'] = _IDTOKEN
DESCRIPTOR.message_types_by_name['TokenPayload'] = _TOKENPAYLOAD
DESCRIPTOR.message_types_by_name['AuthToken'] = _AUTHTOKEN
DESCRIPTOR.message_types_by_name['AuthPayload'] = _AUTHPAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IDTokenPayload = _reflection.GeneratedProtocolMessageType('IDTokenPayload', (_message.Message,), dict(
  DESCRIPTOR = _IDTOKENPAYLOAD,
  __module__ = 'security.Token_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.security.IDTokenPayload)
  ))
_sym_db.RegisterMessage(IDTokenPayload)

IDToken = _reflection.GeneratedProtocolMessageType('IDToken', (_message.Message,), dict(
  DESCRIPTOR = _IDTOKEN,
  __module__ = 'security.Token_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.security.IDToken)
  ))
_sym_db.RegisterMessage(IDToken)

TokenPayload = _reflection.GeneratedProtocolMessageType('TokenPayload', (_message.Message,), dict(
  DESCRIPTOR = _TOKENPAYLOAD,
  __module__ = 'security.Token_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.security.TokenPayload)
  ))
_sym_db.RegisterMessage(TokenPayload)

AuthToken = _reflection.GeneratedProtocolMessageType('AuthToken', (_message.Message,), dict(
  DESCRIPTOR = _AUTHTOKEN,
  __module__ = 'security.Token_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.security.AuthToken)
  ))
_sym_db.RegisterMessage(AuthToken)

AuthPayload = _reflection.GeneratedProtocolMessageType('AuthPayload', (_message.Message,), dict(
  DESCRIPTOR = _AUTHPAYLOAD,
  __module__ = 'security.Token_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.security.AuthPayload)
  ))
_sym_db.RegisterMessage(AuthPayload)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.bloombox.schema.securityH\001P\001\242\002\003BBS'))
# @@protoc_insertion_point(module_scope)
