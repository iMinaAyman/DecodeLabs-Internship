# Rule-Based Medical Chatbot
# Developed by Mina Ayman

from difflib import get_close_matches

responses = {

    # Greetings
    "hello": "Hello. Tell me your symptoms clearly.",
    "hi": "Hi. What seems to be the problem?",
    "hey": "Hey. Describe what you are feeling.",
    "good morning": "Good morning. Health improves through attention.",
    "good evening": "Good evening. Symptoms should never be ignored.",

    # Identity
    "who are you": "A rule-based medical assistant designed for symptom guidance.",
    "what are you": "A conversational healthcare support system.",
    "who made you": "Mina Ayman developed this system.",
    "what is your purpose": "To provide basic medicine and symptom guidance.",

    # System Logic
    "how do you work": "I analyze symptoms using predefined medical response patterns.",
    "can you diagnose": "I provide guidance, not professional diagnosis.",
    "are you a doctor": "I simulate medical assistance through structured logic.",
    "do you learn": "My responses are predefined for safety and consistency.",
    "are you intelligent": "Medical guidance requires structured reasoning.",

    # Medical Philosophy
    "what is health": "Health is balance maintained through discipline and care.",
    "what is medicine": "Medicine attempts to restore the body's natural balance.",
    "what is pain": "Pain is the body's demand for attention.",
    "what is prevention": "Preventing illness is wiser than treating it.",
    "what is recovery": "Recovery requires patience and consistency.",
    "what is discipline": "Discipline protects health before medicine becomes necessary.",
    "what is intelligence": "True intelligence applies knowledge correctly.",
    "what is wisdom": "Wisdom is knowledge guided by judgment.",

    # Medicine Information
    "what is paracetamol": "Paracetamol is commonly used for pain relief and fever reduction.",
    "what is ibuprofen": "Ibuprofen reduces pain, inflammation, and fever.",
    "what is cetirizine": "Cetirizine is commonly used to treat allergy symptoms.",
    "what are antacids": "Antacids reduce excess stomach acid and heartburn symptoms.",
    "what is melatonin": "Melatonin helps regulate the sleep cycle.",
    "what is magnesium": "Magnesium supports nerve and muscle function.",
    "what is ashwagandha": "Ashwagandha is a herbal supplement commonly used for stress support.",
    "what is vitamin c": "Vitamin C supports immune system function.",
    "what is zinc": "Zinc supports immune response and recovery.",
    "what is omega 3": "Omega-3 supports heart, brain, and joint health.",

    # Help
    "help": "Describe symptoms clearly for better guidance.",
    "what can you do": "I provide symptom-based medical guidance and medicine suggestions.",
    "can you help me": "State your symptoms precisely.",

    # Safety
    "is this dangerous": "Severe or persistent symptoms should be evaluated professionally.",
    "emergency": "Seek immediate medical attention or contact emergency services.",

    # Humor
    "tell me a joke": "Humans ignore sleep, then wonder why the body complains.",

    # Goodbye
    "bye": "Take care of your health.",
    "goodbye": "Recovery begins with attention and discipline.",
    "see you": "Monitor symptoms carefully."
}


# Medical knowledge database
# Stores symptoms, keywords, medicine suggestions,
# advice, and severity levels.

symptoms = {

    "headache": {

        "keywords": [
            "headache",
            "head pain",
            "pain in my head",
            "my head hurts"
        ],

        "medicine": [
            "Paracetamol",
            "Ibuprofen"
        ],

        "advice": "Rest and hydration may help.",

        "severity": "mild"
    },

    "fever": {

        "keywords": [
            "fever",
            "high temperature",
            "hot body"
        ],

        "medicine": [
            "Paracetamol"
        ],

        "advice": "Drink water and monitor temperature.",

        "severity": "mild"
    },

    "stress": {

        "keywords": [
            "stress",
            "stressed",
            "anxiety",
            "overthinking"
        ],

        "medicine": [
            "Ashwagandha",
            "Magnesium"
        ],

        "advice": "Sleep and reduced caffeine may help.",

        "severity": "mild"
    },

    "cold": {

        "keywords": [
            "cold",
            "runny nose",
            "sneezing"
        ],

        "medicine": [
            "Cold relief medication"
        ],

        "advice": "Rest and hydration support recovery.",

        "severity": "mild"
    },

    "stomach pain": {

        "keywords": [
            "stomach pain",
            "stomach ache",
            "my stomach hurts"
        ],

        "medicine": [
            "Antacids"
        ],

        "advice": "Avoid heavy meals and monitor symptoms.",

        "severity": "moderate"
    },

    "allergies": {

        "keywords": [
            "allergy",
            "allergies",
            "itching",
            "sneezing allergy"
        ],

        "medicine": [
            "Cetirizine"
        ],

        "advice": "Avoid known allergy triggers if possible.",

        "severity": "mild"
    },

    "sleep problems": {

        "keywords": [
            "cannot sleep",
            "insomnia",
            "i can't sleep",
            "sleep problems"
        ],

        "medicine": [
            "Melatonin"
        ],

        "advice": "Reduce screen exposure before sleep.",

        "severity": "mild"
    },

    "dehydration": {

        "keywords": [
            "dehydrated",
            "dehydration",
            "dry mouth"
        ],

        "medicine": [
            "Electrolyte solution"
        ],

        "advice": "Increase water intake gradually.",

        "severity": "moderate"
    },

    "chest pain": {

        "keywords": [
            "chest pain",
            "pain in chest",
            "tight chest"
        ],

        "medicine": [],

        "advice": "Seek emergency medical attention immediately.",

        "severity": "high"
    }
}


# Main chatbot loop
# Runs continuously until the user exits.
while True:

    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("Goodbye!")
        break

    # Fuzzy correction for direct responses
    if user_input not in responses:

        possible_response = get_close_matches(
            user_input,
            responses.keys(),
            n=1,
            cutoff=0.6
        )

        if possible_response:
            user_input = possible_response[0]

    # 1. Direct responses (greetings, info, etc.)
    reply = responses.get(user_input)

    if reply:
        print(reply)
        continue

    # 2. Symptom matching (still using dict.get style logic)
    matched = False

    for symptom, data in symptoms.items():

        # Fuzzy correction for symptom keywords
        possible_keyword = get_close_matches(
            user_input,
            data["keywords"],
            n=1,
            cutoff=0.5
        )

        if any(keyword in user_input for keyword in data["keywords"]) or possible_keyword:

            matched = True

            if data["severity"] == "high":
                print(data["advice"])
                break

            medicines = ", ".join(data["medicine"]) if data["medicine"] else "No medication required"

            print(f"Suggested medicine: {medicines}")
            print(data["advice"])
            break

    # 3. Final fallback (ONLY dict.get style behavior)
    if not matched:
        print(responses.get(user_input, "I don't understand"))