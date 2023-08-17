import pytest
import json
from ..common_imports import (
    LayoutDataResource,
    DlexResource,
    DlexInput,
    Template,
    ElementPlacement,
    Pdf,
    TextElement
)

class TestDlexInput:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_dlex_input_simple(self, pdf, test_params):
        dlex = DlexResource(test_params.resources_path + "SimpleReportWithCoverPage.dlex")
        layout_data = LayoutDataResource(test_params.resources_path + "SimpleReportData.json")
        pdf.add_dlex(dlex, layout_data)
        pdf.add_additional_resource(test_params.resources_path + "Northwind Logo.gif")
        
        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "dlex_input_simple.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_dlex_input_simple_cloud_data(self, pdf, test_params):
        with open(test_params.resources_path + "SimpleReportData.json", "r", encoding="utf-8-sig") as file:
            json_string = file.read()
        dlex_input = DlexInput("TFWResources/SimpleReportWithCoverPage.dlex", json_string)
        pdf.inputs.append(dlex_input)

        res = pdf.process() 

        if res.is_successful:
            with open(test_params.output_path + "dlex_input_simple_cloud_data.pdf", "wb") as out_stream:
                out_stream.write(res.content)
        assert res.is_successful

    def test_dlex_input_template(self, pdf, test_params):
        dlex = DlexResource(test_params.resources_path + "SimpleReportWithCoverPage.dlex")
        layout_data = LayoutDataResource(test_params.resources_path + "SimpleReportData.json")
        dlex_input = DlexInput(dlex, layout_data)
        pdf.add_additional_resource(test_params.resources_path + "Northwind Logo.gif")
        template = Template("temp1")
        text_element = TextElement("Hello World", ElementPlacement.TopRight)
        text_element.y_offset = -40
        template.elements.append(text_element)
        dlex_input.template = template
        pdf.inputs.append(dlex_input)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "dlex_input_template.pdf", "wb") as out_stream:
                out_stream.write(res.content)
        assert res.is_successful

    def test_dlex_input_image(self, pdf, test_params):
        dlex = DlexResource(test_params.resources_path + "dynamic-image.dlex")
        layout_data = LayoutDataResource(test_params.resources_path + "dynamic-image.json")
        pdf.add_dlex(dlex, layout_data)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "dlex_input_image.pdf", "wb") as out_stream:
                out_stream.write(res.content)
        assert res.is_successful