import os


import dotenv
from icecream import ic

"""
pip install python-dotenv
pip install google-genai
pip show google-genai

"""

def example():
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=token)
    MODEL_ID = "gemini-2.0-flash"  # @param ["gemini-1.5-flash-latest","gemini-2.0-flash-lite","gemini-2.0-flash","gemini-2.5-pro-exp-03-25"] {"allow-input":true, isTemplate: true}
    response = client.models.generate_content(
        model=MODEL_ID,
        contents="What's the largest planet in our solar system?"
    )
    ic(response)
    # response: GenerateContentResponse(
    #   candidates=[Candidate(content=Content(parts=
    #       [Part(video_metadata=None, thought=None, code_execution_result=None, executable_code=None,
    #       file_data=None, function_call=None, function_response=None, inline_data=None,
    #       text='The largest planet in our solar system is **Jupiter**.')
    #       ], role='model'),

    #       citation_metadata=None,
    #       finish_message=None, token_count=None,
    #       finish_reason=<FinishReason.STOP: 'STOP'>,
    #       avg_logprobs=-0.000989527441561222, grounding_metadata=None, index=None, logprobs_result=None,
    #       safety_ratings=None)],
    #
    #       create_time=None, response_id=None, model_version='gemini-2.0-flash',
    #       prompt_feedback=None, usage_metadata=GenerateContentResponseUsageMetadata(cache_tokens_details=None,
    #       cached_content_token_count=None, candidates_token_count=12,
    #       candidates_tokens_details=[ModalityTokenCount(modality=<MediaModality.TEXT: 'TEXT'>, token_count=12)],
    #       prompt_token_count=11, prompt_tokens_details=[
    #         ModalityTokenCount(modality=<MediaModality.TEXT: 'TEXT'>, token_count=11)],
    #       thoughts_token_count=None, tool_use_prompt_token_count=None, tool_use_prompt_tokens_details=None,
    #       total_token_count=23), automatic_function_calling_history=[], parsed=None)
    #
    ic(response.text)
    return


if __name__ == '__main__':
    dotenv.load_dotenv()
    acct = os.getenv(f"gemini_acct")
    token = os.getenv(f"gemini_token")
    assert acct
    assert token
    example()
