from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)

metric_reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
provider = MeterProvider(metric_readers=[metric_reader])

# Sets the global default meter provider
metrics.set_meter_provider(provider)

# Creates a meter from the global meter provider
meter = metrics.get_meter("my.meter.name")

work_counter = meter.create_counter(
    "work.counter", unit="1", description="Counts the amount of work done"
)

def do_work(work_item):
    # count the work being doing
    work_counter.add(1, {"work.type": work_item.work_type})
    print("doing some work...")


# meter = metrics.get_meter("app_or_package_name")

# counter = meter.create_counter(
#     name="first_counter", description="TODO", unit="1",
# )

# counter.add(1, attributes={"foo": "bar"})
# counter.add(10, attributes={"hello": "world"})


## Send Metrics: 
## https://github.com/open-telemetry/opentelemetry-python/blob/main/docs/examples/metrics/instruments/example.py




# import logging
# from opentelemetry._logs import set_logger_provider
# from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
# from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
# from opentelemetry.sdk.resources import Resource

# ## Send Logs:
# ##https://github.com/open-telemetry/opentelemetry-python/blob/main/docs/examples/logs/example.py
# logger_provider = LoggerProvider(
#     resource=Resource.create(
#         {
#             "service.name": "shoppingcart",
#             "service.instance.id": "instance-12",
#         }
#     ),
# )
# set_logger_provider(logger_provider)

# exporter = OTLPLogExporter(insecure=True)
# logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
# handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)

# # Attach OTLP handler to root logger
# logging.getLogger().addHandler(handler)

# # Log directly
# logging.info("Jackdaws love my big sphinx of quartz.")

# # Create different namespaced loggers
# logger1 = logging.getLogger("myapp.area1")
# logger2 = logging.getLogger("myapp.area2")