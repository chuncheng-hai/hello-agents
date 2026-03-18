import re
import random
from memory import Memory
from rules_extension import extended_rules

# 原始 rules（略）...
rules = {
    r'I need (.*)': [
        "Why do you need {0}?",
        "Would it really help you to get {0}?",
        "Are you sure you need {0}?"
    ],
    r'I am (.*)': [
        "Did you come to me because you are {0}?",
        "How long have you been {0}?",
        "How do you feel about being {0}?"
    ],
    r'.*': [
        "Please tell me more.",
        "Can you elaborate on that?"
    ]
}

# 合并规则（扩展规则优先）
rules = {**extended_rules, **rules}

# 代词转换（原样保留）
pronoun_swap = {
    "i": "you", "you": "i", "me": "you", "my": "your",
    "am": "are", "are": "am", "was": "were",
}

def swap_pronouns(phrase):
    words = phrase.lower().split()
    return " ".join([pronoun_swap.get(w, w) for w in words])


memory = Memory()

def respond(user_input):
    # 更新记忆
    memory.update(user_input)

    for pattern, responses in rules.items():
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            captured = match.group(1) if match.groups() else ''
            swapped = swap_pronouns(captured)
            response = random.choice(responses).format(swapped)

            # 注入记忆
            response = memory.inject(response)

            return response

    return "Please tell me more."


if __name__ == '__main__':
    print("Therapist: Hello! How can I help you today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Therapist: Goodbye.")
            break

        print("Therapist:", respond(user_input))
