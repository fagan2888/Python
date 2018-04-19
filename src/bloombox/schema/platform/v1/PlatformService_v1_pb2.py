# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: platform/v1/PlatformService_v1.proto

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


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_swagger.options import swagger_pb2 as protoc__gen__swagger_dot_options_dot_swagger__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='platform/v1/PlatformService_v1.proto',
  package='bloombox.schema.services.platform.v1',
  syntax='proto3',
  serialized_pb=_b('\n$platform/v1/PlatformService_v1.proto\x12$bloombox.schema.services.platform.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\x1a(protoc-gen-swagger/options/swagger.proto\"j\n\x04Ping\x1a\t\n\x07Request\x1aW\n\x08Response\x12K\n\x06status\x18\x01 \x01(\x0e\x32;.bloombox.schema.services.platform.v1.PlatformServiceStatus\"\'\n\x0bHealthcheck\x1a\x18\n\x07Request\x12\r\n\x05probe\x18\x01 \x01(\t\"|\n\rDomainResolve\x1a\x19\n\x07Request\x12\x0e\n\x06origin\x18\x01 \x01(\t\x1aP\n\x08Response\x12\x0f\n\x07partner\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x0e\n\x06\x61pikey\x18\x03 \x01(\t\x12\x11\n\tclient_id\x18\x04 \x01(\t*a\n\rPlatformError\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x18\n\x14SEARCH_NOT_AVAILABLE\x10\x01\x12\x12\n\x0eORIGIN_INVALID\x10\x02\x12\x14\n\x10ORIGIN_NOT_FOUND\x10\x03*G\n\x15PlatformServiceStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02UP\x10\x01\x12\x08\n\x04\x44OWN\x10\x02\x12\x0f\n\x0bMAINTENANCE\x10\x03\x32\xd8\x05\n\x08Platform\x12\xcf\x01\n\x04Ping\x12\x32.bloombox.schema.services.platform.v1.Ping.Request\x1a\x33.bloombox.schema.services.platform.v1.Ping.Response\"^\x82\xd3\xe4\x93\x02\x13\x12\x11/platform/v1/ping\x92\x41\x42\x12\x0cService Ping\x1a,Query for service uptime/maintenance status.*\x04Ping\x12\xcb\x01\n\x06Health\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x90\x01\x82\xd3\xe4\x93\x02\x15\x12\x13/platform/v1/health\x92\x41r\x12\x13Service Healthcheck\x1aNIf the service is running correctly, always responds with an empty HTTP200/OK.*\x0bHealthcheck\x12\xab\x02\n\x07Resolve\x12;.bloombox.schema.services.platform.v1.DomainResolve.Request\x1a<.bloombox.schema.services.platform.v1.DomainResolve.Response\"\xa4\x01\x82\xd3\xe4\x93\x02\x1e\x12\x1c/platform/v1/domain/{origin}\x92\x41}\x12\x0eResolve Domain\x1a\x62\x46or custom-hosting endpoints, given a web origin, resolve the owning partner and location account.*\x07ResolveB\xeb\x08\n\'io.bloombox.schema.services.platform.v1H\x01P\x01\xa2\x02\x03\x42\x42S\x92\x41\xb4\x08\x12\x66\n\x0cPlatform API\x1a\x19https://bloombox.io/terms\"7\n\x08\x42loombox\x12\x13https://bloombox.io\x1a\x16\x64\x65velopers@bloombox.io2\x02v1\x1a\x12\x61pi.bloombox.cloud*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonZ\xb8\x06\nd\n\x0b\x41piKeyParam\x12U\x08\x02\x12JParameter for identifying API key owned by the invoking project or system.\x1a\x03key \x01\nh\n\x0c\x41piKeyHeader\x12X\x08\x02\x12GHeader for identifying API key owned by the invoking project or system.\x1a\tX-API-Key \x01\n\xe5\x04\n\x06OAuth2\x12\xda\x04\x08\x03\x12]Bloombox Identity-powered OAuth2 access, authorized on behalf of an end-user or organization.(\x04\x32,https://authorize.bloombox.cloud/oauth2/auth:-https://authorize.bloombox.cloud/oauth2/tokenB\x97\x03\n1\n\x07offline\x12&Offline access to authorized user data\n9\n\x06openid\x12/OIDC (OpenID Connect) access for seamless logon\nE\n\x0cpartner:read\x12\x35Read access to a partner\'s profile and basic settings\nG\n\rpartner:write\x12\x36Write access to a partner\'s profile and basic settings\nV\n\rpartner:admin\x12\x45\x46ull administrative access rights to a partner\'s profile and settings\n?\n\x0eplatform:admin\x12-Platform-level internal administrative accessb#\n\x0f\n\x0b\x41piKeyParam\x12\x00\n\x10\n\x0c\x41piKeyHeader\x12\x00r/\n\rBloombox APIs\x12\x1ehttps://apidocs.bloombox.cloudb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_swagger__pb2.DESCRIPTOR,])

_PLATFORMERROR = _descriptor.EnumDescriptor(
  name='PlatformError',
  full_name='bloombox.schema.services.platform.v1.PlatformError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_ERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEARCH_NOT_AVAILABLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORIGIN_INVALID', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORIGIN_NOT_FOUND', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=454,
  serialized_end=551,
)
_sym_db.RegisterEnumDescriptor(_PLATFORMERROR)

PlatformError = enum_type_wrapper.EnumTypeWrapper(_PLATFORMERROR)
_PLATFORMSERVICESTATUS = _descriptor.EnumDescriptor(
  name='PlatformServiceStatus',
  full_name='bloombox.schema.services.platform.v1.PlatformServiceStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAINTENANCE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=553,
  serialized_end=624,
)
_sym_db.RegisterEnumDescriptor(_PLATFORMSERVICESTATUS)

PlatformServiceStatus = enum_type_wrapper.EnumTypeWrapper(_PLATFORMSERVICESTATUS)
NO_ERROR = 0
SEARCH_NOT_AVAILABLE = 1
ORIGIN_INVALID = 2
ORIGIN_NOT_FOUND = 3
UNKNOWN = 0
UP = 1
DOWN = 2
MAINTENANCE = 3



_PING_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bloombox.schema.services.platform.v1.Ping.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=187,
  serialized_end=196,
)

