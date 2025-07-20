from voice_engine import VoiceEngine
from lesson_planner import LessonPlanner
import logging

class RoboTeacher:
    def __init__(self):
        self.voice = VoiceEngine()
        self.planner = LessonPlanner()
        logging.basicConfig(level=logging.INFO)
        
    def start_session(self):
        """Main interaction loop"""
        self.voice.speak("Hello! I'm Robo Teacher!")
        while True:
            try:
                user_input = self.voice.listen()
                if "exit" in user_input.lower():
                    break
                
                response = self.planner.generate_response(user_input)
                self.voice.speak(response)
                
            except Exception as e:
                logging.error(f"Error: {e}")
                self.voice.speak("Let's try that again")

if __name__ == "__main__":
    teacher = RoboTeacher()
    teacher.start_session()