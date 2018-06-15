# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: partner/integrations/MailchimpSettings.proto

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
  name='partner/integrations/MailchimpSettings.proto',
  package='bloombox.schema.partner.integrations.mailchimp',
  syntax='proto3',
  serialized_pb=_b('\n,partner/integrations/MailchimpSettings.proto\x12.bloombox.schema.partner.integrations.mailchimp\"S\n\x1cMailchimpIntegrationFeatures\x12\x0f\n\x07signups\x18\x01 \x01(\x08\x12\x10\n\x08segments\x18\x02 \x01(\x08\x12\x10\n\x08ordering\x18\x03 \x01(\x08\"2\n\x0eMailchimpLists\x12\r\n\x05\x63omms\x18\x01 \x01(\t\x12\x11\n\tmarketing\x18\x02 \x01(\t\"\xd3\x01\n\x11MailchimpSettings\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12^\n\x08\x66\x65\x61tures\x18\n \x01(\x0b\x32L.bloombox.schema.partner.integrations.mailchimp.MailchimpIntegrationFeatures\x12M\n\x05lists\x18\x0b \x01(\x0b\x32>.bloombox.schema.partner.integrations.mailchimp.MailchimpListsB=\n1io.bloombox.schema.partner.integrations.mailchimpH\x01P\x00\xa2\x02\x03\x42\x42Sb\x06proto3')
)




_MAILCHIMPINTEGRATIONFEATURES = _descriptor.Descriptor(
  name='MailchimpIntegrationFeatures',
  full_name='bloombox.schema.partner.integrations.mailchimp.MailchimpIntegrationFeatures',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signups', full_name='bloombox.schema.partner.integrations.mailchimp.MailchimpIntegrationFeatures.signups', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='segments', full_name='bloombox.schema.partner.integrations.mailchimp.MailchimpIntegrationFeatures.segments', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ordering', full_name='bloombox.schema.partner.integrations.mailchimp.MailchimpIntegrationFeatures.ordering', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=96,
  serialized_end=179,
)


_MAILCHIMPLISTS = _descriptor.Descriptor(
  name='MailchimpLists',
  full_name='bloombox.schema.partner.integrations.mailchimp.MailchimpLists',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comms', full_name='bloombox.schema.partner.integrations.mailchimp.MailchimpLists.comms', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='marketing', full_name='bloombox.schema.partner.integrations.mailchimp.MailchimpLists.marketing', index=1,
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
  serialized_start=181,
  serialized_end=231,
)


_MAILCHIMPSETTINGS = _descriptor.Descriptor(
  name='MailchimpSettings',
  full_name='bloombox.schema.partner.integrations.mailchimp.MailchimpSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_key', full_name='bloombox.schema.partner.integrations.mailchimp.MailchimpSettings.api_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='bloombox.schema.partner.integrations.mailchimp.MailchimpSettings.features', index=1,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lists', full_name='bloombox.schema.partner.integrations.mailchimp.MailchimpSettings.lists', index=2,
      number=11, type=11, cpp_type=10, label=1,
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
  serialized_start=234,
  serialized_end=445,
)

_MAILCHIMPSETTINGS.fields_by_name['features'].message_type = _MAILCHIMPINTEGRATIONFEATURES
_MAILCHIMPSETTINGS.fields_by_name['lists'].message_type = _MAILCHIMPLISTS
DESCRIPTOR.message_types_by_name['MailchimpIntegrationFeatures'] = _MAILCHIMPINTEGRATIONFEATURES
DESCRIPTOR.message_types_by_name['MailchimpLists'] = _MAILCHIMPLISTS
DESCRIPTOR.message_types_by_name['MailchimpSettings'] = _MAILCHIMPSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MailchimpIntegrationFeatures = _reflection.GeneratedProtocolMessageType('MailchimpIntegrationFeatures', (_message.Message,), dict(
  DESCRIPTOR = _MAILCHIMPINTEGRATIONFEATURES,
  __module__ = 'partner.integrations.MailchimpSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.integrations.mailchimp.MailchimpIntegrationFeatures)
  ))
_sym_db.RegisterMessage(MailchimpIntegrationFeatures)

MailchimpLists = _reflection.GeneratedProtocolMessageType('MailchimpLists', (_message.Message,), dict(
  DESCRIPTOR = _MAILCHIMPLISTS,
  __module__ = 'partner.integrations.MailchimpSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.integrations.mailchimp.MailchimpLists)
  ))
_sym_db.RegisterMessage(MailchimpLists)

MailchimpSettings = _reflection.GeneratedProtocolMessageType('MailchimpSettings', (_message.Message,), dict(
  DESCRIPTOR = _MAILCHIMPSETTINGS,
  __module__ = 'partner.integrations.MailchimpSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.integrations.mailchimp.MailchimpSettings)
  ))
_sym_db.RegisterMessage(MailchimpSettings)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n1io.bloombox.schema.partner.integrations.mailchimpH\001P\000\242\002\003BBS'))
# @@protoc_insertion_point(module_scope)
