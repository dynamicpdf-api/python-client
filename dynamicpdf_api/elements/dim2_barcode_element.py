from .barcode_element import BarcodeElement
from .value_type import ValueType
import base64

class Dim2BarcodeElement(BarcodeElement):
    '''
    The base class for 2 dimensional barcodes (Aztec, Pdf417, DataMatrixBarcode and QrCode).
    '''
    
    def __init__(self, value, placement, x_offset, y_offset):
        self._value_type = ValueType.String
        if isinstance(value, str):
            super().__init__(value, placement, x_offset, y_offset)
        else:
            encoded = base64.b64encode(value).decode('utf-8')
            super().__init__(encoded, placement, x_offset, y_offset)
            self._value_type = ValueType.Base64EncodedBytes
          
