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


from google.ads.googleads.v4.enums.types import tracking_code_page_format
from google.ads.googleads.v4.enums.types import tracking_code_type
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.common",
    marshal="google.ads.googleads.v4",
    manifest={"TagSnippet",},
)


class TagSnippet(proto.Message):
    r"""The site tag and event snippet pair for a TrackingCodeType.

    Attributes:
        type_ (google.ads.googleads.v4.enums.types.TrackingCodeTypeEnum.TrackingCodeType):
            The type of the generated tag snippets for
            tracking conversions.
        page_format (google.ads.googleads.v4.enums.types.TrackingCodePageFormatEnum.TrackingCodePageFormat):
            The format of the web page where the tracking
            tag and snippet will be installed, e.g. HTML.
        global_site_tag (google.protobuf.wrappers_pb2.StringValue):
            The site tag that adds visitors to your basic
            remarketing lists and sets new cookies on your
            domain.
        event_snippet (google.protobuf.wrappers_pb2.StringValue):
            The event snippet that works with the site
            tag to track actions that should be counted as
            conversions.
    """

    type_ = proto.Field(
        proto.ENUM,
        number=1,
        enum=tracking_code_type.TrackingCodeTypeEnum.TrackingCodeType,
    )
    page_format = proto.Field(
        proto.ENUM,
        number=2,
        enum=tracking_code_page_format.TrackingCodePageFormatEnum.TrackingCodePageFormat,
    )
    global_site_tag = proto.Field(
        proto.MESSAGE, number=3, message=wrappers.StringValue,
    )
    event_snippet = proto.Field(
        proto.MESSAGE, number=4, message=wrappers.StringValue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
