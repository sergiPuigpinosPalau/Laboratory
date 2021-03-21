import json
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from Lab_App.models import *

CLIENT_ID = 'A3whkgeQcyoLzHtC2uszlcmu1MSbLmBuTiKlB5Um'
CLIENT_SECRET = 'bqJWKp03ZeiIu7FjsLYet7OgLK7gWhI3MB1GcSs0qshVZEoLfVJDZuy8K94lMT5hBd521hVI8ntEyVmgHrETMQghdS9h31gVJtso2VqVmyDLJgRCgzl0mBOj4ewgFvi1'


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    """
    get token with user/pass
    Request access token
    format: {"username": "username", "password": "1234abcd"}
    """
    try:

        url = "http://127.0.0.1:8000/o/token/"

        payload = 'username=' + str(request.data['username']) + '&password=' + request.data['password'] + \
                  '&grant_type=password&client_id=' + str(CLIENT_ID) + '&client_secret=' + str(CLIENT_SECRET)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, headers=headers, data=payload)

        response_dict = json.loads(response.text)

    except Exception as exception:
        response_dict = {'Exception:': str(exception)}

    return Response(response_dict)


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    """
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    """
    try:

        url = "http://127.0.0.1:8000/o/token/"

        payload = 'refresh_token=' + str(request.data['refresh_token']) + \
                  '&grant_type=refresh_token&client_id=' + str(CLIENT_ID) + '&client_secret=' + str(CLIENT_SECRET)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, headers=headers, data=payload)

        response_dict = json.loads(response.text)

    except Exception as e:
        response_dict = {'error': str(e)}

    return Response(response_dict)


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    """
    Method to revoke tokens.
    {"token": "<token>"}
    """
    try:

        url = "http://127.0.0.1:8000/o/revoke_token/"

        payload = 'token=' + str(request.data['token']) + \
                  '&client_id=' + str(CLIENT_ID) + '&client_secret=' + str(CLIENT_SECRET)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, headers=headers, data=payload)

        response_dict = json.loads(response.text)

        if response.status_code == 200:
            response_dict = {'token': request.data['token'],
                             'status': 'Deleted'}

    except Exception as e:
        response_dict = {'error': str(e)}

    return Response(response_dict)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mainApi(request):
    """
    List with all api items
    """
    response = {'experiments': request.build_absolute_uri('/api/restaurants/')}

    return Response(response)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_experiments_list(request, experiments_pk=None):
    """
    List with all restaurants
    """
    response = {}

    # If no experiment has been specified, show all
    if experiments_pk is None:
        experiments = Experiment.objects.all()
    # Else, return information of the specified experiment
    else:
        experiments = Experiment.objects.filter(pk=experiments_pk)
        if len(experiments) == 0:
            response = {'error': 'experiment does not exist'}
            return Response(response)

    response['experiments'] = []

    for experiment in experiments:
        experiment_data = {}
        experiment_data['id'] = str(experiment.pk)
        experiment_data['name'] = str(experiment.name)
        experiment_data['description'] = str(experiment.description)
        experiment_data['status'] = str(experiment.status)
        experiment_data['init_date'] = str(experiment.init_date)
        experiment_data['url'] = request.build_absolute_uri('/api/experiments/' + str(experiment.pk))

        response['experiments'].append(experiment_data)

    return Response(response)
