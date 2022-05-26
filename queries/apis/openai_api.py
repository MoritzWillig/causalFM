import openai


def startup_openai(keys_dir):
    with open(keys_dir / "openai", "r") as f:
        openai.api_key = f.readline()  # os.getenv("OPENAI_API_KEY")
    return None


def query_openai(context, query_text, dry_run=False):
    print("[querying]", query_text)
    if dry_run:
        return None
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=query_text,
        temperature=0,
        max_tokens=50, #50
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']
