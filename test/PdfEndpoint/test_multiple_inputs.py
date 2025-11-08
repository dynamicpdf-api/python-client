import pytest
from ..common_imports import (
    PdfInput,
    Pdf,
    ImageElement,
    ImageResource,
    ImageInput,
    PageInput,
    TextElement,
    ElementPlacement,
    MergeOptions,
    DlexInput,
)

class TestMultipleInputs:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_different_input(self, pdf, test_params):
        pdf_input = PdfInput("TFWResources/DocumentA100.pdf")
        merge_options = MergeOptions()
        pdf_input.merge_options = merge_options
        pdf.inputs.append(pdf_input)

        page_input = PageInput()
        text_element = TextElement("Hello World", ElementPlacement.TopCenter)
        text_element.font_size = 40
        page_input.elements.append(text_element)
        pdf.inputs.append(page_input)

        page_input = PageInput()
        resource = ImageResource(test_params.resources_path + "DocumentA.jpeg", "DocumentA.jpeg")
        image_element = ImageElement(resource, ElementPlacement.TopCenter)
        image_element.x_offset = 50
        image_element.y_offset = 50
        page_input.elements.append(image_element)
        pdf.inputs.append(page_input)
        
        with open(test_params.resources_path + "SimpleReportData.json", "r", encoding="utf-8-sig") as file:
            json_string = file.read()
        dlex_input = DlexInput("TFWResources/SimpleReportWithCoverPage.dlex", json_string)
        pdf.inputs.append(dlex_input)

        image_input = ImageInput("TFWResources/Northwind Logo.gif")
        image_input.top_margin = 10
        image_input.left_margin = 10
        image_input.right_margin = 10
        image_input.bottom_margin = 10
        pdf.inputs.append(image_input)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "MutipleInput_PdfOutput.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful