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


from google.ads.googleads.v4.resources.types import (
    campaign_draft as gagr_campaign_draft,
)
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.rpc import status_pb2 as status  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.services",
    marshal="google.ads.googleads.v4",
    manifest={
        "GetCampaignDraftRequest",
        "MutateCampaignDraftsRequest",
        "PromoteCampaignDraftRequest",
        "CampaignDraftOperation",
        "MutateCampaignDraftsResponse",
        "MutateCampaignDraftResult",
        "ListCampaignDraftAsyncErrorsRequest",
        "ListCampaignDraftAsyncErrorsResponse",
    },
)


class GetCampaignDraftRequest(proto.Message):
    r"""Request message for
    [CampaignDraftService.GetCampaignDraft][google.ads.googleads.v4.services.CampaignDraftService.GetCampaignDraft].

    Attributes:
        resource_name (str):
            Required. The resource name of the campaign
            draft to fetch.
    """

    resource_name = proto.Field(proto.STRING, number=1)


class MutateCampaignDraftsRequest(proto.Message):
    r"""Request message for
    [CampaignDraftService.MutateCampaignDrafts][google.ads.googleads.v4.services.CampaignDraftService.MutateCampaignDrafts].

    Attributes:
        customer_id (str):
            Required. The ID of the customer whose
            campaign drafts are being modified.
        operations (Sequence[google.ads.googleads.v4.services.types.CampaignDraftOperation]):
            Required. The list of operations to perform
            on individual campaign drafts.
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
        proto.MESSAGE, number=2, message="CampaignDraftOperation",
    )
    partial_failure = proto.Field(proto.BOOL, number=3)
    validate_only = proto.Field(proto.BOOL, number=4)


class PromoteCampaignDraftRequest(proto.Message):
    r"""Request message for
    [CampaignDraftService.PromoteCampaignDraft][google.ads.googleads.v4.services.CampaignDraftService.PromoteCampaignDraft].

    Attributes:
        campaign_draft (str):
            Required. The resource name of the campaign
            draft to promote.
    """

    campaign_draft = proto.Field(proto.STRING, number=1)


class CampaignDraftOperation(proto.Message):
    r"""A single operation (create, update, remove) on a campaign
    draft.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            FieldMask that determines which resource
            fields are modified in an update.
        create (google.ads.googleads.v4.resources.types.CampaignDraft):
            Create operation: No resource name is
            expected for the new campaign draft.
        update (google.ads.googleads.v4.resources.types.CampaignDraft):
            Update operation: The campaign draft is
            expected to have a valid resource name.
        remove (str):
            Remove operation: The campaign draft is expected to have a
            valid resource name, in this format:

            ``customers/{customer_id}/campaignDrafts/{base_campaign_id}~{draft_id}``
    """

    update_mask = proto.Field(
        proto.MESSAGE, number=4, message=field_mask.FieldMask,
    )
    create = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="operation",
        message=gagr_campaign_draft.CampaignDraft,
    )
    update = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="operation",
        message=gagr_campaign_draft.CampaignDraft,
    )
    remove = proto.Field(proto.STRING, number=3, oneof="operation")


class MutateCampaignDraftsResponse(proto.Message):
    r"""Response message for campaign draft mutate.

    Attributes:
        partial_failure_error (google.rpc.status_pb2.Status):
            Errors that pertain to operation failures in the partial
            failure mode. Returned only when partial_failure = true and
            all errors occur inside the operations. If any errors occur
            outside the operations (e.g. auth errors), we return an RPC
            level error.
        results (Sequence[google.ads.googleads.v4.services.types.MutateCampaignDraftResult]):
            All results for the mutate.
    """

    partial_failure_error = proto.Field(
        proto.MESSAGE, number=3, message=status.Status,
    )
    results = proto.RepeatedField(
        proto.MESSAGE, number=2, message="MutateCampaignDraftResult",
    )


class MutateCampaignDraftResult(proto.Message):
    r"""The result for the campaign draft mutate.

    Attributes:
        resource_name (str):
            Returned for successful operations.
    """

    resource_name = proto.Field(proto.STRING, number=1)


class ListCampaignDraftAsyncErrorsRequest(proto.Message):
    r"""Request message for
    [CampaignDraftService.ListCampaignDraftAsyncErrors][google.ads.googleads.v4.services.CampaignDraftService.ListCampaignDraftAsyncErrors].

    Attributes:
        resource_name (str):
            Required. The name of the campaign draft from
            which to retrieve the async errors.
        page_token (str):
            Token of the page to retrieve. If not specified, the first
            page of results will be returned. Use the value obtained
            from ``next_page_token`` in the previous response in order
            to request the next page of results.
        page_size (int):
            Number of elements to retrieve in a single
            page. When a page request is too large, the
            server may decide to further limit the number of
            returned resources.
    """

    resource_name = proto.Field(proto.STRING, number=1)
    page_token = proto.Field(proto.STRING, number=2)
    page_size = proto.Field(proto.INT32, number=3)


class ListCampaignDraftAsyncErrorsResponse(proto.Message):
    r"""Response message for
    [CampaignDraftService.ListCampaignDraftAsyncErrors][google.ads.googleads.v4.services.CampaignDraftService.ListCampaignDraftAsyncErrors].

    Attributes:
        errors (Sequence[google.rpc.status_pb2.Status]):
            Details of the errors when performing the
            asynchronous operation.
        next_page_token (str):
            Pagination token used to retrieve the next page of results.
            Pass the content of this string as the ``page_token``
            attribute of the next request. ``next_page_token`` is not
            returned for the last page.
    """

    @property
    def raw_page(self):
        return self

    errors = proto.RepeatedField(
        proto.MESSAGE, number=1, message=status.Status,
    )
    next_page_token = proto.Field(proto.STRING, number=2)


__all__ = tuple(sorted(__protobuf__.manifest))
