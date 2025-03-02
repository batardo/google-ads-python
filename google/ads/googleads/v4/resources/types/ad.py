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


from google.ads.googleads.v4.common.types import ad_type_infos
from google.ads.googleads.v4.common.types import custom_parameter
from google.ads.googleads.v4.common.types import final_app_url
from google.ads.googleads.v4.common.types import url_collection
from google.ads.googleads.v4.enums.types import ad_type
from google.ads.googleads.v4.enums.types import device
from google.ads.googleads.v4.enums.types import system_managed_entity_source
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"Ad",},
)


class Ad(proto.Message):
    r"""An ad.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the ad. Ad resource names
            have the form:

            ``customers/{customer_id}/ads/{ad_id}``
        id (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The ID of the ad.
        final_urls (Sequence[google.protobuf.wrappers_pb2.StringValue]):
            The list of possible final URLs after all
            cross-domain redirects for the ad.
        final_app_urls (Sequence[google.ads.googleads.v4.common.types.FinalAppUrl]):
            A list of final app URLs that will be used on
            mobile if the user has the specific app
            installed.
        final_mobile_urls (Sequence[google.protobuf.wrappers_pb2.StringValue]):
            The list of possible final mobile URLs after
            all cross-domain redirects for the ad.
        tracking_url_template (google.protobuf.wrappers_pb2.StringValue):
            The URL template for constructing a tracking
            URL.
        final_url_suffix (google.protobuf.wrappers_pb2.StringValue):
            The suffix to use when constructing a final
            URL.
        url_custom_parameters (Sequence[google.ads.googleads.v4.common.types.CustomParameter]):
            The list of mappings that can be used to substitute custom
            parameter tags in a ``tracking_url_template``,
            ``final_urls``, or ``mobile_final_urls``. For mutates,
            please use url custom parameter operations.
        display_url (google.protobuf.wrappers_pb2.StringValue):
            The URL that appears in the ad description
            for some ad formats.
        type_ (google.ads.googleads.v4.enums.types.AdTypeEnum.AdType):
            Output only. The type of ad.
        added_by_google_ads (google.protobuf.wrappers_pb2.BoolValue):
            Output only. Indicates if this ad was
            automatically added by Google Ads and not by a
            user. For example, this could happen when ads
            are automatically created as suggestions for new
            ads based on knowledge of how existing ads are
            performing.
        device_preference (google.ads.googleads.v4.enums.types.DeviceEnum.Device):
            The device preference for the ad. You can
            only specify a preference for mobile devices.
            When this preference is set the ad will be
            preferred over other ads when being displayed on
            a mobile device. The ad can still be displayed
            on other device types, e.g. if no other ads are
            available. If unspecified (no device
            preference), all devices are targeted. This is
            only supported by some ad types.
        url_collections (Sequence[google.ads.googleads.v4.common.types.UrlCollection]):
            Additional URLs for the ad that are tagged
            with a unique identifier that can be referenced
            from other fields in the ad.
        name (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The name of the ad. This is only
            used to be able to identify the ad. It does not
            need to be unique and does not affect the served
            ad.
        system_managed_resource_source (google.ads.googleads.v4.enums.types.SystemManagedResourceSourceEnum.SystemManagedResourceSource):
            Output only. If this ad is system managed,
            then this field will indicate the source. This
            field is read-only.
        text_ad (google.ads.googleads.v4.common.types.TextAdInfo):
            Immutable. Details pertaining to a text ad.
        expanded_text_ad (google.ads.googleads.v4.common.types.ExpandedTextAdInfo):
            Details pertaining to an expanded text ad.
        call_only_ad (google.ads.googleads.v4.common.types.CallOnlyAdInfo):
            Details pertaining to a call-only ad.
        expanded_dynamic_search_ad (google.ads.googleads.v4.common.types.ExpandedDynamicSearchAdInfo):
            Immutable. Details pertaining to an Expanded Dynamic Search
            Ad. This type of ad has its headline, final URLs, and
            display URL auto-generated at serving time according to
            domain name specific information provided by
            ``dynamic_search_ads_setting`` linked at the campaign level.
        hotel_ad (google.ads.googleads.v4.common.types.HotelAdInfo):
            Details pertaining to a hotel ad.
        shopping_smart_ad (google.ads.googleads.v4.common.types.ShoppingSmartAdInfo):
            Details pertaining to a Smart Shopping ad.
        shopping_product_ad (google.ads.googleads.v4.common.types.ShoppingProductAdInfo):
            Details pertaining to a Shopping product ad.
        gmail_ad (google.ads.googleads.v4.common.types.GmailAdInfo):
            Immutable. Details pertaining to a Gmail ad.
        image_ad (google.ads.googleads.v4.common.types.ImageAdInfo):
            Immutable. Details pertaining to an Image ad.
        video_ad (google.ads.googleads.v4.common.types.VideoAdInfo):
            Details pertaining to a Video ad.
        responsive_search_ad (google.ads.googleads.v4.common.types.ResponsiveSearchAdInfo):
            Details pertaining to a responsive search ad.
        legacy_responsive_display_ad (google.ads.googleads.v4.common.types.LegacyResponsiveDisplayAdInfo):
            Details pertaining to a legacy responsive
            display ad.
        app_ad (google.ads.googleads.v4.common.types.AppAdInfo):
            Details pertaining to an app ad.
        legacy_app_install_ad (google.ads.googleads.v4.common.types.LegacyAppInstallAdInfo):
            Immutable. Details pertaining to a legacy app
            install ad.
        responsive_display_ad (google.ads.googleads.v4.common.types.ResponsiveDisplayAdInfo):
            Details pertaining to a responsive display
            ad.
        local_ad (google.ads.googleads.v4.common.types.LocalAdInfo):
            Details pertaining to a local ad.
        display_upload_ad (google.ads.googleads.v4.common.types.DisplayUploadAdInfo):
            Details pertaining to a display upload ad.
        app_engagement_ad (google.ads.googleads.v4.common.types.AppEngagementAdInfo):
            Details pertaining to an app engagement ad.
        shopping_comparison_listing_ad (google.ads.googleads.v4.common.types.ShoppingComparisonListingAdInfo):
            Details pertaining to a Shopping Comparison
            Listing ad.
    """

    resource_name = proto.Field(proto.STRING, number=37)
    id = proto.Field(proto.MESSAGE, number=1, message=wrappers.Int64Value,)
    final_urls = proto.RepeatedField(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    final_app_urls = proto.RepeatedField(
        proto.MESSAGE, number=35, message=final_app_url.FinalAppUrl,
    )
    final_mobile_urls = proto.RepeatedField(
        proto.MESSAGE, number=16, message=wrappers.StringValue,
    )
    tracking_url_template = proto.Field(
        proto.MESSAGE, number=12, message=wrappers.StringValue,
    )
    final_url_suffix = proto.Field(
        proto.MESSAGE, number=38, message=wrappers.StringValue,
    )
    url_custom_parameters = proto.RepeatedField(
        proto.MESSAGE, number=10, message=custom_parameter.CustomParameter,
    )
    display_url = proto.Field(
        proto.MESSAGE, number=4, message=wrappers.StringValue,
    )
    type_ = proto.Field(proto.ENUM, number=5, enum=ad_type.AdTypeEnum.AdType,)
    added_by_google_ads = proto.Field(
        proto.MESSAGE, number=19, message=wrappers.BoolValue,
    )
    device_preference = proto.Field(
        proto.ENUM, number=20, enum=device.DeviceEnum.Device,
    )
    url_collections = proto.RepeatedField(
        proto.MESSAGE, number=26, message=url_collection.UrlCollection,
    )
    name = proto.Field(proto.MESSAGE, number=23, message=wrappers.StringValue,)
    system_managed_resource_source = proto.Field(
        proto.ENUM,
        number=27,
        enum=system_managed_entity_source.SystemManagedResourceSourceEnum.SystemManagedResourceSource,
    )
    text_ad = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="ad_data",
        message=ad_type_infos.TextAdInfo,
    )
    expanded_text_ad = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="ad_data",
        message=ad_type_infos.ExpandedTextAdInfo,
    )
    call_only_ad = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="ad_data",
        message=ad_type_infos.CallOnlyAdInfo,
    )
    expanded_dynamic_search_ad = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="ad_data",
        message=ad_type_infos.ExpandedDynamicSearchAdInfo,
    )
    hotel_ad = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="ad_data",
        message=ad_type_infos.HotelAdInfo,
    )
    shopping_smart_ad = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="ad_data",
        message=ad_type_infos.ShoppingSmartAdInfo,
    )
    shopping_product_ad = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="ad_data",
        message=ad_type_infos.ShoppingProductAdInfo,
    )
    gmail_ad = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="ad_data",
        message=ad_type_infos.GmailAdInfo,
    )
    image_ad = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="ad_data",
        message=ad_type_infos.ImageAdInfo,
    )
    video_ad = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="ad_data",
        message=ad_type_infos.VideoAdInfo,
    )
    responsive_search_ad = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="ad_data",
        message=ad_type_infos.ResponsiveSearchAdInfo,
    )
    legacy_responsive_display_ad = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="ad_data",
        message=ad_type_infos.LegacyResponsiveDisplayAdInfo,
    )
    app_ad = proto.Field(
        proto.MESSAGE,
        number=29,
        oneof="ad_data",
        message=ad_type_infos.AppAdInfo,
    )
    legacy_app_install_ad = proto.Field(
        proto.MESSAGE,
        number=30,
        oneof="ad_data",
        message=ad_type_infos.LegacyAppInstallAdInfo,
    )
    responsive_display_ad = proto.Field(
        proto.MESSAGE,
        number=31,
        oneof="ad_data",
        message=ad_type_infos.ResponsiveDisplayAdInfo,
    )
    local_ad = proto.Field(
        proto.MESSAGE,
        number=32,
        oneof="ad_data",
        message=ad_type_infos.LocalAdInfo,
    )
    display_upload_ad = proto.Field(
        proto.MESSAGE,
        number=33,
        oneof="ad_data",
        message=ad_type_infos.DisplayUploadAdInfo,
    )
    app_engagement_ad = proto.Field(
        proto.MESSAGE,
        number=34,
        oneof="ad_data",
        message=ad_type_infos.AppEngagementAdInfo,
    )
    shopping_comparison_listing_ad = proto.Field(
        proto.MESSAGE,
        number=36,
        oneof="ad_data",
        message=ad_type_infos.ShoppingComparisonListingAdInfo,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
