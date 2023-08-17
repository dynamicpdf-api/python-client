import pytest
from ..common_imports import (
    Pdf,
    PageInput,
    ElementPlacement,
    RectangleElement,
    LineStyle,
    RgbColor
)

class TestRectangle:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_rectangle_element(self, pdf, test_params):
        input1 = PageInput()
        element = RectangleElement(ElementPlacement.TopCenter, 100, 50)
        element.x_offset = 50
        element.y_offset = 50
        element.corner_radius = 10
        element.border_width = 5
        element.border_style = LineStyle.dots()
        element.border_color = RgbColor.blue()
        element.fill_color = RgbColor.green()
        input1.elements.append(element)
        pdf.inputs.append(input1)
        
        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "rectangle_element.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful