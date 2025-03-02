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


from google.ads.googleads.v4.common.types import ad_asset
from google.ads.googleads.v4.enums.types import call_conversion_reporting_state
from google.ads.googleads.v4.enums.types import display_ad_format_setting
from google.ads.googleads.v4.enums.types import (
    display_upload_product_type as gage_display_upload_product_type,
)
from google.ads.googleads.v4.enums.types import legacy_app_install_ad_app_store
from google.ads.googleads.v4.enums.types import mime_type as gage_mime_type
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.common",
    marshal="google.ads.googleads.v4",
    manifest={
        "TextAdInfo",
        "ExpandedTextAdInfo",
        "CallOnlyAdInfo",
        "ExpandedDynamicSearchAdInfo",
        "HotelAdInfo",
        "ShoppingSmartAdInfo",
        "ShoppingProductAdInfo",
        "ShoppingComparisonListingAdInfo",
        "GmailAdInfo",
        "GmailTeaser",
        "DisplayCallToAction",
        "ProductImage",
        "ProductVideo",
        "ImageAdInfo",
        "VideoBumperInStreamAdInfo",
        "VideoNonSkippableInStreamAdInfo",
        "VideoTrueViewInStreamAdInfo",
        "VideoOutstreamAdInfo",
        "VideoTrueViewDiscoveryAdInfo",
        "VideoAdInfo",
        "ResponsiveSearchAdInfo",
        "LegacyResponsiveDisplayAdInfo",
        "AppAdInfo",
        "AppEngagementAdInfo",
        "LegacyAppInstallAdInfo",
        "ResponsiveDisplayAdInfo",
        "LocalAdInfo",
        "DisplayUploadAdInfo",
    },
)


class TextAdInfo(proto.Message):
    r"""A text ad.

    Attributes:
        headline (google.protobuf.wrappers_pb2.StringValue):
            The headline of the ad.
        description1 (google.protobuf.wrappers_pb2.StringValue):
            The first line of the ad's description.
        description2 (google.protobuf.wrappers_pb2.StringValue):
            The second line of the ad's description.
    """

    headline = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )
    description1 = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    description2 = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )


class ExpandedTextAdInfo(proto.Message):
    r"""An expanded text ad.

    Attributes:
        headline_part1 (google.protobuf.wrappers_pb2.StringValue):
            The first part of the ad's headline.
        headline_part2 (google.protobuf.wrappers_pb2.StringValue):
            The second part of the ad's headline.
        headline_part3 (google.protobuf.wrappers_pb2.StringValue):
            The third part of the ad's headline.
        description (google.protobuf.wrappers_pb2.StringValue):
            The description of the ad.
        description2 (google.protobuf.wrappers_pb2.StringValue):
            The second description of the ad.
        path1 (google.protobuf.wrappers_pb2.StringValue):
            The text that can appear alongside the ad's
            displayed URL.
        path2 (google.protobuf.wrappers_pb2.StringValue):
            Additional text that can appear alongside the
            ad's displayed URL.
    """

    headline_part1 = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )
    headline_part2 = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    headline_part3 = proto.Field(
        proto.MESSAGE, number=6, message=wrappers.StringValue,
    )
    description = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )
    description2 = proto.Field(
        proto.MESSAGE, number=7, message=wrappers.StringValue,
    )
    path1 = proto.Field(proto.MESSAGE, number=4, message=wrappers.StringValue,)
    path2 = proto.Field(proto.MESSAGE, number=5, message=wrappers.StringValue,)


