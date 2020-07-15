# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import batch_job_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_batch__job__pb2
from google.ads.google_ads.v4.proto.services import batch_job_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2


class BatchJobServiceStub(object):
  """Proto file describing the BatchJobService.

  Service to manage batch jobs.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.MutateBatchJob = channel.unary_unary(
        '/google.ads.googleads.v4.services.BatchJobService/MutateBatchJob',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.MutateBatchJobRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.MutateBatchJobResponse.FromString,
        )
    self.GetBatchJob = channel.unary_unary(
        '/google.ads.googleads.v4.services.BatchJobService/GetBatchJob',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.GetBatchJobRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_batch__job__pb2.BatchJob.FromString,
        )
    self.ListBatchJobResults = channel.unary_unary(
        '/google.ads.googleads.v4.services.BatchJobService/ListBatchJobResults',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.ListBatchJobResultsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.ListBatchJobResultsResponse.FromString,
        )
    self.RunBatchJob = channel.unary_unary(
        '/google.ads.googleads.v4.services.BatchJobService/RunBatchJob',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.RunBatchJobRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.AddBatchJobOperations = channel.unary_unary(
        '/google.ads.googleads.v4.services.BatchJobService/AddBatchJobOperations',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.AddBatchJobOperationsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.AddBatchJobOperationsResponse.FromString,
        )


class BatchJobServiceServicer(object):
  """Proto file describing the BatchJobService.

  Service to manage batch jobs.
  """

  def MutateBatchJob(self, request, context):
    """Mutates a batch job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBatchJob(self, request, context):
    """Returns the batch job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListBatchJobResults(self, request, context):
    """Returns the results of the batch job. The job must be done.
    Supports standard list paging.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RunBatchJob(self, request, context):
    """Runs the batch job.

    The Operation.metadata field type is BatchJobMetadata. When finished, the
    long running operation will not contain errors or a response. Instead, use
    ListBatchJobResults to get the results of the job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddBatchJobOperations(self, request, context):
    """Add operations to the batch job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BatchJobServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'MutateBatchJob': grpc.unary_unary_rpc_method_handler(
          servicer.MutateBatchJob,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.MutateBatchJobRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.MutateBatchJobResponse.SerializeToString,
      ),
      'GetBatchJob': grpc.unary_unary_rpc_method_handler(
          servicer.GetBatchJob,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.GetBatchJobRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_batch__job__pb2.BatchJob.SerializeToString,
      ),
      'ListBatchJobResults': grpc.unary_unary_rpc_method_handler(
          servicer.ListBatchJobResults,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.ListBatchJobResultsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.ListBatchJobResultsResponse.SerializeToString,
      ),
      'RunBatchJob': grpc.unary_unary_rpc_method_handler(
          servicer.RunBatchJob,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.RunBatchJobRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'AddBatchJobOperations': grpc.unary_unary_rpc_method_handler(
          servicer.AddBatchJobOperations,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.AddBatchJobOperationsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_batch__job__service__pb2.AddBatchJobOperationsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.BatchJobService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
