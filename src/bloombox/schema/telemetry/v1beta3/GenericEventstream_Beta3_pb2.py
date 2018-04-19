# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: telemetry/v1beta3/GenericEventstream_Beta3.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bq_field_pb2 as bq__field__pb2
import bq_table_pb2 as bq__table__pb2
from analytics import Context_pb2 as analytics_dot_Context__pb2
from analytics.stats import SessionStats_pb2 as analytics_dot_stats_dot_SessionStats__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='telemetry/v1beta3/GenericEventstream_Beta3.proto',
  package='bloombox.tables.telemetry.v1beta3',
  syntax='proto3',
  serialized_pb=_b('\n0telemetry/v1beta3/GenericEventstream_Beta3.proto\x12!bloombox.tables.telemetry.v1beta3\x1a\x0e\x62q_field.proto\x1a\x0e\x62q_table.proto\x1a\x17\x61nalytics/Context.proto\x1a\"analytics/stats/SessionStats.proto\"\xe3\x04\n\x06\x45vents\x12\x36\n\x04uuid\x18\x01 \x01(\tB(\xf0?\x01\x8a@\"Event UUID. Generated upon ingest.\x12\x9a\x01\n\x06timing\x18\x02 \x01(\x0b\x32(.bloombox.schema.analytics.EventPositionB`\xf0?\x01\x8a@ZTimestamps related to this event, or, the subject event\'s temporal positioning parameters.\x12\xc4\x01\n\x06\x61\x63tors\x18\x03 \x01(\x0b\x32&.bloombox.schema.analytics.EventActorsB\x8b\x01\x80@\x01\x8a@\x84\x01Inflated records contextually tied to this event, such as the user, device, partner, and location that were active when it was sent.\x12\x8c\x01\n\x07\x63ontext\x18\x04 \x01(\x0b\x32\".bloombox.schema.analytics.ContextBW\xf0?\x01\x8a@QEvent context, specifying the circumstances under which this event was submitted.\x12\"\n\x07payload\x18\x05 \x01(\tB\x11\x8a@\x0e\x45vent payload.:\n\xea?\x07generic\"\xa3\x02\n\tRawStream\x12\x36\n\x04uuid\x18\x01 \x01(\tB(\xf0?\x01\x8a@\"Event UUID. Generated upon ingest.\x12\x9a\x01\n\x06timing\x18\x02 \x01(\x0b\x32(.bloombox.schema.analytics.EventPositionB`\xf0?\x01\x8a@ZTimestamps related to this event, or, the subject event\'s temporal positioning parameters.\x12\x31\n\x03raw\x18\x03 \x01(\tB$\xf0?\x01\x8a@\x1eRaw event, serialized as JSON.:\x0e\xea?\x0b\x65ventstream\"\xa5\x01\n\x08Sessions\x12$\n\x02id\x18\x01 \x01(\tB\x18\xf0?\x01\x8a@\x12Unique session ID.\x12\x66\n\x05stats\x18\x04 \x01(\x0b\x32-.bloombox.schema.analytics.stats.SessionStatsB(\xf0?\x01\x8a@\"Pre-calculated session statistics.:\x0b\xea?\x08sessionsBN\n+io.bloombox.schema.tables.telemetry.v1beta3B\x18GenericEventstream_Beta3H\x01P\x00\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[bq__field__pb2.DESCRIPTOR,bq__table__pb2.DESCRIPTOR,analytics_dot_Context__pb2.DESCRIPTOR,analytics_dot_stats_dot_SessionStats__pb2.DESCRIPTOR,])




_EVENTS = _descriptor.Descriptor(
  name='Events',
  full_name='bloombox.tables.telemetry.v1beta3.Events',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='bloombox.tables.telemetry.v1beta3.Events.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\"Event UUID. Generated upon ingest.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timing', full_name='bloombox.tables.telemetry.v1beta3.Events.timing', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@ZTimestamps related to this event, or, the subject event\'s temporal positioning parameters.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actors', full_name='bloombox.tables.telemetry.v1beta3.Events.actors', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200@\001\212@\204\001Inflated records contextually tied to this event, such as the user, device, partner, and location that were active when it was sent.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='bloombox.tables.telemetry.v1beta3.Events.context', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@QEvent context, specifying the circumstances under which this event was submitted.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='bloombox.tables.telemetry.v1beta3.Events.payload', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\016Event payload.')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\352?\007generic')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=792,
)


