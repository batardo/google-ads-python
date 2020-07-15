# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import account_link_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_account__link__pb2
from google.ads.google_ads.v4.proto.services import account_link_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_account__link__service__pb2


class AccountLinkServiceStub(object):
  """This service allows management of links between Google Ads accounts and other
  accounts.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAccountLink = channel.unary_unary(
        '/google.ads.googleads.v4.services.AccountLinkService/GetAccountLink',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_account__link__service__pb2.GetAccountLinkRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_account__link__pb2.AccountLink.FromString,
        )
    self.MutateAccountLink = channel.unary_unary(
        '/google.ads.googleads.v4.services.AccountLinkService/MutateAccountLink',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_account__link__service__pb2.MutateAccountLinkRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_account__link__service__pb2.MutateAccountLinkResponse.FromString,
        )


class AccountLinkServiceServicer(object):
  """This service allows management of links between Google Ads accounts and other
  accounts.
  """

  def GetAccountLink(self, request, context):
    """Returns the account link in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateAccountLink(self, request, context):
    """Creates or removes an account link.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AccountLinkServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAccountLink': grpc.unary_unary_rpc_method_handler(
          servicer.GetAccountLink,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_account__link__service__pb2.GetAccountLinkRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_account__link__pb2.AccountLink.SerializeToString,
      ),
      'MutateAccountLink': grpc.unary_unary_rpc_method_handler(
          servicer.MutateAccountLink,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_account__link__service__pb2.MutateAccountLinkRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_account__link__service__pb2.MutateAccountLinkResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.AccountLinkService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
