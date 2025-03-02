#!/usr/bin/env python
# Copyright 2018 Google LLC
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
"""This example illustrates how to retrieve ad group bid modifiers."""


import argparse
import sys
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

_DEFAULT_PAGE_SIZE = 1000


def main(client, customer_id, page_size, ad_group_id=None):
    ga_service = client.get_service("GoogleAdsService")

    query = """
        SELECT
          campaign.id,
          ad_group.id,
          ad_group_bid_modifier.criterion_id,
          ad_group_bid_modifier.bid_modifier,
          ad_group_bid_modifier.device.type
        FROM ad_group_bid_modifier"""

    if ad_group_id:
        query += f" WHERE ad_group.id = {ad_group_id}"

    search_request = client.get_type("SearchGoogleAdsRequest")
    search_request.customer_id = customer_id
    search_request.query = query
    search_request.page_size = _DEFAULT_PAGE_SIZE

    results = ga_service.search(request=search_request)

    for row in results:
        modifier = row.ad_group_bid_modifier
        print(
            "Ad group bid modifier with criterion ID "
            '"{modifier.criterion_id.value}", bid modifier value '
            '"{modifier.bid_modifier.value}", device type '
            '"{modifier.device.type.name}" was found in ad group ID '
            '"{row.ad_group.id.value}" of campaign with ID '
            '"{row.campaign.id.value}".'
        )


if __name__ == "__main__":
    # GoogleAdsClient will read the google-ads.yaml configuration file in the
    # home directory if none is specified.
    googleads_client = GoogleAdsClient.load_from_storage(version="v6")

    parser = argparse.ArgumentParser(
        description="List ad group bid modifiers for specified customer."
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
        "--ad_group_id",
        type=str,
        required=False,
        help=(
            "The ad group ID. Specify this to list ad group "
            "bid modifiers solely for this ad group ID."
        ),
    )
    args = parser.parse_args()

    try:
        main(
        googleads_client,
        args.customer_id,
        _DEFAULT_PAGE_SIZE,
        ad_group_id=args.ad_group_id,
    )
    except GoogleAdsException as ex:
        print(
            f'Request with ID "{ex.request_id}" failed with status '
            f'"{ex.error.code().name}" and includes the following errors:'
        )
        for error in ex.failure.errors:
            print(f'	Error with message "{error.message}".')
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")
        sys.exit(1)