_PING_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='bloombox.schema.services.platform.v1.Ping.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bloombox.schema.services.platform.v1.Ping.Response.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=198,
  serialized_end=285,
)

_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='bloombox.schema.services.platform.v1.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_PING_REQUEST, _PING_RESPONSE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=285,
)


_HEALTHCHECK_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bloombox.schema.services.platform.v1.Healthcheck.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='probe', full_name='bloombox.schema.services.platform.v1.Healthcheck.Request.probe', index=0,
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
  serialized_start=302,
  serialized_end=326,
)

_HEALTHCHECK = _descriptor.Descriptor(
  name='Healthcheck',
  full_name='bloombox.schema.services.platform.v1.Healthcheck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_HEALTHCHECK_REQUEST, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=326,
)


_DOMAINRESOLVE_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bloombox.schema.services.platform.v1.DomainResolve.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='bloombox.schema.services.platform.v1.DomainResolve.Request.origin', index=0,
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
  serialized_start=345,
  serialized_end=370,
)

_DOMAINRESOLVE_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='bloombox.schema.services.platform.v1.DomainResolve.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partner', full_name='bloombox.schema.services.platform.v1.DomainResolve.Response.partner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='bloombox.schema.services.platform.v1.DomainResolve.Response.location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apikey', full_name='bloombox.schema.services.platform.v1.DomainResolve.Response.apikey', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='bloombox.schema.services.platform.v1.DomainResolve.Response.client_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=372,
  serialized_end=452,
)

_DOMAINRESOLVE = _descriptor.Descriptor(
  name='DomainResolve',
  full_name='bloombox.schema.services.platform.v1.DomainResolve',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_DOMAINRESOLVE_REQUEST, _DOMAINRESOLVE_RESPONSE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=452,
)

_PING_REQUEST.containing_type = _PING
_PING_RESPONSE.fields_by_name['status'].enum_type = _PLATFORMSERVICESTATUS
_PING_RESPONSE.containing_type = _PING
_HEALTHCHECK_REQUEST.containing_type = _HEALTHCHECK
_DOMAINRESOLVE_REQUEST.containing_type = _DOMAINRESOLVE
_DOMAINRESOLVE_RESPONSE.containing_type = _DOMAINRESOLVE
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Healthcheck'] = _HEALTHCHECK
DESCRIPTOR.message_types_by_name['DomainResolve'] = _DOMAINRESOLVE
DESCRIPTOR.enum_types_by_name['PlatformError'] = _PLATFORMERROR
DESCRIPTOR.enum_types_by_name['PlatformServiceStatus'] = _PLATFORMSERVICESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _PING_REQUEST,
    __module__ = 'platform.v1.PlatformService_v1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.platform.v1.Ping.Request)
    ))
  ,

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _PING_RESPONSE,
    __module__ = 'platform.v1.PlatformService_v1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.platform.v1.Ping.Response)
    ))
  ,
  DESCRIPTOR = _PING,
  __module__ = 'platform.v1.PlatformService_v1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.platform.v1.Ping)
  ))
