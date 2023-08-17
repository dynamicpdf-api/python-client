import pytest
from ..common_imports import (
    Pdf,
    PageInput,
    TextElement,
    ElementPlacement,
    CmykColor,
    RgbColor,
    Grayscale,
    Template
)

class TestColorPattern:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)
    
    def test_color_pattern_named(self, pdf, test_params):
        input = PageInput()
        template = Template("Temp1")
        text_element = TextElement("Hello World", ElementPlacement.TopCenter)
        text_element.color = RgbColor.red()
        input.elements.append(text_element)
        input.template = template
        pdf.inputs.append(input)
    
        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "color_pattern_named.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_color_pattern_RGB(self, pdf, test_params):
        input = PageInput()
        pdf.inputs.append(input)
        text_element = TextElement("Hello World", ElementPlacement.TopCenter)
        text_element.color = RgbColor(0, 1, 0)
        input.elements.append(text_element)
        
        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "color_pattern_RGB.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_color_pattern_CMYK(self, pdf, test_params):
        input = PageInput()
        text_element = TextElement("Hello World", ElementPlacement.TopCenter)
        text_element.color = CmykColor(0, 1, 0, 0)
        input.elements.append(text_element)
        pdf.inputs.append(input)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "color_pattern_CMYK.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_color_pattern_gray_scale(self, pdf, test_params):
        input = PageInput()
        text_element = TextElement("Hello World", ElementPlacement.TopCenter)
        text_element.color = Grayscale(0.8)
        input.elements.append(text_element)
        pdf.inputs.append(input)
        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "color_pattern_gray_scale.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful