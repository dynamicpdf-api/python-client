import pytest
from ..common_imports import PdfXmp, PdfResource

class TestPdfXmp:
    
    @pytest.fixture
    def resource(self, test_params):
        return PdfResource(test_params.resources_path + "XmpAndOtherSample.pdf", "XmpAndOtherSample.pdf")

    @pytest.fixture
    def text(self, resource, test_params, get_endpoint):
        text = PdfXmp(resource)
        return get_endpoint(text, test_params)

    def test_pdf_xmp(self, text, test_params):
        
        res = text.process()

        if res.is_successful:
            with open(test_params.output_path + "pdf_xmp.xml", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful
