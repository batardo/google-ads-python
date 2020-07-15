# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/services/change_status_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v4.proto.resources import change_status_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_change__status__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/services/change_status_service.proto',
  package='google.ads.googleads.v4.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v4.servicesB\030ChangeStatusServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V4.Services\312\002 Google\\Ads\\GoogleAds\\V4\\Services\352\002$Google::Ads::GoogleAds::V4::Services'),
  serialized_pb=_b('\nBgoogle/ads/googleads_v4/proto/services/change_status_service.proto\x12 google.ads.googleads.v4.services\x1a;google/ads/googleads_v4/proto/resources/change_status.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"^\n\x16GetChangeStatusRequest\x12\x44\n\rresource_name\x18\x01 \x01(\tB-\xe0\x41\x02\xfa\x41\'\n%googleads.googleapis.com/ChangeStatus2\xf9\x01\n\x13\x43hangeStatusService\x12\xc4\x01\n\x0fGetChangeStatus\x12\x38.google.ads.googleads.v4.services.GetChangeStatusRequest\x1a/.google.ads.googleads.v4.resources.ChangeStatus\"F\x82\xd3\xe4\x93\x02\x30\x12./v4/{resource_name=customers/*/changeStatus/*}\xda\x41\rresource_name\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xff\x01\n$com.google.ads.googleads.v4.servicesB\x18\x43hangeStatusServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V4.Services\xca\x02 Google\\Ads\\GoogleAds\\V4\\Services\xea\x02$Google::Ads::GoogleAds::V4::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_change__status__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GETCHANGESTATUSREQUEST = _descriptor.Descriptor(
  name='GetChangeStatusRequest',
  full_name='google.ads.googleads.v4.services.GetChangeStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.services.GetChangeStatusRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002\372A\'\n%googleads.googleapis.com/ChangeStatus'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=374,
)

DESCRIPTOR.message_types_by_name['GetChangeStatusRequest'] = _GETCHANGESTATUSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetChangeStatusRequest = _reflection.GeneratedProtocolMessageType('GetChangeStatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCHANGESTATUSREQUEST,
  __module__ = 'google.ads.googleads_v4.proto.services.change_status_service_pb2'
  ,
  __doc__ = """Request message for
  '[ChangeStatusService.GetChangeStatus][google.ads.googleads.v4.services.ChangeStatusService.GetChangeStatus]'.
  
  
  Attributes:
      resource_name:
          Required. The resource name of the change status to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.GetChangeStatusRequest)
  ))
_sym_db.RegisterMessage(GetChangeStatusRequest)


DESCRIPTOR._options = None
_GETCHANGESTATUSREQUEST.fields_by_name['resource_name']._options = None

_CHANGESTATUSSERVICE = _descriptor.ServiceDescriptor(
  name='ChangeStatusService',
  full_name='google.ads.googleads.v4.services.ChangeStatusService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=377,
  serialized_end=626,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetChangeStatus',
    full_name='google.ads.googleads.v4.services.ChangeStatusService.GetChangeStatus',
    index=0,
    containing_service=None,
    input_type=_GETCHANGESTATUSREQUEST,
    output_type=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_change__status__pb2._CHANGESTATUS,
    serialized_options=_b('\202\323\344\223\0020\022./v4/{resource_name=customers/*/changeStatus/*}\332A\rresource_name'),
  ),
])
_sym_db.RegisterServiceDescriptor(_CHANGESTATUSSERVICE)

DESCRIPTOR.services_by_name['ChangeStatusService'] = _CHANGESTATUSSERVICE

# @@protoc_insertion_point(module_scope)
