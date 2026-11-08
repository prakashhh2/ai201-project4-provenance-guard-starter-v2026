# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A client sends a JSON request containing `text` and `creator_id` to
   `POST /submit`.
2. Flask receives the request and the route validates and extracts the two
   fields.
3. `detector.py` reads the text with a local language model and produces
   `model_score`, based on how predictable the text is to that model.
4. `stylometry.py` measures the text's sentence lengths, vocabulary repetition,
   and punctuation patterns and produces `style_score`.
5. `scoring.py::combine_signals` combines the two 0–1 scores into one score;
   higher means more likely AI-generated.
6. `scoring.py::score_to_label` turns the combined score into a machine-readable
   `guess` and a reader-facing `label`, while the route calculates the
   `confidence` value.
7. `audit.py` records the decision with a `content_id`, and Flask returns the
   decision and both signal scores as JSON.

The `content_id` connects the submission, its audit entry, and any later
appeal. The `/ping` route remains the control for checking whether the service
itself is working.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**

`detector.py` measures how predictable the text is to a local language model.
It uses perplexity internally and converts it to a 0–1 `model_score`. A higher
score means the text is more likely to be AI-generated.

**Why that might differ between human and AI writing:**

Language models generate text by choosing likely next words, so AI-generated
text often has predictable word choices and sentence patterns. Human writing
can be more surprising because it includes unusual wording, abrupt changes,
or personal details.

**What it can't see:**

Predictability is not proof of authorship. Plain, ordinary human writing,
writing by someone using a second language, or writing with a deliberately
simple vocabulary can also be very predictable and receive a high AI score.
The model also does not know who actually wrote the text.

### Signal two — the style signal

**What it measures:**

`stylometry.py` measures the shape of the text rather than its meaning. Its
three measures are sentence-length spread, type-token ratio (vocabulary
repetition), and punctuation density. These are combined into a 0–1
`style_score`, where higher means more likely AI-generated.

**Why that might differ between human and AI writing:**

AI-generated prose often has evenly sized sentences, repeated common words,
and regular punctuation. Human writing is often lumpier, with a mixture of
short and long sentences and more individual variation.

**What it can't see:**

It cannot understand the meaning, argument, facts, or authorship of the text.
Typos, inserted quotations, sentence splitting, or changed punctuation can
alter its measurements without changing who wrote the words. Text length also
affects some measures, especially type-token ratio.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

Start with a weighted average so both signals contribute to the decision. Both
signals point in the same direction: 0 means more human-like and 1 means more
AI-like. If the signals disagree, the combined score moves toward the middle
and the result should be treated as less certain rather than allowing one
signal to make an accusation by itself.

**The numbers:**

`model_score × 0.5 + style_score × 0.5`. The initial weights are equal because
the two signals measure different properties and neither should dominate before
calibration.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

If a plain human paragraph is easy for the language model to predict,
`model_score` may be high, while its sentence lengths and punctuation are
irregular enough for `style_score` to be low. For example, scores of `0.80` and
`0.20` produce a combined score of `0.50` with the equal-weight rule. That
disagreement should land in the unsure range instead of treating the model
signal alone as proof that the writer used AI.

### Milestone 4 calibration

I ran the four required text types through the style signal and combiner. The
detector dependencies were unavailable in this environment, so the model
column uses the documented fallback `0.5000`; the route will use the real model
score when `torch` and the detector model are installed.

| Input | Model score | Style score | Combined score |
|---|---:|---:|---:|
| clearly AI | 0.5000 | 0.3797 | 0.4398 |
| clearly human | 0.5000 | 0.2379 | 0.3690 |
| formal human | 0.5000 | 0.1591 | 0.3296 |
| lightly-edited AI | 0.5000 | 0.1994 | 0.3497 |

The style signal separates the deliberately regular AI sample from the human
samples, but it also gives formal human writing a low AI-like score. That is a
useful limitation rather than proof of authorship: the two signals must be
inspected separately when they disagree.


### False-positive trace

A real writer submits their own plain, conventional writing. The model finds
the wording predictable and gives it a high `model_score`, for example `0.90`.
The style signal is lower because the writer's sentence lengths and punctuation
vary, but it still reaches `0.45`. With equal weights, the combined score is
`0.675`, which crosses the starter's `0.65` AI threshold. The writer is shown
the high-confidence AI label even though they wrote the work themselves, along
with the `content_id` needed to appeal.

The writer can send that `content_id` and a reason to `POST /appeal`. The
service checks that the content exists, records the appeal in the append-only
audit log, and changes the item's status to `under_review`. It does not silently
erase the original decision. This appeal path is necessary because neither
signal can prove authorship.


## Endpoint Contracts

These are the contracts the implementation must preserve.

### `POST /submit`

Request JSON:

```json
{
  "text": "some writing to evaluate",
  "creator_id": "writer-123"
}
```

Successful response JSON:

```json
{
  "content_id": "unique-id",
  "guess": "human|unsure|ai",
  "confidence": 0.0,
  "label": "reader-facing explanation",
  "model_score": 0.0,
  "style_score": 0.0
}
```

`content_id` identifies this submission. The two signal scores must be
returned so later testing can show which signal caused a result. A missing or
empty `text`, or a missing or empty `creator_id`, should receive a `400` client
error instead of being scored. The error response has this shape:

```json
{
  "error": "invalid_request",
  "message": "text must be a non-empty string"
}
```

The `message` names the first invalid field so a caller can correct the
request. Text longer than `12,000` characters receives the same `400` shape
with a message explaining the limit; it is rejected before either signal runs.
The route does not return a decision for a rejected submission.

### `POST /appeal`

Request JSON:

```json
{
  "content_id": "unique-id",
  "reasoning": "I wrote this myself and want the decision reviewed."
}
```

Successful response should confirm the `content_id` and report
`"status": "under_review"`:

```json
{
  "content_id": "unique-id",
  "status": "under_review"
}
```

Missing or empty `content_id` or `reasoning`, and an unknown `content_id`,
return `400` with the same `error`/`message` shape as `/submit`. The service
must validate the content before calling `audit.log_appeal`, so an invalid
appeal never creates an audit entry. A valid appeal appends a new entry and
leaves the original decision intact.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00–0.35, inclusive | We think this was probably written by a person. This result is not proof of authorship. |
| unsure | greater than 0.35 and less than 0.65 | We cannot tell reliably whether this was written by a person or generated by AI. |
| high-confidence AI | 0.65–1.00, inclusive | We think this was probably generated by AI. This result is not proof of authorship. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

It says the system cannot tell reliably instead of accusing the writer. The
writer can request a review if the result is wrong.

**Label reachability check:**

| Sample | Combined score | Returned guess |
|---|---:|---|
| clearly human | 0.3296 | `human` |
| borderline | 0.4398 | `unsure` |
| clearly AI-like | 0.6805 | `ai` |



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must handle a wide variety of inputs. Additionally, the overall performance depends on a number of important variables.", "creator_id": "label-unsure"}'
```

```json
{
  "confidence": 0.4398,
  "content_id": "52ffd261-5468-4660-99ec-64cea100357a",
  "guess": "unsure",
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "model_score": 0.5,
  "style_score": 0.3797
}
```

The request was checked against the route with Flask's in-process test client
because this environment does not allow binding a local socket; the same JSON
body is shown above for `curl`. The local detector dependency was unavailable,
so the Milestone 4 fallback model score was `0.5`.

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "52ffd261-5468-4660-99ec-64cea100357a", "reasoning": "I wrote this myself and want the decision reviewed."}'
```

```json
{
  "content_id": "52ffd261-5468-4660-99ec-64cea100357a",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.4398,
      "content_id": "52ffd261-5468-4660-99ec-64cea100357a",
      "creator_id": "label-unsure",
      "guess": "unsure",
      "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
      "model_score": 0.5,
      "status": "decided",
      "style_score": 0.3797,
      "timestamp": "2026-11-02T03:35:00+00:00"
    },
    {
      "content_id": "52ffd261-5468-4660-99ec-64cea100357a",
      "creator_id": "label-unsure",
      "event": "appeal",
      "reasoning": "I wrote this myself and want the decision reviewed.",
      "status": "under_review",
      "timestamp": "2026-11-02T03:35:00+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I asked AI to inspect the starter files and help trace a
  submission from `POST /submit` through both signals, scoring, labels, and the
  audit log.
- *What came back:* It identified the existing route and audit helpers and
  proposed documenting the signal blind spots, false-positive path, and the
  request/response contracts before implementation.
- *What I changed:* I kept the equal-weight rule and wrote the final contracts
  and blind spots into this README, then added explicit validation behavior for
  invalid and oversized submissions.

**Moment 2**

- *What I asked for:* I asked AI to implement the missing stylometry, combined
  scoring, labels, and appeal workflow, then verify the route and audit log.
- *What came back:* It implemented the three style measures, the two-signal
  average, reader-facing labels, and append-only appeals. Testing also exposed
  that this environment lacked `torch`, so the detector could not produce a
  real model score.
- *What I changed:* I kept the documented `0.5` detector fallback, checked the
  style and label outputs myself, verified a real appeal in the log, and
  recorded the limitation instead of claiming the model was calibrated.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

Ten submissions per minute gives a writer room for occasional revisions while
stopping a burst of threshold-mapping requests. The daily limit of 200 still
allows substantial legitimate use without allowing an unattended script to
send thousands of variations.

**What a caller counts as:** `creator_id` <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

The full baseline is in [`results/attack_run_2026-11-08_0149_before.md`](results/attack_run_2026-11-08_0149_before.md).
It contains all 56 attack outcomes: **46 held and 10 broke**. The run returned
40 `200`s, 14 `400`s, and 2 rate-limit `429`s, with no crash. All ten evasion
attacks broke because the service returned `human` or `unsure`; the false-positive,
prompt-injection, malformed-input, and flood attacks held.

The detector model was not available in this environment, so the service used
its documented fallback `model_score = 0.5`. These baseline results therefore
measure the route, style signal, score thresholds, labels, and rate limiter, not
the downloaded model's behavior.


**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
[
  {
    "timestamp": "2026-11-08T07:49:32+00:00",
    "content_id": "96544b6f-686c-46da-86ec-238b4679b0f8",
    "creator_id": "attacker_EV02",
    "guess": "human",
    "model_score": 0.5,
    "style_score": 0.022,
    "combined_score": 0.261,
    "label": "We think this was probably written by a person. This result is not proof of authorship.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T07:49:32+00:00",
    "content_id": "c31a9c03-aa79-474c-abe8-555d3ad3be48",
    "creator_id": "attacker_EV09",
    "guess": "human",
    "model_score": 0.5,
    "style_score": 0.1866,
    "combined_score": 0.3433,
    "label": "We think this was probably written by a person. This result is not proof of authorship.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T07:49:32+00:00",
    "content_id": "7ae5984b-b09b-4683-8230-44e26eea9dc1",
    "creator_id": "attacker_EV10",
    "guess": "unsure",
    "model_score": 0.5,
    "style_score": 0.7718,
    "combined_score": 0.6359,
    "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T07:49:32+00:00",
    "content_id": "6cc2185e-eec9-4ee1-af7d-6f0a1821a307",
    "creator_id": "attacker_FP05",
    "guess": "unsure",
    "model_score": 0.5,
    "style_score": 0.4957,
    "combined_score": 0.4979,
    "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T07:49:32+00:00",
    "content_id": "d13abc06-651d-4e81-b0c0-be9c6a233453",
    "creator_id": "attacker_PI05",
    "guess": "human",
    "model_score": 0.5,
    "style_score": 0.1369,
    "combined_score": 0.3185,
    "label": "We think this was probably written by a person. This result is not proof of authorship.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T07:49:32+00:00",
    "creator_id": "attacker_MF01",
    "event": "rejected",
    "status": "rejected",
    "reason": "invalid_request",
    "message": "text must be a non-empty string"
  },
  {
    "timestamp": "2026-11-08T07:49:32+00:00",
    "content_id": "131087eb-1d8b-4590-85a8-1cab6a59fcd6",
    "creator_id": "attacker_MF06",
    "guess": "ai",
    "model_score": 0.5,
    "style_score": 1.0,
    "combined_score": 0.75,
    "label": "We think this was probably generated by AI. This result is not proof of authorship.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T07:49:32+00:00",
    "creator_id": "attacker_RQ01",
    "event": "rejected",
    "status": "rejected",
    "reason": "invalid_request",
    "message": "text must be a non-empty string"
  },
  {
    "timestamp": "2026-11-08T07:49:32+00:00",
    "content_id": "4d9aacb5-8e43-4425-a247-1a0a7195dba4",
    "creator_id": "attacker_flood",
    "guess": "unsure",
    "model_score": 0.5,
    "style_score": 0.4815,
    "combined_score": 0.4908,
    "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-08T07:49:32+00:00",
    "creator_id": "attacker_flood",
    "event": "rejected",
    "status": "rejected",
    "reason": "rate_limited",
    "limit": "10 per 1 minute"
  }
]
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

EV09 was the most serious detector miss. It submitted AI text with a human
opening paragraph, but the service returned `human` with `model_score = 0.5`,
`style_score = 0.1866`, and `combined_score = 0.3433`:

```text
Right, so. I've been thinking about this since the meeting on Thursday and I
still don't have a neat answer, but here's roughly where I've landed.

The importance of effective communication in the workplace cannot be
overstated. Teams that communicate clearly are better positioned to achieve
their objectives and avoid costly misunderstandings. There are several
strategies organisations can adopt to improve this. First, establishing
regular check-ins ensures that information flows consistently between team
members. Second, documenting decisions provides a reference point that reduces
ambiguity. Finally, encouraging an environment where questions are welcomed
helps surface issues early. Implementing these approaches can lead to
meaningful improvements in team performance and overall satisfaction.
```

No false-positive row crossed the AI threshold in this run; FP05 was the
closest writer-facing concern, receiving `unsure` at `0.4979`.


---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
