import json
import pytest
from ..common_imports import PdfInfo, PdfResource

class TestPdfInfo:
    @pytest.fixture
    def resource(self, test_params):
        return PdfResource(test_params.resources_path + "AllFormFields.pdf")

    @pytest.fixture
    def pdfInfo(self, resource, test_params, get_endpoint):
        pdfInfo = PdfInfo(resource)
        return get_endpoint(pdfInfo, test_params)

    def test_pdf_info(self, pdfInfo, test_params):
        
        res = pdfInfo.process() 
        
        if res.is_successful:
            with open(test_params.output_path + "pdf_info.json", "w") as out_stream:
                json.dump(res.content, out_stream, indent=2)

        assert res.is_successful