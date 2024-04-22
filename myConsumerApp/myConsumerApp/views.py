from django.http import HttpResponse
from .service.KafkaConsumerService import KafkaConsumerService

consumerService = KafkaConsumerService()

def startReceiveMessages(request):
    print("consuming started!")
    consumerService.receiveMessage()
    return HttpResponse("end!")

def stopReceiveMessages(request):
    print("consuming stoped!")
    consumerService.close()
    return HttpResponse("end!")