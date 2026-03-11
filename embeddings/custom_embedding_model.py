from collections.abc import Sequence

from pydantic_ai.embeddings import EmbeddingModel, EmbeddingResult, EmbeddingSettings
from pydantic_ai.embeddings.result import EmbedInputType


class MyCustomEmbeddingModel(EmbeddingModel):
    @property
    def model_name(self) -> str:
        return 'my-custom-model'

    @property
    def system(self) -> str:
        return 'my-provider'

    async def embed(
        self,
        inputs: str | Sequence[str],
        *,
        input_type: EmbedInputType,
        settings: EmbeddingSettings | None = None,
    ) -> EmbeddingResult:
        inputs, settings = self.prepare_embed(inputs, settings)

        # Call your embedding API here
        embeddings = [[0.1, 0.2, 0.3] for _ in inputs]  # Placeholder

        return EmbeddingResult(
            embeddings=embeddings,
            inputs=inputs,
            input_type=input_type,
            model_name=self.model_name,
            provider_name=self.system,
        )