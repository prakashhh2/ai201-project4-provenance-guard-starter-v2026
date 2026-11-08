"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # These are prose passages from this project's README and criteria,
        # written for the submission rather than copied from the attack set.
        "texts": [
            "Accusing a real writer is more damaging than missing some AI-written text, so the system should be conservative before showing an AI accusation.",
            "The system does not need perfect separation, but a visible 0.20 gap gives the scores useful diagnostic value instead of leaving both groups in the same band.",
            "Each label is part of the contract. If one cannot be reached, readers either receive an overconfident result or the label logic has not been meaningfully tested.",
            "An appeal must give a real writer a visible remedy while preserving the original decision. Rejecting unknown IDs prevents the log from claiming that a nonexistent submission was reviewed.",
            "Malformed or oversized input should fail clearly before model scoring rather than crashing the service, wasting resources, or creating a misleading decision record.",
            "The service uses two signals that measure different properties. One reads predictability, while the other reads the shape of the writing.",
            "The content_id connects the submission, its audit entry, and any later appeal. The ping route remains the control for checking whether the service itself is working.",
            "I kept the equal-weight rule and wrote the final contracts and blind spots into this README, then added explicit validation behavior for invalid and oversized submissions.",
            "A wrong accusation costs a writer more than a missed detection. The unsure band should be a real outcome, not a hidden failure.",
            "The writer can request a review if the result is wrong. Neither signal can prove authorship, so the original decision must remain visible in the audit log.",
        ],
    },
    {
        "name": "score separation",
        "criterion": 2,
        # First five are deliberately regular, repetitive AI-like prose; the
        # last five are deliberately irregular human-like prose.
        "texts": [
            "The system works. The system works well. The system works every day. The system works for users. The system works as expected.",
            "The plan is clear. The plan is useful. The plan is simple. The plan is practical. The plan is effective.",
            "The team meets goals. The team meets goals daily. The team meets goals together. The team meets goals consistently. The team meets goals successfully.",
            "The service receives data. The service checks data. The service processes data. The service stores data. The service returns data.",
            "The process creates value. The process creates value quickly. The process creates value reliably. The process creates value for teams. The process creates value for users.",
            "I missed the bus, swore at the timetable, and walked home in the rain; somehow that was the part of Tuesday that fixed my mood. It shouldn't have worked, but it did!",
            "My grandmother kept receipts in a blue biscuit tin. Not important receipts, mostly: a pharmacy slip, a cinema stub, one note with a phone number nobody recognised—and a button.",
            "The first draft was awful. I knew it was awful. Still, the sentence I nearly deleted—about the cracked mug by the sink—was the only bit that sounded like me.",
            "When the power went out, the apartment became strangely honest: no fan, no refrigerator hum, just rain tapping the fire escape and my neighbour laughing through the wall.",
            "I prefer fixing things in the morning. At night every loose screw feels like a personal insult; I start reorganising drawers instead of finishing the job, which is ridiculous.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "I missed the bus, swore at the timetable, and walked home in the rain; somehow that was the part of Tuesday that fixed my mood. It shouldn't have worked, but it did!",
            "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must handle a wide variety of inputs. Additionally, the overall performance depends on a number of important variables.",
            "🙂🙃😀😃😄😁😆😅😂🤣🙂🙃😀😃😄😁😆😅😂🤣🙂🙃😀😃😄😁😆😅😂🤣",
        ],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        "texts": [
            "I wrote this short submission myself and want the decision reviewed because the result does not match my experience.",
            "This second submission is another ordinary piece of writing that a real writer should be able to appeal without losing the original decision.",
        ],
        "appeal_after_submission": True,
        "unknown_appeal": True,
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing_text"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "A request without a creator should be rejected."},
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
