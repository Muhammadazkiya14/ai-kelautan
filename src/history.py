class ConversationHistory:
    def __init__(self, max_turns=20):
        self.messages = []
        self.max_turns = max_turns

    def add_user(self, message):
        self.messages.append({"role": "user", "content": message})
        self._trim()

    def add_assistant(self, message):
        self.messages.append({"role": "assistant", "content": message})
        self._trim()

    def get_messages(self):
        return self.messages.copy()

    def _trim(self):
        if len(self.messages) > self.max_turns * 2:
            self.messages = self.messages[-self.max_turns * 2:]

    def clear(self):
        self.messages = []
