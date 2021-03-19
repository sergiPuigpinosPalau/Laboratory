import json

import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from Lab_App.models import Restaurant

CLIENT_ID = 'kReZWCEH5TolLSCVUtCaSjDP020zbwNyoLMxmwRv'
CLIENT_SECRET = 'jkwao2CiPnyWzMZTzIFecaSVc1g6ZiNA6an81uiKybsY7q0YUmR280ydKk9V5TPneeiB3HJGef1yi7XejB233hCfd2h6li3TskY54x3Umx21GHIboXZgzAiZEGpKrTvp'

@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    """
    get token with user/pass
    format: {"username": "username", "password": "1234abcd"}
    """
    try:

        url = "http://127.0.0.1:8000/o/token/"

        payload = 'username=' + str(request.data['username']) + '&password=' + request.data['password'] +\
                  '&grant_type=password&client_id='+ str(CLIENT_ID) +'&client_secret=' + str(CLIENT_SECRET)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, headers=headers, data=payload)

        responseDict = json.loads(response.text)

    except Exception as e:
        responseDict = {'error': str(e)}

    return Response(responseDict)


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    """
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    """
    try:

        url = "http://127.0.0.1:8000/o/token/"

        payload = 'refresh_token=' + str(request.data['refresh_token']) +\
                  '&grant_type=refresh_token&client_id='+ str(CLIENT_ID) +'&client_secret=' + str(CLIENT_SECRET)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, headers=headers, data=payload)

        responseDict = json.loads(response.text)

    except Exception as e:
        responseDict = {'error': str(e)}

    return Response(responseDict)


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    """
    Method to revoke tokens.
    {"token": "<token>"}
    """
    try:

        url = "http://127.0.0.1:8000/o/revoke_token/"

        payload = 'token=' + str(request.data['token']) +\
                  '&client_id='+ str(CLIENT_ID) +'&client_secret=' + str(CLIENT_SECRET)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            responseDict = {'token': request.data['token'],
                            'status': 'Deleted'}

    except Exception as e:
        responseDict = {'error': str(e)}

    return Response(responseDict)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mainApi(request):
    """
    List with all api items
    """
    response = {}

    response['restaurants'] = request.build_absolute_uri('/api/restaurants/')

    return Response(response)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_restaurants_list(request, restaurant_pk=None):
    """
    List with all restaurants
    """
    response = {}

    # Si s'ha passat un restaurant com a primary key, nomes tornar del restaurant en questió
    if restaurant_pk == None:
        restaurants = Restaurant.objects.all()
    #Si no, tornar llistat de tots els restaurants, per això el paràmetre es per defecte None
    else:
        restaurants = Restaurant.objects.filter(pk=restaurant_pk)
        if len(restaurants) == 0:
            response = {'error': 'restaurant does not exist'}
            return Response(response)

    response['restaurants'] = []

    for restaurant in restaurants:
        restaurantData = {}
        restaurantData['id'] = str(restaurant.pk)
        restaurantData['name'] = str(restaurant.name)
        restaurantData['name'] = str(restaurant.obtain_address())
        restaurantData['phone'] = str(restaurant.telephone)
        restaurantData['url'] = request.build_absolute_uri('/api/restaurants/' + str(restaurant.pk))

        response['restaurants'].append(restaurantData)

    return Response(response)

