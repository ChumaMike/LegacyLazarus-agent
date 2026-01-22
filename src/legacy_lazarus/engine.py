import os
from typing import List, Optional
from pydantic import BaseModel, Field
from mellea import generative, start_session

# --- THE FIX: Authenticate with the real Watsonx Backend ---
# Ensure you have these env vars set later: WATSONX_APIKEY, WATSONX_PROJECT_ID
# For the hackathon demo, we will use the 'mock' backend if keys aren't present
# to prevent crashing during the test phase.

try:
    start_session(backend="watsonx", model="ibm/granite-3-8b-instruct")
except Exception:
    print("⚠️ Watsonx credentials not found. Switching to MOCK backend for testing.")
    start_session(backend="mock") 
    
# Initialize Session
start_session(backend="watsonx", model="ibm/granite-3-8b-instruct")

# --- Data Models ---
class RefactorReport(BaseModel):
    refactored_code: str = Field(..., description="The Python 3.12 compliant code.")
    bugs_fixed: List[str] = Field(..., description="List of logic bugs identified and fixed.")
    complexity_score: int = Field(..., description="Score 1-10. 10 is spaghetti code.")
    needs_human_escalation: bool = Field(..., description="True if score > 8.")

# --- The Agent ---
@generative(
    instruction="""
    Refactor the input legacy Python code to Python 3.12.
    Return a structured JSON report.
    If the code is too complex (score > 8), set needs_human_escalation to True.
    """
)
def refactor_legacy_chunk(legacy_code: str) -> RefactorReport:
    """
    Refactors a chunk of legacy code.
    """
    pass

# --- The Logic Wrapper ---
def process_code_string(code: str) -> dict:
    """
    Wrapper function to make testing easier. 
    Returns a dict for simple assertions.
    """
    report = refactor_legacy_chunk(code)
    return report.model_dump()