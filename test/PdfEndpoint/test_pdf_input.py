import pytest
import io
from ..common_imports import (
    PdfResource,
    PdfInput,
    Pdf,
    MergeOptions
)

class TestPdfInput:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_pdf_input_merge_options(self, pdf, test_params):
        resource1 = PdfResource(test_params.resources_path + "AllPageElements.pdf", "AllPageElements.pdf")
        input1 = PdfInput(resource1)
        merge_options1 = MergeOptions()
        merge_options1.root_form_field = "RootName"
        merge_options1.outlines = False
        input1.merge_options = merge_options1
        pdf.inputs.append(input1)

        with open(test_params.resources_path + "fw9AcroForm_14.pdf", 'rb') as file:
            file_data = io.BytesIO(file.read())
        resource2 = PdfResource(file_data, "fw9AcroForm_14.pdf")
        input2 = PdfInput(resource2)
        merge_options2 = MergeOptions()
        merge_options2.logical_structure = False
        merge_options2.form_fields = False
        input2.merge_options = merge_options1
        pdf.inputs.append(input2)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "pdf_input_merge_options.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful
