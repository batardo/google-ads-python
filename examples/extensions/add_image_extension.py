#!/usr/bin/env python
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Adds an image extension to a campaign.

To create a campaign, run basic_operations/add_campaigns.py. To create an
image asset, run misc/upload_image_asset.py.
"""


import argparse
import sys

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException


def main(client, customer_id, campaign_id, image_asset_id):
    """The main method that creates all necessary entities for the example.

    Args:
        client: An initialized GoogleAdsClient instance.
        customer_id: The client customer ID str.
        campaign_id: A str of a campaign ID.
        image_asset_id: A str of an image asset ID.
    """
    extension_feed_item_service = client.get_service("ExtensionFeedItemService")
    extension_feed_item_operation = client.get_type(
        "ExtensionFeedItemOperation"
    )
    extension_feed_item = extension_feed_item_operation.create
    extension_feed_item.image_feed_item.image_asset = client.get_service(
        "AssetService"
    ).asset_path(customer_id, image_asset_id)

    response = extension_feed_item_service.mutate_extension_feed_items(
        customer_id=customer_id, operations=[extension_feed_item_operation]
    )
    image_resource_name = response.results[0].resource_name
    print(
        "Created an image extension with resource name: "
        f"'{image_resource_name}'"
    )

    campaign_extension_setting_service = client.get_service(
        "CampaignExtensionSettingService"
    )
    campaign_extension_setting_operation = client.get_type(
        "CampaignExtensionSettingOperation"
    )
    ces = campaign_extension_setting_operation.create
    ces.campaign = client.get_service("CampaignService").campaign_path(
        customer_id, campaign_id
    )
    ces.extension_type = client.get_type(
        "ExtensionTypeEnum"
    ).ExtensionType.IMAGE
    ces.extension_feed_items.append(image_resource_name)

    response = (
        campaign_extension_setting_service.mutate_campaign_extension_settings(
            customer_id=customer_id,
            operations=[campaign_extension_setting_operation],
        )
    )
    print(
        "Created a campaign extension setting with resource name: "
        f"'{response.results[0].resource_name}'"
    )


if __name__ == "__main__":
    # GoogleAdsClient will read the google-ads.yaml configuration file in the
    # home directory if none is specified.
    googleads_client = GoogleAdsClient.load_from_storage(version="v6")

    parser = argparse.ArgumentParser(
        description=("Adds an image extension to a campaign.")
    )
    # The following argument(s) should be provided to run the example.
    parser.add_argument(
        "-c",
        "--customer_id",
        type=str,
        required=True,
        help="The Google Ads customer ID.",
    )
    parser.add_argument(
        "-a",
        "--campaign_id",
        type=str,
        required=True,
        help="The ID for a campaign to add an image extension to.",
    )
    parser.add_argument(
        "-i",
        "--image_asset_id",
        type=str,
        required=True,
        help="The ID of an image asset to use for the new extension.",
    )
    args = parser.parse_args()

    try:
        main(
            googleads_client,
            args.customer_id,
            args.campaign_id,
            args.image_asset_id,
        )
    except GoogleAdsException as ex:
        print(
            f'Request with ID "{ex.request_id}" failed with status '
            f'"{ex.error.code().name}" and includes the following errors:'
        )
        for error in ex.failure.errors:
            print(f'\tError with message "{error.message}".')
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")
        sys.exit(1)
