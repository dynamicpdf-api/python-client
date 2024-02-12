import pytest
from ..common_imports import (
    Pdf,
    PageInput,
    TextElement,
    ElementPlacement,
    Font
)

class TestFont:
    
    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_font_core(self, pdf, test_params):
        input = PageInput()
        element = TextElement("Hello World", ElementPlacement.TopCenter)
        element.font = Font.times_bold_italic()
        input.elements.append(element)
        pdf.inputs.append(input)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "font_core.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_font(self, pdf, test_params):
        input1 = PageInput()
        font = Font.from_file(test_params.resources_path + "DejaVuSans.ttf")
        font.embed = True
        font.subset = True
        element = TextElement("Hello World", ElementPlacement.TopLeft)
        element.font = font
        input1.elements.append(element)
        pdf.inputs.append(input1)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "font.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_font_google(self, pdf, test_params):
        input = PageInput()
        font = Font.google("Roboto")
        font.embed = True
        font.subset = True
        element = TextElement("Hello World", ElementPlacement.TopLeft)
        element.font = font
        input.elements.append(element)
        pdf.inputs.append(input)
        
        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "font_google.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_font_global(self, pdf, test_params):
        input = PageInput()
        font = Font.global_font("Paris Normal")
        font.embed = True
        font.subset = True
        element = TextElement("Hello World", ElementPlacement.TopLeft)
        element.font = font
        input.elements.append(element)
        pdf.inputs.append(input)
        
        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "font_global.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful