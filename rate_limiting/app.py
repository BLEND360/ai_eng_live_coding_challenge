from rate_limiting.api import MockAPI
from typing import List


def call_api(prompts: List[str]) -> List[str]:
    api = MockAPI()
    output = [api.call(prompt) for prompt in prompts]
    return output
