import pytest
import io
from ..common_imports import (
    PdfResource,
    PdfInput,
    Pdf,
    PageInput,
    Template,
    AztecBarcodeElement,
    ElementPlacement,
    Gs1DataBarType,
    AztecSymbolSize,
    Code11BarcodeElement,
    Code25BarcodeElement,
    Code128BarcodeElement,
    Code39BarcodeElement,
    Code93BarcodeElement,
    Pdf417BarcodeElement,
    MsiBarcodeElement,
    Iata25BarcodeElement,
    QrCodeElement,
    QrCodeFnc1,
    Compaction,
    Gs1DataBarBarcodeElement,
    StackedGs1DataBarBarcodeElement,
    DataMatrixBarcodeElement,
    RgbColor,
    WebColor,
    StackedGs1DataBarType,
    ErrorCorrection,
    Font,
    MsiBarcodeCheckDigitMode
)

class TestTemplateBarcodeElement:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)


    def test_template_barcode_element_aztec(self, pdf, test_params):
        
        input1 = PageInput()
        templateA = Template("TemplateA")

        element = AztecBarcodeElement("Hello World", ElementPlacement.BottomRight)
        element.symbol_size = AztecSymbolSize.R105xC105
        element.x_dimension = 3
        element.color = RgbColor.red()
        element.aztec_error_correction = 30
        element.process_tilde = True
        element.reader_initialization_symbol = True
        element.value = "test123"
        element.x_offset = -100
        element.y_offset = -100
        templateA.elements.append(element)
        input1.template = templateA

        pdf.inputs.append(input1)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_barcode_element_aztec.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_template_barcode_element_data_matrix(self, pdf, test_params):

        resource1 = PdfResource(test_params.resources_path + "Emptypages.pdf")
        input1 = PdfInput(resource1)

        element = DataMatrixBarcodeElement("Hello World", ElementPlacement.TopRight, 0, 0)
        element.placement = ElementPlacement.TopLeft
        element.x_offset = 50
        element.y_offset = 50
        element.x_dimension = 3
        element.process_tilde = True
        element.color = RgbColor.yellow()
        templateA = Template("TemplateA")
        templateA.elements.append(element)
        input1.template = templateA
        pdf.inputs.append(input1)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_barcode_element_data_matrix.pdf", "wb") as out_stream:
                        out_stream.write(res.content)
        assert res.is_successful

    def test_template_barcode_element_pdf417(self, pdf, test_params):

        input1 = PdfInput('TFWResources/Emptypages.pdf')

        templateA = Template("TemplateA")
        element = Pdf417BarcodeElement("Hello World", ElementPlacement.TopLeft, 2)
        element.color = RgbColor.red()
        element.compaction = Compaction.Text
        element.compact_pdf417 = True
        element.error_correction = ErrorCorrection.Level6
        element.even_pages = True
        element.placement = ElementPlacement.TopRight
        element.process_tilde = True
        element.x_dimension = 4
        element.y_dimension = 5
        element.x_offset = -50
        element.y_offset = 50
        templateA.elements.append(element)
        input1.template = templateA
        pdf.inputs.append(input1)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_barcode_element_pdf417.pdf", "wb") as out_stream:
                        out_stream.write(res.content)
        assert res.is_successful
    
    def test_template_barcode_element_qrcode(self, pdf, test_params):

        with open(test_params.resources_path + "Emptypages.pdf", 'rb') as file:
            memory = io.BytesIO(file.read())
        resource1 = PdfResource(memory)

        input1 = PdfInput(resource1)
        templateA = Template("TemplateA")
        barcodeElement = QrCodeElement("Hello World", ElementPlacement.TopCenter, 50, 50)
        barcodeElement.color = RgbColor.orange()
        barcodeElement.version = 20
        barcodeElement.fnc1 = QrCodeFnc1.Gs1
        templateA.elements.append(barcodeElement)
        input1.template = templateA
        pdf.inputs.append(input1)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_barcode_element_qrcode.pdf", "wb") as out_stream:
                        out_stream.write(res.content)
        assert res.is_successful

    def test_template_barcode_element_code128(self, pdf, test_params):

        resource1 = PdfResource(test_params.resources_path + "Emptypages.pdf")
        input = PdfInput(resource1)
        template = Template("TemplateA")

        element = Code128BarcodeElement("Code 128 ~ABarcode.", ElementPlacement.TopCenter, 50)
        element.height = 60
        element.x_offset = 100
        element.y_offset = 100
        element.color = RgbColor.red()
        element.x_dimension = 2
        element.text_color = RgbColor.blue()
        element.font = Font.courier()
        element.font_size = 15
        element.process_tilde = True
        element.ucc_ean128 = True
        template.elements.append(element)
        input.template = template
        pdf.inputs.append(input)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_barcode_element_code128.pdf", "wb") as out_stream:
                        out_stream.write(res.content)
        assert res.is_successful

    def test_template_barcode_element_code39(self, pdf, test_params):
        
        input1 = PageInput()

        element = Code39BarcodeElement("CODE 39", ElementPlacement.TopCenter, 100, 50, 50)
        element.x_dimension = 1.5
        element.show_text = True
        element.text_color = RgbColor.red()
        element.font = Font.courier_bold()
        input1.elements.append(element)
        pdf.inputs.append(input1)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_barcode_element_code39.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_template_barcode_element_code25(self, pdf, test_params):
        
        with open(test_params.resources_path + "Emptypages.pdf", 'rb') as file:
            memory = io.BytesIO(file.read())
        resource = PdfResource(memory)
        input1 = PdfInput(resource)

        templateA = Template("TemplateA")
        element = Code25BarcodeElement("1234567890", ElementPlacement.TopCenter, 50)
        element.height = 80
        element.x_offset = 100
        element.y_offset = 100
        element.color = RgbColor.red()
        element.x_dimension = 1.5
        element.show_text = True
        element.odd_pages = True
        templateA.elements.append(element)
        input1.template = templateA
        pdf.inputs.append(input1)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_barcode_element_code25.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_template_barcode_element_code93(self, pdf, test_params):

        input1 = PageInput()
        element = Code93BarcodeElement("CODE 93", ElementPlacement.TopCenter, 50)
        element.h = 60
        element.x_offset = 100
        element.y_offset = 100
        element.color = WebColor("#FF0000")
        element.x_dimension = 2
        element.show_text = False
        input1.elements.append(element)
        pdf.inputs.append(input1)

        res = pdf.process()

        if res.is_successful:
                with open(test_params.output_path + "template_barcode_element_code93.pdf", "wb") as out_stream:
                    out_stream.write(res.content)
        assert res.is_successful
        
    def test_template_barcode_element_code11(self, pdf, test_params):
        
        with open(test_params.resources_path + "Emptypages.pdf", 'rb') as file:
            memory = io.BytesIO(file.read())
        resource = PdfResource(memory)
        input1 = PdfInput(resource)

        templateA = Template("TemplateA")
        element = Code11BarcodeElement("12345678", ElementPlacement.BottomLeft, 100, 10, 10);
        element.x_dimension = 3
        element.y_offset = -50
        element.text_color = RgbColor.red()
        element.font = Font.helvetica_oblique()
        element.font_size = 20
        element.even_pages = True
        templateA.elements.append(element)
        input1.template = templateA
        pdf.inputs.append(input1)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_barcode_element_code11.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_template_barcode_element_gs1(self, pdf, test_params):

        pdf_input = PdfInput('TFWResources/Emptypages.pdf')

        templateA = Template("TemplateA")
        element = Gs1DataBarBarcodeElement("12345678", ElementPlacement.TopCenter, 50, Gs1DataBarType.Omnidirectional)
        element.placement = ElementPlacement.BottomCenter
        element.x_offset = 0
        element.y_offset = -100
        element.color = WebColor("#02F1A5")
        element.x_dimension = 1.4
        templateA.elements.append(element)
        pdf_input.template = templateA
        pdf.inputs.append(pdf_input)
        
        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_barcode_element_gs1.pdf", "wb") as out_stream:
                        out_stream.write(res.content)
        assert res.is_successful

    def test_template_barcode_element_stacked_gs1(self, pdf, test_params):
        
        input1 = PageInput()
        element = StackedGs1DataBarBarcodeElement("1234567890", ElementPlacement.TopCenter, StackedGs1DataBarType.Stacked, 25)
        element.row_height = 60
        element.x_offset = 10
        element.y_offset = 20
        element.color = RgbColor.maroon()
        element.x_dimension = 1
        input1.elements.append(element)
        pdf.inputs.append(input1)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_barcode_element_stacked_gs1.pdf", "wb") as out_stream:
                        out_stream.write(res.content)
        assert res.is_successful

    def test_template_barcode_element_iata25(self, pdf, test_params):
        
        input1 = PageInput()
        templateA = Template("TemplateA")
        barcodeElement = Iata25BarcodeElement("12345678", ElementPlacement.TopCenter, 50, 100, 0)
        barcodeElement.height = 60
        barcodeElement.color = RgbColor.yellow()
        barcodeElement.x_dimension = 3
        barcodeElement.text_color = RgbColor.pink()
        barcodeElement.include_check_digit = True
        templateA.elements.append(barcodeElement)

        input1.template = templateA
        pdf.inputs.append(input1)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_barcode_element_iata25.pdf", "wb") as out_stream:
                        out_stream.write(res.content)
        assert res.is_successful

    def test_template_barcode_element_msi(self, pdf, test_params):
        
        resource1 = PdfResource(test_params.resources_path + "Emptypages.pdf")
        input = PdfInput(resource1)
        template = Template("TemplateA")

        element = MsiBarcodeElement("1234567890", ElementPlacement.TopCenter, 50)
        element.height = 70
        element.x_offset = 20
        element.y_offset = 20
        element.color = RgbColor.violet()
        element.x_dimension = 2
        element.show_text = True
        element.append_check_digit = MsiBarcodeCheckDigitMode.Mod1010
        element.even_pages = True
        element.odd_pages = True
        template.elements.append(element)
        input.template = template
        pdf.inputs.append(input)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_barcode_element_msi.pdf", "wb") as out_stream:
                        out_stream.write(res.content)
        assert res.is_successful

