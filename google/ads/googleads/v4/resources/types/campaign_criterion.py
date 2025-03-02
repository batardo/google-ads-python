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
from google.ads.googleads.v4.enums.types import campaign_criterion_status
from google.ads.googleads.v4.enums.types import criterion_type
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"CampaignCriterion",},
)


class CampaignCriterion(proto.Message):
    r"""A campaign criterion.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the campaign criterion.
            Campaign criterion resource names have the form:

            ``customers/{customer_id}/campaignCriteria/{campaign_id}~{criterion_id}``
        campaign (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The campaign to which the
            criterion belongs.
        criterion_id (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The ID of the criterion.
            This field is ignored during mutate.
        bid_modifier (google.protobuf.wrappers_pb2.FloatValue):
            The modifier for the bids when the criterion
            matches. The modifier must be in the range: 0.1
            - 10.0. Most targetable criteria types support
            modifiers. Use 0 to opt out of a Device type.
        negative (google.protobuf.wrappers_pb2.BoolValue):
            Immutable. Whether to target (``false``) or exclude
            (``true``) the criterion.
        type_ (google.ads.googleads.v4.enums.types.CriterionTypeEnum.CriterionType):
            Output only. The type of the criterion.
        status (google.ads.googleads.v4.enums.types.CampaignCriterionStatusEnum.CampaignCriterionStatus):
            The status of the criterion.
        keyword (google.ads.googleads.v4.common.types.KeywordInfo):
            Immutable. Keyword.
        placement (google.ads.googleads.v4.common.types.PlacementInfo):
            Immutable. Placement.
        mobile_app_category (google.ads.googleads.v4.common.types.MobileAppCategoryInfo):
            Immutable. Mobile app category.
        mobile_application (google.ads.googleads.v4.common.types.MobileApplicationInfo):
            Immutable. Mobile application.
        location (google.ads.googleads.v4.common.types.LocationInfo):
            Immutable. Location.
        device (google.ads.googleads.v4.common.types.DeviceInfo):
            Immutable. Device.
        ad_schedule (google.ads.googleads.v4.common.types.AdScheduleInfo):
            Immutable. Ad Schedule.
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
        proximity (google.ads.googleads.v4.common.types.ProximityInfo):
            Immutable. Proximity.
        topic (google.ads.googleads.v4.common.types.TopicInfo):
            Immutable. Topic.
        listing_scope (google.ads.googleads.v4.common.types.ListingScopeInfo):
            Immutable. Listing scope.
        language (google.ads.googleads.v4.common.types.LanguageInfo):
            Immutable. Language.
        ip_block (google.ads.googleads.v4.common.types.IpBlockInfo):
            Immutable. IpBlock.
        content_label (google.ads.googleads.v4.common.types.ContentLabelInfo):
            Immutable. ContentLabel.
        carrier (google.ads.googleads.v4.common.types.CarrierInfo):
            Immutable. Carrier.
        user_interest (google.ads.googleads.v4.common.types.UserInterestInfo):
            Immutable. User Interest.
        webpage (google.ads.googleads.v4.common.types.WebpageInfo):
            Immutable. Webpage.
        operating_system_version (google.ads.googleads.v4.common.types.OperatingSystemVersionInfo):
            Immutable. Operating system version.
        mobile_device (google.ads.googleads.v4.common.types.MobileDeviceInfo):
            Immutable. Mobile Device.
        location_group (google.ads.googleads.v4.common.types.LocationGroupInfo):
            Immutable. Location Group
        custom_affinity (google.ads.googleads.v4.common.types.CustomAffinityInfo):
            Immutable. Custom Affinity.
    """

    resource_name = proto.Field(proto.STRING, number=1)
    campaign = proto.Field(
        proto.MESSAGE, number=4, message=wrappers.StringValue,
    )
    criterion_id = proto.Field(
        proto.MESSAGE, number=5, message=wrappers.Int64Value,
    )
    bid_modifier = proto.Field(
        proto.MESSAGE, number=14, message=wrappers.FloatValue,
    )
    negative = proto.Field(proto.MESSAGE, number=7, message=wrappers.BoolValue,)
    type_ = proto.Field(
        proto.ENUM,
        number=6,
        enum=criterion_type.CriterionTypeEnum.CriterionType,
    )
    status = proto.Field(
        proto.ENUM,
        number=35,
        enum=campaign_criterion_status.CampaignCriterionStatusEnum.CampaignCriterionStatus,
    )
    keyword = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="criterion",
        message=criteria.KeywordInfo,
    )
    placement = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="criterion",
        message=criteria.PlacementInfo,
    )
    mobile_app_category = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="criterion",
        message=criteria.MobileAppCategoryInfo,
    )
    mobile_application = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="criterion",
        message=criteria.MobileApplicationInfo,
    )
    location = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="criterion",
        message=criteria.LocationInfo,
    )
    device = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="criterion",
        message=criteria.DeviceInfo,
    )
    ad_schedule = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="criterion",
        message=criteria.AdScheduleInfo,
    )
    age_range = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="criterion",
        message=criteria.AgeRangeInfo,
    )
    gender = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="criterion",
        message=criteria.GenderInfo,
    )
    income_range = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="criterion",
        message=criteria.IncomeRangeInfo,
    )
    parental_status = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="criterion",
        message=criteria.ParentalStatusInfo,
    )
    user_list = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="criterion",
        message=criteria.UserListInfo,
    )
    youtube_video = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="criterion",
        message=criteria.YouTubeVideoInfo,
    )
    youtube_channel = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="criterion",
        message=criteria.YouTubeChannelInfo,
    )
    proximity = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="criterion",
        message=criteria.ProximityInfo,
    )
    topic = proto.Field(
        proto.MESSAGE, number=24, oneof="criterion", message=criteria.TopicInfo,
    )
    listing_scope = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="criterion",
        message=criteria.ListingScopeInfo,
    )
    language = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="criterion",
        message=criteria.LanguageInfo,
    )
    ip_block = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="criterion",
        message=criteria.IpBlockInfo,
    )
    content_label = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="criterion",
        message=criteria.ContentLabelInfo,
    )
    carrier = proto.Field(
        proto.MESSAGE,
        number=29,
        oneof="criterion",
        message=criteria.CarrierInfo,
    )
    user_interest = proto.Field(
        proto.MESSAGE,
        number=30,
        oneof="criterion",
        message=criteria.UserInterestInfo,
    )
    webpage = proto.Field(
        proto.MESSAGE,
        number=31,
        oneof="criterion",
        message=criteria.WebpageInfo,
    )
    operating_system_version = proto.Field(
        proto.MESSAGE,
        number=32,
        oneof="criterion",
        message=criteria.OperatingSystemVersionInfo,
    )
    mobile_device = proto.Field(
        proto.MESSAGE,
        number=33,
        oneof="criterion",
        message=criteria.MobileDeviceInfo,
    )
    location_group = proto.Field(
        proto.MESSAGE,
        number=34,
        oneof="criterion",
        message=criteria.LocationGroupInfo,
    )
    custom_affinity = proto.Field(
        proto.MESSAGE,
        number=36,
        oneof="criterion",
        message=criteria.CustomAffinityInfo,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
