# src/mellea.py
# CORRECTION: This mock now properly stores instance variables for model_dump

def generative(instruction=None):
    """
    A dummy decorator that returns a Mock Object with real data.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Define the Mock Response Object
            class MockReport:
                def __init__(self):
                    # These must be instance variables (self.x) to show up in model_dump
                    self.refactored_code = "print('Hello World')"
                    self.bugs_fixed = ["Fixed print statement", "Updated to Python 3"]
                    self.complexity_score = 5
                    self.needs_human_escalation = False
                    self.architect_notes = "Fixed via Mock"

                def model_dump(self):
                    # Now this will return the dictionary of the variables above
                    return self.__dict__
            
            # Return an instance of the mock
            return MockReport()
        return wrapper
    return decorator

def start_session(backend=None, model=None):
    print(f"⚡ [MOCK] Started Mellea Session: {backend}")

class MelleaSession:
    pass