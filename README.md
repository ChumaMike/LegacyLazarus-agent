# ⚰️ Legacy Lazarus — Raise the dead code

![Stack](https://img.shields.io/badge/stack-Python%20%7C%20LangChain%20%7C%20IBM%20Granite-blue)
![Status](https://img.shields.io/badge/status-prototype-success)

> A developer agent that autonomously refactors and documents cursed legacy code (old Python 2, spaghetti scripts, orphaned utilities) into clean, governed, Mellea-compliant code.

---

## The problem

Every real codebase has a graveyard: 2012 Python 2 scripts, a PHP cron that no one understands, a Perl one-liner labelled `DO NOT TOUCH`. The knowledge is gone, the author is gone, and nobody will pay to rewrite it. So it sits and rots until it breaks production.

Legacy Lazarus does the rewrite for you — with guardrails.

---

## How it works

1. **Ingest** — point the agent at a file, directory, or archive
2. **Comprehend** — IBM Granite reads the code, infers intent, flags dead branches
3. **Refactor** — the agent rewrites to modern idioms, keeping observable behaviour
4. **Document** — generates docstrings, a module-level README, and a "what changed and why" report
5. **Govern** — Mellea compliance checks ensure outputs meet organisational policy before commit

---

## Stack

| Component | Tech |
| :--- | :--- |
| Agent framework | LangChain · Mellea |
| Model | IBM Granite via watsonx.ai |
| Runtime | Chainlit (interactive UI) |
| CLI | Click |
| Validation | Pydantic |

---

## Quick start

```bash
git clone https://github.com/ChumaMike/LegacyLazarus-agent.git
cd LegacyLazarus-agent
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Configure
cp .env.example .env
# Set WATSONX_API_KEY, WATSONX_PROJECT_ID

# Interactive UI
chainlit run main.py

# Or CLI
python main.py refactor ./legacy_scripts/old_etl.py
```

---

## Tests

```bash
pytest
```

---

## 🗺️ Roadmap

- [ ] Multi-file refactor with dependency graph awareness
- [ ] JavaScript/TypeScript support (currently Python-only)
- [ ] GitHub App integration — run on PRs automatically
- [ ] Cost estimation before running on large codebases

---

## License

MIT · Built by [Chuma Meyiswa](https://github.com/ChumaMike)
