"""
Central AI V2 - Memory Module
Handles short-term and long-term memory
"""

from collections import deque
from datetime import datetime
from config import config

class Memory:
    def __init__(self):
        # Short-term memory for recent conversations
        self.short_term_memory = deque(maxlen=config.SHORT_TERM_MEMORY_SIZE)
        
        # Long-term memory for important information
        self.long_term_memory = []
        
        # Session info
        self.session_start = datetime.now()
        self.total_interactions = 0
    
    def add_to_short_term(self, message, role):
        """Add message to short-term memory"""
        self.short_term_memory.append({
            "role": role,
            "message": message,
            "timestamp": datetime.now()
        })
        self.total_interactions += 1
    
    def add_to_long_term(self, key, value):
        """Add important information to long-term memory"""
        self.long_term_memory.append({
            "key": key,
            "value": value,
            "timestamp": datetime.now()
        })
        
        # Limit long-term memory size
        if len(self.long_term_memory) > config.LONG_TERM_MEMORY_SIZE:
            self.long_term_memory.pop(0)
    
    def get_context(self):
        """Get context from recent conversations"""
        context = []
        for item in self.short_term_memory:
            context.append(f"{item['role']}: {item['message']}")
        return "\n".join(context)
    
    def search_long_term(self, query):
        """Search long-term memory"""
        results = []
        query_lower = query.lower()
        
        for item in self.long_term_memory:
            if query_lower in item['key'].lower() or query_lower in str(item['value']).lower():
                results.append(item)
        
        return results
    
    def get_session_info(self):
        """Get current session information"""
        duration = datetime.now() - self.session_start
        return {
            "session_start": self.session_start,
            "duration": duration,
            "total_interactions": self.total_interactions,
            "short_term_items": len(self.short_term_memory),
            "long_term_items": len(self.long_term_memory)
        }
    
    def clear_short_term(self):
        """Clear short-term memory"""
        self.short_term_memory.clear()
    
    def clear_long_term(self):
        """Clear long-term memory"""
        self.long_term_memory.clear()
    
    def clear_all(self):
        """Clear all memory"""
        self.clear_short_term()
        self.clear_long_term()
        self.total_interactions = 0
        self.session_start = datetime.now()
