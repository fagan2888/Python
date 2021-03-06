# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: checkin/v1beta1/CheckinStream.proto

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


import bq_field_pb2 as bq__field__pb2
import bq_table_pb2 as bq__table__pb2
from identity import UserKey_pb2 as identity_dot_UserKey__pb2
from checkin.v1beta1 import CheckinService_Beta1_pb2 as checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='checkin/v1beta1/CheckinStream.proto',
  package='bloombox.tables.checkin.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n#checkin/v1beta1/CheckinStream.proto\x12\x1f\x62loombox.tables.checkin.v1beta1\x1a\x0e\x62q_field.proto\x1a\x0e\x62q_table.proto\x1a\x16identity/UserKey.proto\x1a*checkin/v1beta1/CheckinService_Beta1.proto\"\xdf\x01\n\x0c\x43heckinScope\x12\x43\n\x07partner\x18\x01 \x01(\tB2\xf0?\x01\x8a@,Partner account attached to a given checkin.\x12?\n\x08location\x18\x02 \x01(\tB-\xf0?\x01\x8a@\'Partner location a checkin occurred at.\x12I\n\x06\x64\x65vice\x18\x03 \x01(\tB9\xf0?\x01\x8a@3Specific device UUID that committed a user checkin.\"\xc9\x06\n\rCheckinStream\x12\\\n\x04uuid\x18\x01 \x01(\tBN\xf0?\x01\x8a@HCheckin UUID. Generated when it happens and used to correlate telemetry.\x12\xa1\x01\n\x04type\x18\x02 \x01(\x0e\x32\x35.bloombox.tables.checkin.v1beta1.CheckinAssertionTypeB\\\xf0?\x01\x8a@VSpecifies the type of checkin assertion that was made. \'ID\', \'PHYSICAL\', or \'DIGITAL\'.\x12T\n\x08occurred\x18\x03 \x01(\x04\x42\x42\xf0?\x01\xfa?\tTIMESTAMP\x8a@0Timestamp describing when this checkin occurred.\x12x\n\x05scope\x18\x04 \x01(\x0b\x32-.bloombox.tables.checkin.v1beta1.CheckinScopeB:\xf0?\x01\x8a@4User key that was matched to this checkin operation.\x12k\n\x04user\x18\x05 \x01(\x0b\x32!.bloombox.schema.identity.UserKeyB:\xf0?\x01\x8a@4User key that was matched to this checkin operation.\x12Z\n\x07granted\x18\x06 \x01(\x08\x42I\xf0?\x01\x8a@CSpecifies whether checkin access was granted for the invoking user.\x12\x8f\x01\n\x05\x65rror\x18\x07 \x01(\x0e\x32\x36.bloombox.schema.services.checkin.v1beta1.CheckinErrorBH\x8a@ESpecifies the error that prevented the user from checking in, if any.:\x0b\xea?\x08\x63heckins*J\n\x14\x43heckinAssertionType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x06\n\x02ID\x10\x01\x12\x0c\n\x08PHYSICAL\x10\x02\x12\x0b\n\x07\x44IGITAL\x10\x03\x42\x41\n)io.bloombox.schema.tables.checkin.v1beta1B\rCheckinTablesH\x01P\x00\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[bq__field__pb2.DESCRIPTOR,bq__table__pb2.DESCRIPTOR,identity_dot_UserKey__pb2.DESCRIPTOR,checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2.DESCRIPTOR,])

_CHECKINASSERTIONTYPE = _descriptor.EnumDescriptor(
  name='CheckinAssertionType',
  full_name='bloombox.tables.checkin.v1beta1.CheckinAssertionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHYSICAL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIGITAL', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1242,
  serialized_end=1316,
)
_sym_db.RegisterEnumDescriptor(_CHECKINASSERTIONTYPE)

CheckinAssertionType = enum_type_wrapper.EnumTypeWrapper(_CHECKINASSERTIONTYPE)
UNSPECIFIED = 0
ID = 1
PHYSICAL = 2
DIGITAL = 3



_CHECKINSCOPE = _descriptor.Descriptor(
  name='CheckinScope',
  full_name='bloombox.tables.checkin.v1beta1.CheckinScope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partner', full_name='bloombox.tables.checkin.v1beta1.CheckinScope.partner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@,Partner account attached to a given checkin.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='bloombox.tables.checkin.v1beta1.CheckinScope.location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\'Partner location a checkin occurred at.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='bloombox.tables.checkin.v1beta1.CheckinScope.device', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@3Specific device UUID that committed a user checkin.')), file=DESCRIPTOR),
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
  serialized_start=173,
  serialized_end=396,
)


