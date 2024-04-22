import pickle
from kafka import KafkaConsumer


class KafkaConsumerService:
    def __init__(self):
        self.consumer = KafkaConsumer('avia', 
        bootstrap_servers=['localhost:9092'] 
        #,consumer_timeout_ms=1000
    )
    def receiveMessage(self):
        for message in self.consumer:
            deserialized_data = pickle.loads(message.value) 
            print(deserialized_data)

    def close(self):
        self.consumer.close()