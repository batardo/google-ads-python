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


from google.ads.googleads.v4.common.types import bidding
from google.ads.googleads.v4.common.types import custom_parameter
from google.ads.googleads.v4.common.types import frequency_cap
from google.ads.googleads.v4.common.types import (
    real_time_bidding_setting as gagc_real_time_bidding_setting,
)
from google.ads.googleads.v4.common.types import (
    targeting_setting as gagc_targeting_setting,
)
from google.ads.googleads.v4.enums.types import (
    ad_serving_optimization_status as gage_ad_serving_optimization_status,
)
from google.ads.googleads.v4.enums.types import (
    advertising_channel_sub_type as gage_advertising_channel_sub_type,
)
from google.ads.googleads.v4.enums.types import (
    advertising_channel_type as gage_advertising_channel_type,
)
from google.ads.googleads.v4.enums.types import app_campaign_app_store
from google.ads.googleads.v4.enums.types import (
    app_campaign_bidding_strategy_goal_type,
)
from google.ads.googleads.v4.enums.types import (
    bidding_strategy_type as gage_bidding_strategy_type,
)
from google.ads.googleads.v4.enums.types import brand_safety_suitability
from google.ads.googleads.v4.enums.types import campaign_experiment_type
from google.ads.googleads.v4.enums.types import campaign_serving_status
from google.ads.googleads.v4.enums.types import campaign_status
from google.ads.googleads.v4.enums.types import (
    location_source_type as gage_location_source_type,
)
from google.ads.googleads.v4.enums.types import (
    negative_geo_target_type as gage_negative_geo_target_type,
)
from google.ads.googleads.v4.enums.types import optimization_goal_type
from google.ads.googleads.v4.enums.types import (
    payment_mode as gage_payment_mode,
)
from google.ads.googleads.v4.enums.types import (
    positive_geo_target_type as gage_positive_geo_target_type,
)
from google.ads.googleads.v4.enums.types import (
    vanity_pharma_display_url_mode as gage_vanity_pharma_display_url_mode,
)
from google.ads.googleads.v4.enums.types import (
    vanity_pharma_text as gage_vanity_pharma_text,
)
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"Campaign",},
)


class Campaign(proto.Message):
    r"""A campaign.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the campaign. Campaign
            resource names have the form:

            ``customers/{customer_id}/campaigns/{campaign_id}``
        id (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The ID of the campaign.
        name (google.protobuf.wrappers_pb2.StringValue):
            The name of the campaign.
            This field is required and should not be empty
            when creating new campaigns.

            It must not contain any null (code point 0x0),
            NL line feed (code point 0xA) or carriage return
            (code point 0xD) characters.
        status (google.ads.googleads.v4.enums.types.CampaignStatusEnum.CampaignStatus):
            The status of the campaign.
            When a new campaign is added, the status
            defaults to ENABLED.
        serving_status (google.ads.googleads.v4.enums.types.CampaignServingStatusEnum.CampaignServingStatus):
            Output only. The ad serving status of the
            campaign.
        ad_serving_optimization_status (google.ads.googleads.v4.enums.types.AdServingOptimizationStatusEnum.AdServingOptimizationStatus):
            The ad serving optimization status of the
            campaign.
        advertising_channel_type (google.ads.googleads.v4.enums.types.AdvertisingChannelTypeEnum.AdvertisingChannelType):
            Immutable. The primary serving target for ads within the
            campaign. The targeting options can be refined in
            ``network_settings``.

            This field is required and should not be empty when creating
            new campaigns.

            Can be set only when creating campaigns. After the campaign
            is created, the field can not be changed.
        advertising_channel_sub_type (google.ads.googleads.v4.enums.types.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType):
            Immutable. Optional refinement to
            ``advertising_channel_type``. Must be a valid sub-type of
            the parent channel type.

            Can be set only when creating campaigns. After campaign is
            created, the field can not be changed.
        tracking_url_template (google.protobuf.wrappers_pb2.StringValue):
            The URL template for constructing a tracking
            URL.
        url_custom_parameters (Sequence[google.ads.googleads.v4.common.types.CustomParameter]):
            The list of mappings used to substitute custom parameter
            tags in a ``tracking_url_template``, ``final_urls``, or
            ``mobile_final_urls``.
        real_time_bidding_setting (google.ads.googleads.v4.common.types.RealTimeBiddingSetting):
            Settings for Real-Time Bidding, a feature
            only available for campaigns targeting the Ad
            Exchange network.
        network_settings (google.ads.googleads.v4.resources.types.Campaign.NetworkSettings):
            The network settings for the campaign.
        hotel_setting (google.ads.googleads.v4.resources.types.Campaign.HotelSettingInfo):
            Immutable. The hotel setting for the
            campaign.
        dynamic_search_ads_setting (google.ads.googleads.v4.resources.types.Campaign.DynamicSearchAdsSetting):
            The setting for controlling Dynamic Search
            Ads (DSA).
        shopping_setting (google.ads.googleads.v4.resources.types.Campaign.ShoppingSetting):
            The setting for controlling Shopping
            campaigns.
        targeting_setting (google.ads.googleads.v4.common.types.TargetingSetting):
            Setting for targeting related features.
        geo_target_type_setting (google.ads.googleads.v4.resources.types.Campaign.GeoTargetTypeSetting):
            The setting for ads geotargeting.
        local_campaign_setting (google.ads.googleads.v4.resources.types.Campaign.LocalCampaignSetting):
            The setting for local campaign.
        app_campaign_setting (google.ads.googleads.v4.resources.types.Campaign.AppCampaignSetting):
            The setting related to App Campaign.
        labels (Sequence[google.protobuf.wrappers_pb2.StringValue]):
            Output only. The resource names of labels
            attached to this campaign.
        experiment_type (google.ads.googleads.v4.enums.types.CampaignExperimentTypeEnum.CampaignExperimentType):
            Output only. The type of campaign: normal,
            draft, or experiment.
        base_campaign (google.protobuf.wrappers_pb2.StringValue):
            Output only. The resource name of the base campaign of a
            draft or experiment campaign. For base campaigns, this is
            equal to ``resource_name``.

            This field is read-only.
        campaign_budget (google.protobuf.wrappers_pb2.StringValue):
            The budget of the campaign.
        bidding_strategy_type (google.ads.googleads.v4.enums.types.BiddingStrategyTypeEnum.BiddingStrategyType):
            Output only. The type of bidding strategy.

            A bidding strategy can be created by setting either the
            bidding scheme to create a standard bidding strategy or the
            ``bidding_strategy`` field to create a portfolio bidding
            strategy.

            This field is read-only.
        start_date (google.protobuf.wrappers_pb2.StringValue):
            The date when campaign started.
            This field must not be used in WHERE clauses.
        end_date (google.protobuf.wrappers_pb2.StringValue):
            The date when campaign ended.
            This field must not be used in WHERE clauses.
        final_url_suffix (google.protobuf.wrappers_pb2.StringValue):
            Suffix used to append query parameters to
            landing pages that are served with parallel
            tracking.
        frequency_caps (Sequence[google.ads.googleads.v4.common.types.FrequencyCapEntry]):
            A list that limits how often each user will
            see this campaign's ads.
        video_brand_safety_suitability (google.ads.googleads.v4.enums.types.BrandSafetySuitabilityEnum.BrandSafetySuitability):
            Output only. 3-Tier Brand Safety setting for
            the campaign.
        vanity_pharma (google.ads.googleads.v4.resources.types.Campaign.VanityPharma):
            Describes how unbranded pharma ads will be
            displayed.
        selective_optimization (google.ads.googleads.v4.resources.types.Campaign.SelectiveOptimization):
            Selective optimization setting for this
            campaign, which includes a set of conversion
            actions to optimize this campaign towards.
        optimization_goal_setting (google.ads.googleads.v4.resources.types.Campaign.OptimizationGoalSetting):
            Optimization goal setting for this campaign,
            which includes a set of optimization goal types.
        tracking_setting (google.ads.googleads.v4.resources.types.Campaign.TrackingSetting):
            Output only. Campaign-level settings for
            tracking information.
        payment_mode (google.ads.googleads.v4.enums.types.PaymentModeEnum.PaymentMode):
            Payment mode for the campaign.
        optimization_score (google.protobuf.wrappers_pb2.DoubleValue):
            Output only. Optimization score of the
            campaign.
            Optimization score is an estimate of how well a
            campaign is set to perform. It ranges from 0%
            (0.0) to 100% (1.0), with 100% indicating that
            the campaign is performing at full potential.
            This field is null for unscored campaigns.

            See "About optimization score" at
            https://support.google.com/google-
            ads/answer/9061546.
            This field is read-only.
        bidding_strategy (google.protobuf.wrappers_pb2.StringValue):
            Portfolio bidding strategy used by campaign.
        commission (google.ads.googleads.v4.common.types.Commission):
            Commission is an automatic bidding strategy
            in which the advertiser pays a certain portion
            of the conversion value.
        manual_cpc (google.ads.googleads.v4.common.types.ManualCpc):
            Standard Manual CPC bidding strategy.
            Manual click-based bidding where user pays per
            click.
        manual_cpm (google.ads.googleads.v4.common.types.ManualCpm):
            Standard Manual CPM bidding strategy.
            Manual impression-based bidding where user pays
            per thousand impressions.
        manual_cpv (google.ads.googleads.v4.common.types.ManualCpv):
            Output only. A bidding strategy that pays a
            configurable amount per video view.
        maximize_conversions (google.ads.googleads.v4.common.types.MaximizeConversions):
            Standard Maximize Conversions bidding
            strategy that automatically maximizes number of
            conversions while spending your budget.
        maximize_conversion_value (google.ads.googleads.v4.common.types.MaximizeConversionValue):
            Standard Maximize Conversion Value bidding
            strategy that automatically sets bids to
            maximize revenue while spending your budget.
        target_cpa (google.ads.googleads.v4.common.types.TargetCpa):
            Standard Target CPA bidding strategy that
            automatically sets bids to help get as many
            conversions as possible at the target cost-per-
            acquisition (CPA) you set.
        target_impression_share (google.ads.googleads.v4.common.types.TargetImpressionShare):
            Target Impression Share bidding strategy. An
            automated bidding strategy that sets bids to
            achieve a desired percentage of impressions.
        target_roas (google.ads.googleads.v4.common.types.TargetRoas):
            Standard Target ROAS bidding strategy that
            automatically maximizes revenue while averaging
            a specific target return on ad spend (ROAS).
        target_spend (google.ads.googleads.v4.common.types.TargetSpend):
            Standard Target Spend bidding strategy that
            automatically sets your bids to help get as many
            clicks as possible within your budget.
        percent_cpc (google.ads.googleads.v4.common.types.PercentCpc):
            Standard Percent Cpc bidding strategy where
            bids are a fraction of the advertised price for
            some good or service.
        target_cpm (google.ads.googleads.v4.common.types.TargetCpm):
            A bidding strategy that automatically
            optimizes cost per thousand impressions.
    """

    class NetworkSettings(proto.Message):
        r"""The network settings for the campaign.

        Attributes:
            target_google_search (google.protobuf.wrappers_pb2.BoolValue):
                Whether ads will be served with google.com
                search results.
            target_search_network (google.protobuf.wrappers_pb2.BoolValue):
                Whether ads will be served on partner sites in the Google
                Search Network (requires ``target_google_search`` to also be
                ``true``).
            target_content_network (google.protobuf.wrappers_pb2.BoolValue):
                Whether ads will be served on specified
                placements in the Google Display Network.
                Placements are specified using the Placement
                criterion.
            target_partner_search_network (google.protobuf.wrappers_pb2.BoolValue):
                Whether ads will be served on the Google
                Partner Network. This is available only to some
                select Google partner accounts.
        """

        target_google_search = proto.Field(
            proto.MESSAGE, number=1, message=wrappers.BoolValue,
        )
        target_search_network = proto.Field(
            proto.MESSAGE, number=2, message=wrappers.BoolValue,
        )
        target_content_network = proto.Field(
            proto.MESSAGE, number=3, message=wrappers.BoolValue,
        )
        target_partner_search_network = proto.Field(
            proto.MESSAGE, number=4, message=wrappers.BoolValue,
        )

    class HotelSettingInfo(proto.Message):
        r"""Campaign-level settings for hotel ads.

        Attributes:
            hotel_center_id (google.protobuf.wrappers_pb2.Int64Value):
                Immutable. The linked Hotel Center account.
        """

        hotel_center_id = proto.Field(
            proto.MESSAGE, number=1, message=wrappers.Int64Value,
        )

    class SelectiveOptimization(proto.Message):
        r"""Selective optimization setting for this campaign, which
        includes a set of conversion actions to optimize this campaign
        towards.

        Attributes:
            conversion_actions (Sequence[google.protobuf.wrappers_pb2.StringValue]):
                The selected set of conversion actions for
                optimizing this campaign.
        """

        conversion_actions = proto.RepeatedField(
            proto.MESSAGE, number=1, message=wrappers.StringValue,
        )

    class OptimizationGoalSetting(proto.Message):
        r"""Optimization goal setting for this campaign, which includes a
        set of optimization goal types.

        Attributes:
            optimization_goal_types (Sequence[google.ads.googleads.v4.enums.types.OptimizationGoalTypeEnum.OptimizationGoalType]):
                The list of optimization goal types.
        """

        optimization_goal_types = proto.RepeatedField(
            proto.ENUM,
            number=1,
            enum=optimization_goal_type.OptimizationGoalTypeEnum.OptimizationGoalType,
        )

    class DynamicSearchAdsSetting(proto.Message):
        r"""The setting for controlling Dynamic Search Ads (DSA).

        Attributes:
            domain_name (google.protobuf.wrappers_pb2.StringValue):
                The Internet domain name that this setting
                represents, e.g., "google.com" or
                "www.google.com".
            language_code (google.protobuf.wrappers_pb2.StringValue):
                The language code specifying the language of
                the domain, e.g., "en".
            use_supplied_urls_only (google.protobuf.wrappers_pb2.BoolValue):
                Whether the campaign uses advertiser supplied
                URLs exclusively.
            feeds (Sequence[google.protobuf.wrappers_pb2.StringValue]):
                Output only. The list of page feeds
                associated with the campaign.
        """

        domain_name = proto.Field(
            proto.MESSAGE, number=1, message=wrappers.StringValue,
        )
        language_code = proto.Field(
            proto.MESSAGE, number=2, message=wrappers.StringValue,
        )
        use_supplied_urls_only = proto.Field(
            proto.MESSAGE, number=3, message=wrappers.BoolValue,
        )
        feeds = proto.RepeatedField(
            proto.MESSAGE, number=5, message=wrappers.StringValue,
        )

    class ShoppingSetting(proto.Message):
        r"""The setting for Shopping campaigns. Defines the universe of
        products that can be advertised by the campaign, and how this
        campaign interacts with other Shopping campaigns.

        Attributes:
            merchant_id (google.protobuf.wrappers_pb2.Int64Value):
                Immutable. ID of the Merchant Center account.
                This field is required for create operations.
                This field is immutable for Shopping campaigns.
            sales_country (google.protobuf.wrappers_pb2.StringValue):
                Immutable. Sales country of products to
                include in the campaign. This field is required
                for Shopping campaigns. This field is immutable.
                This field is optional for non-Shopping
                campaigns, but it must be equal to 'ZZ' if set.
            campaign_priority (google.protobuf.wrappers_pb2.Int32Value):
                Priority of the campaign. Campaigns with
                numerically higher priorities take precedence
                over those with lower priorities. This field is
                required for Shopping campaigns, with values
                between 0 and 2, inclusive.
                This field is optional for Smart Shopping
                campaigns, but must be equal to 3 if set.
            enable_local (google.protobuf.wrappers_pb2.BoolValue):
                Whether to include local products.
        """

        merchant_id = proto.Field(
            proto.MESSAGE, number=1, message=wrappers.Int64Value,
        )
        sales_country = proto.Field(
            proto.MESSAGE, number=2, message=wrappers.StringValue,
        )
        campaign_priority = proto.Field(
            proto.MESSAGE, number=3, message=wrappers.Int32Value,
        )
        enable_local = proto.Field(
            proto.MESSAGE, number=4, message=wrappers.BoolValue,
        )

    class TrackingSetting(proto.Message):
        r"""Campaign-level settings for tracking information.

        Attributes:
            tracking_url (google.protobuf.wrappers_pb2.StringValue):
                Output only. The url used for dynamic
                tracking.
        """

        tracking_url = proto.Field(
            proto.MESSAGE, number=1, message=wrappers.StringValue,
        )

    class GeoTargetTypeSetting(proto.Message):
        r"""Represents a collection of settings related to ads
        geotargeting.

        Attributes:
            positive_geo_target_type (google.ads.googleads.v4.enums.types.PositiveGeoTargetTypeEnum.PositiveGeoTargetType):
                The setting used for positive geotargeting in
                this particular campaign.
            negative_geo_target_type (google.ads.googleads.v4.enums.types.NegativeGeoTargetTypeEnum.NegativeGeoTargetType):
                The setting used for negative geotargeting in
                this particular campaign.
        """

        positive_geo_target_type = proto.Field(
            proto.ENUM,
            number=1,
            enum=gage_positive_geo_target_type.PositiveGeoTargetTypeEnum.PositiveGeoTargetType,
        )
        negative_geo_target_type = proto.Field(
            proto.ENUM,
            number=2,
            enum=gage_negative_geo_target_type.NegativeGeoTargetTypeEnum.NegativeGeoTargetType,
        )

    class VanityPharma(proto.Message):
        r"""Describes how unbranded pharma ads will be displayed.

        Attributes:
            vanity_pharma_display_url_mode (google.ads.googleads.v4.enums.types.VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode):
                The display mode for vanity pharma URLs.
            vanity_pharma_text (google.ads.googleads.v4.enums.types.VanityPharmaTextEnum.VanityPharmaText):
                The text that will be displayed in display
                URL of the text ad when website description is
                the selected display mode for vanity pharma
                URLs.
        """

        vanity_pharma_display_url_mode = proto.Field(
            proto.ENUM,
            number=1,
            enum=gage_vanity_pharma_display_url_mode.VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode,
        )
        vanity_pharma_text = proto.Field(
            proto.ENUM,
            number=2,
            enum=gage_vanity_pharma_text.VanityPharmaTextEnum.VanityPharmaText,
        )

    class LocalCampaignSetting(proto.Message):
        r"""Campaign setting for local campaigns.

        Attributes:
            location_source_type (google.ads.googleads.v4.enums.types.LocationSourceTypeEnum.LocationSourceType):
                The location source type for this local
                campaign.
        """

        location_source_type = proto.Field(
            proto.ENUM,
            number=1,
            enum=gage_location_source_type.LocationSourceTypeEnum.LocationSourceType,
        )

    class AppCampaignSetting(proto.Message):
        r"""Campaign-level settings for App Campaigns.

        Attributes:
            bidding_strategy_goal_type (google.ads.googleads.v4.enums.types.AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType):
                Represents the goal which the bidding
                strategy of this app campaign should optimize
                towards.
            app_id (google.protobuf.wrappers_pb2.StringValue):
                Immutable. A string that uniquely identifies
                a mobile application.
            app_store (google.ads.googleads.v4.enums.types.AppCampaignAppStoreEnum.AppCampaignAppStore):
                Immutable. The application store that
                distributes this specific app.
        """

        bidding_strategy_goal_type = proto.Field(
            proto.ENUM,
            number=1,
            enum=app_campaign_bidding_strategy_goal_type.AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType,
        )
        app_id = proto.Field(
            proto.MESSAGE, number=2, message=wrappers.StringValue,
        )
        app_store = proto.Field(
            proto.ENUM,
            number=3,
            enum=app_campaign_app_store.AppCampaignAppStoreEnum.AppCampaignAppStore,
        )

    resource_name = proto.Field(proto.STRING, number=1)
    id = proto.Field(proto.MESSAGE, number=3, message=wrappers.Int64Value,)
    name = proto.Field(proto.MESSAGE, number=4, message=wrappers.StringValue,)
    status = proto.Field(
        proto.ENUM,
        number=5,
        enum=campaign_status.CampaignStatusEnum.CampaignStatus,
    )
    serving_status = proto.Field(
        proto.ENUM,
        number=21,
        enum=campaign_serving_status.CampaignServingStatusEnum.CampaignServingStatus,
    )
    ad_serving_optimization_status = proto.Field(
        proto.ENUM,
        number=8,
        enum=gage_ad_serving_optimization_status.AdServingOptimizationStatusEnum.AdServingOptimizationStatus,
    )
    advertising_channel_type = proto.Field(
        proto.ENUM,
        number=9,
        enum=gage_advertising_channel_type.AdvertisingChannelTypeEnum.AdvertisingChannelType,
    )
    advertising_channel_sub_type = proto.Field(
        proto.ENUM,
        number=10,
        enum=gage_advertising_channel_sub_type.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType,
    )
    tracking_url_template = proto.Field(
        proto.MESSAGE, number=11, message=wrappers.StringValue,
    )
    url_custom_parameters = proto.RepeatedField(
        proto.MESSAGE, number=12, message=custom_parameter.CustomParameter,
    )
    real_time_bidding_setting = proto.Field(
        proto.MESSAGE,
        number=39,
        message=gagc_real_time_bidding_setting.RealTimeBiddingSetting,
    )
    network_settings = proto.Field(
        proto.MESSAGE, number=14, message=NetworkSettings,
    )
    hotel_setting = proto.Field(
        proto.MESSAGE, number=32, message=HotelSettingInfo,
    )
    dynamic_search_ads_setting = proto.Field(
        proto.MESSAGE, number=33, message=DynamicSearchAdsSetting,
    )
    shopping_setting = proto.Field(
        proto.MESSAGE, number=36, message=ShoppingSetting,
    )
    targeting_setting = proto.Field(
        proto.MESSAGE,
        number=43,
        message=gagc_targeting_setting.TargetingSetting,
    )
    geo_target_type_setting = proto.Field(
        proto.MESSAGE, number=47, message=GeoTargetTypeSetting,
    )
    local_campaign_setting = proto.Field(
        proto.MESSAGE, number=50, message=LocalCampaignSetting,
    )
    app_campaign_setting = proto.Field(
        proto.MESSAGE, number=51, message=AppCampaignSetting,
    )
    labels = proto.RepeatedField(
        proto.MESSAGE, number=53, message=wrappers.StringValue,
    )
    experiment_type = proto.Field(
        proto.ENUM,
        number=17,
        enum=campaign_experiment_type.CampaignExperimentTypeEnum.CampaignExperimentType,
    )
    base_campaign = proto.Field(
        proto.MESSAGE, number=28, message=wrappers.StringValue,
    )
    campaign_budget = proto.Field(
        proto.MESSAGE, number=6, message=wrappers.StringValue,
    )
    bidding_strategy_type = proto.Field(
        proto.ENUM,
        number=22,
        enum=gage_bidding_strategy_type.BiddingStrategyTypeEnum.BiddingStrategyType,
    )
    start_date = proto.Field(
        proto.MESSAGE, number=19, message=wrappers.StringValue,
    )
    end_date = proto.Field(
        proto.MESSAGE, number=20, message=wrappers.StringValue,
    )
    final_url_suffix = proto.Field(
        proto.MESSAGE, number=38, message=wrappers.StringValue,
    )
    frequency_caps = proto.RepeatedField(
        proto.MESSAGE, number=40, message=frequency_cap.FrequencyCapEntry,
    )
    video_brand_safety_suitability = proto.Field(
        proto.ENUM,
        number=42,
        enum=brand_safety_suitability.BrandSafetySuitabilityEnum.BrandSafetySuitability,
    )
    vanity_pharma = proto.Field(proto.MESSAGE, number=44, message=VanityPharma,)
    selective_optimization = proto.Field(
        proto.MESSAGE, number=45, message=SelectiveOptimization,
    )
    optimization_goal_setting = proto.Field(
        proto.MESSAGE, number=54, message=OptimizationGoalSetting,
    )
    tracking_setting = proto.Field(
        proto.MESSAGE, number=46, message=TrackingSetting,
    )
    payment_mode = proto.Field(
        proto.ENUM,
        number=52,
        enum=gage_payment_mode.PaymentModeEnum.PaymentMode,
    )
    optimization_score = proto.Field(
        proto.MESSAGE, number=55, message=wrappers.DoubleValue,
    )
    bidding_strategy = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="campaign_bidding_strategy",
        message=wrappers.StringValue,
    )
    commission = proto.Field(
        proto.MESSAGE,
        number=49,
        oneof="campaign_bidding_strategy",
        message=bidding.Commission,
    )
    manual_cpc = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="campaign_bidding_strategy",
        message=bidding.ManualCpc,
    )
    manual_cpm = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="campaign_bidding_strategy",
        message=bidding.ManualCpm,
    )
    manual_cpv = proto.Field(
        proto.MESSAGE,
        number=37,
        oneof="campaign_bidding_strategy",
        message=bidding.ManualCpv,
    )
    maximize_conversions = proto.Field(
        proto.MESSAGE,
        number=30,
        oneof="campaign_bidding_strategy",
        message=bidding.MaximizeConversions,
    )
    maximize_conversion_value = proto.Field(
        proto.MESSAGE,
        number=31,
        oneof="campaign_bidding_strategy",
        message=bidding.MaximizeConversionValue,
    )
    target_cpa = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="campaign_bidding_strategy",
        message=bidding.TargetCpa,
    )
    target_impression_share = proto.Field(
        proto.MESSAGE,
        number=48,
        oneof="campaign_bidding_strategy",
        message=bidding.TargetImpressionShare,
    )
    target_roas = proto.Field(
        proto.MESSAGE,
        number=29,
        oneof="campaign_bidding_strategy",
        message=bidding.TargetRoas,
    )
    target_spend = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="campaign_bidding_strategy",
        message=bidding.TargetSpend,
    )
    percent_cpc = proto.Field(
        proto.MESSAGE,
        number=34,
        oneof="campaign_bidding_strategy",
        message=bidding.PercentCpc,
    )
    target_cpm = proto.Field(
        proto.MESSAGE,
        number=41,
        oneof="campaign_bidding_strategy",
        message=bidding.TargetCpm,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