_CHECKINSTREAM = _descriptor.Descriptor(
  name='CheckinStream',
  full_name='bloombox.tables.checkin.v1beta1.CheckinStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='bloombox.tables.checkin.v1beta1.CheckinStream.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@HCheckin UUID. Generated when it happens and used to correlate telemetry.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='bloombox.tables.checkin.v1beta1.CheckinStream.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@VSpecifies the type of checkin assertion that was made. \'ID\', \'PHYSICAL\', or \'DIGITAL\'.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occurred', full_name='bloombox.tables.checkin.v1beta1.CheckinStream.occurred', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\372?\tTIMESTAMP\212@0Timestamp describing when this checkin occurred.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scope', full_name='bloombox.tables.checkin.v1beta1.CheckinStream.scope', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@4User key that was matched to this checkin operation.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='bloombox.tables.checkin.v1beta1.CheckinStream.user', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@4User key that was matched to this checkin operation.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='granted', full_name='bloombox.tables.checkin.v1beta1.CheckinStream.granted', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@CSpecifies whether checkin access was granted for the invoking user.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='bloombox.tables.checkin.v1beta1.CheckinStream.error', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@ESpecifies the error that prevented the user from checking in, if any.')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\352?\010checkins')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=399,
  serialized_end=1240,
)

_CHECKINSTREAM.fields_by_name['type'].enum_type = _CHECKINASSERTIONTYPE
_CHECKINSTREAM.fields_by_name['scope'].message_type = _CHECKINSCOPE
_CHECKINSTREAM.fields_by_name['user'].message_type = identity_dot_UserKey__pb2._USERKEY
_CHECKINSTREAM.fields_by_name['error'].enum_type = checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2._CHECKINERROR
DESCRIPTOR.message_types_by_name['CheckinScope'] = _CHECKINSCOPE
DESCRIPTOR.message_types_by_name['CheckinStream'] = _CHECKINSTREAM
DESCRIPTOR.enum_types_by_name['CheckinAssertionType'] = _CHECKINASSERTIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckinScope = _reflection.GeneratedProtocolMessageType('CheckinScope', (_message.Message,), dict(
  DESCRIPTOR = _CHECKINSCOPE,
  __module__ = 'checkin.v1beta1.CheckinStream_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.tables.checkin.v1beta1.CheckinScope)
  ))
_sym_db.RegisterMessage(CheckinScope)

CheckinStream = _reflection.GeneratedProtocolMessageType('CheckinStream', (_message.Message,), dict(
  DESCRIPTOR = _CHECKINSTREAM,
  __module__ = 'checkin.v1beta1.CheckinStream_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.tables.checkin.v1beta1.CheckinStream)
  ))
_sym_db.RegisterMessage(CheckinStream)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n)io.bloombox.schema.tables.checkin.v1beta1B\rCheckinTablesH\001P\000\370\001\001'))
_CHECKINSCOPE.fields_by_name['partner'].has_options = True
_CHECKINSCOPE.fields_by_name['partner']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@,Partner account attached to a given checkin.'))
_CHECKINSCOPE.fields_by_name['location'].has_options = True
_CHECKINSCOPE.fields_by_name['location']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\'Partner location a checkin occurred at.'))
_CHECKINSCOPE.fields_by_name['device'].has_options = True
_CHECKINSCOPE.fields_by_name['device']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@3Specific device UUID that committed a user checkin.'))
_CHECKINSTREAM.fields_by_name['uuid'].has_options = True
_CHECKINSTREAM.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@HCheckin UUID. Generated when it happens and used to correlate telemetry.'))
_CHECKINSTREAM.fields_by_name['type'].has_options = True
_CHECKINSTREAM.fields_by_name['type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@VSpecifies the type of checkin assertion that was made. \'ID\', \'PHYSICAL\', or \'DIGITAL\'.'))
_CHECKINSTREAM.fields_by_name['occurred'].has_options = True
_CHECKINSTREAM.fields_by_name['occurred']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\372?\tTIMESTAMP\212@0Timestamp describing when this checkin occurred.'))
_CHECKINSTREAM.fields_by_name['scope'].has_options = True
_CHECKINSTREAM.fields_by_name['scope']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@4User key that was matched to this checkin operation.'))
_CHECKINSTREAM.fields_by_name['user'].has_options = True
_CHECKINSTREAM.fields_by_name['user']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@4User key that was matched to this checkin operation.'))
_CHECKINSTREAM.fields_by_name['granted'].has_options = True
_CHECKINSTREAM.fields_by_name['granted']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@CSpecifies whether checkin access was granted for the invoking user.'))
_CHECKINSTREAM.fields_by_name['error'].has_options = True
_CHECKINSTREAM.fields_by_name['error']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@ESpecifies the error that prevented the user from checking in, if any.'))
_CHECKINSTREAM.has_options = True
_CHECKINSTREAM._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\352?\010checkins'))
# @@protoc_insertion_point(module_scope)
