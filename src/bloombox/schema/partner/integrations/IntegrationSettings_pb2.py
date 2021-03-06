# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: partner/integrations/IntegrationSettings.proto

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
from partner.integrations import TreezSettings_pb2 as partner_dot_integrations_dot_TreezSettings__pb2
from partner.integrations import GSuiteSettings_pb2 as partner_dot_integrations_dot_GSuiteSettings__pb2
from partner.integrations import TwilioSettings_pb2 as partner_dot_integrations_dot_TwilioSettings__pb2
from partner.integrations import OnFleetSettings_pb2 as partner_dot_integrations_dot_OnFleetSettings__pb2
from partner.integrations import SendgridSettings_pb2 as partner_dot_integrations_dot_SendgridSettings__pb2
from partner.integrations import MailchimpSettings_pb2 as partner_dot_integrations_dot_MailchimpSettings__pb2
from partner.integrations import GreenbitsSettings_pb2 as partner_dot_integrations_dot_GreenbitsSettings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='partner/integrations/IntegrationSettings.proto',
  package='bloombox.schema.partner.integrations',
  syntax='proto3',
  serialized_pb=_b('\n.partner/integrations/IntegrationSettings.proto\x12$bloombox.schema.partner.integrations\x1a\x16temporal/Instant.proto\x1a(partner/integrations/TreezSettings.proto\x1a)partner/integrations/GSuiteSettings.proto\x1a)partner/integrations/TwilioSettings.proto\x1a*partner/integrations/OnFleetSettings.proto\x1a+partner/integrations/SendgridSettings.proto\x1a,partner/integrations/MailchimpSettings.proto\x1a,partner/integrations/GreenbitsSettings.proto\"\xc2\x01\n\x1aGenericIntegrationSettings\x12I\n\x07partner\x18\x01 \x01(\x0e\x32\x38.bloombox.schema.partner.integrations.IntegrationPartner\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x13\n\x0b\x66ully_setup\x18\x03 \x01(\x08\x12\x33\n\x0blast_tested\x18\x04 \x01(\x0b\x32\x1e.opencannabis.temporal.Instant\"\xa6\x06\n\x1bLocationIntegrationSettings\x12N\n\x0cintegrations\x18\x01 \x03(\x0e\x32\x38.bloombox.schema.partner.integrations.IntegrationPartner\x12_\n\x07generic\x18\x02 \x03(\x0b\x32N.bloombox.schema.partner.integrations.LocationIntegrationSettings.GenericEntry\x12T\n\tgreenbits\x18\n \x01(\x0b\x32\x41.bloombox.schema.partner.integrations.greenbits.GreenbitsSettings\x12T\n\tmailchimp\x18\x0b \x01(\x0b\x32\x41.bloombox.schema.partner.integrations.mailchimp.MailchimpSettings\x12Q\n\x08sendgrid\x18\x0c \x01(\x0b\x32?.bloombox.schema.partner.integrations.sendgrid.SendgridSettings\x12K\n\x06twilio\x18\r \x01(\x0b\x32;.bloombox.schema.partner.integrations.twilio.TwilioSettings\x12N\n\x07onfleet\x18\x0e \x01(\x0b\x32=.bloombox.schema.partner.integrations.onfleet.OnFleetSettings\x12H\n\x05treez\x18\x0f \x01(\x0b\x32\x39.bloombox.schema.partner.integrations.treez.TreezSettings\x1ap\n\x0cGenericEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12O\n\x05value\x18\x02 \x01(\x0b\x32@.bloombox.schema.partner.integrations.GenericIntegrationSettings:\x02\x38\x01\"\x8b\x03\n\x1aPartnerIntegrationSettings\x12N\n\x0cintegrations\x18\x01 \x03(\x0e\x32\x38.bloombox.schema.partner.integrations.IntegrationPartner\x12^\n\x07generic\x18\x02 \x03(\x0b\x32M.bloombox.schema.partner.integrations.PartnerIntegrationSettings.GenericEntry\x12K\n\x06gsuite\x18\n \x01(\x0b\x32;.bloombox.schema.partner.integrations.gsuite.GSuiteSettings\x1ap\n\x0cGenericEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12O\n\x05value\x18\x02 \x01(\x0b\x32@.bloombox.schema.partner.integrations.GenericIntegrationSettings:\x02\x38\x01*\x95\x01\n\x12IntegrationPartner\x12\x0c\n\x08INTERNAL\x10\x00\x12\x0b\n\x07SALSIFY\x10\x01\x12\x08\n\x04KEEN\x10\x02\x12\r\n\tGREENBITS\x10\x03\x12\r\n\tMAILCHIMP\x10\x04\x12\x0c\n\x08SENDGRID\x10\x05\x12\n\n\x06TWILIO\x10\x06\x12\x0b\n\x07ONFLEET\x10\x07\x12\n\n\x06GSUITE\x10\x08\x12\t\n\x05TREEZ\x10\tB3\n\'io.bloombox.schema.partner.integrationsH\x01P\x00\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[temporal_dot_Instant__pb2.DESCRIPTOR,partner_dot_integrations_dot_TreezSettings__pb2.DESCRIPTOR,partner_dot_integrations_dot_GSuiteSettings__pb2.DESCRIPTOR,partner_dot_integrations_dot_TwilioSettings__pb2.DESCRIPTOR,partner_dot_integrations_dot_OnFleetSettings__pb2.DESCRIPTOR,partner_dot_integrations_dot_SendgridSettings__pb2.DESCRIPTOR,partner_dot_integrations_dot_MailchimpSettings__pb2.DESCRIPTOR,partner_dot_integrations_dot_GreenbitsSettings__pb2.DESCRIPTOR,])

_INTEGRATIONPARTNER = _descriptor.EnumDescriptor(
  name='IntegrationPartner',
  full_name='bloombox.schema.partner.integrations.IntegrationPartner',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INTERNAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SALSIFY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEEN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREENBITS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAILCHIMP', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENDGRID', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWILIO', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONFLEET', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GSUITE', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TREEZ', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1826,
  serialized_end=1975,
)
_sym_db.RegisterEnumDescriptor(_INTEGRATIONPARTNER)

IntegrationPartner = enum_type_wrapper.EnumTypeWrapper(_INTEGRATIONPARTNER)
INTERNAL = 0
SALSIFY = 1
KEEN = 2
GREENBITS = 3
MAILCHIMP = 4
SENDGRID = 5
TWILIO = 6
ONFLEET = 7
GSUITE = 8
TREEZ = 9



_GENERICINTEGRATIONSETTINGS = _descriptor.Descriptor(
  name='GenericIntegrationSettings',
  full_name='bloombox.schema.partner.integrations.GenericIntegrationSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partner', full_name='bloombox.schema.partner.integrations.GenericIntegrationSettings.partner', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='bloombox.schema.partner.integrations.GenericIntegrationSettings.enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fully_setup', full_name='bloombox.schema.partner.integrations.GenericIntegrationSettings.fully_setup', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_tested', full_name='bloombox.schema.partner.integrations.GenericIntegrationSettings.last_tested', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=422,
  serialized_end=616,
)


_LOCATIONINTEGRATIONSETTINGS_GENERICENTRY = _descriptor.Descriptor(
  name='GenericEntry',
  full_name='bloombox.schema.partner.integrations.LocationIntegrationSettings.GenericEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bloombox.schema.partner.integrations.LocationIntegrationSettings.GenericEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='bloombox.schema.partner.integrations.LocationIntegrationSettings.GenericEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1313,
  serialized_end=1425,
)

_LOCATIONINTEGRATIONSETTINGS = _descriptor.Descriptor(
  name='LocationIntegrationSettings',
  full_name='bloombox.schema.partner.integrations.LocationIntegrationSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='integrations', full_name='bloombox.schema.partner.integrations.LocationIntegrationSettings.integrations', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generic', full_name='bloombox.schema.partner.integrations.LocationIntegrationSettings.generic', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='greenbits', full_name='bloombox.schema.partner.integrations.LocationIntegrationSettings.greenbits', index=2,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mailchimp', full_name='bloombox.schema.partner.integrations.LocationIntegrationSettings.mailchimp', index=3,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sendgrid', full_name='bloombox.schema.partner.integrations.LocationIntegrationSettings.sendgrid', index=4,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='twilio', full_name='bloombox.schema.partner.integrations.LocationIntegrationSettings.twilio', index=5,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='onfleet', full_name='bloombox.schema.partner.integrations.LocationIntegrationSettings.onfleet', index=6,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='treez', full_name='bloombox.schema.partner.integrations.LocationIntegrationSettings.treez', index=7,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOCATIONINTEGRATIONSETTINGS_GENERICENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=619,
  serialized_end=1425,
)


_PARTNERINTEGRATIONSETTINGS_GENERICENTRY = _descriptor.Descriptor(
  name='GenericEntry',
  full_name='bloombox.schema.partner.integrations.PartnerIntegrationSettings.GenericEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bloombox.schema.partner.integrations.PartnerIntegrationSettings.GenericEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='bloombox.schema.partner.integrations.PartnerIntegrationSettings.GenericEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1313,
  serialized_end=1425,
)

_PARTNERINTEGRATIONSETTINGS = _descriptor.Descriptor(
  name='PartnerIntegrationSettings',
  full_name='bloombox.schema.partner.integrations.PartnerIntegrationSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='integrations', full_name='bloombox.schema.partner.integrations.PartnerIntegrationSettings.integrations', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generic', full_name='bloombox.schema.partner.integrations.PartnerIntegrationSettings.generic', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gsuite', full_name='bloombox.schema.partner.integrations.PartnerIntegrationSettings.gsuite', index=2,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PARTNERINTEGRATIONSETTINGS_GENERICENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1428,
  serialized_end=1823,
)

_GENERICINTEGRATIONSETTINGS.fields_by_name['partner'].enum_type = _INTEGRATIONPARTNER
_GENERICINTEGRATIONSETTINGS.fields_by_name['last_tested'].message_type = temporal_dot_Instant__pb2._INSTANT
_LOCATIONINTEGRATIONSETTINGS_GENERICENTRY.fields_by_name['value'].message_type = _GENERICINTEGRATIONSETTINGS
_LOCATIONINTEGRATIONSETTINGS_GENERICENTRY.containing_type = _LOCATIONINTEGRATIONSETTINGS
_LOCATIONINTEGRATIONSETTINGS.fields_by_name['integrations'].enum_type = _INTEGRATIONPARTNER
_LOCATIONINTEGRATIONSETTINGS.fields_by_name['generic'].message_type = _LOCATIONINTEGRATIONSETTINGS_GENERICENTRY
_LOCATIONINTEGRATIONSETTINGS.fields_by_name['greenbits'].message_type = partner_dot_integrations_dot_GreenbitsSettings__pb2._GREENBITSSETTINGS
_LOCATIONINTEGRATIONSETTINGS.fields_by_name['mailchimp'].message_type = partner_dot_integrations_dot_MailchimpSettings__pb2._MAILCHIMPSETTINGS
_LOCATIONINTEGRATIONSETTINGS.fields_by_name['sendgrid'].message_type = partner_dot_integrations_dot_SendgridSettings__pb2._SENDGRIDSETTINGS
_LOCATIONINTEGRATIONSETTINGS.fields_by_name['twilio'].message_type = partner_dot_integrations_dot_TwilioSettings__pb2._TWILIOSETTINGS
_LOCATIONINTEGRATIONSETTINGS.fields_by_name['onfleet'].message_type = partner_dot_integrations_dot_OnFleetSettings__pb2._ONFLEETSETTINGS
_LOCATIONINTEGRATIONSETTINGS.fields_by_name['treez'].message_type = partner_dot_integrations_dot_TreezSettings__pb2._TREEZSETTINGS
_PARTNERINTEGRATIONSETTINGS_GENERICENTRY.fields_by_name['value'].message_type = _GENERICINTEGRATIONSETTINGS
_PARTNERINTEGRATIONSETTINGS_GENERICENTRY.containing_type = _PARTNERINTEGRATIONSETTINGS
_PARTNERINTEGRATIONSETTINGS.fields_by_name['integrations'].enum_type = _INTEGRATIONPARTNER
_PARTNERINTEGRATIONSETTINGS.fields_by_name['generic'].message_type = _PARTNERINTEGRATIONSETTINGS_GENERICENTRY
_PARTNERINTEGRATIONSETTINGS.fields_by_name['gsuite'].message_type = partner_dot_integrations_dot_GSuiteSettings__pb2._GSUITESETTINGS
DESCRIPTOR.message_types_by_name['GenericIntegrationSettings'] = _GENERICINTEGRATIONSETTINGS
DESCRIPTOR.message_types_by_name['LocationIntegrationSettings'] = _LOCATIONINTEGRATIONSETTINGS
DESCRIPTOR.message_types_by_name['PartnerIntegrationSettings'] = _PARTNERINTEGRATIONSETTINGS
DESCRIPTOR.enum_types_by_name['IntegrationPartner'] = _INTEGRATIONPARTNER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenericIntegrationSettings = _reflection.GeneratedProtocolMessageType('GenericIntegrationSettings', (_message.Message,), dict(
  DESCRIPTOR = _GENERICINTEGRATIONSETTINGS,
  __module__ = 'partner.integrations.IntegrationSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.integrations.GenericIntegrationSettings)
  ))
_sym_db.RegisterMessage(GenericIntegrationSettings)

LocationIntegrationSettings = _reflection.GeneratedProtocolMessageType('LocationIntegrationSettings', (_message.Message,), dict(

  GenericEntry = _reflection.GeneratedProtocolMessageType('GenericEntry', (_message.Message,), dict(
    DESCRIPTOR = _LOCATIONINTEGRATIONSETTINGS_GENERICENTRY,
    __module__ = 'partner.integrations.IntegrationSettings_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.partner.integrations.LocationIntegrationSettings.GenericEntry)
    ))
  ,
  DESCRIPTOR = _LOCATIONINTEGRATIONSETTINGS,
  __module__ = 'partner.integrations.IntegrationSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.integrations.LocationIntegrationSettings)
  ))
_sym_db.RegisterMessage(LocationIntegrationSettings)
_sym_db.RegisterMessage(LocationIntegrationSettings.GenericEntry)

PartnerIntegrationSettings = _reflection.GeneratedProtocolMessageType('PartnerIntegrationSettings', (_message.Message,), dict(

  GenericEntry = _reflection.GeneratedProtocolMessageType('GenericEntry', (_message.Message,), dict(
    DESCRIPTOR = _PARTNERINTEGRATIONSETTINGS_GENERICENTRY,
    __module__ = 'partner.integrations.IntegrationSettings_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.partner.integrations.PartnerIntegrationSettings.GenericEntry)
    ))
  ,
  DESCRIPTOR = _PARTNERINTEGRATIONSETTINGS,
  __module__ = 'partner.integrations.IntegrationSettings_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.partner.integrations.PartnerIntegrationSettings)
  ))
_sym_db.RegisterMessage(PartnerIntegrationSettings)
_sym_db.RegisterMessage(PartnerIntegrationSettings.GenericEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\'io.bloombox.schema.partner.integrationsH\001P\000\242\002\003BBS'))
_LOCATIONINTEGRATIONSETTINGS_GENERICENTRY.has_options = True
_LOCATIONINTEGRATIONSETTINGS_GENERICENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_PARTNERINTEGRATIONSETTINGS_GENERICENTRY.has_options = True
_PARTNERINTEGRATIONSETTINGS_GENERICENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
