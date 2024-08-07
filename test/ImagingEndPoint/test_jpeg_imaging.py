import pytest
from ..common_imports import (
    PdfImage,
    PdfResource,
    JpegImageFormat,
    FixedImageSize,
    ImageSizeUnit,
    MaxImageSize,
    DpiImageSize,
    PercentageImageSize,
)

class TestJpegImageFormat:

    def test_jpeg_imageformat(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        jpegImageFormat = JpegImageFormat()
        pdfImage.image_format = jpegImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"jpeg_image_format_", res)
        assert res.is_successful

    def test_jpeg_imageformat_pagecount(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        pdfImage.start_page_number = 1
        pdfImage.page_count = 2
        jpegImageFormat = JpegImageFormat()
        pdfImage.image_format = jpegImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"jpeg_image_format_pageCount_", res)
        assert res.is_successful
        
    def test_jpeg_imageformat_fixed_point(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        fixedImageSize = FixedImageSize()
        fixedImageSize.unit = ImageSizeUnit.Point
        fixedImageSize.height=500
        fixedImageSize.width=500
        jpegImageFormat = JpegImageFormat()
        pdfImage.image_format = jpegImageFormat
        pdfImage.image_size = fixedImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"jpeg_image_format_fixed_point_", res)
        assert res.is_successful

    def test_jpeg_imageformat_fixed_inch(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        fixedImageSize = FixedImageSize()
        fixedImageSize.unit = ImageSizeUnit.Inch
        fixedImageSize.height=5
        fixedImageSize.width=5
        jpegImageFormat = JpegImageFormat()
        pdfImage.image_format = jpegImageFormat
        pdfImage.image_size = fixedImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"jpeg_image_format_fixed_inch_", res)
        assert res.is_successful

    def test_jpeg_imageformat_fixed_millimeter(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        fixedImageSize = FixedImageSize()
        fixedImageSize.unit = ImageSizeUnit.Millimeter
        fixedImageSize.height=200
        fixedImageSize.width=200
        jpegImageFormat = JpegImageFormat()
        pdfImage.image_format = jpegImageFormat
        pdfImage.image_size = fixedImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"jpeg_image_format_fixed_millimeter_", res)
        assert res.is_successful

    def test_jpeg_imageformat_max_point(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        maxImageSize = MaxImageSize()
        maxImageSize.unit = ImageSizeUnit.Point
        maxImageSize.max_height=500
        maxImageSize.max_width=500
        jpegImageFormat = JpegImageFormat()
        pdfImage.image_format = jpegImageFormat
        pdfImage.image_size = maxImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"jpeg_image_format_max_point_", res)
        assert res.is_successful

    def test_jpeg_imageformat_max_inch(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        maxImageSize = MaxImageSize()
        maxImageSize.unit = ImageSizeUnit.Inch
        maxImageSize.max_width=7
        maxImageSize.max_height=7
        jpegImageFormat = JpegImageFormat()
        pdfImage.image_format = jpegImageFormat
        pdfImage.image_size = maxImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"jpeg_image_format_max_inch_", res)
        assert res.is_successful

    def test_jpeg_imageformat_max_millimeter(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        maxImageSize = MaxImageSize()
        maxImageSize.unit = ImageSizeUnit.Millimeter
        maxImageSize.max_height=400
        maxImageSize.max_width=400
        jpegImageFormat = JpegImageFormat()
        pdfImage.image_format = jpegImageFormat
        pdfImage.image_size = maxImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"jpeg_image_format_max_millimeter_", res)
        assert res.is_successful

    def test_jpeg_imageformat_dpi(self, test_params, get_endpoint , get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        dpiImageSize = DpiImageSize()
        dpiImageSize.horizontal_dpi=155
        dpiImageSize.vertical_dpi=155

        pdfImage.image_size = dpiImageSize
        
        jpegImageFormat = JpegImageFormat()
        pdfImage.image_format = jpegImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"jpeg_image_format_dpi_", res)
        assert res.is_successful

    def test_jpeg_imageformat_percentage(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        percentageImageSize = PercentageImageSize()
        percentageImageSize.horizontal_percentage =50
        percentageImageSize.vertical_percentage=50
        jpegImageFormat = JpegImageFormat()
        pdfImage.image_size = percentageImageSize
        pdfImage.image_format = jpegImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"jpeg_image_format_percentage_", res)
        assert res.is_successful

    def test_jpeg_imageformat_Quality(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        jpegImageFormat = JpegImageFormat()
        jpegImageFormat.quality = 10
        pdfImage.image_format = jpegImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"jpeg_image_format_quality_", res)
        assert res.is_successful