# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: commerce/Currency.proto

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
  name='commerce/Currency.proto',
  package='opencannabis.commerce',
  syntax='proto3',
  serialized_pb=_b('\n\x17\x63ommerce/Currency.proto\x12\x15opencannabis.commerce\"\xa0\x01\n\rCurrencyValue\x12\r\n\x05value\x18\x01 \x01(\x02\x12\x31\n\x04type\x18\x02 \x01(\x0e\x32#.opencannabis.commerce.CurrencyType\x12\x33\n\x04\x66iat\x18\n \x01(\x0e\x32#.opencannabis.commerce.FiatCurrencyH\x00\x12\x10\n\x06\x63ustom\x18\x64 \x01(\tH\x00\x42\x06\n\x04spec*.\n\x0c\x43urrencyType\x12\x08\n\x04\x46IAT\x10\x00\x12\x08\n\x04REAL\x10\x01\x12\n\n\x06\x43RYPTO\x10\x02*\x17\n\x0c\x46iatCurrency\x12\x07\n\x03USD\x10\x00\x42=\n\x1fio.opencannabis.schema.currencyB\x10\x43ommerceCurrencyH\x01P\x01\xa2\x02\x03OCSb\x06proto3')
)

_CURRENCYTYPE = _descriptor.EnumDescriptor(
  name='CurrencyType',
  full_name='opencannabis.commerce.CurrencyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FIAT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRYPTO', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=213,
  serialized_end=259,
)
_sym_db.RegisterEnumDescriptor(_CURRENCYTYPE)

CurrencyType = enum_type_wrapper.EnumTypeWrapper(_CURRENCYTYPE)
_FIATCURRENCY = _descriptor.EnumDescriptor(
  name='FiatCurrency',
  full_name='opencannabis.commerce.FiatCurrency',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USD', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=261,
  serialized_end=284,
)
_sym_db.RegisterEnumDescriptor(_FIATCURRENCY)

FiatCurrency = enum_type_wrapper.EnumTypeWrapper(_FIATCURRENCY)
FIAT = 0
REAL = 1
CRYPTO = 2
USD = 0



_CURRENCYVALUE = _descriptor.Descriptor(
  name='CurrencyValue',
  full_name='opencannabis.commerce.CurrencyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='opencannabis.commerce.CurrencyValue.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='opencannabis.commerce.CurrencyValue.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fiat', full_name='opencannabis.commerce.CurrencyValue.fiat', index=2,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom', full_name='opencannabis.commerce.CurrencyValue.custom', index=3,
      number=100, type=9, cpp_type=9, label=1,
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
      name='spec', full_name='opencannabis.commerce.CurrencyValue.spec',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=51,
  serialized_end=211,
)

_CURRENCYVALUE.fields_by_name['type'].enum_type = _CURRENCYTYPE
_CURRENCYVALUE.fields_by_name['fiat'].enum_type = _FIATCURRENCY
_CURRENCYVALUE.oneofs_by_name['spec'].fields.append(
  _CURRENCYVALUE.fields_by_name['fiat'])
_CURRENCYVALUE.fields_by_name['fiat'].containing_oneof = _CURRENCYVALUE.oneofs_by_name['spec']
_CURRENCYVALUE.oneofs_by_name['spec'].fields.append(
  _CURRENCYVALUE.fields_by_name['custom'])
_CURRENCYVALUE.fields_by_name['custom'].containing_oneof = _CURRENCYVALUE.oneofs_by_name['spec']
DESCRIPTOR.message_types_by_name['CurrencyValue'] = _CURRENCYVALUE
DESCRIPTOR.enum_types_by_name['CurrencyType'] = _CURRENCYTYPE
DESCRIPTOR.enum_types_by_name['FiatCurrency'] = _FIATCURRENCY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CurrencyValue = _reflection.GeneratedProtocolMessageType('CurrencyValue', (_message.Message,), dict(
  DESCRIPTOR = _CURRENCYVALUE,
  __module__ = 'commerce.Currency_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.commerce.CurrencyValue)
  ))
_sym_db.RegisterMessage(CurrencyValue)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037io.opencannabis.schema.currencyB\020CommerceCurrencyH\001P\001\242\002\003OCS'))
# @@protoc_insertion_point(module_scope)
