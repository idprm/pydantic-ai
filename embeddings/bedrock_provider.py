from pydantic_ai import Embedder
from pydantic_ai.embeddings.bedrock import BedrockEmbeddingModel
from pydantic_ai.providers.bedrock import BedrockProvider

provider = BedrockProvider(
    region_name='us-west-2',
    aws_access_key_id='your-access-key',
    aws_secret_access_key='your-secret-key',
)

model = BedrockEmbeddingModel('amazon.titan-embed-text-v2:0', provider=provider)
embedder = Embedder(model)