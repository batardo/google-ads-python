# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/resources/campaign_extension_setting.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v4.proto.enums import extension_setting_device_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_extension__setting__device__pb2
from google.ads.google_ads.v4.proto.enums import extension_type_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_extension__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/resources/campaign_extension_setting.proto',
  package='google.ads.googleads.v4.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v4.resourcesB\035CampaignExtensionSettingProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V4.Resources\312\002!Google\\Ads\\GoogleAds\\V4\\Resources\352\002%Google::Ads::GoogleAds::V4::Resources'),
  serialized_pb=_b('\nHgoogle/ads/googleads_v4/proto/resources/campaign_extension_setting.proto\x12!google.ads.googleads.v4.resources\x1a\x42google/ads/googleads_v4/proto/enums/extension_setting_device.proto\x1a\x38google/ads/googleads_v4/proto/enums/extension_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xfa\x04\n\x18\x43\x61mpaignExtensionSetting\x12P\n\rresource_name\x18\x01 \x01(\tB9\xe0\x41\x05\xfa\x41\x33\n1googleads.googleapis.com/CampaignExtensionSetting\x12[\n\x0e\x65xtension_type\x18\x02 \x01(\x0e\x32>.google.ads.googleads.v4.enums.ExtensionTypeEnum.ExtensionTypeB\x03\xe0\x41\x05\x12Y\n\x08\x63\x61mpaign\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueB)\xe0\x41\x05\xfa\x41#\n!googleads.googleapis.com/Campaign\x12k\n\x14\x65xtension_feed_items\x18\x04 \x03(\x0b\x32\x1c.google.protobuf.StringValueB/\xfa\x41,\n*googleads.googleapis.com/ExtensionFeedItem\x12`\n\x06\x64\x65vice\x18\x05 \x01(\x0e\x32P.google.ads.googleads.v4.enums.ExtensionSettingDeviceEnum.ExtensionSettingDevice:\x84\x01\xea\x41\x80\x01\n1googleads.googleapis.com/CampaignExtensionSetting\x12Kcustomers/{customer}/campaignExtensionSettings/{campaign_extension_setting}B\x8a\x02\n%com.google.ads.googleads.v4.resourcesB\x1d\x43\x61mpaignExtensionSettingProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V4.Resources\xca\x02!Google\\Ads\\GoogleAds\\V4\\Resources\xea\x02%Google::Ads::GoogleAds::V4::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_extension__setting__device__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_extension__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CAMPAIGNEXTENSIONSETTING = _descriptor.Descriptor(
  name='CampaignExtensionSetting',
  full_name='google.ads.googleads.v4.resources.CampaignExtensionSetting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.resources.CampaignExtensionSetting.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005\372A3\n1googleads.googleapis.com/CampaignExtensionSetting'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension_type', full_name='google.ads.googleads.v4.resources.CampaignExtensionSetting.extension_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v4.resources.CampaignExtensionSetting.campaign', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005\372A#\n!googleads.googleapis.com/Campaign'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension_feed_items', full_name='google.ads.googleads.v4.resources.CampaignExtensionSetting.extension_feed_items', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372A,\n*googleads.googleapis.com/ExtensionFeedItem'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='google.ads.googleads.v4.resources.CampaignExtensionSetting.device', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352A\200\001\n1googleads.googleapis.com/CampaignExtensionSetting\022Kcustomers/{customer}/campaignExtensionSettings/{campaign_extension_setting}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=360,
  serialized_end=994,
)

_CAMPAIGNEXTENSIONSETTING.fields_by_name['extension_type'].enum_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_extension__type__pb2._EXTENSIONTYPEENUM_EXTENSIONTYPE
_CAMPAIGNEXTENSIONSETTING.fields_by_name['campaign'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNEXTENSIONSETTING.fields_by_name['extension_feed_items'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNEXTENSIONSETTING.fields_by_name['device'].enum_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_enums_dot_extension__setting__device__pb2._EXTENSIONSETTINGDEVICEENUM_EXTENSIONSETTINGDEVICE
DESCRIPTOR.message_types_by_name['CampaignExtensionSetting'] = _CAMPAIGNEXTENSIONSETTING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignExtensionSetting = _reflection.GeneratedProtocolMessageType('CampaignExtensionSetting', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNEXTENSIONSETTING,
  __module__ = 'google.ads.googleads_v4.proto.resources.campaign_extension_setting_pb2'
  ,
  __doc__ = """A campaign extension setting.
  
  
  Attributes:
      resource_name:
          Immutable. The resource name of the campaign extension
          setting. CampaignExtensionSetting resource names have the
          form:  ``customers/{customer_id}/campaignExtensionSettings/{ca
          mpaign_id}~{extension_type}``
      extension_type:
          Immutable. The extension type of the customer extension
          setting.
      campaign:
          Immutable. The resource name of the campaign. The linked
          extension feed items will serve under this campaign. Campaign
          resource names have the form:
          ``customers/{customer_id}/campaigns/{campaign_id}``
      extension_feed_items:
          The resource names of the extension feed items to serve under
          the campaign. ExtensionFeedItem resource names have the form:
          ``customers/{customer_id}/extensionFeedItems/{feed_item_id}``
      device:
          The device for which the extensions will serve. Optional.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.resources.CampaignExtensionSetting)
  ))
_sym_db.RegisterMessage(CampaignExtensionSetting)


DESCRIPTOR._options = None
_CAMPAIGNEXTENSIONSETTING.fields_by_name['resource_name']._options = None
_CAMPAIGNEXTENSIONSETTING.fields_by_name['extension_type']._options = None
_CAMPAIGNEXTENSIONSETTING.fields_by_name['campaign']._options = None
_CAMPAIGNEXTENSIONSETTING.fields_by_name['extension_feed_items']._options = None
_CAMPAIGNEXTENSIONSETTING._options = None
# @@protoc_insertion_point(module_scope)
