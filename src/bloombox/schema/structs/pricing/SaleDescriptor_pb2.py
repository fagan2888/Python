# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: structs/pricing/SaleDescriptor.proto

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


from temporal import Instant_pb2 as temporal_dot_Instant__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='structs/pricing/SaleDescriptor.proto',
  package='opencannabis.structs.pricing',
  syntax='proto3',
  serialized_pb=_b('\n$structs/pricing/SaleDescriptor.proto\x12\x1copencannabis.structs.pricing\x1a\x16temporal/Instant.proto\"&\n\x12PercentageDiscount\x12\x10\n\x08\x64iscount\x18\x14 \x01(\r\"/\n\x0c\x42OGODiscount\x12\x0f\n\x07trigger\x18\x15 \x01(\r\x12\x0e\n\x06reward\x18\x16 \x01(\r\"2\n\x0fLoyaltyDiscount\x12\x0f\n\x07trigger\x18\x17 \x01(\r\x12\x0e\n\x06reward\x18\x18 \x01(\r\"\xff\x02\n\x0eSaleDescriptor\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.opencannabis.structs.pricing.SaleType\x12\x31\n\teffective\x18\x02 \x01(\x0b\x32\x1e.opencannabis.temporal.Instant\x12\x32\n\nexpiration\x18\x03 \x01(\x0b\x32\x1e.opencannabis.temporal.Instant\x12J\n\x0epercentage_off\x18\x04 \x01(\x0b\x32\x30.opencannabis.structs.pricing.PercentageDiscountH\x00\x12:\n\x04\x62ogo\x18\x05 \x01(\x0b\x32*.opencannabis.structs.pricing.BOGODiscountH\x00\x12@\n\x07loyalty\x18\x06 \x01(\x0b\x32-.opencannabis.structs.pricing.LoyaltyDiscountH\x00\x42\x06\n\x04sale*P\n\x08SaleType\x12\x18\n\x14PERCENTAGE_REDUCTION\x10\x00\x12\x13\n\x0fVALUE_REDUCTION\x10\x01\x12\x08\n\x04\x42OGO\x10\x02\x12\x0b\n\x07LOYALTY\x10\x03\x42\x42\n%io.opencannabis.schema.product.structB\x0fProductDiscountH\x01P\x01\xa2\x02\x03OCSb\x06proto3')
  ,
  dependencies=[temporal_dot_Instant__pb2.DESCRIPTOR,])

_SALETYPE = _descriptor.EnumDescriptor(
  name='SaleType',
  full_name='opencannabis.structs.pricing.SaleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PERCENTAGE_REDUCTION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_REDUCTION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOGO', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOYALTY', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=621,
  serialized_end=701,
)
_sym_db.RegisterEnumDescriptor(_SALETYPE)

SaleType = enum_type_wrapper.EnumTypeWrapper(_SALETYPE)
PERCENTAGE_REDUCTION = 0
VALUE_REDUCTION = 1
BOGO = 2
LOYALTY = 3



_PERCENTAGEDISCOUNT = _descriptor.Descriptor(
  name='PercentageDiscount',
  full_name='opencannabis.structs.pricing.PercentageDiscount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='discount', full_name='opencannabis.structs.pricing.PercentageDiscount.discount', index=0,
      number=20, type=13, cpp_type=3, label=1,
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
  serialized_start=94,
  serialized_end=132,
)


_BOGODISCOUNT = _descriptor.Descriptor(
  name='BOGODiscount',
  full_name='opencannabis.structs.pricing.BOGODiscount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trigger', full_name='opencannabis.structs.pricing.BOGODiscount.trigger', index=0,
      number=21, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='opencannabis.structs.pricing.BOGODiscount.reward', index=1,
      number=22, type=13, cpp_type=3, label=1,
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
  serialized_start=134,
  serialized_end=181,
)


_LOYALTYDISCOUNT = _descriptor.Descriptor(
  name='LoyaltyDiscount',
  full_name='opencannabis.structs.pricing.LoyaltyDiscount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trigger', full_name='opencannabis.structs.pricing.LoyaltyDiscount.trigger', index=0,
      number=23, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='opencannabis.structs.pricing.LoyaltyDiscount.reward', index=1,
      number=24, type=13, cpp_type=3, label=1,
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
  serialized_start=183,
  serialized_end=233,
)


_SALEDESCRIPTOR = _descriptor.Descriptor(
  name='SaleDescriptor',
  full_name='opencannabis.structs.pricing.SaleDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='opencannabis.structs.pricing.SaleDescriptor.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='effective', full_name='opencannabis.structs.pricing.SaleDescriptor.effective', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='opencannabis.structs.pricing.SaleDescriptor.expiration', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='percentage_off', full_name='opencannabis.structs.pricing.SaleDescriptor.percentage_off', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bogo', full_name='opencannabis.structs.pricing.SaleDescriptor.bogo', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loyalty', full_name='opencannabis.structs.pricing.SaleDescriptor.loyalty', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
      name='sale', full_name='opencannabis.structs.pricing.SaleDescriptor.sale',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=236,
  serialized_end=619,
)

_SALEDESCRIPTOR.fields_by_name['type'].enum_type = _SALETYPE
_SALEDESCRIPTOR.fields_by_name['effective'].message_type = temporal_dot_Instant__pb2._INSTANT
_SALEDESCRIPTOR.fields_by_name['expiration'].message_type = temporal_dot_Instant__pb2._INSTANT
_SALEDESCRIPTOR.fields_by_name['percentage_off'].message_type = _PERCENTAGEDISCOUNT
_SALEDESCRIPTOR.fields_by_name['bogo'].message_type = _BOGODISCOUNT
_SALEDESCRIPTOR.fields_by_name['loyalty'].message_type = _LOYALTYDISCOUNT
_SALEDESCRIPTOR.oneofs_by_name['sale'].fields.append(
  _SALEDESCRIPTOR.fields_by_name['percentage_off'])
_SALEDESCRIPTOR.fields_by_name['percentage_off'].containing_oneof = _SALEDESCRIPTOR.oneofs_by_name['sale']
_SALEDESCRIPTOR.oneofs_by_name['sale'].fields.append(
  _SALEDESCRIPTOR.fields_by_name['bogo'])
_SALEDESCRIPTOR.fields_by_name['bogo'].containing_oneof = _SALEDESCRIPTOR.oneofs_by_name['sale']
_SALEDESCRIPTOR.oneofs_by_name['sale'].fields.append(
  _SALEDESCRIPTOR.fields_by_name['loyalty'])
_SALEDESCRIPTOR.fields_by_name['loyalty'].containing_oneof = _SALEDESCRIPTOR.oneofs_by_name['sale']
DESCRIPTOR.message_types_by_name['PercentageDiscount'] = _PERCENTAGEDISCOUNT
DESCRIPTOR.message_types_by_name['BOGODiscount'] = _BOGODISCOUNT
DESCRIPTOR.message_types_by_name['LoyaltyDiscount'] = _LOYALTYDISCOUNT
DESCRIPTOR.message_types_by_name['SaleDescriptor'] = _SALEDESCRIPTOR
DESCRIPTOR.enum_types_by_name['SaleType'] = _SALETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PercentageDiscount = _reflection.GeneratedProtocolMessageType('PercentageDiscount', (_message.Message,), dict(
  DESCRIPTOR = _PERCENTAGEDISCOUNT,
  __module__ = 'structs.pricing.SaleDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.structs.pricing.PercentageDiscount)
  ))
_sym_db.RegisterMessage(PercentageDiscount)

BOGODiscount = _reflection.GeneratedProtocolMessageType('BOGODiscount', (_message.Message,), dict(
  DESCRIPTOR = _BOGODISCOUNT,
  __module__ = 'structs.pricing.SaleDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.structs.pricing.BOGODiscount)
  ))
_sym_db.RegisterMessage(BOGODiscount)

LoyaltyDiscount = _reflection.GeneratedProtocolMessageType('LoyaltyDiscount', (_message.Message,), dict(
  DESCRIPTOR = _LOYALTYDISCOUNT,
  __module__ = 'structs.pricing.SaleDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.structs.pricing.LoyaltyDiscount)
  ))
_sym_db.RegisterMessage(LoyaltyDiscount)

SaleDescriptor = _reflection.GeneratedProtocolMessageType('SaleDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _SALEDESCRIPTOR,
  __module__ = 'structs.pricing.SaleDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.structs.pricing.SaleDescriptor)
  ))
_sym_db.RegisterMessage(SaleDescriptor)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%io.opencannabis.schema.product.structB\017ProductDiscountH\001P\001\242\002\003OCS'))
# @@protoc_insertion_point(module_scope)
