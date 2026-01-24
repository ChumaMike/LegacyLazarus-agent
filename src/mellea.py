# src/mellea.py
# CORRECTION: This "Super Mock" handles both Refactoring and Security requests.

def generative(instruction=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            class MockResponse:
                def __init__(self):
                    # --- Refactoring Data ---
                    # In a real demo, we want to echo the user's input slightly changed
                    input_code = args[0] if args else "print('Hello')"
                    self.refactored_code = input_code.replace("print ", "print(").replace('"', "'") + ")" 
                    if not self.refactored_code.endswith("))"): 
                        # simple fix to avoid double brackets if input was already correct
                        self.refactored_code = self.refactored_code.replace("))", ")")
                    
                    self.bugs_fixed = ["Converted Python 2 print to Python 3", "Fixed syntax error"]
                    self.complexity_score = 2
                    self.needs_human_escalation = False
                    self.architect_notes = "Refactored successfully via Mock."

                    # --- Security Data (Guardian) ---
                    self.is_safe = True  # <--- THIS WAS MISSING
                    self.issues = []

                def model_dump(self):
                    return self.__dict__
            
            return MockResponse()
        return wrapper
    return decorator

def start_session(backend=None, model=None):
    print(f"⚡ [MOCK] Started Mellea Session: {backend}")

class MelleaSession:
    pass