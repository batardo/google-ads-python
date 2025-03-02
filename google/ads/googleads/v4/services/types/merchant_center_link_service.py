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


from google.ads.googleads.v4.resources.types import merchant_center_link
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.services",
    marshal="google.ads.googleads.v4",
    manifest={
        "ListMerchantCenterLinksRequest",
        "ListMerchantCenterLinksResponse",
        "GetMerchantCenterLinkRequest",
        "MutateMerchantCenterLinkRequest",
        "MerchantCenterLinkOperation",
        "MutateMerchantCenterLinkResponse",
        "MutateMerchantCenterLinkResult",
    },
)


class ListMerchantCenterLinksRequest(proto.Message):
    r"""Request message for
    [MerchantCenterLinkService.ListMerchantCenterLinks][google.ads.googleads.v4.services.MerchantCenterLinkService.ListMerchantCenterLinks].

    Attributes:
        customer_id (str):
            Required. The ID of the customer onto which
            to apply the Merchant Center link list
            operation.
    """

    customer_id = proto.Field(proto.STRING, number=1)


class ListMerchantCenterLinksResponse(proto.Message):
    r"""Response message for
    [MerchantCenterLinkService.ListMerchantCenterLinks][google.ads.googleads.v4.services.MerchantCenterLinkService.ListMerchantCenterLinks].

    Attributes:
        merchant_center_links (Sequence[google.ads.googleads.v4.resources.types.MerchantCenterLink]):
            Merchant Center links available for the
            requested customer
    """

    merchant_center_links = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=merchant_center_link.MerchantCenterLink,
    )


class GetMerchantCenterLinkRequest(proto.Message):
    r"""Request message for
    [MerchantCenterLinkService.GetMerchantCenterLink][google.ads.googleads.v4.services.MerchantCenterLinkService.GetMerchantCenterLink].

    Attributes:
        resource_name (str):
            Required. Resource name of the Merchant
            Center link.
    """

    resource_name = proto.Field(proto.STRING, number=1)


class MutateMerchantCenterLinkRequest(proto.Message):
    r"""Request message for
    [MerchantCenterLinkService.MutateMerchantCenterLink][google.ads.googleads.v4.services.MerchantCenterLinkService.MutateMerchantCenterLink].

    Attributes:
        customer_id (str):
            Required. The ID of the customer being
            modified.
        operation (google.ads.googleads.v4.services.types.MerchantCenterLinkOperation):
            Required. The operation to perform on the
            link
    """

    customer_id = proto.Field(proto.STRING, number=1)
    operation = proto.Field(
        proto.MESSAGE, number=2, message="MerchantCenterLinkOperation",
    )


class MerchantCenterLinkOperation(proto.Message):
    r"""A single update on a Merchant Center link.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            FieldMask that determines which resource
            fields are modified in an update.
        update (google.ads.googleads.v4.resources.types.MerchantCenterLink):
            Update operation: The merchant center link is
            expected to have a valid resource name.
        remove (str):
            Remove operation: A resource name for the removed merchant
            center link is expected, in this format:

            ``customers/{customer_id}/merchantCenterLinks/{merchant_center_id}``
    """

    update_mask = proto.Field(
        proto.MESSAGE, number=3, message=field_mask.FieldMask,
    )
    update = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="operation",
        message=merchant_center_link.MerchantCenterLink,
    )
    remove = proto.Field(proto.STRING, number=2, oneof="operation")


class MutateMerchantCenterLinkResponse(proto.Message):
    r"""Response message for Merchant Center link mutate.

    Attributes:
        result (google.ads.googleads.v4.services.types.MutateMerchantCenterLinkResult):
            Result for the mutate.
    """

    result = proto.Field(
        proto.MESSAGE, number=2, message="MutateMerchantCenterLinkResult",
    )


class MutateMerchantCenterLinkResult(proto.Message):
    r"""The result for the Merchant Center link mutate.

    Attributes:
        resource_name (str):
            Returned for successful operations.
    """

    resource_name = proto.Field(proto.STRING, number=1)


__all__ = tuple(sorted(__protobuf__.manifest))
