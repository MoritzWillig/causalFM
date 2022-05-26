from aleph_alpha_client import AlephAlphaClient


def startup_aleph_alpha(keys_dir):
    with open(keys_dir / "aleph_alpha", "r") as f:
        token = f.readline()
    client = AlephAlphaClient(
        host="https://api.aleph-alpha.com",
        token=token
    )

    return client


def query_aleph_alpha(context, query_text, dry_run=False):
    print("[querying]", query_text)
    if dry_run:
        return None

    model = "luminous-base"

    #client = AlephAlphaClient()
    client = context
    result = client.complete(
        model,
        query_text,
        maximum_tokens=50,
        temperature=0.0,
        top_k=0,
        top_p=0,
        presence_penalty=0,
        frequency_penalty=0
    )

    return result['completions'][0]['completion']
