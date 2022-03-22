from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'pkc-l6ojq.asia-northeast1.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'QHQFIXFP5L6YZR4I',
    'sasl.password': 'k6tr9eU/TgJxWmhRCdCSKBp6ep4Oj+nQqIrnRCKGAnjZW3z7Ce/ofecbcZP2//G6',
    'sasl.mechanism': 'PLAIN',
})
