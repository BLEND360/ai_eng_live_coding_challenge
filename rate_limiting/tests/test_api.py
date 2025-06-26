from rate_limiting.app import call_api


def test_call_api():
    request_len = 5
    prompts = [f"Prompt {i}" for i in range(request_len)]
    response = call_api(prompts)
    assert len(response) == request_len
    assert response == [
        f"Response for: Prompt {i}" for i in range(request_len)
    ]
