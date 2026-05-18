from PIL import Image

from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration
)


class ImageDescriptionService:
    model = None

    processor = None

    def load_model(self):

     if self.model is None:

        print(
                "Loading BLIP model..."
            )

        self.processor = (
            BlipProcessor.from_pretrained(
                "Salesforce/blip-image-captioning-base"
            )
        )

        self.model = (
            BlipForConditionalGeneration
            .from_pretrained(
                "Salesforce/blip-image-captioning-base"
            )
        )

    async def describe_image(
        self,
        image_path: str
    ):

        self.load_model()
        image = Image.open(
            image_path
        ).convert("RGB")

        inputs = self.processor(
            image,
            return_tensors="pt"
        )

        output = self.model.generate(
            **inputs
        )

        description = self.processor.decode(
            output[0],
            skip_special_tokens=True
        )

        return description