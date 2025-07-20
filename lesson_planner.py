from typing import Dict
import random

class LessonPlanner:
    def __init__(self):
        self.lessons = {
            "math": self._math_response,
            "alphabet": self._alphabet_response,
            "story": self._story_response
        }
        
    def generate_response(self, user_input: str) -> str:
        """Route user input to appropriate lesson handler"""
        input_lower = user_input.lower()
        
        if any(word in input_lower for word in ["math", "number", "count"]):
            return self.lessons["math"]()
        elif any(word in input_lower for word in ["alphabet", "letter", "abc"]):
            return self.lessons["alphabet"]()
        elif any(word in input_lower for word in ["story", "tell me"]):
            return self.lessons["story"]()
        else:
            return "I can help with math, alphabet, or stories. What would you like?"

    def _math_response(self) -> str:
        a, b = random.randint(1, 5), random.randint(1, 5)
        return f"What is {a} plus {b}? Try solving it!"

    def _alphabet_response(self) -> str:
        letters = ["A", "B", "C", "D", "E"]
        return f"Let's practice letters! Can you say {random.choice(letters)}?"

    def _story_response(self) -> str:
        stories = [
            "Once upon a time, a little robot wanted to learn...",
            "There was a friendly dinosaur who loved numbers..."
        ]
        return random.choice(stories)