class CallOnlyAdInfo(proto.Message):
    r"""A call-only ad.

    Attributes:
        country_code (google.protobuf.wrappers_pb2.StringValue):
            The country code in the ad.
        phone_number (google.protobuf.wrappers_pb2.StringValue):
            The phone number in the ad.
        business_name (google.protobuf.wrappers_pb2.StringValue):
            The business name in the ad.
        headline1 (google.protobuf.wrappers_pb2.StringValue):
            First headline in the ad.
        headline2 (google.protobuf.wrappers_pb2.StringValue):
            Second headline in the ad.
        description1 (google.protobuf.wrappers_pb2.StringValue):
            The first line of the ad's description.
        description2 (google.protobuf.wrappers_pb2.StringValue):
            The second line of the ad's description.
        call_tracked (google.protobuf.wrappers_pb2.BoolValue):
            Whether to enable call tracking for the
            creative. Enabling call tracking also enables
            call conversions.
        disable_call_conversion (google.protobuf.wrappers_pb2.BoolValue):
            Whether to disable call conversion for the creative. If set
            to ``true``, disables call conversions even when
            ``call_tracked`` is ``true``. If ``call_tracked`` is
            ``false``, this field is ignored.
        phone_number_verification_url (google.protobuf.wrappers_pb2.StringValue):
            The URL to be used for phone number
            verification.
        conversion_action (google.protobuf.wrappers_pb2.StringValue):
            The conversion action to attribute a call conversion to. If
            not set a default conversion action is used. This field only
            has effect if call_tracked is set to true. Otherwise this
            field is ignored.
        conversion_reporting_state (google.ads.googleads.v4.enums.types.CallConversionReportingStateEnum.CallConversionReportingState):
            The call conversion behavior of this call
            only ad. It can use its own call conversion
            setting, inherit the account level setting, or
            be disabled.
    """

    country_code = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )
    phone_number = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    business_name = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )
    headline1 = proto.Field(
        proto.MESSAGE, number=11, message=wrappers.StringValue,
    )
    headline2 = proto.Field(
        proto.MESSAGE, number=12, message=wrappers.StringValue,
    )
    description1 = proto.Field(
        proto.MESSAGE, number=4, message=wrappers.StringValue,
    )
    description2 = proto.Field(
        proto.MESSAGE, number=5, message=wrappers.StringValue,
    )
    call_tracked = proto.Field(
        proto.MESSAGE, number=6, message=wrappers.BoolValue,
    )
    disable_call_conversion = proto.Field(
        proto.MESSAGE, number=7, message=wrappers.BoolValue,
    )
    phone_number_verification_url = proto.Field(
        proto.MESSAGE, number=8, message=wrappers.StringValue,
    )
    conversion_action = proto.Field(
        proto.MESSAGE, number=9, message=wrappers.StringValue,
    )
    conversion_reporting_state = proto.Field(
        proto.ENUM,
        number=10,
        enum=call_conversion_reporting_state.CallConversionReportingStateEnum.CallConversionReportingState,
    )


class ExpandedDynamicSearchAdInfo(proto.Message):
    r"""An expanded dynamic search ad.

    Attributes:
        description (google.protobuf.wrappers_pb2.StringValue):
            The description of the ad.
        description2 (google.protobuf.wrappers_pb2.StringValue):
            The second description of the ad.
    """

    description = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )
    description2 = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )


class HotelAdInfo(proto.Message):
    r"""A hotel ad."""


class ShoppingSmartAdInfo(proto.Message):
    r"""A Smart Shopping ad."""


class ShoppingProductAdInfo(proto.Message):
    r"""A standard Shopping ad."""


class ShoppingComparisonListingAdInfo(proto.Message):
    r"""A Shopping Comparison Listing ad.

    Attributes:
        headline (google.protobuf.wrappers_pb2.StringValue):
            Headline of the ad. This field is required.
            Allowed length is between 25 and 45 characters.
    """

    headline = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )


class GmailAdInfo(proto.Message):
    r"""A Gmail ad.

    Attributes:
        teaser (google.ads.googleads.v4.common.types.GmailTeaser):
            The Gmail teaser.
        header_image (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource name of the header
            image. Valid image types are GIF, JPEG and PNG.
            The minimum size is 300x100 pixels and the
            aspect ratio must be between 3:1 and 5:1 (+-1%).
        marketing_image (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource name of the marketing
            image. Valid image types are GIF, JPEG and PNG.
            The image must either be landscape with a
            minimum size of 600x314 pixels and aspect ratio
            of 600:314 (+-1%) or square with a minimum size
            of 300x300 pixels and aspect ratio of 1:1 (+-1%)
        marketing_image_headline (google.protobuf.wrappers_pb2.StringValue):
            Headline of the marketing image.
        marketing_image_description (google.protobuf.wrappers_pb2.StringValue):
            Description of the marketing image.
        marketing_image_display_call_to_action (google.ads.googleads.v4.common.types.DisplayCallToAction):
            Display-call-to-action of the marketing
            image.
        product_images (Sequence[google.ads.googleads.v4.common.types.ProductImage]):
            Product images. Up to 15 images are
            supported.
        product_videos (Sequence[google.ads.googleads.v4.common.types.ProductVideo]):
            Product videos. Up to 7 videos are supported.
            At least one product video or a marketing image
            must be specified.
    """

    teaser = proto.Field(proto.MESSAGE, number=1, message="GmailTeaser",)
    header_image = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    marketing_image = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )
    marketing_image_headline = proto.Field(
        proto.MESSAGE, number=4, message=wrappers.StringValue,
    )
    marketing_image_description = proto.Field(
        proto.MESSAGE, number=5, message=wrappers.StringValue,
    )
    marketing_image_display_call_to_action = proto.Field(
        proto.MESSAGE, number=6, message="DisplayCallToAction",
    )
    product_images = proto.RepeatedField(
        proto.MESSAGE, number=7, message="ProductImage",
    )
    product_videos = proto.RepeatedField(
        proto.MESSAGE, number=8, message="ProductVideo",
    )


class GmailTeaser(proto.Message):
    r"""Gmail teaser data. The teaser is a small header that acts as
    an invitation to view the rest of the ad (the body).

    Attributes:
        headline (google.protobuf.wrappers_pb2.StringValue):
            Headline of the teaser.
        description (google.protobuf.wrappers_pb2.StringValue):
            Description of the teaser.
        business_name (google.protobuf.wrappers_pb2.StringValue):
            Business name of the advertiser.
        logo_image (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource name of the logo
            image. Valid image types are GIF, JPEG and PNG.
            The minimum size is 144x144 pixels and the
            aspect ratio must be 1:1 (+-1%).
    """

    headline = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )
    description = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    business_name = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )
    logo_image = proto.Field(
        proto.MESSAGE, number=4, message=wrappers.StringValue,
    )


class DisplayCallToAction(proto.Message):
    r"""Data for display call to action. The call to action is a
    piece of the ad that prompts the user to do something. Like
    clicking a link or making a phone call.

    Attributes:
        text (google.protobuf.wrappers_pb2.StringValue):
            Text for the display-call-to-action.
        text_color (google.protobuf.wrappers_pb2.StringValue):
            Text color for the display-call-to-action in
            hexadecimal, e.g. #ffffff for white.
        url_collection_id (google.protobuf.wrappers_pb2.StringValue):
            Identifies the url collection in the ad.url_collections
            field. If not set the url defaults to final_url.
    """

    text = proto.Field(proto.MESSAGE, number=1, message=wrappers.StringValue,)
    text_color = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    url_collection_id = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )


class ProductImage(proto.Message):
    r"""Product image specific data.

    Attributes:
        product_image (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource name of the product
            image. Valid image types are GIF, JPEG and PNG.
            The minimum size is 300x300 pixels and the
            aspect ratio must be 1:1 (+-1%).
        description (google.protobuf.wrappers_pb2.StringValue):
            Description of the product.
        display_call_to_action (google.ads.googleads.v4.common.types.DisplayCallToAction):
            Display-call-to-action of the product image.
    """

    product_image = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )
    description = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    display_call_to_action = proto.Field(
        proto.MESSAGE, number=3, message="DisplayCallToAction",
    )


class ProductVideo(proto.Message):
    r"""Product video specific data.

    Attributes:
        product_video (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource name of a video which
            must be hosted on YouTube.
    """

    product_video = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )


class ImageAdInfo(proto.Message):
    r"""An image ad.

    Attributes:
        pixel_width (google.protobuf.wrappers_pb2.Int64Value):
            Width in pixels of the full size image.
        pixel_height (google.protobuf.wrappers_pb2.Int64Value):
            Height in pixels of the full size image.
        image_url (google.protobuf.wrappers_pb2.StringValue):
            URL of the full size image.
        preview_pixel_width (google.protobuf.wrappers_pb2.Int64Value):
            Width in pixels of the preview size image.
        preview_pixel_height (google.protobuf.wrappers_pb2.Int64Value):
            Height in pixels of the preview size image.
        preview_image_url (google.protobuf.wrappers_pb2.StringValue):
            URL of the preview size image.
        mime_type (google.ads.googleads.v4.enums.types.MimeTypeEnum.MimeType):
            The mime type of the image.
        name (google.protobuf.wrappers_pb2.StringValue):
            The name of the image. If the image was
            created from a MediaFile, this is the
            MediaFile's name. If the image was created from
            bytes, this is empty.
        media_file (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource to use for the image.
        data (google.protobuf.wrappers_pb2.BytesValue):
            Raw image data as bytes.
        ad_id_to_copy_image_from (google.protobuf.wrappers_pb2.Int64Value):
            An ad ID to copy the image from.
    """

    pixel_width = proto.Field(
        proto.MESSAGE, number=4, message=wrappers.Int64Value,
    )
    pixel_height = proto.Field(
        proto.MESSAGE, number=5, message=wrappers.Int64Value,
    )
    image_url = proto.Field(
        proto.MESSAGE, number=6, message=wrappers.StringValue,
    )
    preview_pixel_width = proto.Field(
        proto.MESSAGE, number=7, message=wrappers.Int64Value,
    )
    preview_pixel_height = proto.Field(
        proto.MESSAGE, number=8, message=wrappers.Int64Value,
    )
    preview_image_url = proto.Field(
        proto.MESSAGE, number=9, message=wrappers.StringValue,
    )
    mime_type = proto.Field(
        proto.ENUM, number=10, enum=gage_mime_type.MimeTypeEnum.MimeType,
    )
    name = proto.Field(proto.MESSAGE, number=11, message=wrappers.StringValue,)
    media_file = proto.Field(
        proto.MESSAGE, number=1, oneof="image", message=wrappers.StringValue,
    )
    data = proto.Field(
        proto.MESSAGE, number=2, oneof="image", message=wrappers.BytesValue,
    )
    ad_id_to_copy_image_from = proto.Field(
        proto.MESSAGE, number=3, oneof="image", message=wrappers.Int64Value,
    )


class VideoBumperInStreamAdInfo(proto.Message):
    r"""Representation of video bumper in-stream ad format (very
    short in-stream non-skippable video ad).

    Attributes:
        companion_banner (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource name of the companion
            banner used with the ad.
    """

    companion_banner = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )


class VideoNonSkippableInStreamAdInfo(proto.Message):
    r"""Representation of video non-skippable in-stream ad format (15
    second in-stream non-skippable video ad).

    Attributes:
        companion_banner (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource name of the companion
            banner used with the ad.
    """

    companion_banner = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )


class VideoTrueViewInStreamAdInfo(proto.Message):
    r"""Representation of video TrueView in-stream ad format (ad
    shown during video playback, often at beginning, which displays
    a skip button a few seconds into the video).

    Attributes:
        action_button_label (google.protobuf.wrappers_pb2.StringValue):
            Label on the CTA (call-to-action) button
            taking the user to the video ad's final URL.
            Required for TrueView for action campaigns,
            optional otherwise.
        action_headline (google.protobuf.wrappers_pb2.StringValue):
            Additional text displayed with the CTA (call-
            o-action) button to give context and encourage
            clicking on the button.
        companion_banner (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource name of the companion
            banner used with the ad.
    """

    action_button_label = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )
    action_headline = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    companion_banner = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )


class VideoOutstreamAdInfo(proto.Message):
    r"""Representation of video out-stream ad format (ad shown
    alongside a feed with automatic playback, without sound).

    Attributes:
        headline (google.protobuf.wrappers_pb2.StringValue):
            The headline of the ad.
        description (google.protobuf.wrappers_pb2.StringValue):
            The description line.
    """

    headline = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )
    description = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )


class VideoTrueViewDiscoveryAdInfo(proto.Message):
    r"""Representation of video TrueView discovery ad format.

    Attributes:
        headline (google.protobuf.wrappers_pb2.StringValue):
            The headline of the ad.
        description1 (google.protobuf.wrappers_pb2.StringValue):
            First text line for a TrueView video
            discovery ad.
        description2 (google.protobuf.wrappers_pb2.StringValue):
            Second text line for a TrueView video
            discovery ad.
    """

    headline = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )
    description1 = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    description2 = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )


class VideoAdInfo(proto.Message):
    r"""A video ad.

    Attributes:
        media_file (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource to use for the video.
        in_stream (google.ads.googleads.v4.common.types.VideoTrueViewInStreamAdInfo):
            Video TrueView in-stream ad format.
        bumper (google.ads.googleads.v4.common.types.VideoBumperInStreamAdInfo):
            Video bumper in-stream ad format.
        out_stream (google.ads.googleads.v4.common.types.VideoOutstreamAdInfo):
            Video out-stream ad format.
        non_skippable (google.ads.googleads.v4.common.types.VideoNonSkippableInStreamAdInfo):
            Video non-skippable in-stream ad format.
        discovery (google.ads.googleads.v4.common.types.VideoTrueViewDiscoveryAdInfo):
            Video TrueView discovery ad format.
    """

    media_file = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )
    in_stream = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="format",
        message="VideoTrueViewInStreamAdInfo",
    )
    bumper = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="format",
        message="VideoBumperInStreamAdInfo",
    )
    out_stream = proto.Field(
        proto.MESSAGE, number=4, oneof="format", message="VideoOutstreamAdInfo",
    )
    non_skippable = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="format",
        message="VideoNonSkippableInStreamAdInfo",
    )
    discovery = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="format",
        message="VideoTrueViewDiscoveryAdInfo",
    )


