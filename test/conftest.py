import pytest
import json
import os
import base64
import os

@pytest.fixture
def test_params():
    test_config_file = './test-config.json'

    params = None
    defaults = {
        "Author": "DynamicPDF",
        "Title": "Python Client API Tests",
        "ApiKey": "",
        "BaseUrl": "https://api.dynamicpdf.com",
        "ResourcesPath":"./Resources/",
        "OutputPath":"./Output/"
    }

    try:
        with open(test_config_file, 'r') as file:
            params = json.load(file)
    except FileNotFoundError:
        params = defaults

    class TestParams:
        @property
        def author(self):
            return params['Author']

        @property
        def title(self):
            return params['Title']
        
        @property
        def api_key(self):
            return params['ApiKey']

        @property
        def base_url(self):
            return params['BaseUrl']
        
        @property
        def resources_path(self):
            return params['ResourcesPath']
        
        @property
        def output_path(self):
            return params['OutputPath']
        
    return TestParams()

@pytest.fixture
def get_endpoint():
    def _get_endpoint(endpoint, test_params):
        if len(test_params.base_url) > 0:
            endpoint.base_url = test_params.base_url
        if len(test_params.api_key) > 0:
            endpoint.api_key = test_params.api_key
        if len(test_params.author) > 0:
            endpoint.author = test_params.author
        if len(test_params.title) > 0:
            endpoint.title = test_params.title
        if not os.path.exists(test_params.output_path):
            os.makedirs(test_params.output_path)
        return endpoint
    return _get_endpoint

@pytest.fixture
def get_imaging():
    def _get_imaging(outputFile, res):
        i = 0
        for image in res.images:
            output_file_path = outputFile +str(i)+"."+res.image_format
            with open(output_file_path, 'wb') as file:
                file.write(base64.b64decode(res.images[i].data))
                i = i + 1
    return _get_imaging