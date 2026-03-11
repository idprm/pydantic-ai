import logfire

from pydantic_evals import Case, Dataset

# Configure Logfire
logfire.configure(
    send_to_logfire='if-token-present',  
)


# Your evaluation code
def my_task(inputs: str) -> str:
    return f'result for {inputs}'


dataset = Dataset(cases=[Case(name='test', inputs='example')])
report = dataset.evaluate_sync(my_task)