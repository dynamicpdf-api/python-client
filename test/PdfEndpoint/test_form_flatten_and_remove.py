import pytest
import io
from ..common_imports import (
    PdfResource,
    PdfInput,
    Pdf,
    FormField,
)

class TestFormFlattenAndRemove:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_form_flatten(self, pdf, test_params):
        resource = PdfResource(test_params.resources_path + "fw9AcroForm_14.pdf", "fw9AcroForm_14.pdf")
        input = PdfInput(resource)
        pdf.inputs.append(input)

        field = FormField("topmostSubform[0].Page1[0].f1_1[0]", "Any Company, Inc.")
        field.flatten = True
        pdf.form_fields.append(field)
        field1 = FormField("topmostSubform[0].Page1[0].f1_2[0]", "Any Company")
        field1.flatten = True
        pdf.form_fields.append(field1)
        field2 = FormField("topmostSubform[0].Page1[0].FederalClassification[0].c1_1[0]", "1")
        field2.flatten = True
        pdf.form_fields.append(field2)
        field3 = FormField("topmostSubform[0].Page1[0].Address[0].f1_7[0]", "123 Main Street")
        field3.Flatten = False
        pdf.form_fields.append(field3)
        field4 = FormField("topmostSubform[0].Page1[0].Address[0].f1_8[0]", "Washington, DC  22222")
        field.flatten = False
        pdf.form_fields.append(field4)
        field5 = FormField("topmostSubform[0].Page1[0].f1_9[0]", "Any Requester")
        field.flatten = True
        pdf.form_fields.append(field5)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "form_flatten.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_form_remove(self, pdf, test_params):
        resource = PdfResource(test_params.resources_path + "fw9AcroForm_14.pdf", "fw9AcroForm_14.pdf")
        input = PdfInput(resource)
        pdf.inputs.append(input)

        field = FormField("topmostSubform[0].Page1[0].f1_1[0]", "Any Company, Inc.")
        field.remove = True
        pdf.form_fields.append(field)
        field1 = FormField("topmostSubform[0].Page1[0].f1_2[0]", "Any Company")
        field1.remove = True
        pdf.form_fields.append(field1)
        field2 = FormField("topmostSubform[0].Page1[0].FederalClassification[0].c1_1[0]", "1")
        field2.remove = False
        pdf.form_fields.append(field2)
        field3 = FormField("topmostSubform[0].Page1[0].Address[0].f1_7[0]", "123 Main Street")
        field3.remove = False
        pdf.form_fields.append(field3)
        field4 = FormField("topmostSubform[0].Page1[0].Address[0].f1_8[0]", "Washington, DC  22222")
        field4.remove = True
        pdf.form_fields.append(field4)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "form_remove.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_form_flatten_all(self, pdf, test_params):
        with open(test_params.resources_path + "fw9AcroForm_14.pdf", "rb") as file:
            memory = io.BytesIO(file.read())
        resource = PdfResource(memory)
        input = PdfInput(resource)
        pdf.inputs.append(input)

        field = FormField("topmostSubform[0].Page1[0].f1_1[0]", "Any Company, Inc.")
        pdf.form_fields.append(field)
        field1 = FormField("topmostSubform[0].Page1[0].f1_2[0]", "Any Company")
        pdf.form_fields.append(field1)
        field2 = FormField("topmostSubform[0].Page1[0].FederalClassification[0].c1_1[0]", "1")
        pdf.form_fields.append(field2)
        field3 = FormField("topmostSubform[0].Page1[0].Address[0].f1_7[0]", "123 Main Street")
        pdf.form_fields.append(field3)
        field4 = FormField("topmostSubform[0].Page1[0].Address[0].f1_8[0]", "Washington, DC  22222")
        pdf.form_fields.append(field4)
        field5 = FormField("topmostSubform[0].Page1[0].f1_9[0]", "Any Requester")
        pdf.form_fields.append(field5)
        field6 = FormField("topmostSubform[0].Page1[0].f1_10[0]", "17288825617")
        pdf.form_fields.append(field6)
        field7 = FormField("topmostSubform[0].Page1[0].EmployerID[0].f1_14[0]", "52")
        pdf.form_fields.append(field7)
        field8 = FormField("topmostSubform[0].Page1[0].EmployerID[0].f1_15[0]", "1234567")
        pdf.form_fields.append(field8)
        
        pdf.flatten_all_form_fields = True

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "form_flatten_all.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_form_retain_signature(self, pdf, test_params):
        resource = PdfResource(test_params.resources_path + "Signature.pdf")
        input = PdfInput(resource)
        pdf.inputs.append(input)
        pdf.flatten_all_form_fields = False
        pdf.retain_signature_form_fields = False

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "form_retain_signature.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful