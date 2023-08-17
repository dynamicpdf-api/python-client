import pytest
from ..common_imports import (
    Pdf,
    PdfInput,
    PdfResource,
    TextElement,
    ElementPlacement,
    Template,
    RgbColor,
    Font
)

class TestTemplate:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_template(self, pdf, test_params):
        resource = PdfResource(test_params.resources_path + "DocumentA100.pdf")
        input = PdfInput(resource)
        pdf.inputs.append(input)

        template = Template("TemplateA")
        element = TextElement("Hello World", ElementPlacement.TopCenter)
        element.x_offset = 0
        element.y_offset = 0
        element.color = RgbColor.green()
        element.font_size = 20
        element.font = Font.times_roman()
        template.elements.append(element)
        input.template = template

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful
