import pytest

from ..common_imports import (
    PdfImage,
    PdfResource,
    TiffImageFormat,
    FixedImageSize,
    ImageSizeUnit,
    MaxImageSize,
    DpiImageSize,
    PercentageImageSize,
    TiffMonochromeColorFormat,
    TiffIndexedColorFormat,
    QuantizationAlgorithm,
    ColorFormatType,
    DitheringAlgorithm,
    TiffColorFormat
)

class TestTiffImageFormat:

    def test_tiff_imageformat(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        tiffImageFormat = TiffImageFormat()
        pdfImage.image_format = tiffImageFormat
        
        pdfImage = get_endpoint(pdfImage, test_params)
        
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"TiffImageFormat_", res)

        assert res.is_successful

    def test_tiff_imageformat_pagecount(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        pdfImage.start_page_number = 1
        pdfImage.page_count = 2
        tiffImageFormat = TiffImageFormat()
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"TiffImageFormat_page_Count_", res)

        assert res.is_successful
        
    def test_tiff_imageformat_fixed_point(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        fixedImageSize = FixedImageSize()
        fixedImageSize.unit = ImageSizeUnit.Point
        fixedImageSize.height=500
        fixedImageSize.width=500
        tiffImageFormat = TiffImageFormat()
        pdfImage.image_format = tiffImageFormat
        pdfImage.image_size = fixedImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_fixed_point_", res)
        assert res.is_successful

    def test_tiff_imageformat_fixed_inch(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        fixedImageSize = FixedImageSize()
        fixedImageSize.unit = ImageSizeUnit.Inch
        fixedImageSize.height=5
        fixedImageSize.width=5
        tiffImageFormat = TiffImageFormat()
        pdfImage.image_format = tiffImageFormat
        pdfImage.image_size = fixedImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_fixed_inch_", res)
        assert res.is_successful

    def test_tiff_imageformat_fixed_millimeter(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        fixedImageSize = FixedImageSize()
        fixedImageSize.unit = ImageSizeUnit.Millimeter
        fixedImageSize.height=200
        fixedImageSize.width=200
        tiffImageFormat = TiffImageFormat()
        pdfImage.image_format = tiffImageFormat
        pdfImage.image_size = fixedImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_fixed_millimeter_", res)
        assert res.is_successful

    def test_tiff_imageformat_max_point(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        maxImageSize = MaxImageSize()
        maxImageSize.unit = ImageSizeUnit.Point
        maxImageSize.max_height=500
        maxImageSize.max_width=500
        tiffImageFormat = TiffImageFormat()
        pdfImage.image_format = tiffImageFormat
        pdfImage.image_size = maxImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_max_point_", res)
        assert res.is_successful

    def test_tiff_imageformat_max_inch(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        maxImageSize = MaxImageSize()
        maxImageSize.unit = ImageSizeUnit.Inch
        maxImageSize.max_height=7
        maxImageSize.max_width=7
        tiffImageFormat = TiffImageFormat()
        pdfImage.image_format = tiffImageFormat
        pdfImage.image_size = maxImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_max_inch_", res)
        assert res.is_successful

    def test_tiff_imageformat_max_millimeter(self, test_params, get_endpoint, get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        
        maxImageSize = MaxImageSize()
        maxImageSize.unit = ImageSizeUnit.Millimeter
        maxImageSize.max_height=400
        maxImageSize.max_width=400
        tiffImageFormat = TiffImageFormat()
        pdfImage.image_format = tiffImageFormat
        pdfImage.image_size = maxImageSize

        pdfImage = get_endpoint(pdfImage, test_params)

        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_max_millimeter_", res)
        assert res.is_successful

    def test_tiff_imageformat_dpi(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        dpiImageSize = DpiImageSize()
        dpiImageSize.horizontal_dpi=155
        dpiImageSize.vertical_dpi=155

        pdfImage.image_size = dpiImageSize
        
        tiffImageFormat = TiffImageFormat()
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_dpi_", res)
        assert res.is_successful

    def test_tiff_imageformat_percentage(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        percentageImageSize = PercentageImageSize()
        percentageImageSize.horizontal_percentage =50
        percentageImageSize.vertical_percentage=50
        tiffImageFormat = TiffImageFormat()
        pdfImage.image_size = percentageImageSize
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_percentage_", res)
        assert res.is_successful

    def test_tiff_imageformat_floyd_monochrome(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        tiffMonochrome = TiffMonochromeColorFormat()
        tiffMonochrome.dithering_algorithm = DitheringAlgorithm.FloydSteinberg
        tiffMonochrome.dithering_percent = 50
        
        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = tiffMonochrome
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_floyd_monochrome_", res)
        assert res.is_successful

    def test_tiff_imageformat_bayer_indexed(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        tiffMonochrome = TiffMonochromeColorFormat()
        tiffMonochrome.dithering_algorithm = DitheringAlgorithm.Bayer
        tiffMonochrome.dithering_percent = 50
        
        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = tiffMonochrome
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_bayer_monochrome_", res)
        assert res.is_successful

    def test_tiff_imageformat_floyd_indexed(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        tiffIndexed = TiffIndexedColorFormat()
        tiffIndexed.dithering_algorithm = DitheringAlgorithm.FloydSteinberg
        tiffIndexed.dithering_percent = 50
        
        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = tiffIndexed
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_floyd_indexed_", res)
        assert res.is_successful

    def test_tiff_imageformat_bayer_indexed(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        tiffIndexed = TiffIndexedColorFormat()
        tiffIndexed.dithering_algorithm = DitheringAlgorithm.Bayer
        tiffIndexed.dithering_percent = 50
        
        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = tiffIndexed
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_bayer_indexed_", res)
        assert res.is_successful

    def test_tiff_imageformat_qa_octree(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        tiffIndexed = TiffIndexedColorFormat()
        tiffIndexed.quantization_algorithm = QuantizationAlgorithm.Octree
        
        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = tiffIndexed
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_qa_octree_", res)
        assert res.is_successful

    def test_tiff_imageformat_qa_WebSafe(self, test_params, get_endpoint , get_imaging):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        tiffIndexed = TiffIndexedColorFormat()
        tiffIndexed.quantization_algorithm = QuantizationAlgorithm.WebSafe
        
        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = tiffIndexed
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_qa_WebSafe_", res)
        assert res.is_successful

    def test_tiff_imageformat_qa_Werner(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        tiffIndexed = TiffIndexedColorFormat()
        tiffIndexed.quantization_algorithm = QuantizationAlgorithm.Werner
        
        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = tiffIndexed
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_qa_Werner_", res)
        assert res.is_successful

    def test_tiff_imageformat_qa_Wu(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        tiffIndexed = TiffIndexedColorFormat()
        tiffIndexed.quantization_algorithm = QuantizationAlgorithm.Wu
        
        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = tiffIndexed
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_qa_Wu_", res)
        assert res.is_successful

    def test_tiff_imageformat_rgb(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = TiffColorFormat(ColorFormatType.Rgb)
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_rgb_", res)
        assert res.is_successful

    def test_tiff_imageformat_rgba(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = TiffColorFormat(ColorFormatType.Rgba)
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_rgba_", res)
        assert res.is_successful

    def test_tiff_imageformat_Monochrome(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = TiffColorFormat(ColorFormatType.Monochrome)
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_Monochrome_", res)
        assert res.is_successful

    def test_tiff_imageformat_Grayscale(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = TiffColorFormat(ColorFormatType.Grayscale)
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_Grayscale_", res)
        assert res.is_successful

    def test_tiff_imageformat_Indexed(self, test_params, get_endpoint, get_imaging ):
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)

        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = TiffColorFormat(ColorFormatType.Indexed)
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_Indexed_", res)
        assert res.is_successful

    def test_tiff_imageformat_black_threshold(self, test_params, get_endpoint , get_imaging):
        resource = PdfResource(test_params.resources_path + "Gray.pdf")
        pdfImage = PdfImage(resource)

        tiffmonochrome = TiffMonochromeColorFormat()
        tiffmonochrome.black_threshold = 200

        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.color_format = tiffmonochrome
        pdfImage.image_format = tiffImageFormat

        pdfImage = get_endpoint(pdfImage, test_params)
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_black_threshold_", res)
        assert res.is_successful

    def test_tiff_imageformat_multipage(self, test_params, get_endpoint, get_imaging ):
        
        
        resource = PdfResource(test_params.resources_path + "DocumentA.pdf")
        pdfImage = PdfImage(resource)
        pdfImage = get_endpoint(pdfImage, test_params)
        tiffImageFormat = TiffImageFormat()
        tiffImageFormat.multi_page = True
        pdfImage.image_format = tiffImageFormat

        
        res = pdfImage.process()

        if res.is_successful:
            get_imaging(test_params.output_path+"tiff_image_format_multipage_", res)
        assert res.is_successful
