# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.ads.googleads.v4.resources.types import shared_set
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.rpc import status_pb2 as status  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.services",
    marshal="google.ads.googleads.v4",
    manifest={
        "GetSharedSetRequest",
        "MutateSharedSetsRequest",
        "SharedSetOperation",
        "MutateSharedSetsResponse",
        "MutateSharedSetResult",
    },
)


class GetSharedSetRequest(proto.Message):
    r"""Request message for
    [SharedSetService.GetSharedSet][google.ads.googleads.v4.services.SharedSetService.GetSharedSet].

    Attributes:
        resource_name (str):
            Required. The resource name of the shared set
            to fetch.
    """

    resource_name = proto.Field(proto.STRING, number=1)


class MutateSharedSetsRequest(proto.Message):
    r"""Request message for
    [SharedSetService.MutateSharedSets][google.ads.googleads.v4.services.SharedSetService.MutateSharedSets].

    Attributes:
        customer_id (str):
            Required. The ID of the customer whose shared
            sets are being modified.
        operations (Sequence[google.ads.googleads.v4.services.types.SharedSetOperation]):
            Required. The list of operations to perform
            on individual shared sets.
        partial_failure (bool):
            If true, successful operations will be
            carried out and invalid operations will return
            errors. If false, all operations will be carried
            out in one transaction if and only if they are
            all valid. Default is false.
        validate_only (bool):
            If true, the request is validated but not
            executed. Only errors are returned, not results.
    """

    customer_id = proto.Field(proto.STRING, number=1)
    operations = proto.RepeatedField(
        proto.MESSAGE, number=2, message="SharedSetOperation",
    )
    partial_failure = proto.Field(proto.BOOL, number=3)
    validate_only = proto.Field(proto.BOOL, number=4)


class SharedSetOperation(proto.Message):
    r"""A single operation (create, update, remove) on an shared set.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            FieldMask that determines which resource
            fields are modified in an update.
        create (google.ads.googleads.v4.resources.types.SharedSet):
            Create operation: No resource name is
            expected for the new shared set.
        update (google.ads.googleads.v4.resources.types.SharedSet):
            Update operation: The shared set is expected
            to have a valid resource name.
        remove (str):
            Remove operation: A resource name for the removed shared set
            is expected, in this format:

            ``customers/{customer_id}/sharedSets/{shared_set_id}``
    """

    update_mask = proto.Field(
        proto.MESSAGE, number=4, message=field_mask.FieldMask,
    )
    create = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="operation",
        message=shared_set.SharedSet,
    )
    update = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="operation",
        message=shared_set.SharedSet,
    )
    remove = proto.Field(proto.STRING, number=3, oneof="operation")


class MutateSharedSetsResponse(proto.Message):
    r"""Response message for a shared set mutate.

    Attributes:
        partial_failure_error (google.rpc.status_pb2.Status):
            Errors that pertain to operation failures in the partial
            failure mode. Returned only when partial_failure = true and
            all errors occur inside the operations. If any errors occur
            outside the operations (e.g. auth errors), we return an RPC
            level error.
        results (Sequence[google.ads.googleads.v4.services.types.MutateSharedSetResult]):
            All results for the mutate.
    """

    partial_failure_error = proto.Field(
        proto.MESSAGE, number=3, message=status.Status,
    )
    results = proto.RepeatedField(
        proto.MESSAGE, number=2, message="MutateSharedSetResult",
    )


class MutateSharedSetResult(proto.Message):
    r"""The result for the shared set mutate.

    Attributes:
        resource_name (str):
            Returned for successful operations.
    """

    resource_name = proto.Field(proto.STRING, number=1)


__all__ = tuple(sorted(__protobuf__.manifest))
