import json
import pytest
from ..common_imports import PdfSecurityInfo,PdfSecurityInfoEndpoint, PdfResource

class TestPdfSecurityInfo:

    def test_Aes128PdfSecurityInfo_PdfOutput(self, test_params, get_endpoint):
        resource = PdfResource(test_params.resources_path + "Aes128Security.pdf")
        pdf_info = PdfSecurityInfoEndpoint(resource)
        pdfSecurityInfoEndpoint = get_endpoint(pdf_info, test_params)
        
        res = pdfSecurityInfoEndpoint.process()
        
        if res.is_successful:
            with open(test_params.output_path + "Aes128PdfSecurity_JsonOutput.json", "w") as out_stream:
                out_stream.write(res.json_content)


        assert res.is_successful
        
    def test_Aes256PdfSecurityInfo_PdfOutput(self, test_params, get_endpoint):
        resource = PdfResource(test_params.resources_path + "Aes256Security.pdf")
        pdf_info = PdfSecurityInfoEndpoint(resource)
        pdfSecurityInfoEndpoint = get_endpoint(pdf_info, test_params)
        
        res = pdfSecurityInfoEndpoint.process()

        if res.is_successful:
            with open(test_params.output_path + "Aes256PdfSecurity_JsonOutput.json", "w") as out_stream:
                out_stream.write(res.json_content)

        assert res.is_successful
        
    def test_RC440PdfSecurityInfo_PdfOutput(self, test_params, get_endpoint):
        resource = PdfResource(test_params.resources_path + "Rc440Security.pdf")
        pdf_info = PdfSecurityInfoEndpoint(resource)
        pdfSecurityInfoEndpoint = get_endpoint(pdf_info, test_params)
        
        res = pdfSecurityInfoEndpoint.process()

        if res.is_successful:
            with open(test_params.output_path + "Rc440PdfSecurity_JsonOutput.json", "w") as out_stream:
                out_stream.write(res.json_content)

        assert res.is_successful
        
    def test_RC4128PdfSecurityInfo_PdfOutput(self, test_params, get_endpoint):
        resource = PdfResource(test_params.resources_path + "Rc4128Security.pdf")
        pdf_info = PdfSecurityInfoEndpoint(resource)
        pdfSecurityInfoEndpoint = get_endpoint(pdf_info, test_params)
        
        res = pdfSecurityInfoEndpoint.process()

        if res.is_successful:
            with open(test_params.output_path + "Rc4128PdfSecurity_JsonOutput.json", "w") as out_stream:
                out_stream.write(res.json_content)

        assert res.is_successful