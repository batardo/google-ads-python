# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import keyword_plan_campaign_keyword_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_keyword__plan__campaign__keyword__pb2
from google.ads.google_ads.v4.proto.services import keyword_plan_campaign_keyword_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_keyword__plan__campaign__keyword__service__pb2


class KeywordPlanCampaignKeywordServiceStub(object):
  """Proto file describing the keyword plan campaign keyword service.

  Service to manage Keyword Plan campaign keywords. KeywordPlanCampaign is
  required to add the campaign keywords. Only negative keywords are supported.
  A maximum of 1000 negative keywords are allowed per plan. This includes both
  campaign negative keywords and ad group negative keywords.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetKeywordPlanCampaignKeyword = channel.unary_unary(
        '/google.ads.googleads.v4.services.KeywordPlanCampaignKeywordService/GetKeywordPlanCampaignKeyword',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_keyword__plan__campaign__keyword__service__pb2.GetKeywordPlanCampaignKeywordRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_keyword__plan__campaign__keyword__pb2.KeywordPlanCampaignKeyword.FromString,
        )
    self.MutateKeywordPlanCampaignKeywords = channel.unary_unary(
        '/google.ads.googleads.v4.services.KeywordPlanCampaignKeywordService/MutateKeywordPlanCampaignKeywords',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_keyword__plan__campaign__keyword__service__pb2.MutateKeywordPlanCampaignKeywordsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_keyword__plan__campaign__keyword__service__pb2.MutateKeywordPlanCampaignKeywordsResponse.FromString,
        )


class KeywordPlanCampaignKeywordServiceServicer(object):
  """Proto file describing the keyword plan campaign keyword service.

  Service to manage Keyword Plan campaign keywords. KeywordPlanCampaign is
  required to add the campaign keywords. Only negative keywords are supported.
  A maximum of 1000 negative keywords are allowed per plan. This includes both
  campaign negative keywords and ad group negative keywords.
  """

  def GetKeywordPlanCampaignKeyword(self, request, context):
    """Returns the requested plan in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateKeywordPlanCampaignKeywords(self, request, context):
    """Creates, updates, or removes Keyword Plan campaign keywords. Operation
    statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_KeywordPlanCampaignKeywordServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetKeywordPlanCampaignKeyword': grpc.unary_unary_rpc_method_handler(
          servicer.GetKeywordPlanCampaignKeyword,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_keyword__plan__campaign__keyword__service__pb2.GetKeywordPlanCampaignKeywordRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_keyword__plan__campaign__keyword__pb2.KeywordPlanCampaignKeyword.SerializeToString,
      ),
      'MutateKeywordPlanCampaignKeywords': grpc.unary_unary_rpc_method_handler(
          servicer.MutateKeywordPlanCampaignKeywords,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_keyword__plan__campaign__keyword__service__pb2.MutateKeywordPlanCampaignKeywordsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_keyword__plan__campaign__keyword__service__pb2.MutateKeywordPlanCampaignKeywordsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.KeywordPlanCampaignKeywordService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
