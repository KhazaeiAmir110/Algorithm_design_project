import gzip
import io
from django.core.files.base import ContentFile
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Message
from .serializers import MessageSerializer

@csrf_exempt
@api_view(['POST'])
def compress_message(request):
    # Deserialize the JSON data sent by the client
    data = JSONParser().parse(request)
    serializer = MessageSerializer(data=data)

    # If the data is valid, compress the message and save it to the database
    if serializer.is_valid():
        message = serializer.validated_data['message']
        compressed_message = gzip.compress(message.encode())
        compressed_file = ContentFile(compressed_message)
        instance = serializer.save(compressed_message=compressed_file)

        # Return the compressed message ID to the client
        return JsonResponse({'id': instance.id})

    # If the data is invalid, return an error response
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def decompress_message(request, message_id):
    # Retrieve the compressed message from the database
    try:
        message = Message.objects.get(id=message_id)
    except Message.DoesNotExist:
        return HttpResponse(status=404)

    # Decompress the message and return it to the client
    compressed_message = message.compressed_message.read()
    decompressed_message = gzip.decompress(compressed_message).decode()
    return JsonResponse({'message': decompressed_message})