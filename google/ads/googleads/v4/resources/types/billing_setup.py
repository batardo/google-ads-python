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


from google.ads.googleads.v4.enums.types import billing_setup_status
from google.ads.googleads.v4.enums.types import time_type
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"BillingSetup",},
)


class BillingSetup(proto.Message):
    r"""A billing setup, which associates a payments account and an
    advertiser. A billing setup is specific to one advertiser.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the billing setup.
            BillingSetup resource names have the form:

            ``customers/{customer_id}/billingSetups/{billing_setup_id}``
        id (google.protobuf.wrappers_pb2.Int64Value):
            Output only. The ID of the billing setup.
        status (google.ads.googleads.v4.enums.types.BillingSetupStatusEnum.BillingSetupStatus):
            Output only. The status of the billing setup.
        payments_account (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The resource name of the payments account
            associated with this billing setup. Payments resource names
            have the form:

            ``customers/{customer_id}/paymentsAccounts/{payments_account_id}``
            When setting up billing, this is used to signup with an
            existing payments account (and then payments_account_info
            should not be set). When getting a billing setup, this and
            payments_account_info will be populated.
        payments_account_info (google.ads.googleads.v4.resources.types.BillingSetup.PaymentsAccountInfo):
            Immutable. The payments account information associated with
            this billing setup. When setting up billing, this is used to
            signup with a new payments account (and then
            payments_account should not be set). When getting a billing
            setup, this and payments_account will be populated.
        start_date_time (google.protobuf.wrappers_pb2.StringValue):
            Immutable. The start date time in yyyy-MM-dd
            or yyyy-MM-dd HH:mm:ss format. Only a future
            time is allowed.
        start_time_type (google.ads.googleads.v4.enums.types.TimeTypeEnum.TimeType):
            Immutable. The start time as a type. Only NOW
            is allowed.
        end_date_time (google.protobuf.wrappers_pb2.StringValue):
            Output only. The end date time in yyyy-MM-dd
            or yyyy-MM-dd HH:mm:ss format.
        end_time_type (google.ads.googleads.v4.enums.types.TimeTypeEnum.TimeType):
            Output only. The end time as a type.  The
            only possible value is FOREVER.
    """

    class PaymentsAccountInfo(proto.Message):
        r"""Container of payments account information for this billing.

        Attributes:
            payments_account_id (google.protobuf.wrappers_pb2.StringValue):
                Output only. A 16 digit id used to identify
                the payments account associated with the billing
                setup.
                This must be passed as a string with dashes,
                e.g. "1234-5678-9012-3456".
            payments_account_name (google.protobuf.wrappers_pb2.StringValue):
                Immutable. The name of the payments account
                associated with the billing setup.
                This enables the user to specify a meaningful
                name for a payments account to aid in
                reconciling monthly invoices.

                This name will be printed in the monthly
                invoices.
            payments_profile_id (google.protobuf.wrappers_pb2.StringValue):
                Immutable. A 12 digit id used to identify the
                payments profile associated with the billing
                setup.
                This must be passed in as a string with dashes,
                e.g. "1234-5678-9012".
            payments_profile_name (google.protobuf.wrappers_pb2.StringValue):
                Output only. The name of the payments profile
                associated with the billing setup.
            secondary_payments_profile_id (google.protobuf.wrappers_pb2.StringValue):
                Output only. A secondary payments profile id
                present in uncommon situations, e.g. when a
                sequential liability agreement has been
                arranged.
        """

        payments_account_id = proto.Field(
            proto.MESSAGE, number=1, message=wrappers.StringValue,
        )
        payments_account_name = proto.Field(
            proto.MESSAGE, number=2, message=wrappers.StringValue,
        )
        payments_profile_id = proto.Field(
            proto.MESSAGE, number=3, message=wrappers.StringValue,
        )
        payments_profile_name = proto.Field(
            proto.MESSAGE, number=4, message=wrappers.StringValue,
        )
        secondary_payments_profile_id = proto.Field(
            proto.MESSAGE, number=5, message=wrappers.StringValue,
        )

    resource_name = proto.Field(proto.STRING, number=1)
    id = proto.Field(proto.MESSAGE, number=2, message=wrappers.Int64Value,)
    status = proto.Field(
        proto.ENUM,
        number=3,
        enum=billing_setup_status.BillingSetupStatusEnum.BillingSetupStatus,
    )
    payments_account = proto.Field(
        proto.MESSAGE, number=11, message=wrappers.StringValue,
    )
    payments_account_info = proto.Field(
        proto.MESSAGE, number=12, message=PaymentsAccountInfo,
    )
    start_date_time = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="start_time",
        message=wrappers.StringValue,
    )
    start_time_type = proto.Field(
        proto.ENUM,
        number=10,
        oneof="start_time",
        enum=time_type.TimeTypeEnum.TimeType,
    )
    end_date_time = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="end_time",
        message=wrappers.StringValue,
    )
    end_time_type = proto.Field(
        proto.ENUM,
        number=14,
        oneof="end_time",
        enum=time_type.TimeTypeEnum.TimeType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
