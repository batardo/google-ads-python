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


from google.ads.googleads.v4.common.types import criteria
from google.ads.googleads.v4.common.types import custom_parameter
from google.ads.googleads.v4.enums.types import (
    ad_group_criterion_approval_status,
)
from google.ads.googleads.v4.enums.types import ad_group_criterion_status
from google.ads.googleads.v4.enums.types import bidding_source
from google.ads.googleads.v4.enums.types import criterion_system_serving_status
from google.ads.googleads.v4.enums.types import criterion_type
from google.ads.googleads.v4.enums.types import quality_score_bucket
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"AdGroupCriterion",},
)


class AdGroupCriterion(proto.Message):
    r"""An ad group criterion.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the ad group criterion. Ad
            group criterion resource names have the form:

            ``customers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}``
        criterion_id (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The ID of the criterion.
            This field is ignored for mutates.
        status (google.ads.googleads.v4.enums.types.AdGroupCriterionStatusEnum.AdGroupCriterionStatus):
            The status of the criterion.
            This is the status of the ad group criterion
            entity, set by the client. Note: UI reports may
            incorporate additional information that affects
            whether a criterion is eligible to run. In some
            cases a criterion that's REMOVED in the API can
            still show as enabled in the UI. For example,
            campaigns by default show to users of all age
            ranges unless excluded. The UI will show each
            age range as "enabled", since they're eligible
            to see the ads; but AdGroupCriterion.status will
            show "removed", since no positive criterion was
            added.
        quality_info (google.ads.googleads.v4.resources.types.AdGroupCriterion.QualityInfo):
            Output only. Information regarding the
            quality of the criterion.
        ad_group (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The ad group to which the
            criterion belongs.
        type_ (google.ads.googleads.v4.enums.types.CriterionTypeEnum.CriterionType):
            Output only. The type of the criterion.
        negative (google.protobuf.wrappers_pb2.BoolValue):
            Immutable. Whether to target (``false``) or exclude
            (``true``) the criterion.

            This field is immutable. To switch a criterion from positive
            to negative, remove then re-add it.
        system_serving_status (google.ads.googleads.v4.enums.types.CriterionSystemServingStatusEnum.CriterionSystemServingStatus):
            Output only. Serving status of the criterion.
        approval_status (google.ads.googleads.v4.enums.types.AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus):
            Output only. Approval status of the
            criterion.
        disapproval_reasons (Sequence[google.protobuf.wrappers_pb2.StringValue]):
            Output only. List of disapproval reasons of
            the criterion.
            The different reasons for disapproving a
            criterion can be found here:
            https://support.google.com/adspolicy/answer/6008942
            This field is read-only.
        bid_modifier (google.protobuf.wrappers_pb2.DoubleValue):
            The modifier for the bid when the criterion
            matches. The modifier must be in the range: 0.1
            - 10.0. Most targetable criteria types support
            modifiers.
        cpc_bid_micros (google.protobuf.wrappers_pb2.Int64Value):
            The CPC (cost-per-click) bid.
        cpm_bid_micros (google.protobuf.wrappers_pb2.Int64Value):
            The CPM (cost-per-thousand viewable
            impressions) bid.
        cpv_bid_micros (google.protobuf.wrappers_pb2.Int64Value):
            The CPV (cost-per-view) bid.
        percent_cpc_bid_micros (google.protobuf.wrappers_pb2.Int64Value):
            The CPC bid amount, expressed as a fraction of the
            advertised price for some good or service. The valid range
            for the fraction is [0,1) and the value stored here is
            1,000,000 \* [fraction].
        effective_cpc_bid_micros (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The effective CPC (cost-per-
            lick) bid.
        effective_cpm_bid_micros (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The effective CPM (cost-per-
            housand viewable impressions) bid.
        effective_cpv_bid_micros (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The effective CPV (cost-per-
            iew) bid.
        effective_percent_cpc_bid_micros (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The effective Percent CPC bid
            amount.
        effective_cpc_bid_source (google.ads.googleads.v4.enums.types.BiddingSourceEnum.BiddingSource):
            Output only. Source of the effective CPC bid.
        effective_cpm_bid_source (google.ads.googleads.v4.enums.types.BiddingSourceEnum.BiddingSource):
            Output only. Source of the effective CPM bid.
        effective_cpv_bid_source (google.ads.googleads.v4.enums.types.BiddingSourceEnum.BiddingSource):
            Output only. Source of the effective CPV bid.
        effective_percent_cpc_bid_source (google.ads.googleads.v4.enums.types.BiddingSourceEnum.BiddingSource):
            Output only. Source of the effective Percent
            CPC bid.
        position_estimates (google.ads.googleads.v4.resources.types.AdGroupCriterion.PositionEstimates):
            Output only. Estimates for criterion bids at
            various positions.
        final_urls (Sequence[google.protobuf.wrappers_pb2.StringValue]):
            The list of possible final URLs after all
            cross-domain redirects for the ad.
        final_mobile_urls (Sequence[google.protobuf.wrappers_pb2.StringValue]):
            The list of possible final mobile URLs after
            all cross-domain redirects.
        final_url_suffix (google.protobuf.wrappers_pb2.StringValue):
            URL template for appending params to final
            URL.
        tracking_url_template (google.protobuf.wrappers_pb2.StringValue):
            The URL template for constructing a tracking
            URL.
        url_custom_parameters (Sequence[google.ads.googleads.v4.common.types.CustomParameter]):
            The list of mappings used to substitute custom parameter
            tags in a ``tracking_url_template``, ``final_urls``, or
            ``mobile_final_urls``.
        keyword (google.ads.googleads.v4.common.types.KeywordInfo):
            Immutable. Keyword.
        placement (google.ads.googleads.v4.common.types.PlacementInfo):
            Immutable. Placement.
        mobile_app_category (google.ads.googleads.v4.common.types.MobileAppCategoryInfo):
            Immutable. Mobile app category.
        mobile_application (google.ads.googleads.v4.common.types.MobileApplicationInfo):
            Immutable. Mobile application.
        listing_group (google.ads.googleads.v4.common.types.ListingGroupInfo):
            Immutable. Listing group.
        age_range (google.ads.googleads.v4.common.types.AgeRangeInfo):
            Immutable. Age range.
        gender (google.ads.googleads.v4.common.types.GenderInfo):
            Immutable. Gender.
        income_range (google.ads.googleads.v4.common.types.IncomeRangeInfo):
            Immutable. Income range.
        parental_status (google.ads.googleads.v4.common.types.ParentalStatusInfo):
            Immutable. Parental status.
        user_list (google.ads.googleads.v4.common.types.UserListInfo):
            Immutable. User List.
        youtube_video (google.ads.googleads.v4.common.types.YouTubeVideoInfo):
            Immutable. YouTube Video.
        youtube_channel (google.ads.googleads.v4.common.types.YouTubeChannelInfo):
            Immutable. YouTube Channel.
        topic (google.ads.googleads.v4.common.types.TopicInfo):
            Immutable. Topic.
        user_interest (google.ads.googleads.v4.common.types.UserInterestInfo):
            Immutable. User Interest.
        webpage (google.ads.googleads.v4.common.types.WebpageInfo):
            Immutable. Webpage
        app_payment_model (google.ads.googleads.v4.common.types.AppPaymentModelInfo):
            Immutable. App Payment Model.
        custom_affinity (google.ads.googleads.v4.common.types.CustomAffinityInfo):
            Immutable. Custom Affinity.
        custom_intent (google.ads.googleads.v4.common.types.CustomIntentInfo):
            Immutable. Custom Intent.
    """

    class QualityInfo(proto.Message):
        r"""A container for ad group criterion quality information.

        Attributes:
            quality_score (google.protobuf.wrappers_pb2.Int32Value):
                Output only. The quality score.
                This field may not be populated if Google does
                not have enough information to determine a
                value.
            creative_quality_score (google.ads.googleads.v4.enums.types.QualityScoreBucketEnum.QualityScoreBucket):
                Output only. The performance of the ad
                compared to other advertisers.
            post_click_quality_score (google.ads.googleads.v4.enums.types.QualityScoreBucketEnum.QualityScoreBucket):
                Output only. The quality score of the landing
                page.
            search_predicted_ctr (google.ads.googleads.v4.enums.types.QualityScoreBucketEnum.QualityScoreBucket):
                Output only. The click-through rate compared
                to that of other advertisers.
        """

        quality_score = proto.Field(
            proto.MESSAGE, number=1, message=wrappers.Int32Value,
        )
        creative_quality_score = proto.Field(
            proto.ENUM,
            number=2,
            enum=quality_score_bucket.QualityScoreBucketEnum.QualityScoreBucket,
        )
        post_click_quality_score = proto.Field(
            proto.ENUM,
            number=3,
            enum=quality_score_bucket.QualityScoreBucketEnum.QualityScoreBucket,
        )
        search_predicted_ctr = proto.Field(
            proto.ENUM,
            number=4,
            enum=quality_score_bucket.QualityScoreBucketEnum.QualityScoreBucket,
        )

    class PositionEstimates(proto.Message):
        r"""Estimates for criterion bids at various positions.

        Attributes:
            first_page_cpc_micros (google.protobuf.wrappers_pb2.Int64Value):
                Output only. The estimate of the CPC bid
                required for ad to be shown on first page of
                search results.
            first_position_cpc_micros (google.protobuf.wrappers_pb2.Int64Value):
                Output only. The estimate of the CPC bid
                required for ad to be displayed in first
                position, at the top of the first page of search
                results.
            top_of_page_cpc_micros (google.protobuf.wrappers_pb2.Int64Value):
                Output only. The estimate of the CPC bid
                required for ad to be displayed at the top of
                the first page of search results.
            estimated_add_clicks_at_first_position_cpc (google.protobuf.wrappers_pb2.Int64Value):
                Output only. Estimate of how many clicks per week you might
                get by changing your keyword bid to the value in
                first_position_cpc_micros.
            estimated_add_cost_at_first_position_cpc (google.protobuf.wrappers_pb2.Int64Value):
                Output only. Estimate of how your cost per week might change
                when changing your keyword bid to the value in
                first_position_cpc_micros.
        """

        first_page_cpc_micros = proto.Field(
            proto.MESSAGE, number=1, message=wrappers.Int64Value,
        )
        first_position_cpc_micros = proto.Field(
            proto.MESSAGE, number=2, message=wrappers.Int64Value,
        )
        top_of_page_cpc_micros = proto.Field(
            proto.MESSAGE, number=3, message=wrappers.Int64Value,
        )
        estimated_add_clicks_at_first_position_cpc = proto.Field(
            proto.MESSAGE, number=4, message=wrappers.Int64Value,
        )
        estimated_add_cost_at_first_position_cpc = proto.Field(
            proto.MESSAGE, number=5, message=wrappers.Int64Value,
        )

    resource_name = proto.Field(proto.STRING, number=1)
    criterion_id = proto.Field(
        proto.MESSAGE, number=26, message=wrappers.Int64Value,
    )
    status = proto.Field(
        proto.ENUM,
        number=3,
        enum=ad_group_criterion_status.AdGroupCriterionStatusEnum.AdGroupCriterionStatus,
    )
    quality_info = proto.Field(proto.MESSAGE, number=4, message=QualityInfo,)
    ad_group = proto.Field(
        proto.MESSAGE, number=5, message=wrappers.StringValue,
    )
    type_ = proto.Field(
        proto.ENUM,
        number=25,
        enum=criterion_type.CriterionTypeEnum.CriterionType,
    )
    negative = proto.Field(
        proto.MESSAGE, number=31, message=wrappers.BoolValue,
    )
    system_serving_status = proto.Field(
        proto.ENUM,
        number=52,
        enum=criterion_system_serving_status.CriterionSystemServingStatusEnum.CriterionSystemServingStatus,
    )
    approval_status = proto.Field(
        proto.ENUM,
        number=53,
        enum=ad_group_criterion_approval_status.AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus,
    )
    disapproval_reasons = proto.RepeatedField(
        proto.MESSAGE, number=55, message=wrappers.StringValue,
    )
    bid_modifier = proto.Field(
        proto.MESSAGE, number=44, message=wrappers.DoubleValue,
    )
    cpc_bid_micros = proto.Field(
        proto.MESSAGE, number=16, message=wrappers.Int64Value,
    )
    cpm_bid_micros = proto.Field(
        proto.MESSAGE, number=17, message=wrappers.Int64Value,
    )
    cpv_bid_micros = proto.Field(
        proto.MESSAGE, number=24, message=wrappers.Int64Value,
    )
    percent_cpc_bid_micros = proto.Field(
        proto.MESSAGE, number=33, message=wrappers.Int64Value,
    )
    effective_cpc_bid_micros = proto.Field(
        proto.MESSAGE, number=18, message=wrappers.Int64Value,
    )
    effective_cpm_bid_micros = proto.Field(
        proto.MESSAGE, number=19, message=wrappers.Int64Value,
    )
    effective_cpv_bid_micros = proto.Field(
        proto.MESSAGE, number=20, message=wrappers.Int64Value,
    )
    effective_percent_cpc_bid_micros = proto.Field(
        proto.MESSAGE, number=34, message=wrappers.Int64Value,
    )
    effective_cpc_bid_source = proto.Field(
        proto.ENUM,
        number=21,
        enum=bidding_source.BiddingSourceEnum.BiddingSource,
    )
    effective_cpm_bid_source = proto.Field(
        proto.ENUM,
        number=22,
        enum=bidding_source.BiddingSourceEnum.BiddingSource,
    )
    effective_cpv_bid_source = proto.Field(
        proto.ENUM,
        number=23,
        enum=bidding_source.BiddingSourceEnum.BiddingSource,
    )
    effective_percent_cpc_bid_source = proto.Field(
        proto.ENUM,
        number=35,
        enum=bidding_source.BiddingSourceEnum.BiddingSource,
    )
    position_estimates = proto.Field(
        proto.MESSAGE, number=10, message=PositionEstimates,
    )
    final_urls = proto.RepeatedField(
        proto.MESSAGE, number=11, message=wrappers.StringValue,
    )
    final_mobile_urls = proto.RepeatedField(
        proto.MESSAGE, number=51, message=wrappers.StringValue,
    )
    final_url_suffix = proto.Field(
        proto.MESSAGE, number=50, message=wrappers.StringValue,
    )
    tracking_url_template = proto.Field(
        proto.MESSAGE, number=13, message=wrappers.StringValue,
    )
    url_custom_parameters = proto.RepeatedField(
        proto.MESSAGE, number=14, message=custom_parameter.CustomParameter,
    )
    keyword = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="criterion",
        message=criteria.KeywordInfo,
    )
    placement = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="criterion",
        message=criteria.PlacementInfo,
    )
    mobile_app_category = proto.Field(
        proto.MESSAGE,
        number=29,
        oneof="criterion",
        message=criteria.MobileAppCategoryInfo,
    )
    mobile_application = proto.Field(
        proto.MESSAGE,
        number=30,
        oneof="criterion",
        message=criteria.MobileApplicationInfo,
    )
    listing_group = proto.Field(
        proto.MESSAGE,
        number=32,
        oneof="criterion",
        message=criteria.ListingGroupInfo,
    )
    age_range = proto.Field(
        proto.MESSAGE,
        number=36,
        oneof="criterion",
        message=criteria.AgeRangeInfo,
    )
    gender = proto.Field(
        proto.MESSAGE,
        number=37,
        oneof="criterion",
        message=criteria.GenderInfo,
    )
    income_range = proto.Field(
        proto.MESSAGE,
        number=38,
        oneof="criterion",
        message=criteria.IncomeRangeInfo,
    )
    parental_status = proto.Field(
        proto.MESSAGE,
        number=39,
        oneof="criterion",
        message=criteria.ParentalStatusInfo,
    )
    user_list = proto.Field(
        proto.MESSAGE,
        number=42,
        oneof="criterion",
        message=criteria.UserListInfo,
    )
    youtube_video = proto.Field(
        proto.MESSAGE,
        number=40,
        oneof="criterion",
        message=criteria.YouTubeVideoInfo,
    )
    youtube_channel = proto.Field(
        proto.MESSAGE,
        number=41,
        oneof="criterion",
        message=criteria.YouTubeChannelInfo,
    )
    topic = proto.Field(
        proto.MESSAGE, number=43, oneof="criterion", message=criteria.TopicInfo,
    )
    user_interest = proto.Field(
        proto.MESSAGE,
        number=45,
        oneof="criterion",
        message=criteria.UserInterestInfo,
    )
    webpage = proto.Field(
        proto.MESSAGE,
        number=46,
        oneof="criterion",
        message=criteria.WebpageInfo,
    )
    app_payment_model = proto.Field(
        proto.MESSAGE,
        number=47,
        oneof="criterion",
        message=criteria.AppPaymentModelInfo,
    )
    custom_affinity = proto.Field(
        proto.MESSAGE,
        number=48,
        oneof="criterion",
        message=criteria.CustomAffinityInfo,
    )
    custom_intent = proto.Field(
        proto.MESSAGE,
        number=49,
        oneof="criterion",
        message=criteria.CustomIntentInfo,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