class ResponsiveSearchAdInfo(proto.Message):
    r"""A responsive search ad.
    Responsive search ads let you create an ad that adapts to show
    more text, and more relevant messages, to your customers. Enter
    multiple headlines and descriptions when creating a responsive
    search ad, and over time, Google Ads will automatically test
    different combinations and learn which combinations perform
    best. By adapting your ad's content to more closely match
    potential customers' search terms, responsive search ads may
    improve your campaign's performance.

    More information at https://support.google.com/google-
    ads/answer/7684791

    Attributes:
        headlines (Sequence[google.ads.googleads.v4.common.types.AdTextAsset]):
            List of text assets for headlines. When the
            ad serves the headlines will be selected from
            this list.
        descriptions (Sequence[google.ads.googleads.v4.common.types.AdTextAsset]):
            List of text assets for descriptions. When
            the ad serves the descriptions will be selected
            from this list.
        path1 (google.protobuf.wrappers_pb2.StringValue):
            First part of text that may appear appended
            to the url displayed in the ad.
        path2 (google.protobuf.wrappers_pb2.StringValue):
            Second part of text that may appear appended
            to the url displayed in the ad. This field can
            only be set when path1 is also set.
    """

    headlines = proto.RepeatedField(
        proto.MESSAGE, number=1, message=ad_asset.AdTextAsset,
    )
    descriptions = proto.RepeatedField(
        proto.MESSAGE, number=2, message=ad_asset.AdTextAsset,
    )
    path1 = proto.Field(proto.MESSAGE, number=3, message=wrappers.StringValue,)
    path2 = proto.Field(proto.MESSAGE, number=4, message=wrappers.StringValue,)


class LegacyResponsiveDisplayAdInfo(proto.Message):
    r"""A legacy responsive display ad. Ads of this type are labeled
    'Responsive ads' in the Google Ads UI.

    Attributes:
        short_headline (google.protobuf.wrappers_pb2.StringValue):
            The short version of the ad's headline.
        long_headline (google.protobuf.wrappers_pb2.StringValue):
            The long version of the ad's headline.
        description (google.protobuf.wrappers_pb2.StringValue):
            The description of the ad.
        business_name (google.protobuf.wrappers_pb2.StringValue):
            The business name in the ad.
        allow_flexible_color (google.protobuf.wrappers_pb2.BoolValue):
            Advertiser's consent to allow flexible color. When true, the
            ad may be served with different color if necessary. When
            false, the ad will be served with the specified colors or a
            neutral color. The default value is true. Must be true if
            main_color and accent_color are not set.
        accent_color (google.protobuf.wrappers_pb2.StringValue):
            The accent color of the ad in hexadecimal, e.g. #ffffff for
            white. If one of main_color and accent_color is set, the
            other is required as well.
        main_color (google.protobuf.wrappers_pb2.StringValue):
            The main color of the ad in hexadecimal, e.g. #ffffff for
            white. If one of main_color and accent_color is set, the
            other is required as well.
        call_to_action_text (google.protobuf.wrappers_pb2.StringValue):
            The call-to-action text for the ad.
        logo_image (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource name of the logo image
            used in the ad.
        square_logo_image (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource name of the square
            logo image used in the ad.
        marketing_image (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource name of the marketing
            image used in the ad.
        square_marketing_image (google.protobuf.wrappers_pb2.StringValue):
            The MediaFile resource name of the square
            marketing image used in the ad.
        format_setting (google.ads.googleads.v4.enums.types.DisplayAdFormatSettingEnum.DisplayAdFormatSetting):
            Specifies which format the ad will be served in. Default is
            ALL_FORMATS.
        price_prefix (google.protobuf.wrappers_pb2.StringValue):
            Prefix before price. E.g. 'as low as'.
        promo_text (google.protobuf.wrappers_pb2.StringValue):
            Promotion text used for dyanmic formats of
            responsive ads. For example 'Free two-day
            shipping'.
    """

    short_headline = proto.Field(
        proto.MESSAGE, number=1, message=wrappers.StringValue,
    )
    long_headline = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )
    description = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )
    business_name = proto.Field(
        proto.MESSAGE, number=4, message=wrappers.StringValue,
    )
    allow_flexible_color = proto.Field(
        proto.MESSAGE, number=5, message=wrappers.BoolValue,
    )
    accent_color = proto.Field(
        proto.MESSAGE, number=6, message=wrappers.StringValue,
    )
    main_color = proto.Field(
        proto.MESSAGE, number=7, message=wrappers.StringValue,
    )
    call_to_action_text = proto.Field(
        proto.MESSAGE, number=8, message=wrappers.StringValue,
    )
    logo_image = proto.Field(
        proto.MESSAGE, number=9, message=wrappers.StringValue,
    )
    square_logo_image = proto.Field(
        proto.MESSAGE, number=10, message=wrappers.StringValue,
    )
    marketing_image = proto.Field(
        proto.MESSAGE, number=11, message=wrappers.StringValue,
    )
    square_marketing_image = proto.Field(
        proto.MESSAGE, number=12, message=wrappers.StringValue,
    )
    format_setting = proto.Field(
        proto.ENUM,
        number=13,
        enum=display_ad_format_setting.DisplayAdFormatSettingEnum.DisplayAdFormatSetting,
    )
    price_prefix = proto.Field(
        proto.MESSAGE, number=14, message=wrappers.StringValue,
    )
    promo_text = proto.Field(
        proto.MESSAGE, number=15, message=wrappers.StringValue,
    )


