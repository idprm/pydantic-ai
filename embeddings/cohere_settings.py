from pydantic_ai import Embedder
from pydantic_ai.embeddings.cohere import CohereEmbeddingSettings

embedder = Embedder(
    'cohere:embed-v4.0',
    settings=CohereEmbeddingSettings(
        dimensions=512,
        cohere_truncate='END',  # Truncate long inputs instead of erroring
        cohere_max_tokens=256,  # Limit tokens per input
    ),
)