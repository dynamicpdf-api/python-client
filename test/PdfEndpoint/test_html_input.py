import pytest
from ..common_imports import ( 
    HtmlInput,
    PageSize,
    PageOrientation, 
    HtmlResource,
    Pdf
    )

class TestHtmlInput:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_html_input_string(self, pdf, test_params):
        html_string = "<html><body>hello</body></html>"
        resource = HtmlResource(html_string)
        html = HtmlInput(resource)
        html.page_width = 300
        html.page_height = 200

        html.top_margin = 10
        html.bottom_margin = 10
        html.right_margin = 40
        html.left_margin = 40
        
        pdf.inputs.append(html)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "html_input_string.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_html_input_string_parameter(self, pdf, test_params):
        html_string = "<html><body>hello</body></html>"
        resource = HtmlResource(html_string)
        input = HtmlInput(resource, None, PageSize.Letter, PageOrientation.Portrait, 10)
        pdf.inputs.append(input)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "html_input_string_parameter.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful == True

    def test_html_input_resource(self, pdf, test_params):
        with open(test_params.resources_path + "html.html", 'r', encoding='utf-8') as file:
            htmlString = file.read()
        resource = HtmlResource(htmlString)
        html = HtmlInput(resource)
        html.page_size = PageSize.B4
        html.page_orientation = PageOrientation.Landscape

        html.top_margin = 50
        html.bottom_margin = 50
        html.right_margin = 80
        html.left_margin = 80
        pdf.inputs.append(html)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "html_input_resource.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_html_input_resource_page_size(self, pdf, test_params):
        with open(test_params.resources_path + "html.html", 'r', encoding='utf-8') as file:
            htmlString = file.read()
        resource = HtmlResource(htmlString)
        input = HtmlInput(resource)
        input.page_size = PageSize.Postcard
        pdf.inputs.append(input)
        
        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "html_input_page_size.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_html_input_resource_page_height(self, pdf, test_params):
        with open(test_params.resources_path + "html.html", 'r', encoding='utf-8') as file:
            htmlString = file.read()
        resource = HtmlResource(htmlString)
        input = HtmlInput(resource)
        input.page_height = 400
        input.page_width = 300
        pdf.inputs.append(input)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "html_input_page_height.pdf", "wb") as out_stream:
                out_stream.write(res.content)
        
        assert res.is_successful


    def test_html_input_resource_parameter(self, pdf, test_params):
        with open(test_params.resources_path + "html.html", 'r', encoding='utf-8') as file:
            html_string = file.read()
        resource = HtmlResource(html_string)
        input = HtmlInput(resource, None, PageSize.A3, PageOrientation.Landscape, 30)
        pdf.inputs.append(input)

        res = pdf.process()
        
        if res.is_successful:
            with open(test_params.output_path + "html_input_resource_parameter.pdf", "wb") as out_stream:
                out_stream.write(res.content)
        
        assert res.is_successful

