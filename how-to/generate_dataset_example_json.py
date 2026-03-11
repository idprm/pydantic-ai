from pathlib import Path

from pydantic_evals import Dataset
from pydantic_evals.generation import generate_dataset

from generate_dataset_example import AnswerOutput, MetadataType, QuestionInputs


async def main():
    dataset = await generate_dataset(  
        dataset_type=Dataset[QuestionInputs, AnswerOutput, MetadataType],
        n_examples=2,
        extra_instructions="""
        Generate question-answer pairs about world capitals and landmarks.
        Make sure to include both easy and challenging questions.
        """,
    )
    output_file = Path('questions_cases.json')
    dataset.to_file(output_file)  
    print(output_file.read_text(encoding='utf-8'))
    """
    {
      "$schema": "questions_cases_schema.json",
      "name": null,
      "cases": [
        {
          "name": "Easy Capital Question",
          "inputs": {
            "question": "What is the capital of France?",
            "context": null
          },
          "metadata": {
            "difficulty": "easy",
            "category": "Geography"
          },
          "expected_output": {
            "answer": "Paris",
            "confidence": 0.95
          },
          "evaluators": [
            "EqualsExpected"
          ]
        },
        {
          "name": "Challenging Landmark Question",
          "inputs": {
            "question": "Which world-famous landmark is located on the banks of the Seine River?",
            "context": null
          },
          "metadata": {
            "difficulty": "hard",
            "category": "Landmarks"
          },
          "expected_output": {
            "answer": "Eiffel Tower",
            "confidence": 0.9
          },
          "evaluators": [
            "EqualsExpected"
          ]
        }
      ],
      "evaluators": [],
      "report_evaluators": []
    }
    """