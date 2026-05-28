# 🤖 Rule-Based Medical Chatbot

> A rule-based AI medical assistant developed in Python that provides symptom-based guidance, medicine suggestions, emergency advice, and typo tolerance through fuzzy matching.

**DecodeLabs Internship — Batch 2026 | Project 1: Artificial Intelligence**  
**Author:** Mina Ayman Kamal

---

## 📌 Overview

This project is the first milestone of the DecodeLabs AI Engineering internship track. It demonstrates foundational AI concepts through the construction of a deterministic, rule-based chatbot — a "white box" system where every decision is fully traceable and explainable.

Rather than relying on machine learning, this chatbot operates through structured control flow, dictionary-based intent matching, and fuzzy string correction to simulate intelligent medical assistance.

---

## ✨ Features

- 🩺 **Symptom Recognition** — Detects 9 medical conditions including headache, fever, stress, allergies, chest pain, and more
- 💊 **Medicine Suggestions** — Returns appropriate over-the-counter medicine recommendations per symptom
- 🚨 **Emergency Detection** — Flags high-severity conditions (e.g. chest pain) and advises immediate medical attention
- 🔤 **Fuzzy Matching** — Handles typos and near-match inputs using Python's `difflib.get_close_matches`
- 💬 **General Conversation** — Responds to greetings, identity questions, medical philosophy, and medicine information queries
- 🔁 **Continuous Loop** — Runs indefinitely until the user types `exit`
- 🧹 **Input Sanitization** — Normalizes all input via `.lower().strip()` before processing

---

## 🗂️ Project Structure

```
rule_based_medical_chatbot/
│
├── rule_based_medical_chatbot.py   # Main chatbot script
└── README.md                       # Project documentation
```

---

## ⚙️ How It Works

The chatbot follows the **IPO Model** (Input → Process → Output):

1. **Input & Sanitization** — Raw user input is lowercased and stripped of whitespace
2. **Fuzzy Correction** — If the input doesn't match any key exactly, `get_close_matches` attempts to find the closest known intent
3. **Direct Response Matching** — Checks the `responses` dictionary for greetings, identity, and general queries (O(1) lookup)
4. **Symptom Matching** — Iterates through the `symptoms` database, matching keywords and fuzzy corrections
5. **Severity Routing** — High-severity symptoms trigger emergency advice; others return medicine and general guidance
6. **Fallback** — Unrecognized inputs return a default `"I don't understand"` response

---

## 🧠 Knowledge Base

### Response Categories (`responses` dict)
| Category | Examples |
|---|---|
| Greetings | hello, hi, hey, good morning |
| Identity | who are you, what is your purpose |
| Medicine Info | what is paracetamol, what is ibuprofen |
| Medical Philosophy | what is health, what is pain |
| Safety & Emergency | emergency, is this dangerous |

### Symptom Database (`symptoms` dict)
| Symptom | Severity | Suggested Medicine |
|---|---|---|
| Headache | Mild | Paracetamol, Ibuprofen |
| Fever | Mild | Paracetamol |
| Stress / Anxiety | Mild | Ashwagandha, Magnesium |
| Cold | Mild | Cold relief medication |
| Allergies | Mild | Cetirizine |
| Sleep Problems | Mild | Melatonin |
| Stomach Pain | Moderate | Antacids |
| Dehydration | Moderate | Electrolyte solution |
| Chest Pain | **High** | ⚠️ Seek emergency care |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- No external libraries required (`difflib` is part of the Python standard library)

### Run the Chatbot

```bash
python rule_based_medical_chatbot.py
```

### Example Interaction

```
You: hello
Hello. Tell me your symptoms clearly.

You: i have a headahce
Suggested medicine: Paracetamol, Ibuprofen
Rest and hydration may help.

You: chest pain
Seek emergency medical attention immediately.

You: exit
Goodbye!
```

---

## 🔬 Technical Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Control Flow | `while` loop, `if/elif`, `break` |
| Data Structures | Python dictionaries (O(1) lookup) |
| Input Sanitization | `.lower().strip()` |
| Fuzzy Matching | `difflib.get_close_matches` |
| Fallback Logic | `.get()` with default value |
| Severity Routing | Conditional branching on `data["severity"]` |


