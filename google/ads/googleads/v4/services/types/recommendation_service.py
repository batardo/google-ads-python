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


from google.ads.googleads.v4.common.types import extensions
from google.ads.googleads.v4.enums.types import keyword_match_type
from google.ads.googleads.v4.resources.types import ad as gagr_ad
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore
from google.rpc import status_pb2 as status  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.services",
    marshal="google.ads.googleads.v4",
    manifest={
        "GetRecommendationRequest",
        "ApplyRecommendationRequest",
        "ApplyRecommendationOperation",
        "ApplyRecommendationResponse",
        "ApplyRecommendationResult",
        "DismissRecommendationRequest",
        "DismissRecommendationResponse",
    },
)


class GetRecommendationRequest(proto.Message):
    r"""Request message for
    [RecommendationService.GetRecommendation][google.ads.googleads.v4.services.RecommendationService.GetRecommendation].

    Attributes:
        resource_name (str):
            Required. The resource name of the
            recommendation to fetch.
    """

    resource_name = proto.Field(proto.STRING, number=1)


class ApplyRecommendationRequest(proto.Message):
    r"""Request message for
    [RecommendationService.ApplyRecommendation][google.ads.googleads.v4.services.RecommendationService.ApplyRecommendation].

    Attributes:
        customer_id (str):
            Required. The ID of the customer with the
            recommendation.
        operations (Sequence[google.ads.googleads.v4.services.types.ApplyRecommendationOperation]):
            Required. The list of operations to apply recommendations.
            If partial_failure=false all recommendations should be of
            the same type There is a limit of 100 operations per
            request.
        partial_failure (bool):
            If true, successful operations will be
            carried out and invalid operations will return
            errors. If false, operations will be carried out
            as a transaction if and only if they are all
            valid. Default is false.
    """

    customer_id = proto.Field(proto.STRING, number=1)
    operations = proto.RepeatedField(
        proto.MESSAGE, number=2, message="ApplyRecommendationOperation",
    )
    partial_failure = proto.Field(proto.BOOL, number=3)