_sym_db.RegisterMessage(Ping)
_sym_db.RegisterMessage(Ping.Request)
_sym_db.RegisterMessage(Ping.Response)

Healthcheck = _reflection.GeneratedProtocolMessageType('Healthcheck', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _HEALTHCHECK_REQUEST,
    __module__ = 'platform.v1.PlatformService_v1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.platform.v1.Healthcheck.Request)
    ))
  ,
  DESCRIPTOR = _HEALTHCHECK,
  __module__ = 'platform.v1.PlatformService_v1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.platform.v1.Healthcheck)
  ))
_sym_db.RegisterMessage(Healthcheck)
_sym_db.RegisterMessage(Healthcheck.Request)

DomainResolve = _reflection.GeneratedProtocolMessageType('DomainResolve', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _DOMAINRESOLVE_REQUEST,
    __module__ = 'platform.v1.PlatformService_v1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.platform.v1.DomainResolve.Request)
    ))
  ,

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _DOMAINRESOLVE_RESPONSE,
    __module__ = 'platform.v1.PlatformService_v1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.platform.v1.DomainResolve.Response)
    ))
  ,
  DESCRIPTOR = _DOMAINRESOLVE,
  __module__ = 'platform.v1.PlatformService_v1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.platform.v1.DomainResolve)
  ))
_sym_db.RegisterMessage(DomainResolve)
_sym_db.RegisterMessage(DomainResolve.Request)
_sym_db.RegisterMessage(DomainResolve.Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\'io.bloombox.schema.services.platform.v1H\001P\001\242\002\003BBS\222A\264\010\022f\n\014Platform API\032\031https://bloombox.io/terms\"7\n\010Bloombox\022\023https://bloombox.io\032\026developers@bloombox.io2\002v1\032\022api.bloombox.cloud*\001\0022\020application/json:\020application/jsonZ\270\006\nd\n\013ApiKeyParam\022U\010\002\022JParameter for identifying API key owned by the invoking project or system.\032\003key \001\nh\n\014ApiKeyHeader\022X\010\002\022GHeader for identifying API key owned by the invoking project or system.\032\tX-API-Key \001\n\345\004\n\006OAuth2\022\332\004\010\003\022]Bloombox Identity-powered OAuth2 access, authorized on behalf of an end-user or organization.(\0042,https://authorize.bloombox.cloud/oauth2/auth:-https://authorize.bloombox.cloud/oauth2/tokenB\227\003\n1\n\007offline\022&Offline access to authorized user data\n9\n\006openid\022/OIDC (OpenID Connect) access for seamless logon\nE\n\014partner:read\0225Read access to a partner\'s profile and basic settings\nG\n\rpartner:write\0226Write access to a partner\'s profile and basic settings\nV\n\rpartner:admin\022EFull administrative access rights to a partner\'s profile and settings\n?\n\016platform:admin\022-Platform-level internal administrative accessb#\n\017\n\013ApiKeyParam\022\000\n\020\n\014ApiKeyHeader\022\000r/\n\rBloombox APIs\022\036https://apidocs.bloombox.cloud'))

_PLATFORM = _descriptor.ServiceDescriptor(
  name='Platform',
  full_name='bloombox.schema.services.platform.v1.Platform',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=627,
  serialized_end=1355,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='bloombox.schema.services.platform.v1.Platform.Ping',
    index=0,
    containing_service=None,
    input_type=_PING_REQUEST,
    output_type=_PING_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\023\022\021/platform/v1/ping\222AB\022\014Service Ping\032,Query for service uptime/maintenance status.*\004Ping')),
  ),
  _descriptor.MethodDescriptor(
    name='Health',
    full_name='bloombox.schema.services.platform.v1.Platform.Health',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\025\022\023/platform/v1/health\222Ar\022\023Service Healthcheck\032NIf the service is running correctly, always responds with an empty HTTP200/OK.*\013Healthcheck')),
  ),
  _descriptor.MethodDescriptor(
    name='Resolve',
    full_name='bloombox.schema.services.platform.v1.Platform.Resolve',
    index=2,
    containing_service=None,
    input_type=_DOMAINRESOLVE_REQUEST,
    output_type=_DOMAINRESOLVE_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\036\022\034/platform/v1/domain/{origin}\222A}\022\016Resolve Domain\032bFor custom-hosting endpoints, given a web origin, resolve the owning partner and location account.*\007Resolve')),
  ),
])
_sym_db.RegisterServiceDescriptor(_PLATFORM)

DESCRIPTOR.services_by_name['Platform'] = _PLATFORM

# @@protoc_insertion_point(module_scope)