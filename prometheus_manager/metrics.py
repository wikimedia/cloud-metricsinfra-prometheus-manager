# SPDX-FileCopyrightText: 2021-2024 Taavi Väänänen <hi@taavi.wtf>
# SPDX-License-Identifier: AGPL-3.0-only

import os

from prometheus_flask_exporter import PrometheusMetrics
from prometheus_flask_exporter.multiprocess import UWsgiPrometheusMetrics

if "PROMETHEUS_MULTIPROC_DIR" in os.environ:
    metrics = UWsgiPrometheusMetrics.for_app_factory(group_by="url_rule")
else:
    metrics = PrometheusMetrics.for_app_factory(group_by="url_rule", path=None)