class AppAdInfo(proto.Message):
    r"""An app ad.

    Attributes:
        mandatory_ad_text (google.ads.googleads.v4.common.types.AdTextAsset):
            Mandatory ad text.
        headlines (Sequence[google.ads.googleads.v4.common.types.AdTextAsset]):
            List of text assets for headlines. When the
            ad serves the headlines will be selected from
            this list.
        descriptions (Sequence[google.ads.googleads.v4.common.types.AdTextAsset]):
            List of text assets for descriptions. When
            the ad serves the descriptions will be selected
            from this list.
        images (Sequence[google.ads.googleads.v4.common.types.AdImageAsset]):
            List of image assets that may be displayed
            with the ad.
        youtube_videos (Sequence[google.ads.googleads.v4.common.types.AdVideoAsset]):
            List of YouTube video assets that may be
            displayed with the ad.
        html5_media_bundles (Sequence[google.ads.googleads.v4.common.types.AdMediaBundleAsset]):
            List of media bundle assets that may be used
            with the ad.
    """

    mandatory_ad_text = proto.Field(
        proto.MESSAGE, number=1, message=ad_asset.AdTextAsset,
    )
    headlines = proto.RepeatedField(
        proto.MESSAGE, number=2, message=ad_asset.AdTextAsset,
    )
    descriptions = proto.RepeatedField(
        proto.MESSAGE, number=3, message=ad_asset.AdTextAsset,
    )
    images = proto.RepeatedField(
        proto.MESSAGE, number=4, message=ad_asset.AdImageAsset,
    )
    youtube_videos = proto.RepeatedField(
        proto.MESSAGE, number=5, message=ad_asset.AdVideoAsset,
    )
    html5_media_bundles = proto.RepeatedField(
        proto.MESSAGE, number=6, message=ad_asset.AdMediaBundleAsset,
    )


class AppEngagementAdInfo(proto.Message):
    r"""App engagement ads allow you to write text encouraging a
    specific action in the app, like checking in, making a purchase,
    or booking a flight. They allow you to send users to a specific
    part of your app where they can find what they're looking for
    easier and faster.

    Attributes:
        headlines (Sequence[google.ads.googleads.v4.common.types.AdTextAsset]):
            List of text assets for headlines. When the
            ad serves the headlines will be selected from
            this list.
        descriptions (Sequence[google.ads.googleads.v4.common.types.AdTextAsset]):
            List of text assets for descriptions. When
            the ad serves the descriptions will be selected
            from this list.
        images (Sequence[google.ads.googleads.v4.common.types.AdImageAsset]):
            List of image assets that may be displayed
            with the ad.
        videos (Sequence[google.ads.googleads.v4.common.types.AdVideoAsset]):
            List of video assets that may be displayed
            with the ad.
    """

    headlines = proto.RepeatedField(
        proto.MESSAGE, number=1, message=ad_asset.AdTextAsset,
    )
    descriptions = proto.RepeatedField(
        proto.MESSAGE, number=2, message=ad_asset.AdTextAsset,
    )
    images = proto.RepeatedField(
        proto.MESSAGE, number=3, message=ad_asset.AdImageAsset,
    )
    videos = proto.RepeatedField(
        proto.MESSAGE, number=4, message=ad_asset.AdVideoAsset,
    )


class LegacyAppInstallAdInfo(proto.Message):
    r"""A legacy app install ad that only can be used by a few select
    customers.

    Attributes:
        app_id (google.protobuf.wrappers_pb2.StringValue):
            The id of the mobile app.
        app_store (google.ads.googleads.v4.enums.types.LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore):
            The app store the mobile app is available in.
        headline (google.protobuf.wrappers_pb2.StringValue):
            The headline of the ad.
        description1 (google.protobuf.wrappers_pb2.StringValue):
            The first description line of the ad.
        description2 (google.protobuf.wrappers_pb2.StringValue):
            The second description line of the ad.
    """

    app_id = proto.Field(proto.MESSAGE, number=1, message=wrappers.StringValue,)
    app_store = proto.Field(
        proto.ENUM,
        number=2,
        enum=legacy_app_install_ad_app_store.LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore,
    )
    headline = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )
    description1 = proto.Field(
        proto.MESSAGE, number=4, message=wrappers.StringValue,
    )
    description2 = proto.Field(
        proto.MESSAGE, number=5, message=wrappers.StringValue,
    )


