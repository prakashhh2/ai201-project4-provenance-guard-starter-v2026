# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 01:49
- Auto-marked BROKE (5xx, crash, no response): **0**
- Manual verdicts: **46 HELD · 10 BROKE**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `5c2fba27-6660-4f76-877a-ae5918b5e053` | unsure | 0.442 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `96544b6f-686c-46da-86ec-238b4679b0f8` | human | 0.261 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `f0600eb4-09c0-4916-bdc2-326ccc9a9427` | human | 0.334 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `1854b590-1790-40a1-ae9b-06eb230a4e30` | unsure | 0.431 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `1729aa08-b663-4a84-99bc-54d1bb948f60` | human | 0.312 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `0b92595a-fa00-49d1-b627-ab7f8dd97105` | unsure | 0.363 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `552171c4-8eca-4871-8b5a-30073730714d` | unsure | 0.427 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `758aad58-b7f7-4677-a0e3-40d4f75108ac` | unsure | 0.358 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c31a9c03-aa79-474c-abe8-555d3ad3be48` | human | 0.343 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `7ae5984b-b09b-4683-8230-44e26eea9dc1` | unsure | 0.636 | BROKE |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `406e07df-8483-439c-86de-e7fbe95d1eba` | unsure | 0.441 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `19a837dc-d102-4fa8-9af7-dca5cfb7bb0d` | unsure | 0.479 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `71e151b9-bcb2-45d0-88f7-3415b439763e` | unsure | 0.473 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `1346c22a-1e40-40c3-b8da-3c4bf7a61441` | unsure | 0.397 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `6cc2185e-eec9-4ee1-af7d-6f0a1821a307` | unsure | 0.498 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `0e1d8b12-1107-4a05-8a6f-95c5edce7dfa` | unsure | 0.408 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `192afb82-cc79-4fb9-88c1-003981f9ab60` | unsure | 0.431 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `8f029960-b5cb-4abb-a24b-e0a76609b1d5` | human | 0.327 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `567706d8-6357-49c5-9468-cc9e805ae425` | unsure | 0.353 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `acc64a30-a8fe-4357-80b1-5f21b650c82b` | human | 0.299 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `afee67d6-2597-4a14-9d03-517665e3ee98` | unsure | 0.406 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `844131a3-fa18-43cd-87b8-657e584da3d0` | human | 0.334 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `d13abc06-651d-4e81-b0c0-be9c6a233453` | human | 0.319 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `e090cb51-3473-4659-abd0-e7004d981c86` | unsure | 0.444 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 200 | `17c13fe2-f18b-4548-a6ea-af4686cd98e1` | unsure | 0.583 | HELD |
| MF03 | malformed | text is control characters | 200 | `c169671e-7bc8-4098-a4cc-e8d813215dd2` | unsure | 0.417 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `b25d3a87-ccf1-48c6-b7f2-804765610373` | ai | 0.750 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `5c289c12-b07b-44b3-a988-bd9179163575` | unsure | 0.583 | HELD |
| MF06 | malformed | text is emoji only | 200 | `131087eb-1d8b-4590-85a8-1cab6a59fcd6` | ai | 0.750 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `a89ebfc1-9f07-4032-a679-9b01060e8ca9` | ai | 0.750 | HELD |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4d9aacb5-8e43-4425-a247-1a0a7195dba4` | unsure | 0.491 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `66e697d2-b65f-46f2-9aad-edfebc614ef5` | unsure | 0.491 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2a48895f-542b-4bcb-b97f-a365a4241f11` | unsure | 0.491 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d5414943-b4b2-4506-bf4b-710d28aed731` | unsure | 0.491 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8c2b0a09-b5c6-464a-a03a-3f6c320fe65a` | unsure | 0.491 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7bcaa7fe-f016-4cb0-b03a-ce760503455a` | unsure | 0.491 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `77488871-3b30-46ce-9c5b-8fe0572e36d8` | unsure | 0.491 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `db35803f-b86d-4383-84c4-338a1d748b98` | unsure | 0.491 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `af23bba6-198f-4ac4-b6ca-bceed9659357` | unsure | 0.491 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ed72446e-f302-4f9b-8d7b-603ea9c8f32b` | unsure | 0.491 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Held | Broke |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
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
  "content_id": "5c2fba27-6660-4f76-877a-ae5918b5e053",
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
  "content_id": "96544b6f-686c-46da-86ec-238b4679b0f8",
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
  "content_id": "f0600eb4-09c0-4916-bdc2-326ccc9a9427",
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
  "content_id": "1854b590-1790-40a1-ae9b-06eb230a4e30",
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
  "content_id": "1729aa08-b663-4a84-99bc-54d1bb948f60",
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
  "content_id": "0b92595a-fa00-49d1-b627-ab7f8dd97105",
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
  "content_id": "552171c4-8eca-4871-8b5a-30073730714d",
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
  "content_id": "758aad58-b7f7-4677-a0e3-40d4f75108ac",
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
  "content_id": "c31a9c03-aa79-474c-abe8-555d3ad3be48",
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
  "content_id": "7ae5984b-b09b-4683-8230-44e26eea9dc1",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.6359,
  "model_score": 0.5,
  "style_score": 0.7718,
  "label": "We cannot tell reliably whether this was written by a person or generated by AI.",
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
  "content_id": "406e07df-8483-439c-86de-e7fbe95d1eba",
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
  "content_id": "19a837dc-d102-4fa8-9af7-dca5cfb7bb0d",
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
  "content_id": "71e151b9-bcb2-45d0-88f7-3415b439763e",
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
  "content_id": "1346c22a-1e40-40c3-b8da-3c4bf7a61441",
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
  "content_id": "6cc2185e-eec9-4ee1-af7d-6f0a1821a307",
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
  "content_id": "0e1d8b12-1107-4a05-8a6f-95c5edce7dfa",
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
  "content_id": "192afb82-cc79-4fb9-88c1-003981f9ab60",
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
  "content_id": "8f029960-b5cb-4abb-a24b-e0a76609b1d5",
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
  "content_id": "567706d8-6357-49c5-9468-cc9e805ae425",
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
  "content_id": "acc64a30-a8fe-4357-80b1-5f21b650c82b",
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
  "content_id": "afee67d6-2597-4a14-9d03-517665e3ee98",
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
  "content_id": "844131a3-fa18-43cd-87b8-657e584da3d0",
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
  "content_id": "d13abc06-651d-4e81-b0c0-be9c6a233453",
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
  "content_id": "e090cb51-3473-4659-abd0-e7004d981c86",
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
  "content_id": "17c13fe2-f18b-4548-a6ea-af4686cd98e1",
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
  "content_id": "c169671e-7bc8-4098-a4cc-e8d813215dd2",
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
  "content_id": "b25d3a87-ccf1-48c6-b7f2-804765610373",
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
  "content_id": "5c289c12-b07b-44b3-a988-bd9179163575",
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
  "content_id": "131087eb-1d8b-4590-85a8-1cab6a59fcd6",
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
  "content_id": "a89ebfc1-9f07-4032-a679-9b01060e8ca9",
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
  "content_id": "4d9aacb5-8e43-4425-a247-1a0a7195dba4",
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
  "content_id": "66e697d2-b65f-46f2-9aad-edfebc614ef5",
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
  "content_id": "2a48895f-542b-4bcb-b97f-a365a4241f11",
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
  "content_id": "d5414943-b4b2-4506-bf4b-710d28aed731",
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
  "content_id": "8c2b0a09-b5c6-464a-a03a-3f6c320fe65a",
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
  "content_id": "7bcaa7fe-f016-4cb0-b03a-ce760503455a",
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
  "content_id": "77488871-3b30-46ce-9c5b-8fe0572e36d8",
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
  "content_id": "db35803f-b86d-4383-84c4-338a1d748b98",
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
  "content_id": "af23bba6-198f-4ac4-b6ca-bceed9659357",
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
  "content_id": "ed72446e-f302-4f9b-8d7b-603ea9c8f32b",
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
