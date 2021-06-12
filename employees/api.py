import json
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .serializers import EmployeeSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.response import Response 
from .models import Employee
import requests
import hashlib
@api_view(['POST'])
def insert(request):
    serializer=EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else :
        raise AuthenticationFailed('data not valid')
    response=Response()
    response.data={
        'message':status.HTTP_200_OK
    }
    return response
@api_view(['GET'])
def get_data(request):
    employees=Employee.objects.all()
    serializar=EmployeeSerializer(employees,many=True)
    return Response(serializar.data)


@api_view(['GET'])   
def payment(request):
    # importing the requests library
    # importing Hash Library

    # FawryPay Refund API Endpoint
    URL = "https://atfawry.fawrystaging.com/ECommerceWeb/Fawry/payments/refund"

    merchantCode    = '1tSa6uxz2nTwlaAmt38enA=='
    referenceNumber  = '99900642041'
    refundAmount = '362.50'
    reason  = 'Item not as described'
    merchant_sec_key =  '259af31fc2f74453b3a55739b21ae9ef'
    encode_payload=(merchantCode + referenceNumber + refundAmount + reason + merchant_sec_key).encode('utf-8')
    signature = hashlib.sha256(encode_payload).hexdigest()
    # defining a params dict for the parameters to be sent to the API
    PaymentData = {
        'merchantCode' : merchantCode,
        'referenceNumber' : referenceNumber,
        'refundAmount' : refundAmount,
        'reason'  : reason,
        'signature' : signature
    }

    # sending get request and saving the response as response object
    status_request = requests.get(url = URL, params = json.dumps(PaymentData))
    try :
        return Response(status_request.json())
    except :
        return Response(
            {
         "type": "ChargeResponse",
            "statusDescription": "wrong info",
            "statusCode": 9935,
        }
        )
