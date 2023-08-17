import pytest
from ..common_imports import (
    Pdf,
    TextReplace,
    WordInput,
    WordResource
)

class TestWordInput:

    @pytest.fixture
    def pdf(self, test_params, get_endpoint):
        pdf = Pdf()
        return get_endpoint(pdf, test_params)

    def test_word_input(self, pdf, test_params):

        wordResource = WordResource(test_params.resources_path + "DocumentA.docx")
        word = WordInput(wordResource)

        word.page_width = 300
        word.page_height = 200

        word.top_margin = 10
        word.bottom_margin = 10
        word.right_margin = 40
        word.left_margin = 40
        pdf.inputs.append(word)

        res = pdf.process()

        if res.is_successful:
            with open(test_params.output_path + "word_input.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful

    def test_word_input_text_replace(self, pdf, test_params):

        wordResource = WordResource(test_params.resources_path + "DocumentA.docx")
        word = WordInput(wordResource)

        word.page_width = 300
        word.page_height = 200

        word.top_margin = 10
        word.bottom_margin = 10
        word.right_margin = 40
        word.left_margin = 40
        word.text_replace.append(TextReplace("ve", "Data", True))
        pdf.inputs.append(word)

        res = pdf.process()
        
        if res.is_successful:
            with open(test_params.output_path + "word_input_text_replace.pdf", "wb") as out_stream:
                out_stream.write(res.content)

        assert res.is_successful