class ResponsiveDisplayAdInfo(proto.Message):
    r"""A responsive display ad.

    Attributes:
        marketing_images (Sequence[google.ads.googleads.v4.common.types.AdImageAsset]):
            Marketing images to be used in the ad. Valid image types are
            GIF, JPEG, and PNG. The minimum size is 600x314 and the
            aspect ratio must be 1.91:1 (+-1%). At least one
            marketing_image is required. Combined with
            square_marketing_images the maximum is 15.
        square_marketing_images (Sequence[google.ads.googleads.v4.common.types.AdImageAsset]):
            Square marketing images to be used in the ad. Valid image
            types are GIF, JPEG, and PNG. The minimum size is 300x300
            and the aspect ratio must be 1:1 (+-1%). At least one square
            marketing_image is required. Combined with marketing_images
            the maximum is 15.
        logo_images (Sequence[google.ads.googleads.v4.common.types.AdImageAsset]):
            Logo images to be used in the ad. Valid image types are GIF,
            JPEG, and PNG. The minimum size is 512x128 and the aspect
            ratio must be 4:1 (+-1%). Combined with square_logo_images
            the maximum is 5.
        square_logo_images (Sequence[google.ads.googleads.v4.common.types.AdImageAsset]):
            Square logo images to be used in the ad. Valid image types
            are GIF, JPEG, and PNG. The minimum size is 128x128 and the
            aspect ratio must be 1:1 (+-1%). Combined with
            square_logo_images the maximum is 5.
        headlines (Sequence[google.ads.googleads.v4.common.types.AdTextAsset]):
            Short format headlines for the ad. The
            maximum length is 30 characters. At least 1 and
            max 5 headlines can be specified.
        long_headline (google.ads.googleads.v4.common.types.AdTextAsset):
            A required long format headline. The maximum
            length is 90 characters.
        descriptions (Sequence[google.ads.googleads.v4.common.types.AdTextAsset]):
            Descriptive texts for the ad. The maximum
            length is 90 characters. At least 1 and max 5
            headlines can be specified.
        youtube_videos (Sequence[google.ads.googleads.v4.common.types.AdVideoAsset]):
            Optional YouTube videos for the ad. A maximum
            of 5 videos can be specified.
        business_name (google.protobuf.wrappers_pb2.StringValue):
            The advertiser/brand name. Maximum display
            width is 25.
        main_color (google.protobuf.wrappers_pb2.StringValue):
            The main color of the ad in hexadecimal, e.g. #ffffff for
            white. If one of main_color and accent_color is set, the
            other is required as well.
        accent_color (google.protobuf.wrappers_pb2.StringValue):
            The accent color of the ad in hexadecimal, e.g. #ffffff for
            white. If one of main_color and accent_color is set, the
            other is required as well.
        allow_flexible_color (google.protobuf.wrappers_pb2.BoolValue):
            Advertiser's consent to allow flexible color. When true, the
            ad may be served with different color if necessary. When
            false, the ad will be served with the specified colors or a
            neutral color. The default value is true. Must be true if
            main_color and accent_color are not set.
        call_to_action_text (google.protobuf.wrappers_pb2.StringValue):
            The call-to-action text for the ad. Maximum
            display width is 30.
        price_prefix (google.protobuf.wrappers_pb2.StringValue):
            Prefix before price. E.g. 'as low as'.
        promo_text (google.protobuf.wrappers_pb2.StringValue):
            Promotion text used for dyanmic formats of
            responsive ads. For example 'Free two-day
            shipping'.
        format_setting (google.ads.googleads.v4.enums.types.DisplayAdFormatSettingEnum.DisplayAdFormatSetting):
            Specifies which format the ad will be served in. Default is
            ALL_FORMATS.
    """

    marketing_images = proto.RepeatedField(
        proto.MESSAGE, number=1, message=ad_asset.AdImageAsset,
    )
    square_marketing_images = proto.RepeatedField(
        proto.MESSAGE, number=2, message=ad_asset.AdImageAsset,
    )
    logo_images = proto.RepeatedField(
        proto.MESSAGE, number=3, message=ad_asset.AdImageAsset,
    )
    square_logo_images = proto.RepeatedField(
        proto.MESSAGE, number=4, message=ad_asset.AdImageAsset,
    )
    headlines = proto.RepeatedField(
        proto.MESSAGE, number=5, message=ad_asset.AdTextAsset,
    )
    long_headline = proto.Field(
        proto.MESSAGE, number=6, message=ad_asset.AdTextAsset,
    )
    descriptions = proto.RepeatedField(
        proto.MESSAGE, number=7, message=ad_asset.AdTextAsset,
    )
    youtube_videos = proto.RepeatedField(
        proto.MESSAGE, number=8, message=ad_asset.AdVideoAsset,
    )
    business_name = proto.Field(
        proto.MESSAGE, number=9, message=wrappers.StringValue,
    )
    main_color = proto.Field(
        proto.MESSAGE, number=10, message=wrappers.StringValue,
    )
    accent_color = proto.Field(
        proto.MESSAGE, number=11, message=wrappers.StringValue,
    )
    allow_flexible_color = proto.Field(
        proto.MESSAGE, number=12, message=wrappers.BoolValue,
    )
    call_to_action_text = proto.Field(
        proto.MESSAGE, number=13, message=wrappers.StringValue,
    )
    price_prefix = proto.Field(
        proto.MESSAGE, number=14, message=wrappers.StringValue,
    )
    promo_text = proto.Field(
        proto.MESSAGE, number=15, message=wrappers.StringValue,
    )
    format_setting = proto.Field(
        proto.ENUM,
        number=16,
        enum=display_ad_format_setting.DisplayAdFormatSettingEnum.DisplayAdFormatSetting,
    )


