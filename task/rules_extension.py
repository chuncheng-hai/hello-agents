extended_rules = {
    # 工作
    r'I work as (.*)': [
        "How do you feel about working as {0}?",
        "What do you enjoy most about being {0}?",
        "Does working as {0} satisfy you?"
    ],

    # 学习
    r'I am studying (.*)': [
        "Why did you choose to study {0}?",
        "What do you find most difficult about {0}?",
        "How do you plan to improve in {0}?"
    ],

    # 爱好
    r'I like (.*)': [
        "Why do you like {0}?",
        "How often do you spend time on {0}?",
        "What do you get from {0}?"
    ],

    # 姓名（用于记忆）
    r'My name is (.*)': [
        "Nice to meet you, {0}.",
        "Hello {0}, how can I assist you today?"
    ],

    # 职业（用于记忆）
    r'I am a (.*)': [
        "Being a {0} sounds interesting. Tell me more.",
        "What made you become a {0}?"
    ]
}
