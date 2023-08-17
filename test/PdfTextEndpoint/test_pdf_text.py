import json
import pytest
from ..common_imports import PdfText, PdfResource

class TestPdfText:

    @pytest.fixture
    def resource(self, test_params):
        return PdfResource(test_params.resources_path + "TimeMachine.pdf", "TimeMachine.pdf")

    @pytest.fixture
    def text(self, resource, test_params, get_endpoint):
        text = PdfText(resource)
        return get_endpoint(text, test_params)

    def test_pdf_text_text_extraction(self, text, test_params):
        
        res = text.process() 

        if res.is_successful:
            with open(test_params.output_path + "pdf_text_text_extraction.json", "w") as out_stream:
                json.dump(res.content, out_stream, indent=2)

        assert res.is_successful

    def test_pdf_text_single_page(self, text, test_params):
        
        text.start_page = 5
        text.page_count = 1
        
        res = text.process()

        if res.is_successful:
            with open(test_params.output_path + "pdf_text_single_page.json", "w") as out_stream:
                json.dump(res.content, out_stream, indent=2)

        assert res.is_successful

    def test_pdf_text_multi_page(self, text, test_params):
        
        text.start_page = 2
        text.page_count = 3
        
        res = text.process()

        if res.is_successful:
            with open(test_params.output_path + "pdf_text_multi_page.json", "w") as out_stream:
                json.dump(res.content, out_stream, indent=2)

        assert res.is_successful