class LocalAdInfo(proto.Message):
    r"""A local ad.

    Attributes:
        headlines (Sequence[google.ads.googleads.v4.common.types.AdTextAsset]):
            List of text assets for headlines. When the
            ad serves the headlines will be selected from
            this list. At least 1 and at most 5 headlines
            must be specified.
        descriptions (Sequence[google.ads.googleads.v4.common.types.AdTextAsset]):
            List of text assets for descriptions. When
            the ad serves the descriptions will be selected
            from this list. At least 1 and at most 5
            descriptions must be specified.
        call_to_actions (Sequence[google.ads.googleads.v4.common.types.AdTextAsset]):
            List of text assets for call-to-actions. When
            the ad serves the call-to-actions will be
            selected from this list. Call-to-actions are
            optional and at most 5 can be specified.
        marketing_images (Sequence[google.ads.googleads.v4.common.types.AdImageAsset]):
            List of marketing image assets that may be
            displayed with the ad. The images must be
            314x600 pixels or 320x320 pixels. At least 1 and
            at most 20 image assets must be specified.
        logo_images (Sequence[google.ads.googleads.v4.common.types.AdImageAsset]):
            List of logo image assets that may be
            displayed with the ad. The images must be
            128x128 pixels and not larger than 120KB. At
            least 1 and at most 5 image assets must be
            specified.
        videos (Sequence[google.ads.googleads.v4.common.types.AdVideoAsset]):
            List of YouTube video assets that may be
            displayed with the ad. Videos are optional and
            at most 20 can be specified.
        path1 (google.protobuf.wrappers_pb2.StringValue):
            First part of optional text that may appear
            appended to the url displayed in the ad.
        path2 (google.protobuf.wrappers_pb2.StringValue):
            Second part of optional text that may appear
            appended to the url displayed in the ad. This
            field can only be set when path1 is also set.
    """

    headlines = proto.RepeatedField(
        proto.MESSAGE, number=1, message=ad_asset.AdTextAsset,
    )
    descriptions = proto.RepeatedField(
        proto.MESSAGE, number=2, message=ad_asset.AdTextAsset,
    )
    call_to_actions = proto.RepeatedField(
        proto.MESSAGE, number=3, message=ad_asset.AdTextAsset,
    )
    marketing_images = proto.RepeatedField(
        proto.MESSAGE, number=4, message=ad_asset.AdImageAsset,
    )
    logo_images = proto.RepeatedField(
        proto.MESSAGE, number=5, message=ad_asset.AdImageAsset,
    )
    videos = proto.RepeatedField(
        proto.MESSAGE, number=6, message=ad_asset.AdVideoAsset,
    )
    path1 = proto.Field(proto.MESSAGE, number=7, message=wrappers.StringValue,)
    path2 = proto.Field(proto.MESSAGE, number=8, message=wrappers.StringValue,)


class DisplayUploadAdInfo(proto.Message):
    r"""A generic type of display ad. The exact ad format is controlled by
    the display_upload_product_type field, which determines what kinds
    of data need to be included with the ad.

    Attributes:
        display_upload_product_type (google.ads.googleads.v4.enums.types.DisplayUploadProductTypeEnum.DisplayUploadProductType):
            The product type of this ad. See comments on
            the enum for details.
        media_bundle (google.ads.googleads.v4.common.types.AdMediaBundleAsset):
            A media bundle asset to be used in the ad. For information
            about the media bundle for HTML5_UPLOAD_AD see
            https://support.google.com/google-ads/answer/1722096 Media
            bundles that are part of dynamic product types use a special
            format that needs to be created through the Google Web
            Designer. See
            https://support.google.com/webdesigner/answer/7543898 for
            more information.
    """

    display_upload_product_type = proto.Field(
        proto.ENUM,
        number=1,
        enum=gage_display_upload_product_type.DisplayUploadProductTypeEnum.DisplayUploadProductType,
    )
    media_bundle = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="media_asset",
        message=ad_asset.AdMediaBundleAsset,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
