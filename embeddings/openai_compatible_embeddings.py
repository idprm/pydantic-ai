# Using Azure OpenAI
from openai import AsyncAzureOpenAI

from pydantic_ai import Embedder
from pydantic_ai.embeddings.openai import OpenAIEmbeddingModel
from pydantic_ai.providers.openai import OpenAIProvider

azure_client = AsyncAzureOpenAI(
    azure_endpoint='https://your-resource.openai.azure.com',
    api_version='2024-02-01',
    api_key='your-azure-key',
)
model = OpenAIEmbeddingModel(
    'text-embedding-3-small',
    provider=OpenAIProvider(openai_client=azure_client),
)
embedder = Embedder(model)


# Using any OpenAI-compatible API
model = OpenAIEmbeddingModel(
    'your-model-name',
    provider=OpenAIProvider(
        base_url='https://your-provider.com/v1',
        api_key='your-api-key',
    ),
)
embedder = Embedder(model)