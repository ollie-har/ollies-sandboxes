FROM gcr.io/datadoghq/agent:latest-jmx
ADD conf.d/kafka.yaml /etc/datadog-agent/conf.d/kafka.yaml
ADD conf.d/metrics.yaml /etc/datadog-agent/conf.d/metrics.yaml
RUN curl -L https://github.com/jiaqi/jmxterm/releases/download/v1.0.1/jmxterm-1.0.1-uber.jar -o /tmp/jmxterm-1.0.1-uber.jar