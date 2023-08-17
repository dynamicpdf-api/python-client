import pytest
from ..common_imports import (
    Pdf,
    PageInput,
    ElementPlacement,
    LineElement,
    RgbColor,
    LineStyle
)

class TestLine:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_line_element(self, pdf, test_params):
        input1 = PageInput()
        line_element = LineElement(ElementPlacement.TopLeft, 200, 200)
        line_element.x_offset = 50
        line_element.y_offset = 50
        line_element.color = RgbColor(0, 0, 1)
        line_element.line_style = LineStyle.dash_large()
        line_element.width = 4
        input1.elements.append(line_element)
        pdf.inputs.append(input1)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "line_element.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful