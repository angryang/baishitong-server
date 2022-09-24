# Copyright 2021 99cloud
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

from __future__ import annotations

from typing import List

from pydantic import StrictBool, StrictStr

from baishitong.config.base import Opt

debug = Opt(
    name="debug",
    description="Enable debug",
    schema=StrictBool,
    default=False,
)

log_dir = Opt(
    name="log_dir",
    description="Log directory",
    schema=StrictStr,
    default="./log",
)

database_url = Opt(
    name="database_url",
    description="Database url. For mariadb, set as 'mysql://root:root@localhost:3306/skyline'",
    schema=StrictStr,
    default="sqlite:////tmp/skyline.db",
)

cors_allow_origins = Opt(
    name="cors_allow_origins",
    description="CORS allow origins",
    schema=List[StrictStr],
    default=[],
)


GROUP_NAME = __name__.split(".")[-1]
ALL_OPTS = (
    debug,
    log_dir,
    database_url,
    cors_allow_origins
)

__all__ = ("GROUP_NAME", "ALL_OPTS")
