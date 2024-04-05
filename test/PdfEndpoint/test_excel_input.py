import pytest
from ..common_imports import (
    Pdf,
    ExcelInput,
    ExcelResource
)

class TestExcelInput:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_excel_input(self, pdf, test_params):

        excelResource = ExcelResource(test_params.resources_path + "DocumentA.xlsx")
        excel = ExcelInput(excelResource)

        excel.page_width = 300
        excel.page_height = 200

        excel.top_margin = 10
        excel.bottom_margin = 10
        excel.right_margin = 40
        excel.left_margin = 40
        pdf.inputs.append(excel)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "excel_input.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful