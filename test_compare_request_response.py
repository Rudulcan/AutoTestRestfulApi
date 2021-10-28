import requests
import json
import pytest
from test_parser import *


@pytest.fixture()
def filename(pytestconfig):
    return pytestconfig.getoption("filename")


def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True


def test_compare_request_response(filename):
    request_type = ""
    request_method = ""
    request_headers = ""
    request_params = ""
    request_data = ""
    request_json_data = ""
    request_url = ""

    cfg_parser = Parser()
    cfg_parser.set_attributes_from_config_file()
    if len(get_type_request_for_test(filename)) > 1:
        request_type = get_type_request_for_test(filename)
    if len(get_method_request_for_test(filename)) > 1:
        request_method = get_method_request_for_test(filename)
    if len(get_header_request_for_test(filename)) > 1:
        request_headers = json.loads(get_header_request_for_test(filename).replace("'", "\""))
    if len(get_params_request_for_test(filename)) > 1:
        request_params = json.loads(get_params_request_for_test(filename).replace("'", "\""))
    if len(str(get_request_for_test(filename))) > 4:
        request_data = json.loads(get_request_for_test(filename))
    if len(request_data) > 1:
        request_json_data = json.dumps(request_data)
    if len(cfg_parser.get_service_url()) > 1:
        request_url = cfg_parser.get_service_url()
    if len(request_method) > 1:
        request_url = cfg_parser.get_service_url() + "/" + request_method

    response = None
    if request_type.lower() == 'post':
        response = requests.post(request_url, data=request_json_data, headers=request_headers, params=request_params)
    elif request_type.lower() == 'get':
        response = requests.get(request_url, data=request_json_data, headers=request_headers, params=request_params)
    elif request_type.lower() == 'put':
        response = requests.put(request_url, data=request_json_data, headers=request_headers, params=request_params)
    elif request_type.lower() == 'del':
        response = requests.delete(request_url, data=request_json_data, headers=request_headers, params=request_params)


    # Validation
    # First let us validate if the response equals 200
    assert response.status_code == 200
    # Now lets validate if the response matches the expected response
    if response.status_code == 200:
        if is_json(response.content):
            body = response.json()
            expected_response = json.loads(get_response_for_test(filename))
            expected_response_data = json.dumps(expected_response, sort_keys=True)
            resp_data = json.dumps(body, sort_keys=True)
            assert expected_response_data == resp_data
        else:
            current_response = response.text
            expected_response = get_response_for_test(filename)
            assert expected_response == current_response

