"""
Central AI V2 - Brain Module
Handles AI processing and response generation
"""

import requests
import json
from config import config
from core.memory import Memory

class Brain:
    def __init__(self):
        self.name = config.AI_NAME
        self.version = config.VERSION
        self.memory = Memory()
        self.current_key_index = 0
        self.model = config.GEMINI_MODEL
        
        # Initialize conversation history with persona
        self.conversation_history = [
            {
                "role": "user",
                "parts": [{"text": config.PERSONA}]
            },
            {
                "role": "model",
                "parts": [{"text": f"Understood. Saya adalah {self.name} versi {self.version}, siap membantu Anda dengan profesional dan maksimal!"}]
            }
        ]
    
    def get_current_api_key(self):
        """Get current API key"""
        return config.GEMINI_API_KEYS[self.current_key_index]
    
    def rotate_api_key(self):
        """Rotate to next API key if current one fails"""
        self.current_key_index = (self.current_key_index + 1) % len(config.GEMINI_API_KEYS)
        print(f"[DEBUG] Rotated to API key index: {self.current_key_index}")
    
    def call_gemini_api(self, user_input, retry_count=0):
        """Call Gemini API with retry logic"""
        if retry_count >= config.MAX_RETRIES:
            return "Maaf, semua API key sedang tidak tersedia. Silakan coba lagi nanti."
        
        try:
            api_key = self.get_current_api_key()
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={api_key}"
            
            # Add user message to history
            self.conversation_history.append({
                "role": "user",
                "parts": [{"text": user_input}]
            })
            
            # Prepare request payload
            payload = {
                "contents": self.conversation_history
            }
            
            headers = {
                "Content-Type": "application/json"
            }
            
            # Make API request
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=config.TIMEOUT
            )
            
            # Check for rate limit or auth errors
            if response.status_code in [429, 403]:
                print(f"[DEBUG] API key {self.current_key_index} failed with status {response.status_code}")
                self.rotate_api_key()
                # Remove the last user message before retry
                self.conversation_history.pop()
                return self.call_gemini_api(user_input, retry_count + 1)
            
            response.raise_for_status()
            
            # Parse response
            data = response.json()
            
            if 'candidates' in data and len(data['candidates']) > 0:
                ai_response = data['candidates'][0]['content']['parts'][0]['text']
                
                # Add AI response to history
                self.conversation_history.append({
                    "role": "model",
                    "parts": [{"text": ai_response}]
                })
                
                return ai_response
            else:
                return "Maaf, saya tidak mendapat respon yang valid dari API."
                
        except requests.exceptions.Timeout:
            return "Request timeout. Silakan coba lagi."
        except requests.exceptions.RequestException as e:
            if retry_count < config.MAX_RETRIES - 1:
                self.rotate_api_key()
                # Remove the last user message before retry
                if self.conversation_history[-1]["role"] == "user":
                    self.conversation_history.pop()
                return self.call_gemini_api(user_input, retry_count + 1)
            return f"Error connecting to API: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    
    def process_input(self, user_input):
        """Process user input and generate response"""
        # Store in memory
        self.memory.add_to_short_term(user_input, "user")
        
        # Get context from memory
        context = self.memory.get_context()
        
        # Generate response using Gemini API
        response = self.call_gemini_api(user_input)
        
        # Store response in memory
        self.memory.add_to_short_term(response, "ai")
        
        return response
    
    def clear_conversation(self):
        """Clear conversation history (keep persona)"""
        self.conversation_history = self.conversation_history[:2]
        self.memory.clear_short_term()
