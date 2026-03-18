import re

class Memory:
    def __init__(self):
        self.data = {}

    def update(self, user_input):
        """
        从用户输入中提取关键信息
        """
        patterns = {
            "name": r"My name is (.*)",
            "age": r"I am (\d+) years old",
            "job": r"I am a (.*)",
        }

        for key, pattern in patterns.items():
            match = re.search(pattern, user_input, re.IGNORECASE)
            if match:
                self.data[key] = match.group(1)

    def inject(self, response):
        """
        在回复中注入记忆信息（简单增强）
        """
        if "name" in self.data:
            response = f"{self.data['name']}, {response}"
        return response

    def recall(self, key):
        return self.data.get(key, None)
