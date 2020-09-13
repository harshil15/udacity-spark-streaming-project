import logging
from kafka import KafkaConsumer
import time
import json 

def consume_message(topic):
    print("Initialize Consumer")
    consumer = KafkaConsumer(bootstrap_servers = "localhost:9092",
                            group_id="police-callss-v12",
                            auto_offset_reset="earliest",
                            max_poll_records = 5,
                            value_deserializer = lambda m : json.loads(m.decode('utf-8')))
    
    print("Consumer subscribe to topic")
    print(consumer.topics())
    consumer.subscribe(topic)
    
    print("Topics Partitions ")
    print(consumer.partitions_for_topic(topic))
    
    try:
        while True:
            print("Pollling messages")
            msgs = consumer.poll()
            print("Type of Record Return ", type(msgs))
            for key,value in msgs.items():
                print(key)
                for item in value:
                    print(item.value)
            time.sleep(5)
            
    except KeyboardInterrupt as e:
        print("Closing Consumer")
        consumer.close()
    
if __name__=="__main__":
    logger = logging.getLogger(__name__)
    consume_message("com.city.sf.police.department.calls.v1")
    
    
        