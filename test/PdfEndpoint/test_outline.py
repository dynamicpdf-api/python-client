import pytest
from ..common_imports import (
    PdfResource,
    PdfInput,
    Pdf,
    PageZoom,
    RgbColor,
    OutlineStyle,
    TextElement,
    ElementPlacement,
    GoToAction,
    UrlAction
)

class TestOutline:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)
    
    def test_outline_with_goto_action(self, pdf, test_params):
        resource = PdfResource(test_params.resources_path + "EmptyPages.pdf")
        input = PdfInput(resource)
        pdf.inputs.append(input)

        resource1 = PdfResource(test_params.resources_path + "SinglePage.pdf")
        input1 = PdfInput(resource1)
        pdf.inputs.append(input1)

        outline = pdf.outlines.add("OutlineA")
        outline.color = RgbColor.red()
        outline.style = OutlineStyle.Bold
        outline.expanded = True

        linkTo = GoToAction(input1)
        linkTo.page_offset = -5
        linkTo.page_zoom = PageZoom.FitPage
        outline.action = linkTo

        res = pdf.process()
        
        if res.is_successful:
            with open(test_params.output_path + "outline_with_goto_action.pdf", "wb") as out_stream:
                out_stream.write(res.content)
        
        assert res.is_successful

    def test_outline_with_url_action(self, pdf, test_params):
        resource = PdfResource(test_params.resources_path + "EmptyPages.pdf")
        input = PdfInput(resource)
        pdf.inputs.append(input)

        outline = pdf.outlines.add("OutlineA")
        outline.color = RgbColor.red()
        outline.style = OutlineStyle.Bold
        outline.expanded = True

        action = UrlAction("https://www.dynamicpdf.com")
        outline.action = action

        res = pdf.process()
        
        if res.is_successful:
            with open(test_params.output_path + "outline_with_url_action.pdf", "wb") as out_stream:
                out_stream.write(res.content)
        
        assert res.is_successful

    def test_outline_for_new_pdf(self, pdf, test_params):
        page_input1 = pdf.add_page()
        element1 = TextElement("Hello World 1", ElementPlacement.TopCenter)
        page_input1.elements.append(element1)

        page_input2 = pdf.add_page()
        element2 = TextElement("Hello World 2", ElementPlacement.TopCenter)
        page_input2.elements.append(element2)

        page_input3 = pdf.add_page()
        element3 = TextElement("Hello World 3", ElementPlacement.TopCenter)
        page_input3.elements.append(element3)

        root_outline = pdf.outlines.add("Root Outline")

        root_outline.children.add("Page 1", page_input1)
        root_outline.children.add("Page 2", page_input2)
        root_outline.children.add("Page 3", page_input3)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "outline_for_new_pdf.pdf", "wb") as out_stream:
                out_stream.write(res.content)
        
        assert res.is_successful

    def test_outline_for_exsisting_pdf(self, pdf, test_params):
        resource1 = PdfResource(test_params.resources_path + "DocumentA100.pdf")
        input1 = pdf.add_pdf(resource1)
        input1.Id = "document2"

        resource2 = PdfResource(test_params.resources_path + "InvoiceTemplate.pdf")
        input2 = pdf.add_pdf(resource2)
        input2.Id = "invoice"

        root_outline = pdf.outlines.add("Root Outline")
        root_outline.expanded = True

        root_outline.children.add("DocumentA 100", input1, 0, PageZoom.FitPage)
        root_outline.children.add("Invoice", input2)

        res = pdf.process()
        
        if res.is_successful:
            with open(test_params.output_path + "outline_for_exsisting_pdf.pdf", "wb") as out_stream:
                out_stream.write(res.content)
        
        assert res.is_successful

    def test_outline_import(self, pdf, test_params):
        resource = PdfResource(test_params.resources_path + "AllPageElements.pdf")
        input = pdf.add_pdf(resource)
        input.id = "AllPageElements"

        resource1 = PdfResource(test_params.resources_path + "PdfOutlineInput.pdf")
        input1 = pdf.add_pdf(resource1)
        input1.id = "outlineDoc1"

        root_outline = pdf.outlines.add("Imported Outline")
        root_outline.expanded = True

        root_outline.children.add_pdf_outlines(input)
        root_outline.children.add_pdf_outlines(input1)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "outline_import.pdf", "wb") as out_stream:
                out_stream.write(res.content)
        
        assert res.is_successful