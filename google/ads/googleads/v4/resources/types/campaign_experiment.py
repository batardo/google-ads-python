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


from google.ads.googleads.v4.enums.types import campaign_experiment_status
from google.ads.googleads.v4.enums.types import (
    campaign_experiment_traffic_split_type,
)
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"CampaignExperiment",},
)


class CampaignExperiment(proto.Message):
    r"""An A/B experiment that compares the performance of the base
    campaign (the control) and a variation of that campaign (the
    experiment).

    Attributes:
        resource_name (str):
            Immutable. The resource name of the campaign experiment.
            Campaign experiment resource names have the form:

            ``customers/{customer_id}/campaignExperiments/{campaign_experiment_id}``
        id (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The ID of the campaign
            experiment.
            This field is read-only.
        campaign_draft (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The campaign draft with staged
            changes to the base campaign.
        name (google.protobuf.wrappers_pb2.StringValue):
            The name of the campaign experiment.
            This field is required when creating new
            campaign experiments and must not conflict with
            the name of another non-removed campaign
            experiment or campaign.

            It must not contain any null (code point 0x0),
            NL line feed (code point 0xA) or carriage return
            (code point 0xD) characters.
        description (google.protobuf.wrappers_pb2.StringValue):
            The description of the experiment.
        traffic_split_percent (google.protobuf.wrappers_pb2.Int64Value):
            Immutable. Share of traffic directed to experiment as a
            percent (must be between 1 and 99 inclusive. Base campaign
            receives the remainder of the traffic (100 -
            traffic_split_percent). Required for create.
        traffic_split_type (google.ads.googleads.v4.enums.types.CampaignExperimentTrafficSplitTypeEnum.CampaignExperimentTrafficSplitType):
            Immutable. Determines the behavior of the
            traffic split.
        experiment_campaign (google.protobuf.wrappers_pb2.StringValue):
            Output only. The experiment campaign, as
            opposed to the base campaign.
        status (google.ads.googleads.v4.enums.types.CampaignExperimentStatusEnum.CampaignExperimentStatus):
            Output only. The status of the campaign
            experiment. This field is read-only.
        long_running_operation (google.protobuf.wrappers_pb2.StringValue):
            Output only. The resource name of the long-
            unning operation that can be used to poll for
            completion of experiment create or promote. The
            most recent long running operation is returned.
        start_date (google.protobuf.wrappers_pb2.StringValue):
            Date when the campaign experiment starts. By
            default, the experiment starts now or on the
            campaign's start date, whichever is later. If
            this field is set, then the experiment starts at
            the beginning of the specified date in the
            customer's time zone. Cannot be changed once the
            experiment starts.
            Format: YYYY-MM-DD
            Example: 2019-03-14
        end_date (google.protobuf.wrappers_pb2.StringValue):
            Date when the campaign experiment ends. By
            default, the experiment ends on the campaign's
            end date. If this field is set, then the
            experiment ends at the end of the specified date
            in the customer's time zone.
            Format: YYYY-MM-DD
            Example: 2019-04-18
    """

    resource_name = proto.Field(proto.STRING, number=1)
    id = proto.Field(proto.MESSAGE, number=2, message=wrappers.Int64Value,)
    campaign_draft = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )
    name = proto.Field(proto.MESSAGE, number=4, message=wrappers.StringValue,)
    description = proto.Field(
        proto.MESSAGE, number=5, message=wrappers.StringValue,
    )
    traffic_split_percent = proto.Field(
        proto.MESSAGE, number=6, message=wrappers.Int64Value,
    )
    traffic_split_type = proto.Field(
        proto.ENUM,
        number=7,
        enum=campaign_experiment_traffic_split_type.CampaignExperimentTrafficSplitTypeEnum.CampaignExperimentTrafficSplitType,
    )
    experiment_campaign = proto.Field(
        proto.MESSAGE, number=8, message=wrappers.StringValue,
    )
    status = proto.Field(
        proto.ENUM,
        number=9,
        enum=campaign_experiment_status.CampaignExperimentStatusEnum.CampaignExperimentStatus,
    )
    long_running_operation = proto.Field(
        proto.MESSAGE, number=10, message=wrappers.StringValue,
    )
    start_date = proto.Field(
        proto.MESSAGE, number=11, message=wrappers.StringValue,
    )
    end_date = proto.Field(
        proto.MESSAGE, number=12, message=wrappers.StringValue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
