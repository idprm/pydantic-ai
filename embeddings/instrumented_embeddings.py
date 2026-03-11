import logfire

from pydantic_ai import Embedder

logfire.configure()

# Instrument a specific embedder
embedder = Embedder('openai:text-embedding-3-small', instrument=True)

# Or instrument all embedders globally
Embedder.instrument_all()