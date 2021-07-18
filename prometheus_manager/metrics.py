from prometheus_flask_exporter.multiprocess import UWsgiPrometheusMetrics

metrics = UWsgiPrometheusMetrics.for_app_factory()
