import pytest
from ..common_imports import (
    Pdf,
    ImageResource,
    ImageInput
)

class TestImageInput:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_image_input_png(self, pdf, test_params):
        resource = ImageResource(test_params.resources_path + "DPDFLogo.png")
        input = ImageInput(resource)
        input.scale_x = 4
        input.scale_y = 4
        input.page_width = 400
        input.page_height = 400

        pdf.inputs.append(input)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "image_input_png.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_image_input_multi_tiff(self, pdf, test_params):
        resource = ImageResource(test_params.resources_path + "fw9_18.tif", "fw9_18.tif")
        input = ImageInput(resource)
        input.right_margin = 50
        input.bottom_margin = 50
        input.top_margin = 50
        input.left_margin = 50
        pdf.inputs.append(input)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "image_input_multi_tiff.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful
