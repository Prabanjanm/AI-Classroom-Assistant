from PIL import Image

from transformers import (
    CLIPProcessor,
    CLIPModel
)

import torch


class CLIPEmbeddingService:

    model = None
    processor = None

    def load_model(self):

     if self.model is None:


        self.model = CLIPModel.from_pretrained(
            "openai/clip-vit-base-patch32"
        )

        self.processor = CLIPProcessor.from_pretrained(
            "openai/clip-vit-base-patch32"
        )

    async def generate_image_embedding(
        self,
        image_path: str
    ):


        self.load_model()
        image = Image.open(
            image_path
        ).convert("RGB")

        inputs = self.processor(
            images=image,
            return_tensors="pt"
        )

        with torch.no_grad():

            outputs = (
                self.model.get_image_features(
                    **inputs
                )
            )

            # Handle tensor/object safely
            if not isinstance(
                outputs,
                torch.Tensor
            ):

                image_features = (
                    outputs.pooler_output
                )

            else:

                image_features = outputs

            # Normalize embedding
            image_features = (
                image_features /
                image_features.norm(
                    p=2,
                    dim=-1,
                    keepdim=True
                )
            )

        embedding = (
            image_features.squeeze()
            .cpu()
            .numpy()
            .tolist()
        )

        print(
            f"Embedding dimension: {len(embedding)}"
        )

        return embedding