_RAWSTREAM = _descriptor.Descriptor(
  name='RawStream',
  full_name='bloombox.tables.telemetry.v1beta3.RawStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='bloombox.tables.telemetry.v1beta3.RawStream.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\"Event UUID. Generated upon ingest.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timing', full_name='bloombox.tables.telemetry.v1beta3.RawStream.timing', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@ZTimestamps related to this event, or, the subject event\'s temporal positioning parameters.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw', full_name='bloombox.tables.telemetry.v1beta3.RawStream.raw', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\036Raw event, serialized as JSON.')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\352?\013eventstream')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=795,
  serialized_end=1086,
)


_SESSIONS = _descriptor.Descriptor(
  name='Sessions',
  full_name='bloombox.tables.telemetry.v1beta3.Sessions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bloombox.tables.telemetry.v1beta3.Sessions.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\022Unique session ID.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='bloombox.tables.telemetry.v1beta3.Sessions.stats', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\"Pre-calculated session statistics.')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\352?\010sessions')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1089,
  serialized_end=1254,
)

_EVENTS.fields_by_name['timing'].message_type = analytics_dot_Context__pb2._EVENTPOSITION
_EVENTS.fields_by_name['actors'].message_type = analytics_dot_Context__pb2._EVENTACTORS
_EVENTS.fields_by_name['context'].message_type = analytics_dot_Context__pb2._CONTEXT
_RAWSTREAM.fields_by_name['timing'].message_type = analytics_dot_Context__pb2._EVENTPOSITION
_SESSIONS.fields_by_name['stats'].message_type = analytics_dot_stats_dot_SessionStats__pb2._SESSIONSTATS
DESCRIPTOR.message_types_by_name['Events'] = _EVENTS
DESCRIPTOR.message_types_by_name['RawStream'] = _RAWSTREAM
DESCRIPTOR.message_types_by_name['Sessions'] = _SESSIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Events = _reflection.GeneratedProtocolMessageType('Events', (_message.Message,), dict(
  DESCRIPTOR = _EVENTS,
  __module__ = 'telemetry.v1beta3.GenericEventstream_Beta3_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.tables.telemetry.v1beta3.Events)
  ))
_sym_db.RegisterMessage(Events)

RawStream = _reflection.GeneratedProtocolMessageType('RawStream', (_message.Message,), dict(
  DESCRIPTOR = _RAWSTREAM,
  __module__ = 'telemetry.v1beta3.GenericEventstream_Beta3_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.tables.telemetry.v1beta3.RawStream)
  ))
_sym_db.RegisterMessage(RawStream)

Sessions = _reflection.GeneratedProtocolMessageType('Sessions', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONS,
  __module__ = 'telemetry.v1beta3.GenericEventstream_Beta3_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.tables.telemetry.v1beta3.Sessions)
  ))
_sym_db.RegisterMessage(Sessions)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n+io.bloombox.schema.tables.telemetry.v1beta3B\030GenericEventstream_Beta3H\001P\000\370\001\001'))
_EVENTS.fields_by_name['uuid'].has_options = True
_EVENTS.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\"Event UUID. Generated upon ingest.'))
_EVENTS.fields_by_name['timing'].has_options = True
_EVENTS.fields_by_name['timing']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@ZTimestamps related to this event, or, the subject event\'s temporal positioning parameters.'))
_EVENTS.fields_by_name['actors'].has_options = True
_EVENTS.fields_by_name['actors']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200@\001\212@\204\001Inflated records contextually tied to this event, such as the user, device, partner, and location that were active when it was sent.'))
_EVENTS.fields_by_name['context'].has_options = True
_EVENTS.fields_by_name['context']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@QEvent context, specifying the circumstances under which this event was submitted.'))
_EVENTS.fields_by_name['payload'].has_options = True
_EVENTS.fields_by_name['payload']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\016Event payload.'))
_EVENTS.has_options = True
_EVENTS._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\352?\007generic'))
_RAWSTREAM.fields_by_name['uuid'].has_options = True
_RAWSTREAM.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\"Event UUID. Generated upon ingest.'))
_RAWSTREAM.fields_by_name['timing'].has_options = True
_RAWSTREAM.fields_by_name['timing']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@ZTimestamps related to this event, or, the subject event\'s temporal positioning parameters.'))
_RAWSTREAM.fields_by_name['raw'].has_options = True
_RAWSTREAM.fields_by_name['raw']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\036Raw event, serialized as JSON.'))
_RAWSTREAM.has_options = True
_RAWSTREAM._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\352?\013eventstream'))
_SESSIONS.fields_by_name['id'].has_options = True
_SESSIONS.fields_by_name['id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\022Unique session ID.'))
_SESSIONS.fields_by_name['stats'].has_options = True
_SESSIONS.fields_by_name['stats']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\"Pre-calculated session statistics.'))
_SESSIONS.has_options = True
_SESSIONS._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\352?\010sessions'))
# @@protoc_insertion_point(module_scope)
