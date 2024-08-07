import base64
import io
import pytest
from ..common_imports import PdfResource, PdfImage

class TestPdfImage:

    @pytest.fixture
    def resource(self, test_params):
        return PdfResource(test_params.resources_path + "AllPageElements.pdf", "AllPageElements.pdf")

    @pytest.fixture
    def rasterizer(self, resource, test_params, get_endpoint):
        rasterizer = PdfImage(resource)
        rasterizer.start_page_number=1
        rasterizer.page_count=1
        return get_endpoint(rasterizer, test_params)

    def test_pdf_image(self, rasterizer, test_params):

        res = rasterizer.process()

        if res.is_successful:
            for i, image in enumerate(res.images):
                file_name = f"image_{i}.{res.image_format}"
                with open(test_params.output_path + file_name, "wb") as out_stream:
                    out_stream.write(base64.b64decode(image.data))

        assert res.is_successful