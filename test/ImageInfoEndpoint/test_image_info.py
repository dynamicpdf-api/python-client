import json
from ..common_imports import ImageInfo,ImageResource

class TestImageInfo:
    def test_multiple_image_inputs(self, test_params, get_endpoint):
        images = [test_params.resources_path + "Northwind Logo.gif",test_params.resources_path + "fw9_13.tif",test_params.resources_path + "DPDFLogo.png",test_params.resources_path + "DocumentA.jpeg"]
        for i in range(len(images)):
            resource = ImageResource(images[i])
            image = ImageInfo(resource)
            image = get_endpoint(image, test_params)
            res = image.process() 
            if res.is_successful:
                with open(test_params.output_path + "image_info"+str(i)+".json", "w") as out_stream:
                    json.dump(res.content, out_stream, indent=2)
            assert res.is_successful

