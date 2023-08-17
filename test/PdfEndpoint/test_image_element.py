import pytest
from ..common_imports import (
    Pdf,
    PageInput,
    ImageResource,
    ImageElement,
    ElementPlacement,
)

class TestImageElement:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_image_element(self, pdf, test_params):
        input = PageInput()
        resource1 = ImageResource(test_params.resources_path + "Northwind Logo.gif", "Northwind Logo.gif")
        element = ImageElement(resource1, ElementPlacement.TopCenter)
        element.x_offset = 50
        element.y_offset = 50
        element.scale_x = 3
        element.scale_y = 3
        input.elements.append(element)
        pdf.inputs.append(input)
        
        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "image_element.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful