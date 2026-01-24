def generative(instruction=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            class MockResponse:
                def __init__(self):
                    input_code = args[0] if args else ""
                    
                    # SCENARIO 1: COMPLEXITY TRIGGER
                    if "urllib2" in input_code or "complex" in input_code:
                        self.refactored_code = (
                            "import requests  # Replaced deprecated urllib2\n"
                            "def fetch_data(url):\n"
                            "    try:\n"
                            "        # Added timeout to prevent hanging (Resiliency)\n"
                            "        response = requests.get(url, timeout=10)\n"
                            "        response.raise_for_status()\n"
                            "        return response.json()\n"
                            "    except requests.exceptions.RequestException as e:\n"
                            "        # Added proper error logging\n"
                            "        print(f'Critical Error: {e}')\n"
                            "        return None"
                        )
                        self.bugs_fixed = [
                            "CRITICAL: Replaced deprecated 'urllib2' with 'requests'",
                            "SECURITY: Added timeout to prevent DOS attacks",
                            "STABILITY: Added try/except error handling"
                        ]
                        self.complexity_score = 7 # High but handled
                        self.needs_human_escalation = False
                        self.architect_notes = "Refactoring required library migration. Validated security headers."
                    
                    # SCENARIO 2: SIMPLE TRIGGER
                    else:
                        self.refactored_code = input_code.replace("print ", "print(").replace('"', "'") + ")"
                        if not self.refactored_code.endswith("))"):
                             self.refactored_code = self.refactored_code.replace("))", ")")
                        self.bugs_fixed = ["Syntax: Python 3 Print Statement"]
                        self.complexity_score = 2
                        self.needs_human_escalation = False
                        self.architect_notes = "Simple syntax translation."

                    # --- Security Data ---
                    self.is_safe = True
                    self.issues = []

                def model_dump(self):
                    return self.__dict__
            return MockResponse()
        return wrapper
    return decorator