class ApplyRecommendationOperation(proto.Message):
    r"""Information about the operation to apply a recommendation and
    any parameters to customize it.

    Attributes:
        resource_name (str):
            The resource name of the recommendation to
            apply.
        campaign_budget (google.ads.googleads.v4.services.types.ApplyRecommendationOperation.CampaignBudgetParameters):
            Optional parameters to use when applying a
            campaign budget recommendation.
        text_ad (google.ads.googleads.v4.services.types.ApplyRecommendationOperation.TextAdParameters):
            Optional parameters to use when applying a
            text ad recommendation.
        keyword (google.ads.googleads.v4.services.types.ApplyRecommendationOperation.KeywordParameters):
            Optional parameters to use when applying
            keyword recommendation.
        target_cpa_opt_in (google.ads.googleads.v4.services.types.ApplyRecommendationOperation.TargetCpaOptInParameters):
            Optional parameters to use when applying
            target CPA opt-in recommendation.
        callout_extension (google.ads.googleads.v4.services.types.ApplyRecommendationOperation.CalloutExtensionParameters):
            Parameters to use when applying callout
            extension recommendation.
        call_extension (google.ads.googleads.v4.services.types.ApplyRecommendationOperation.CallExtensionParameters):
            Parameters to use when applying call
            extension recommendation.
        sitelink_extension (google.ads.googleads.v4.services.types.ApplyRecommendationOperation.SitelinkExtensionParameters):
            Parameters to use when applying sitelink
            extension recommendation.
        move_unused_budget (google.ads.googleads.v4.services.types.ApplyRecommendationOperation.MoveUnusedBudgetParameters):
            Parameters to use when applying move unused
            budget recommendation.
    """

    class CampaignBudgetParameters(proto.Message):
        r"""Parameters to use when applying a campaign budget
        recommendation.

        Attributes:
            new_budget_amount_micros (google.protobuf.wrappers_pb2.Int64Value):
                New budget amount to set for target budget
                resource. This is a required field.
        """

        new_budget_amount_micros = proto.Field(
            proto.MESSAGE, number=1, message=wrappers.Int64Value,
        )

    class TextAdParameters(proto.Message):
        r"""Parameters to use when applying a text ad recommendation.

        Attributes:
            ad (google.ads.googleads.v4.resources.types.Ad):
                New ad to add to recommended ad group. All
                necessary fields need to be set in this message.
                This is a required field.
        """

        ad = proto.Field(proto.MESSAGE, number=1, message=gagr_ad.Ad,)

    class KeywordParameters(proto.Message):
        r"""Parameters to use when applying keyword recommendation.

        Attributes:
            ad_group (google.protobuf.wrappers_pb2.StringValue):
                The ad group resource to add keyword to. This
                is a required field.
            match_type (google.ads.googleads.v4.enums.types.KeywordMatchTypeEnum.KeywordMatchType):
                The match type of the keyword. This is a
                required field.
            cpc_bid_micros (google.protobuf.wrappers_pb2.Int64Value):
                Optional, CPC bid to set for the keyword. If
                not set, keyword will use bid based on bidding
                strategy used by target ad group.
        """

        ad_group = proto.Field(
            proto.MESSAGE, number=1, message=wrappers.StringValue,
        )
        match_type = proto.Field(
            proto.ENUM,
            number=2,
            enum=keyword_match_type.KeywordMatchTypeEnum.KeywordMatchType,
        )
        cpc_bid_micros = proto.Field(
            proto.MESSAGE, number=3, message=wrappers.Int64Value,
        )

    class TargetCpaOptInParameters(proto.Message):
        r"""Parameters to use when applying Target CPA recommendation.

        Attributes:
            target_cpa_micros (google.protobuf.wrappers_pb2.Int64Value):
                Average CPA to use for Target CPA bidding
                strategy. This is a required field.
            new_campaign_budget_amount_micros (google.protobuf.wrappers_pb2.Int64Value):
                Optional, budget amount to set for the
                campaign.
        """

        target_cpa_micros = proto.Field(
            proto.MESSAGE, number=1, message=wrappers.Int64Value,
        )
        new_campaign_budget_amount_micros = proto.Field(
            proto.MESSAGE, number=2, message=wrappers.Int64Value,
        )

    class CalloutExtensionParameters(proto.Message):
        r"""Parameters to use when applying callout extension
        recommendation.

        Attributes:
            callout_extensions (Sequence[google.ads.googleads.v4.common.types.CalloutFeedItem]):
                Callout extensions to be added. This is a
                required field.
        """

        callout_extensions = proto.RepeatedField(
            proto.MESSAGE, number=1, message=extensions.CalloutFeedItem,
        )

    class CallExtensionParameters(proto.Message):
        r"""Parameters to use when applying call extension
        recommendation.

        Attributes:
            call_extensions (Sequence[google.ads.googleads.v4.common.types.CallFeedItem]):
                Call extensions to be added. This is a
                required field.
        """

        call_extensions = proto.RepeatedField(
            proto.MESSAGE, number=1, message=extensions.CallFeedItem,
        )

    class SitelinkExtensionParameters(proto.Message):
        r"""Parameters to use when applying sitelink extension
        recommendation.

        Attributes:
            sitelink_extensions (Sequence[google.ads.googleads.v4.common.types.SitelinkFeedItem]):
                Sitelink extensions to be added. This is a
                required field.
        """

        sitelink_extensions = proto.RepeatedField(
            proto.MESSAGE, number=1, message=extensions.SitelinkFeedItem,
        )

    class MoveUnusedBudgetParameters(proto.Message):
        r"""Parameters to use when applying move unused budget
        recommendation.

        Attributes:
            budget_micros_to_move (google.protobuf.wrappers_pb2.Int64Value):
                Budget amount to move from excess budget to
                constrained budget. This is a required field.
        """

        budget_micros_to_move = proto.Field(
            proto.MESSAGE, number=1, message=wrappers.Int64Value,
        )

    resource_name = proto.Field(proto.STRING, number=1)
    campaign_budget = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="apply_parameters",
        message=CampaignBudgetParameters,
    )
    text_ad = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="apply_parameters",
        message=TextAdParameters,
    )
    keyword = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="apply_parameters",
        message=KeywordParameters,
    )
    target_cpa_opt_in = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="apply_parameters",
        message=TargetCpaOptInParameters,
    )
    callout_extension = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="apply_parameters",
        message=CalloutExtensionParameters,
    )
    call_extension = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="apply_parameters",
        message=CallExtensionParameters,
    )
    sitelink_extension = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="apply_parameters",
        message=SitelinkExtensionParameters,
    )
    move_unused_budget = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="apply_parameters",
        message=MoveUnusedBudgetParameters,
    )


