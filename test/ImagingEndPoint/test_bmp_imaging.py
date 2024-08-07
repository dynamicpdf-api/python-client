import pytest
from ..common_imports import (
    PdfImage,
    PdfResource,
    BmpImageFormat,
    FixedImageSize,
    ImageSizeUnit,
    MaxImageSize,
    DpiImageSize,
    PercentageImageSize,
    DitheringAlgorithm,
    BmpMonochromeColorFormat,
    BmpColorFormat,
    ColorFormatType
)

class TestBmpImageFormat:

    def test_bmp_imageformat(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        bmpImageFormat = BmpImageFormat()
        pdfImage.image_format = bmpImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_", res)
        assert res.is_successful

    def test_bmp_imageformat_pagecount(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        pdfImage.start_page_number = 1
        pdfImage.page_count = 2
        bmpImageFormat = BmpImageFormat()
        pdfImage.image_format = bmpImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_pageCount_", res)
        assert res.is_successful
        
    def test_bmp_imageformat_fixed_point(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        fixedImageSize = FixedImageSize()
        fixedImageSize.unit = ImageSizeUnit.Point
        fixedImageSize.height=500
        fixedImageSize.width=500
        bmpImageFormat = BmpImageFormat()
        pdfImage.image_format = bmpImageFormat
        pdfImage.image_size = fixedImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_fixed_point_", res)
        assert res.is_successful

    def test_bmp_imageformat_fixed_inch(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        fixedImageSize = FixedImageSize()
        fixedImageSize.unit = ImageSizeUnit.Inch
        fixedImageSize.height=5
        fixedImageSize.width=5
        bmpImageFormat = BmpImageFormat()
        pdfImage.image_format = bmpImageFormat
        pdfImage.image_size = fixedImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_fixed_inch_", res)
        assert res.is_successful

    def test_bmp_imageformat_fixed_millimeter(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        fixedImageSize = FixedImageSize()
        fixedImageSize.unit = ImageSizeUnit.Millimeter
        fixedImageSize.height=200
        fixedImageSize.width=200
        bmpImageFormat = BmpImageFormat()
        pdfImage.image_format = bmpImageFormat
        pdfImage.image_size = fixedImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_fixed_millimeter_", res)
        assert res.is_successful

    def test_bmp_imageformat_max_point(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        maxImageSize = MaxImageSize()
        maxImageSize.unit = ImageSizeUnit.Point
        maxImageSize.max_height=500
        maxImageSize.max_width=500
        bmpImageFormat = BmpImageFormat()
        pdfImage.image_format = bmpImageFormat
        pdfImage.image_size = maxImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_max_point_", res)
        assert res.is_successful

    def test_bmp_imageformat_max_inch(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        maxImageSize = MaxImageSize()
        maxImageSize.unit = ImageSizeUnit.Inch
        maxImageSize.max_height=7
        maxImageSize.max_width=7
        bmpImageFormat = BmpImageFormat()
        pdfImage.image_format = bmpImageFormat
        pdfImage.image_size = maxImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_max_inch_", res)
        assert res.is_successful

    def test_bmp_imageformat_max_millimeter(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        maxImageSize = MaxImageSize()
        maxImageSize.unit = ImageSizeUnit.Millimeter
        maxImageSize.max_height=400
        maxImageSize.max_width=400
        bmpImageFormat = BmpImageFormat()
        pdfImage.image_format = bmpImageFormat
        pdfImage.image_size = maxImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_max_millimeter_", res)
        assert res.is_successful

    def test_bmp_imageformat_dpi(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        dpiImageSize = DpiImageSize()
        dpiImageSize.horizontal_dpi=155
        dpiImageSize.vertical_dpi=155

        pdfImage.image_size = dpiImageSize
        
        bmpImageFormat = BmpImageFormat()
        pdfImage.image_format = bmpImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_dpi_", res)
        assert res.is_successful

    def test_bmp_imageformat_percentage(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        percentageImageSize = PercentageImageSize()
        percentageImageSize.horizontal_percentage =50
        percentageImageSize.vertical_percentage=50
        bmpImageFormat = BmpImageFormat()
        pdfImage.image_size = percentageImageSize
        pdfImage.image_format = bmpImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_percentage_", res)
        assert res.is_successful

    def test_bmp_imageformat_Bayer(self, test_params, get_endpoint , get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        bmpmono = BmpMonochromeColorFormat()
        bmpmono.dithering_algorithm = DitheringAlgorithm.Bayer
        bmpImageFormat = BmpImageFormat()
        bmpImageFormat.color_format = bmpmono
        
        pdfImage.image_format = bmpImageFormat
    

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_Bayer_", res)
        assert res.is_successful

    def test_bmp_imageformat_FloydSteinberg(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        bmpmono = BmpMonochromeColorFormat()
        bmpmono.dithering_algorithm = DitheringAlgorithm.FloydSteinberg
        bmpImageFormat = BmpImageFormat()
        bmpImageFormat.color_format = bmpmono
        
        pdfImage.image_format = bmpImageFormat
    

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_FloydSteinberg_", res)
        assert res.is_successful

    def test_bmp_imageformat_rgb(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        bmpImageFormat = BmpImageFormat()
        bmpImageFormat.color_format = BmpColorFormat(ColorFormatType.Rgb)
        pdfImage.image_format = bmpImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_rgb_", res)
        assert res.is_successful

    def test_bmp_imageformat_rgba(self, test_params, get_endpoint , get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        bmpImageFormat = BmpImageFormat()
        bmpImageFormat.color_format = BmpColorFormat(ColorFormatType.Rgba)
        pdfImage.image_format = bmpImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_rgba_", res)
        assert res.is_successful

    def test_bmp_imageformat_Monochrome(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        bmpImageFormat = BmpImageFormat()
        bmpImageFormat.color_format = BmpColorFormat(ColorFormatType.Monochrome)
        pdfImage.image_format = bmpImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_Monochrome_", res)
        assert res.is_successful

    def test_bmp_imageformat_Grayscale(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        bmpImageFormat = BmpImageFormat()
        bmpImageFormat.color_format = BmpColorFormat(ColorFormatType.Grayscale)
        pdfImage.image_format = bmpImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_Grayscale_", res)
        assert res.is_successful

    def test_bmp_imageformat_Indexed(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        bmpImageFormat = BmpImageFormat()
        bmpImageFormat.color_format = BmpColorFormat(ColorFormatType.Indexed)
        pdfImage.image_format = bmpImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_Indexed_", res)
        assert res.is_successful

    def test_bmp_imageformat_black_threshold(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "Gray.pdf")
        pdfImage = PdfImage(resource)

        bmpmonochrome = BmpMonochromeColorFormat()
        bmpmonochrome.black_threshold = 200

        bmpImageFormat = BmpImageFormat()
        bmpImageFormat.color_format = bmpmonochrome
        pdfImage.image_format = bmpImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"bmp_image_format_black_threshold_", res)
        assert res.is_successful