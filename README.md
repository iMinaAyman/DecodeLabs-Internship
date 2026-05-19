# Rule-Based Medical Chatbot
**Developer:** Mina Ayman
**Project:** DecodeLabs Industrial Training Kit — Artificial Intelligence, Project 1
**Batch:** 2026

---

## Project Overview

A rule-based medical chatbot built in Python that provides symptom guidance and basic medicine suggestions through predefined logic. This project demonstrates mastery of control flow, dictionary-based decision making, and continuous input loop architecture — the foundational skills required for building deterministic AI systems.

---

## Project 1 Requirements Checklist

| Requirement | Status | Implementation Detail |
|---|---|---|
| Continuous input loop | Complete | `while True` loop runs until the user types `exit` |
| Input sanitization | Complete | `.lower().strip()` normalizes all user input |
| Knowledge base with 5+ intents | Complete | 50+ intents in `responses` dict + 9 symptom categories |
| Fallback response for unknowns | Complete | `responses.get(user_input, "I don't understand")` |
| Clean exit command | Complete | `if user_input == "exit": break` |
| If-else logic for responses | Complete | Layered matching: direct response → symptom → fallback |

---

## Architecture

The chatbot follows the IPO (Input, Process, Output) model taught in the training kit:

**Input Phase** — Raw user text is collected and sanitized using `.lower().strip()`, ensuring case and whitespace variations are handled before any matching occurs.

**Process Phase** — The system applies a three-tier matching strategy:

1. Direct dictionary lookup via `.get()` on the `responses` dict (O(1) complexity, no if-elif ladder).
2. Fuzzy correction using `difflib.get_close_matches` before dictionary lookup, tolerating minor typos.
3. Symptom keyword matching across the `symptoms` database, also with fuzzy correction at cutoff 0.5.

**Output Phase** — The system returns either a direct response, a structured symptom response (medicine + advice), or a fallback message. High-severity symptoms (e.g., chest pain) bypass medicine suggestions and route directly to emergency advice.

---

## Knowledge Base

**Response Dictionary** — Covers greetings, identity queries, medical philosophy, medicine information, safety prompts, and exit phrases (50+ keys).

**Symptoms Database** — 9 symptom categories with structured data per entry:

| Symptom | Suggested Medicine | Severity |
|---|---|---|
| Headache | Paracetamol, Ibuprofen | Mild |
| Fever | Paracetamol | Mild |
| Stress | Ashwagandha, Magnesium | Mild |
| Cold | Cold relief medication | Mild |
| Stomach Pain | Antacids | Moderate |
| Allergies | Cetirizine | Mild |
| Sleep Problems | Melatonin | Mild |
| Dehydration | Electrolyte solution | Moderate |
| Chest Pain | None — emergency referral | High |

---

## Technical Design Decisions

**Dictionary over if-elif ladder** — Response lookup uses Python's `.get()` method, achieving O(1) constant-time lookup regardless of knowledge base size. This avoids the O(n) linear complexity and high technical debt associated with chained if-elif structures.

**Fuzzy matching** — `difflib.get_close_matches` is applied at two points in the pipeline: once on the full response dictionary (cutoff 0.6) and once per symptom keyword list (cutoff 0.5). This makes the bot tolerant of minor spelling errors without requiring machine learning.

**Severity routing** — The symptom processor checks severity before constructing any response. High-severity conditions skip medicine output entirely and return only emergency guidance, preventing inappropriate self-medication advice.

**White-box transparency** — Every response is fully traceable: input → sanitization → lookup → output. There is no probabilistic behavior. This aligns with the rule-based "white box" model described in the architecture briefing.

---

## How to Run

**Requirements:** Python 3.x (no external libraries required — `difflib` is part of the standard library)

```bash
python rule_based_medical_chatbot.py
```

Type any symptom, greeting, or medical question at the `You:` prompt. Type `exit` to terminate the session.

**Example interaction:**

```
You: hello
Hello. Tell me your symptoms clearly.

You: i have a headache
Suggested medicine: Paracetamol, Ibuprofen
Rest and hydration may help.

You: chest pain
Seek emergency medical attention immediately.

You: exit
Goodbye!
```

---

## Disclaimer

This chatbot provides general informational guidance only. It does not perform clinical diagnosis and is not a substitute for professional medical advice. Users experiencing serious or persistent symptoms should consult a licensed healthcare provider.