class ApplyRecommendationResponse(proto.Message):
    r"""Response message for
    [RecommendationService.ApplyRecommendation][google.ads.googleads.v4.services.RecommendationService.ApplyRecommendation].

    Attributes:
        results (Sequence[google.ads.googleads.v4.services.types.ApplyRecommendationResult]):
            Results of operations to apply
            recommendations.
        partial_failure_error (google.rpc.status_pb2.Status):
            Errors that pertain to operation failures in the partial
            failure mode. Returned only when partial_failure = true and
            all errors occur inside the operations. If any errors occur
            outside the operations (e.g. auth errors) we return the RPC
            level error.
    """

    results = proto.RepeatedField(
        proto.MESSAGE, number=1, message="ApplyRecommendationResult",
    )
    partial_failure_error = proto.Field(
        proto.MESSAGE, number=2, message=status.Status,
    )


class ApplyRecommendationResult(proto.Message):
    r"""The result of applying a recommendation.

    Attributes:
        resource_name (str):
            Returned for successful applies.
    """

    resource_name = proto.Field(proto.STRING, number=1)


class DismissRecommendationRequest(proto.Message):
    r"""Request message for
    [RecommendationService.DismissRecommendation][google.ads.googleads.v4.services.RecommendationService.DismissRecommendation].

    Attributes:
        customer_id (str):
            Required. The ID of the customer with the
            recommendation.
        operations (Sequence[google.ads.googleads.v4.services.types.DismissRecommendationRequest.DismissRecommendationOperation]):
            Required. The list of operations to dismiss recommendations.
            If partial_failure=false all recommendations should be of
            the same type There is a limit of 100 operations per
            request.
        partial_failure (bool):
            If true, successful operations will be
            carried out and invalid operations will return
            errors. If false, operations will be carried in
            a single transaction if and only if they are all
            valid. Default is false.
    """

    class DismissRecommendationOperation(proto.Message):
        r"""Operation to dismiss a single recommendation identified by
        resource_name.

        Attributes:
            resource_name (str):
                The resource name of the recommendation to
                dismiss.
        """

        resource_name = proto.Field(proto.STRING, number=1)

    customer_id = proto.Field(proto.STRING, number=1)
    operations = proto.RepeatedField(
        proto.MESSAGE, number=3, message=DismissRecommendationOperation,
    )
    partial_failure = proto.Field(proto.BOOL, number=2)


class DismissRecommendationResponse(proto.Message):
    r"""Response message for
    [RecommendationService.DismissRecommendation][google.ads.googleads.v4.services.RecommendationService.DismissRecommendation].

    Attributes:
        results (Sequence[google.ads.googleads.v4.services.types.DismissRecommendationResponse.DismissRecommendationResult]):
            Results of operations to dismiss
            recommendations.
        partial_failure_error (google.rpc.status_pb2.Status):
            Errors that pertain to operation failures in the partial
            failure mode. Returned only when partial_failure = true and
            all errors occur inside the operations. If any errors occur
            outside the operations (e.g. auth errors) we return the RPC
            level error.
    """

    class DismissRecommendationResult(proto.Message):
        r"""The result of dismissing a recommendation.

        Attributes:
            resource_name (str):
                Returned for successful dismissals.
        """

        resource_name = proto.Field(proto.STRING, number=1)

    results = proto.RepeatedField(
        proto.MESSAGE, number=1, message=DismissRecommendationResult,
    )
    partial_failure_error = proto.Field(
        proto.MESSAGE, number=2, message=status.Status,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
