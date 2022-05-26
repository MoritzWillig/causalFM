from pathlib import Path
import numpy as np

from causalFM.answer_helpers import get_response_flags, categorize_answers
from causalFM.query_helpers import load_query_instances

evaluations_dir = Path("./evaluations")

from_apis = ["openai", "aleph_alpha", "opt"]
datasets = ["intuitive_physics"]

allow_quiz_answers = True  # include quiz-style answers


positive_response_flags, negative_response_flags, undecided_response_flags = get_response_flags(allow_quiz_answers)


for dataset_name in datasets:
    print(f"[{dataset_name}]")

    queries = load_query_instances(Path(f"./queries/{dataset_name}_questions.txt"))
    for i, query in enumerate(queries):

        responses = []

        for api_name in from_apis:
            answer_dir = Path(f"./queries/{api_name}_{dataset_name}")
            summary_path = answer_dir / "summary.txt"
            with summary_path.open("r") as f:
                answers = f.readlines()

            canswers = categorize_answers(answers, positive_response_flags, negative_response_flags, undecided_response_flags)
            responses.append(canswers)

        responses = np.array(responses)
        print(responses.shape, responses)


        #answer = Path(answer_dir / f"{i}.txt").read_text()
        #print("===QUERY===")
        #print(query)
        #print("===ANSWERS===")
        #print(answer.strip())

