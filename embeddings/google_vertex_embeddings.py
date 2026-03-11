from pydantic_ai import Embedder
from pydantic_ai.embeddings.google import GoogleEmbeddingModel
from pydantic_ai.providers.google import GoogleProvider

# Using provider prefix
embedder = Embedder('google-vertex:gemini-embedding-001')

# Or with explicit provider configuration
model = GoogleEmbeddingModel(
    'gemini-embedding-001',
    provider=GoogleProvider(vertexai=True, project='my-project', location='us-central1'),
)
embedder = Embedder(model)