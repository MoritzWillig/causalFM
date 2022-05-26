from causalFM.query_helpers import questions, AttrDict, instantiate_questions, store_query_instances

dry_run = False
queries_path = "./queries/causal_chains"

physics_questions = [
    # reasoning on A->B->C chain
    "If A causes B and B causes C. Does A cause C?",  # A->B->C. A->C?
    "If A causes B and B causes C. Does A cause B?",  # A->B->C. A->B?
    "If A causes B and B causes C. Does B cause C?",  # A->B->C. B->C?
    "If A causes B and B causes C. Does A cause A?",  # A->B->C. A->A?
    "If A causes B and B causes C. Does B cause A?",  # A->B->C. B->A?
    "If A causes B and B causes C. Does C cause A?",  # A->B->C. C->A?

    # extending chain
    "If A causes B, B causes C and C causes D. Does A cause D?",
    "If A causes B, B causes C, C causes D and D causes E. Does A cause E?",
    "If A causes B, B causes C, C causes D, D causes E, E causes F. Does A cause F?",
    "If A causes B, B causes C, C causes D, D causes E, E causes F. Does B cause E?",
    "If A causes B, B causes C, C causes D, D causes E, E causes F. Does E cause B?",

    # changing clause order
    "If B causes C and A causes B. Does A cause C?",  # B->C, A->B. A->C?
    "If B causes C and A causes B. Does C cause A?",  # B->C, A->B. C->A?

    # changing variable names
    "If G causes Q and Q causes S. Does G cause S?",  # G->Q->S. G->S?

    # changing clause order and rename
    "If Q causes S and G causes Q . Does G cause S?"  # Q->S, G->Q. G->S?
]


def generate_physic_questions():
    question_instances = []

    for question_str in physics_questions:
        info = {
            "template": question_str
        }
        question = question_str

        question_instances.append({
            "question": question,
            "info": info
        })

    return question_instances


def main():
    question_instances = generate_physic_questions()
    if not dry_run:
        store_query_instances(queries_path, question_instances)
    print("done.")


if __name__ == "__main__":
    main()
