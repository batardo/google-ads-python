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


from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v4.resources",
    marshal="google.ads.googleads.v4",
    manifest={"LandingPageView",},
)


class LandingPageView(proto.Message):
    r"""A landing page view with metrics aggregated at the unexpanded
    final URL level.

    Attributes:
        resource_name (str):
            Output only. The resource name of the landing page view.
            Landing page view resource names have the form:

            ``customers/{customer_id}/landingPageViews/{unexpanded_final_url_fingerprint}``
        unexpanded_final_url (google.protobuf.wrappers_pb2.StringValue):
            Output only. The advertiser-specified final
            URL.
    """

    resource_name = proto.Field(proto.STRING, number=1)
    unexpanded_final_url = proto.Field(
        proto.MESSAGE, number=2, message=wrappers.StringValue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
