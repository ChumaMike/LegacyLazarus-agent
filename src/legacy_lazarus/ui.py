import chainlit as cl
from legacy_lazarus.engine import refactor_legacy_chunk
from legacy_lazarus.guardian import scan_code

# --- IBM CARBON THEME CONFIGURATION ---
# We force the UI to look like IBM's native "Carbon" Design System
# (Dark Mode, Crisp Tyopgraphy, Blue Accents)
@cl.on_chat_start
async def start():
    await cl.Message(
        content="**Legacy Lazarus Enterprise**\n\nSystem Online. \nTarget: Legacy Codebase Refactoring.\nGuardian: Active.",
        author="System"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    # 1. VISUALIZE THE THINKING PROCESS (The "Glass Box")
    # This creates a spinner in the UI showing "AI is thinking..."
    async with cl.Step(name="Mellea Architect", type="run") as step:
        step.input = message.content
        
        # Call your actual AI engine
        report = refactor_legacy_chunk(message.content)
        
        # Show the raw logic to the user (Transparency)
        step.output = f"Complexity Score: {report.complexity_score}/10"

    # 2. GOVERNANCE CHECK (The "Trust" Layer)
    if report.needs_human_escalation:
        await cl.Message(
            content=f"⚠️ **Escalation Triggered**\n\nReason: Complexity Score {report.complexity_score} exceeds safety threshold.\n\n*Forwarding to Senior Engineer...*",
            author="Governance Bot"
        ).send()
        return

    # 3. GUARDIAN SECURITY SCAN
    async with cl.Step(name="Granite Guardian", type="tool") as guardian_step:
        guardian_step.input = "Scanning for Vulnerabilities..."
        
        security = scan_code(report.refactored_code)
        
        if security.is_safe:
            guardian_step.output = "✅ No CVEs or PII detected."
        else:
            guardian_step.output = f"❌ THREAT DETECTED: {security.issues}"
            await cl.Message(content="🚫 **Refactor Rejected by Policy**", author="Guardian").send()
            return

    # 4. FINAL DELIVERABLE
    # Display the code in a nice syntax-highlighted block
    await cl.Message(
        content=f"### Refactoring Complete\n\n```python\n{report.refactored_code}\n```\n\n**Changelog:**\n" + "\n".join([f"- {bug}" for bug in report.bugs_fixed]),
        author="Lazarus Agent"
    ).send()