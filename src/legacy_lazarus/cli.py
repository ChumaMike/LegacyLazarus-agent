import click
import os
from .engine import refactor_legacy_chunk
from .guardian import scan_code

@click.group()
def cli():
    """Legacy Lazarus CLI"""
    pass

@click.command()
@click.argument('filepath')
def revive(filepath):
    """Refactor a single file."""
    if not os.path.exists(filepath):
        click.echo("File not found!")
        return

    with open(filepath, 'r') as f:
        code = f.read()

    click.echo("🧠 Analyzing...")
    report = refactor_legacy_chunk(code)

    if report.needs_human_escalation:
        click.echo("⚠️  Too complex for AI. Escalating to human.")
    else:
        # Governance Check
        click.echo("🛡️  Guardian Scanning...")
        security = scan_code(report.refactored_code)
        
        if security.is_safe:
            new_path = filepath.replace(".py", "_v2.py")
            with open(new_path, 'w') as f:
                f.write(report.refactored_code)
            click.echo(f"✅ Saved to {new_path}")
        else:
            click.echo(f"❌ Security Risk Found: {security.issues}")

cli.add_command(revive)