from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='test-group'
)

print("Listening for messages on 'test-topic'...")
for msg in consumer:
    print(f"Received: {msg.value.decode('utf-8')}")
