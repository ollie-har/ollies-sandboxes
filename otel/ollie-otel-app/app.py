# from opentelemetry import metrics

import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)


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