import pytest
from ..common_imports import (
    Pdf,
    PageInput,
    TextElement,
    ElementPlacement,
    Template,
)

class TestPageInput:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_page_input_text_element(self, pdf, test_params):
        input1 = PageInput()
        text_element = TextElement("Hello World", ElementPlacement.TopCenter)
        input1.elements.append(text_element)
        pdf.inputs.append(input1)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "page_input_text_element.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful


    def test_page_input_text_element_added_to_page_and_template(self, pdf, test_params):
        page_input = pdf.add_page(500, 500)
        template = Template("Temp1")
        element = TextElement("Hello World", ElementPlacement.TopLeft)
        template.elements.append(element)
        page_input.template = template

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "page_input_text_element_added_to_page_and_template.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful
