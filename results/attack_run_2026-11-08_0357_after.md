# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 03:57
- Auto-marked BROKE (5xx, crash, no response): **0**
- Manual verdicts: **47 HELD · 9 BROKE**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c9f7250f-6133-46c1-9c84-3a3215c2f51e` | unsure | 0.442 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `93140bf8-b150-458d-b898-8b8aa49fc0f7` | human | 0.261 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `d32a3e3b-a90b-4c4f-91f5-f68e434775af` | human | 0.334 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `5461ca0c-5b5f-4e94-a9e4-01b566434709` | unsure | 0.431 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `99032eec-ddd3-4c6d-97d0-9210720ebfa0` | human | 0.312 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `bb0ef3a2-28fe-4a0b-92cf-47d62238a29b` | unsure | 0.363 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `9103598f-8c88-4f7a-8ba1-a54968febde9` | unsure | 0.427 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `802ce4a1-0fcc-4449-9f8a-93ac9c542832` | unsure | 0.358 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `4c61c2c9-418f-4d30-80c3-41f956acec07` | human | 0.343 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `fd0d7a85-7975-4d4c-a0ae-8c796cac1989` | ai | 0.636 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `efb95a8f-af6b-40c3-b51f-312912cb1558` | unsure | 0.441 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `cc8f13a6-298d-499c-b832-c945d9f9f592` | unsure | 0.479 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `da1eda5d-b25d-44e2-bdf0-15999d51ac06` | unsure | 0.473 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `951cd29a-6016-49d7-b6f1-f5c2c18ef539` | unsure | 0.397 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `10d3aa51-9086-42a8-9a85-e778e0be60f2` | unsure | 0.498 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `be858d3c-9038-4616-b5ad-38cb634e6add` | unsure | 0.408 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `44e64765-b156-484d-ab0d-1e3a5909e2c1` | unsure | 0.431 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `a0ade7b9-38df-4b3a-86b4-ced7412afe8c` | human | 0.327 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `fdf8d09b-005f-4376-a136-8ad375b9f537` | unsure | 0.353 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `9fe3f9ca-0791-4d37-b8c3-b09a4005a056` | human | 0.299 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `8d921b8a-15d1-4415-bee7-56b8f13f1c60` | unsure | 0.406 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `4b798b40-a5fa-4103-a595-5837f8452504` | human | 0.334 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `d479db71-6357-4b88-8d6f-c675ddab17c2` | human | 0.319 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `df53cd3b-070a-4198-bd9d-65b81df27195` | unsure | 0.444 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 200 | `ebacefdd-c9b4-4a28-8a4a-7a6484fe92d4` | unsure | 0.583 | HELD |
| MF03 | malformed | text is control characters | 200 | `990d2397-62fc-48fd-84a5-b2afc0b12d7a` | unsure | 0.417 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `dca6e134-1569-4452-9726-35a41f67ab45` | ai | 0.750 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `8c1ecc28-8367-427a-831e-cdf234bc0b13` | unsure | 0.583 | HELD |
| MF06 | malformed | text is emoji only | 200 | `e4c846ce-b42c-46ad-9d2b-94c9c25e2c23` | ai | 0.750 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `9b7375f1-930d-41fd-8440-fd6a4070d9a2` | ai | 0.750 | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d7be8d48-ec2f-4c6f-b6bb-97a0b55d3d7b` | unsure | 0.491 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f2d58160-da98-4c96-8e7b-7261a9c94019` | unsure | 0.491 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `946476bc-5b35-4828-b81f-6c558466450a` | unsure | 0.491 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `81af9fa0-8f66-4915-af31-d9b472503da8` | unsure | 0.491 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4672e82f-3e90-4fd0-81fe-a7ee8a8c0c2d` | unsure | 0.491 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3977806f-2265-407d-978e-80a1775a0fce` | unsure | 0.491 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a0ade440-7c51-4f43-ad3f-1431f3cf1831` | unsure | 0.491 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `35f31359-174d-4142-a390-79e223a3a991` | unsure | 0.491 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `93c7e2a8-d73d-4dc3-9914-a2541498c254` | unsure | 0.491 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `da2a34cf-e0ff-4234-afb7-f2bda9f39375` | unsure | 0.491 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Held | Broke |
|---|---|---|---|
| `evasion` | 10 | 1 | 9 |
| `false_positive` | 8 | 8 | 0 |
| `flood_same_creator` | 12 | 12 | 0 |
| `malformed` | 20 | 20 | 0 |
| `prompt_injection` | 6 | 6 | 0 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "c9f7250f-6133-46c1-9c84-3a3215c2f51e",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.442,
  "model_score": 0.5,
  "style_score": 0.384,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "93140bf8-b150-458d-b898-8b8aa49fc0f7",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.261,
  "model_score": 0.5,
  "style_score": 0.022,
  "label": "We think this was probably written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "d32a3e3b-a90b-4c4f-91f5-f68e434775af",
  "creator_id": "attacker_EV03",
  "guess": "human",
  "confidence": 0.3337,
  "model_score": 0.5,
  "style_score": 0.1675,
  "label": "We think this was probably written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "5461ca0c-5b5f-4e94-a9e4-01b566434709",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.4308,
  "model_score": 0.5,
  "style_score": 0.3616,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "99032eec-ddd3-4c6d-97d0-9210720ebfa0",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3121,
  "model_score": 0.5,
  "style_score": 0.1242,
  "label": "We think this was probably written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "bb0ef3a2-28fe-4a0b-92cf-47d62238a29b",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.3627,
  "model_score": 0.5,
  "style_score": 0.2254,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "9103598f-8c88-4f7a-8ba1-a54968febde9",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4266,
  "model_score": 0.5,
  "style_score": 0.3532,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "802ce4a1-0fcc-4449-9f8a-93ac9c542832",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3578,
  "model_score": 0.5,
  "style_score": 0.2155,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "4c61c2c9-418f-4d30-80c3-41f956acec07",
  "creator_id": "attacker_EV09",
  "guess": "human",
  "confidence": 0.3433,
  "model_score": 0.5,
  "style_score": 0.1866,
  "label": "We think this was probably written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "fd0d7a85-7975-4d4c-a0ae-8c796cac1989",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.6359,
  "model_score": 0.5,
  "style_score": 0.7718,
  "label": "We think this was probably generated by AI. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "efb95a8f-af6b-40c3-b51f-312912cb1558",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4409,
  "model_score": 0.5,
  "style_score": 0.3818,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "cc8f13a6-298d-499c-b832-c945d9f9f592",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.4787,
  "model_score": 0.5,
  "style_score": 0.4574,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "da1eda5d-b25d-44e2-bdf0-15999d51ac06",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.4733,
  "model_score": 0.5,
  "style_score": 0.4465,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "951cd29a-6016-49d7-b6f1-f5c2c18ef539",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.3967,
  "model_score": 0.5,
  "style_score": 0.2933,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "10d3aa51-9086-42a8-9a85-e778e0be60f2",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.4979,
  "model_score": 0.5,
  "style_score": 0.4957,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "be858d3c-9038-4616-b5ad-38cb634e6add",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.4083,
  "model_score": 0.5,
  "style_score": 0.3167,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "44e64765-b156-484d-ab0d-1e3a5909e2c1",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.4307,
  "model_score": 0.5,
  "style_score": 0.3615,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "a0ade7b9-38df-4b3a-86b4-ced7412afe8c",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.3265,
  "model_score": 0.5,
  "style_score": 0.1529,
  "label": "We think this was probably written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "fdf8d09b-005f-4376-a136-8ad375b9f537",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.3527,
  "model_score": 0.5,
  "style_score": 0.2054,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "9fe3f9ca-0791-4d37-b8c3-b09a4005a056",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2994,
  "model_score": 0.5,
  "style_score": 0.0988,
  "label": "We think this was probably written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "8d921b8a-15d1-4415-bee7-56b8f13f1c60",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4058,
  "model_score": 0.5,
  "style_score": 0.3116,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "4b798b40-a5fa-4103-a595-5837f8452504",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.334,
  "model_score": 0.5,
  "style_score": 0.168,
  "label": "We think this was probably written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "d479db71-6357-4b88-8d6f-c675ddab17c2",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.3185,
  "model_score": 0.5,
  "style_score": 0.1369,
  "label": "We think this was probably written by a person. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "df53cd3b-070a-4198-bd9d-65b81df27195",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4435,
  "model_score": 0.5,
  "style_score": 0.387,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 200,
  "content_id": "ebacefdd-c9b4-4a28-8a4a-7a6484fe92d4",
  "creator_id": "attacker_MF02",
  "guess": "unsure",
  "confidence": 0.5834,
  "model_score": 0.5,
  "style_score": 0.6667,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "990d2397-62fc-48fd-84a5-b2afc0b12d7a",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.4166,
  "model_score": 0.5,
  "style_score": 0.3333,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "dca6e134-1569-4452-9726-35a41f67ab45",
  "creator_id": "attacker_MF04",
  "guess": "ai",
  "confidence": 0.75,
  "model_score": 0.5,
  "style_score": 1.0,
  "label": "We think this was probably generated by AI. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "8c1ecc28-8367-427a-831e-cdf234bc0b13",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.5834,
  "model_score": 0.5,
  "style_score": 0.6667,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "e4c846ce-b42c-46ad-9d2b-94c9c25e2c23",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.75,
  "model_score": 0.5,
  "style_score": 1.0,
  "label": "We think this was probably generated by AI. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "9b7375f1-930d-41fd-8440-fd6a4070d9a2",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.75,
  "model_score": 0.5,
  "style_score": 1.0,
  "label": "We think this was probably generated by AI. This result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "d7be8d48-ec2f-4c6f-b6bb-97a0b55d3d7b",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4908,
  "model_score": 0.5,
  "style_score": 0.4815,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "f2d58160-da98-4c96-8e7b-7261a9c94019",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4908,
  "model_score": 0.5,
  "style_score": 0.4815,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "946476bc-5b35-4828-b81f-6c558466450a",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4908,
  "model_score": 0.5,
  "style_score": 0.4815,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "81af9fa0-8f66-4915-af31-d9b472503da8",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4908,
  "model_score": 0.5,
  "style_score": 0.4815,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "4672e82f-3e90-4fd0-81fe-a7ee8a8c0c2d",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4908,
  "model_score": 0.5,
  "style_score": 0.4815,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "3977806f-2265-407d-978e-80a1775a0fce",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4908,
  "model_score": 0.5,
  "style_score": 0.4815,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "a0ade440-7c51-4f43-ad3f-1431f3cf1831",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4908,
  "model_score": 0.5,
  "style_score": 0.4815,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "35f31359-174d-4142-a390-79e223a3a991",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4908,
  "model_score": 0.5,
  "style_score": 0.4815,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "93c7e2a8-d73d-4dc3-9914-a2541498c254",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4908,
  "model_score": 0.5,
  "style_score": 0.4815,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "da2a34cf-e0ff-4234-afb7-f2bda9f39375",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4908,
  "model_score": 0.5,
  "style_score": 0.4815,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
