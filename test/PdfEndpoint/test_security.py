import pytest
from ..common_imports import (
    PdfResource,
    PdfInput,
    Pdf,
    Aes128Security,
    Aes256Security,
    RC4128Security,
    EncryptDocumentComponents
)

class TestSecurity:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_security_aes256(self, pdf, test_params):
        resource1 = PdfResource(test_params.resources_path + "XmpAndOtherSample.pdf", "XmpAndOtherSample.pdf")
        input1 = PdfInput(resource1)
        pdf.inputs.append(input1)

        security = Aes256Security("user", "owner")
        security.allow_form_filling = False
        security.allow_update_annots_and_fields = False
        security.allow_edit = False
        security.document_components = EncryptDocumentComponents.AllExceptMetadata
        pdf.security = security
        
        res = pdf.process() 

        if res.is_successful:
            with open(test_params.output_path + "security_aes256.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_security_aes128(self, pdf, test_params):
        resource1 = PdfResource(test_params.resources_path + "XmpAndOtherSample.pdf", "XmpAndOtherSample.pdf")
        input1 = PdfInput(resource1)
        pdf.inputs.append(input1)

        security = Aes128Security("", "")
        security.owner_password = "owner"
        security.user_password = "user"
        security.allow_document_assembly = False
        security.allow_edit = False
        security.document_components = EncryptDocumentComponents.All
        pdf.security = security
        
        res = pdf.process() 

        if res.is_successful:
            with open(test_params.output_path + "security_aes128.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_security_rc4128(self, pdf, test_params):
        resource1 = PdfResource(test_params.resources_path + "XmpAndOtherSample.pdf", "XmpAndOtherSample.pdf")
        input1 = PdfInput(resource1)
        pdf.inputs.append(input1)

        security = RC4128Security("owner", "user")
        security.allow_high_resolution_printing = True
        security.allow_print = True
        security.encrypt_metadata = True
        pdf.security = security
        
        res = pdf.process() 

        if res.is_successful:
            with open(test_params.output_path + "security_rc4128.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful