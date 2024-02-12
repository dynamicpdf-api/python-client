import io
from ..common_imports import DlexLayout, LayoutDataResource, DlexResource, AdditionalResourceType
from .invoice_data import InvoiceData

class TestDlexLayout:

    def test_dlex_layout(self, test_params, get_endpoint):

        layout_data = LayoutDataResource(test_params.resources_path + "SimpleReportData.json")
        dlex_endpoint = DlexLayout("TFWResources/SimpleReportWithCoverPage.dlex", layout_data)
        
        dlex_endpoint = get_endpoint(dlex_endpoint, test_params)
        res = dlex_endpoint.process()

        if res.is_successful:
            with open(test_params.output_path + "dlex_layout_simple.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_dlex_layout_with_resource(self, test_params, get_endpoint):

        layout_data = LayoutDataResource(test_params.resources_path + "SimpleReportData.json")
        dlex_resource = DlexResource(test_params.resources_path + "SimpleReportWithCoverPage.dlex", "SimpleReportWithCoverPage.dlex")
        dlex_endpoint = DlexLayout(dlex_resource, layout_data)
        dlex_endpoint.add_additional_resource(test_params.resources_path + "Northwind Logo.gif", "Northwind Logo.gif")
       
        dlex_endpoint = get_endpoint(dlex_endpoint, test_params)
        res = dlex_endpoint.process()

        if res.is_successful:
            with open(test_params.output_path + "test_dlex_layout_with_resource.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful
        
    def test_dlex_layout_with_resource_data(self, test_params, get_endpoint):

        layout_data = LayoutDataResource(test_params.resources_path + "SimpleReportData.json")
        dlex_resource = DlexResource(test_params.resources_path + "SimpleReportWithCoverPage.dlex", "SimpleReportWithCoverPage.dlex")
        dlex_endpoint = DlexLayout(dlex_resource, layout_data)
        
        with open(test_params.resources_path + "Northwind Logo.gif", 'rb') as file:
            file_data = io.BytesIO(file.read())
            
        dlex_endpoint.add_additional_resource(file_data, AdditionalResourceType.Image, "Northwind Logo.gif")
        dlex_endpoint = get_endpoint(dlex_endpoint, test_params)
        res = dlex_endpoint.process()

        if res.is_successful:
            with open(test_params.output_path + "test_dlex_layout_with_resource_data.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful
        
    def test_dlex_layout_invoice_data(self, test_params, get_endpoint):

        invoiceLinqData = InvoiceData.Order11077()

        layout_data = LayoutDataResource(invoiceLinqData.to_json())
        dlex_endpoint = DlexLayout("TFWResources/InvoiceOrderId.dlex", layout_data)
        
        dlex_endpoint = get_endpoint(dlex_endpoint, test_params)
        res = dlex_endpoint.process()

        if res.is_successful:
            with open(test_params.output_path + "dlex_layout_invoice_data.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_dlex_layout_with_globalfont(self, test_params, get_endpoint):

        layout_data = LayoutDataResource(test_params.resources_path + "test.json")
        dlex_resource = DlexResource(test_params.resources_path + "test.dlex", "test.dlex")
        dlex_endpoint = DlexLayout(dlex_resource, layout_data)
        
        dlex_endpoint = get_endpoint(dlex_endpoint, test_params)
        res = dlex_endpoint.process()

        if res.is_successful:
            with open(test_params.output_path + "dlex_layout_with_globalfont.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful