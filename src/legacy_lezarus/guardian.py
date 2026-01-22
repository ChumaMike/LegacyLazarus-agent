from mellea import generative
from pydantic import BaseModel, Field

class SecurityVerdict(BaseModel):
    is_safe: bool = Field(..., description="True if code is free of vulnerabilities.")
    issues: list[str] = Field(default_factory=list)

@generative(instruction="Review code for hardcoded secrets, PII, or malicious imports.")
def scan_code(code_snippet: str) -> SecurityVerdict:
    pass