import pytest
from ..common_imports import (
    PdfResource,
    PdfInput,
    Pdf,
    Template,
    ElementPlacement,
    PageNumberingElement,
    Font,
    RgbColor
)

class TestTemplatePageNumbering:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_template_page_numbering(self, pdf, test_params):
        
        resource = PdfResource(test_params.resources_path + "DocumentA100.pdf", "DocumentA100.pdf")
        input1 = PdfInput(resource)
        pdf.inputs.append(input1)

        font_resource = Font.from_file(test_params.resources_path + "DejaVuSans.ttf", "DejaVuSans")

        template_A = Template("TemplateA")
        page_numbering_element = PageNumberingElement("%%CP%% of %%TP%%", ElementPlacement.TopCenter)
        page_numbering_element.font = font_resource
        page_numbering_element.font_size = 14
        page_numbering_element.color = RgbColor.red()
        template_A.elements.append(page_numbering_element)
        input1.template = template_A

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_page_numbering.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_template_page_numbering_with_tokens(self, pdf, test_params):
        resource = PdfResource(test_params.resources_path + "Emptypages.pdf", "Emptypages.pdf")
        input1 = PdfInput(resource)
        pdf.inputs.append(input1)

        template_A = Template("TemplateA")
        top_left_element = PageNumberingElement("%%CP(1)%% of %%TP%%", ElementPlacement.TopLeft)
        top_left_element.even_pages = True
        template_A.elements.append(top_left_element)

        top_center_element = PageNumberingElement("%%SP(I)%% of %%ST%%", ElementPlacement.TopCenter)
        top_center_element.odd_pages = True
        template_A.elements.append(top_center_element)

        top_right_element = PageNumberingElement("%%CP(i)%% of %%TP%%", ElementPlacement.TopRight)
        top_right_element.even_pages = True
        template_A.elements.append(top_right_element)

        bottom_left_element = PageNumberingElement("%%CP(I)%% of %%TP%%", ElementPlacement.BottomLeft)
        bottom_left_element.odd_pages = True
        template_A.elements.append(bottom_left_element)

        bottom_center_element = PageNumberingElement("%%CP(b)%% of %%TP%%", ElementPlacement.BottomCenter)
        bottom_center_element.even_pages = True
        template_A.elements.append(bottom_center_element)

        bottom_right_element = PageNumberingElement("%%CP(a)%% of %%TP%%", ElementPlacement.BottomRight)
        bottom_right_element.odd_pages = True
        template_A.elements.append(bottom_right_element)

        input1.template = template_A

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "template_page_numbering_with_tokens.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful