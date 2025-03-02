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


from google.ads.googleads.v4.common.types import policy
from google.ads.googleads.v4.resources.types import ad_group_criterion
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.rpc import status_pb2 as status  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.services",
    marshal="google.ads.googleads.v4",
    manifest={
        "GetAdGroupCriterionRequest",
        "MutateAdGroupCriteriaRequest",
        "AdGroupCriterionOperation",
        "MutateAdGroupCriteriaResponse",
        "MutateAdGroupCriterionResult",
    },
)


class GetAdGroupCriterionRequest(proto.Message):
    r"""Request message for
    [AdGroupCriterionService.GetAdGroupCriterion][google.ads.googleads.v4.services.AdGroupCriterionService.GetAdGroupCriterion].

    Attributes:
        resource_name (str):
            Required. The resource name of the criterion
            to fetch.
    """

    resource_name = proto.Field(proto.STRING, number=1)


class MutateAdGroupCriteriaRequest(proto.Message):
    r"""Request message for
    [AdGroupCriterionService.MutateAdGroupCriteria][google.ads.googleads.v4.services.AdGroupCriterionService.MutateAdGroupCriteria].

    Attributes:
        customer_id (str):
            Required. ID of the customer whose criteria
            are being modified.
        operations (Sequence[google.ads.googleads.v4.services.types.AdGroupCriterionOperation]):
            Required. The list of operations to perform
            on individual criteria.
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
        proto.MESSAGE, number=2, message="AdGroupCriterionOperation",
    )
    partial_failure = proto.Field(proto.BOOL, number=3)
    validate_only = proto.Field(proto.BOOL, number=4)


class AdGroupCriterionOperation(proto.Message):
    r"""A single operation (create, remove, update) on an ad group
    criterion.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            FieldMask that determines which resource
            fields are modified in an update.
        exempt_policy_violation_keys (Sequence[google.ads.googleads.v4.common.types.PolicyViolationKey]):
            The list of policy violation keys that should not cause a
            PolicyViolationError to be reported. Not all policy
            violations are exemptable, please refer to the is_exemptible
            field in the returned PolicyViolationError.

            Resources violating these polices will be saved, but will
            not be eligible to serve. They may begin serving at a later
            time due to a change in policies, re-review of the resource,
            or a change in advertiser certificates.
        create (google.ads.googleads.v4.resources.types.AdGroupCriterion):
            Create operation: No resource name is
            expected for the new criterion.
        update (google.ads.googleads.v4.resources.types.AdGroupCriterion):
            Update operation: The criterion is expected
            to have a valid resource name.
        remove (str):
            Remove operation: A resource name for the removed criterion
            is expected, in this format:

            ``customers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}``
    """

    update_mask = proto.Field(
        proto.MESSAGE, number=4, message=field_mask.FieldMask,
    )
    exempt_policy_violation_keys = proto.RepeatedField(
        proto.MESSAGE, number=5, message=policy.PolicyViolationKey,
    )
    create = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="operation",
        message=ad_group_criterion.AdGroupCriterion,
    )
    update = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="operation",
        message=ad_group_criterion.AdGroupCriterion,
    )
    remove = proto.Field(proto.STRING, number=3, oneof="operation")


class MutateAdGroupCriteriaResponse(proto.Message):
    r"""Response message for an ad group criterion mutate.

    Attributes:
        partial_failure_error (google.rpc.status_pb2.Status):
            Errors that pertain to operation failures in the partial
            failure mode. Returned only when partial_failure = true and
            all errors occur inside the operations. If any errors occur
            outside the operations (e.g. auth errors), we return an RPC
            level error.
        results (Sequence[google.ads.googleads.v4.services.types.MutateAdGroupCriterionResult]):
            All results for the mutate.
    """

    partial_failure_error = proto.Field(
        proto.MESSAGE, number=3, message=status.Status,
    )
    results = proto.RepeatedField(
        proto.MESSAGE, number=2, message="MutateAdGroupCriterionResult",
    )


class MutateAdGroupCriterionResult(proto.Message):
    r"""The result for the criterion mutate.

    Attributes:
        resource_name (str):
            Returned for successful operations.
    """

    resource_name = proto.Field(proto.STRING, number=1)


__all__ = tuple(sorted(__protobuf__.manifest))
