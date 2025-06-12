import os
import openai

class CoachService:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        openai.api_key = self.api_key

    def get_response(self, message_history):
        response = openai.ChatCompletion.create(
            model='gpt-4o-mini',
            messages=message_history
        )
        return response.choices[0].message['content']

coach_service = CoachService()
