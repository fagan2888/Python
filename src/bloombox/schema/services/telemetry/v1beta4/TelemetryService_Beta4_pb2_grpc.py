# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from telemetry.v1beta4 import GenericEvents_Beta4_pb2 as telemetry_dot_v1beta4_dot_GenericEvents__Beta4__pb2
from telemetry.v1beta4 import TelemetryService_Beta4_pb2 as telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2


class EventTelemetryStub(object):
  """Provides support for transmission of operational and experiential telemetry data from first and second-party devices.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Ping = channel.unary_unary(
        '/bloombox.schema.services.telemetry.v1beta4.EventTelemetry/Ping',
        request_serializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.TelemetryPing.Request.SerializeToString,
        response_deserializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.TelemetryPing.Response.FromString,
        )
    self.Event = channel.unary_unary(
        '/bloombox.schema.services.telemetry.v1beta4.EventTelemetry/Event',
        request_serializer=telemetry_dot_v1beta4_dot_GenericEvents__Beta4__pb2.Event.Request.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Batch = channel.unary_unary(
        '/bloombox.schema.services.telemetry.v1beta4.EventTelemetry/Batch',
        request_serializer=telemetry_dot_v1beta4_dot_GenericEvents__Beta4__pb2.Event.BatchRequest.SerializeToString,
        response_deserializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.TelemetryResponse.FromString,
        )
    self.Error = channel.unary_unary(
        '/bloombox.schema.services.telemetry.v1beta4.EventTelemetry/Error',
        request_serializer=telemetry_dot_v1beta4_dot_GenericEvents__Beta4__pb2.Exception.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class EventTelemetryServicer(object):
  """Provides support for transmission of operational and experiential telemetry data from first and second-party devices.
  """

  def Ping(self, request, context):
    """Ping the server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Event(self, request, context):
    """Submit a generic event.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Batch(self, request, context):
    """Submit one or more generic events via the batch interface.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Error(self, request, context):
    """Submit one or more exception events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EventTelemetryServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.TelemetryPing.Request.FromString,
          response_serializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.TelemetryPing.Response.SerializeToString,
      ),
      'Event': grpc.unary_unary_rpc_method_handler(
          servicer.Event,
          request_deserializer=telemetry_dot_v1beta4_dot_GenericEvents__Beta4__pb2.Event.Request.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Batch': grpc.unary_unary_rpc_method_handler(
          servicer.Batch,
          request_deserializer=telemetry_dot_v1beta4_dot_GenericEvents__Beta4__pb2.Event.BatchRequest.FromString,
          response_serializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.TelemetryResponse.SerializeToString,
      ),
      'Error': grpc.unary_unary_rpc_method_handler(
          servicer.Error,
          request_deserializer=telemetry_dot_v1beta4_dot_GenericEvents__Beta4__pb2.Exception.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'bloombox.schema.services.telemetry.v1beta4.EventTelemetry', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class CommercialTelemetryStub(object):
  """Provides support for tailored analytics payloads w.r.t. interactions between end-users and commercial models, like
  menu sections, products, and user orders.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Impression = channel.unary_unary(
        '/bloombox.schema.services.telemetry.v1beta4.CommercialTelemetry/Impression',
        request_serializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.CommercialEvent.Impression.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.View = channel.unary_unary(
        '/bloombox.schema.services.telemetry.v1beta4.CommercialTelemetry/View',
        request_serializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.CommercialEvent.View.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Action = channel.unary_unary(
        '/bloombox.schema.services.telemetry.v1beta4.CommercialTelemetry/Action',
        request_serializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.CommercialEvent.Action.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class CommercialTelemetryServicer(object):
  """Provides support for tailored analytics payloads w.r.t. interactions between end-users and commercial models, like
  menu sections, products, and user orders.
  """

  def Impression(self, request, context):
    """Register that a menu section was presented to a user, regardless of whether they acted on it or not.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def View(self, request, context):
    """Register that a menu section was viewed, browsed-to, or otherwise served to a user.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Action(self, request, context):
    """Register that an end-user elected to take action within a section in some way.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CommercialTelemetryServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Impression': grpc.unary_unary_rpc_method_handler(
          servicer.Impression,
          request_deserializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.CommercialEvent.Impression.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'View': grpc.unary_unary_rpc_method_handler(
          servicer.View,
          request_deserializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.CommercialEvent.View.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Action': grpc.unary_unary_rpc_method_handler(
          servicer.Action,
          request_deserializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.CommercialEvent.Action.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'bloombox.schema.services.telemetry.v1beta4.CommercialTelemetry', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class IdentityTelemetryStub(object):
  """Provides support for recording telemetry information about user events and actions related to their own identity,
  account, profile, preferences, and so on.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Action = channel.unary_unary(
        '/bloombox.schema.services.telemetry.v1beta4.IdentityTelemetry/Action',
        request_serializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.IdentityEvent.Action.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class IdentityTelemetryServicer(object):
  """Provides support for recording telemetry information about user events and actions related to their own identity,
  account, profile, preferences, and so on.
  """

  def Action(self, request, context):
    """Register affirmative action taken by an end-user on their own account or identity.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IdentityTelemetryServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Action': grpc.unary_unary_rpc_method_handler(
          servicer.Action,
          request_deserializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.IdentityEvent.Action.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'bloombox.schema.services.telemetry.v1beta4.IdentityTelemetry', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class SearchTelemetryStub(object):
  """Provides support for recording telemetry information specific to user-submitted search queries, the resultsets they
  produce, and the user's response to those resultsets.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Query = channel.unary_unary(
        '/bloombox.schema.services.telemetry.v1beta4.SearchTelemetry/Query',
        request_serializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.SearchEvent.Query.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Result = channel.unary_unary(
        '/bloombox.schema.services.telemetry.v1beta4.SearchTelemetry/Result',
        request_serializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.SearchEvent.Result.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class SearchTelemetryServicer(object):
  """Provides support for recording telemetry information specific to user-submitted search queries, the resultsets they
  produce, and the user's response to those resultsets.
  """

  def Query(self, request, context):
    """Record a search performed by a user.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Result(self, request, context):
    """Record a search result selected by a user after performing a search.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SearchTelemetryServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Query': grpc.unary_unary_rpc_method_handler(
          servicer.Query,
          request_deserializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.SearchEvent.Query.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Result': grpc.unary_unary_rpc_method_handler(
          servicer.Result,
          request_deserializer=telemetry_dot_v1beta4_dot_TelemetryService__Beta4__pb2.SearchEvent.Result.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'bloombox.schema.services.telemetry.v1beta4.SearchTelemetry', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
