from django.http.response import JsonResponse


def init_response():
    response = {"res_str": "", "res_data": {}}
    return response


def _send(data, status_code):
    return JsonResponse(data=data, status=status_code)


def send_200(data):
    return _send(data, 200)