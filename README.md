# Swift DocC Agent Skills Suite

A specialized collection of production-grade agent skills, authoring standards, boilerplate templates, and quality-gate tooling for building Apple-grade documentation and interactive tutorials with **Swift DocC**.

---

## Overview

Writing developer documentation that matches Apple's official documentation requires mastering multiple distinct disciplines:
1. **API Reference Architecture**: Precision in-source doc comments, documentation catalogs, topic curation, and symbol graphs.
2. **Interactive Tutorials**: Multi-chapter curriculum structures, synchronized step-by-step code diffs, and knowledge assessment directives.
3. **Apple Technical Writing Standards**: Down-to-earth pragmatic voice, the 3-Sentence Step Anatomy, prohibited vocabulary, and visual media guidelines.
4. **Publishing & Deployment**: CLI flags for static web hosting, live local development servers, and automated GitHub Pages workflows.
5. **Deterministic Quality Gates**: Algorithmic auditing to eliminate the Myers diff brace shift defect in compiled tutorial outputs.

This repository packages these disciplines into 4 modular agent skills, reusable templates, and an automated audit script.

---

## Directory Structure

```
swift-docc-skills/
├── LICENSE                                # Apache License 2.0
├── README.md                              # Comprehensive suite guide
├── justfile                               # Command runner targets (test, audit)
├── scripts/
│   └── audit-docc-highlights.py          # Myers diff brace shift auditor
├── skills/
│   ├── swift-docc-reference/              # Reference documentation skill
│   │   └── SKILL.md
│   ├── swift-docc-tutorials/              # Interactive tutorials skill
│   │   └── SKILL.md
│   ├── swift-docc-techwriting/            # Apple writing style standard skill
│   │   └── SKILL.md
│   └── swift-docc-publishing/             # Static export & hosting skill
│       └── SKILL.md
├── templates/
│   ├── reference/
│   │   └── PackageLandingPage.md          # Reference catalog landing page template
│   └── tutorials/
│       ├── TableOfContents.tutorial       # Curriculum TOC (@Tutorials) template
│       ├── StepByStep.tutorial            # Guided tutorial (@Tutorial) template
│       └── ConceptualArticle.article      # Conceptual guide (@Article) template
└── tests/
    └── test_audit_docc_highlights.py      # Unit tests for the audit script
```

---

## The 4 Skills

### 1. `swift-docc-reference`
Covers authoritative API reference documentation:
- **In-source doc comments**: Triple slash syntax (`///`), single-sentence summaries, parameter tags (`- Parameter:`, `- Parameters:`), return value tags (`- Returns:`), error tags (`- Throws:`), and callout blocks (`> Note:`, `> Important:`, `> Warning:`, `> Tip:`, `> Experiment:`).
- **Documentation Catalogs (`.docc`)**: Folder hierarchy, catalog placement inside target sources, and resource management.
- **Target Landing Pages**: Module headings with double backticks (`# ``TargetName```), executive overviews, and curated `## Topics`.
- **Symbol Linking & Disambiguation**: Cross-referencing types, properties, and methods using double backticks (` ``Coordinate/distance(to:unit:)`` `).
- **Symbol Graphs**: Extraction via `swift package dump-symbol-graph` and relationship synthesis.

### 2. `swift-docc-tutorials`
Covers the mechanics of interactive DocC tutorials:
- **Curriculum Architecture**: `@Tutorials` table of contents, `@Chapter`, `@TutorialReference`, and `@Resources` collections.
- **Interactive Pages**: `@Tutorial(time: ..., projectFiles: "...")`, `@Intro`, `@Section`, `@ContentAndMedia`, and `@Steps`.
- **Atomic Code Steps**: `@Step` pairing with `@Code(name: "...", file: "...")`, maintaining 1–5 lines diff discipline between code files.
- **Knowledge Assessments**: `@Assessments`, `@MultipleChoice`, `@Choice(isCorrect: ...)`, and `@Justification(reaction: "...")`.
- **Escape Hatches**: Resetting diff state with `@Code(..., reset: true)` or targeting specific ancestor versions with `previousFile: "..."`.

### 3. `swift-docc-techwriting`
Encodes the Apple technical writing philosophy and linguistic style:
- **The Empowering Guide Persona**: Warm, clear, collaborative, humble, and authoritative voice.
- **Anti-Grandiose Principle**: Explaining technical realities plainly; eliminating academic pretensions and marketing jargon.
- **The 3-Sentence Step Anatomy**:
  $$\text{Imperative Action} \longrightarrow \text{Context / Principle} \longrightarrow \text{Observable Feedback}$$
  *(Maximum 3 sentences per `@Step`)*.
- **Prohibited Vocabulary Index**: Ban on diminutives (*simply*, *just*, *easily*, *obviously*), marketing superlatives (*blazing-fast*, *revolutionary*, *magical*), and academic buzzwords (*epistemic*, *dichotomy*, *heuristics*).
- **Hero Image Standard**: Hero slots must exclusively feature running application screenshots or device mockups—never architectural diagrams or flowcharts.
- **Visual Safe Margins**: Minimum $\ge 32\text{px}$ safe padding around all text labels to prevent clipping.

### 4. `swift-docc-publishing`
Provides deployment workflows and compilation pipelines:
- **CLI Compilation Flags**: `--transform-for-static-hosting`, `--hosting-base-path <repo>`, and `--output-path <dir>`.
- **SwiftPM Integration**: Using `swift package generate-documentation` with `swift-docc-plugin`.
- **Local Live Development**: Preview server via `swift package --disable-sandbox preview-documentation`.
- **Static Artifact Previewing**: Local static testing via `python3 -m http.server`.
- **GitHub Actions CI/CD**: Ready-to-use `.github/workflows/documentation.yml` with automated deployment to GitHub Pages.

---

## The Myers Diff Highlight Auditor (`audit-docc-highlights.py`)

### The Problem
DocC computes code transitions between consecutive `@Code` steps using the Myers diff algorithm. Because Myers diff operates on raw text without Swift AST or lexical scope awareness, appending a new block ending with `}` directly after an existing scope ending with `}` produces an ambiguous edit graph.

The diff engine often matches the new closing brace to the previous scope's closing brace. This causes the highlight to **slide upward by one line**: the preceding closing brace is highlighted erroneously, and the actual new closing brace is left unhighlighted.

### The Quality Gate
The Python script `scripts/audit-docc-highlights.py` inspects static DocC tutorial JSON output, identifies contiguous highlight ranges, and flags any shifted closing braces:

```bash
# Run the audit against compiled static tutorial data
just audit
# or directly:
python3 scripts/audit-docc-highlights.py .build/docc-static/data/tutorials
```

### Remediation Rules
When a brace shift is detected:
1. **Rule of Prefix Stability**: Ensure no lines above the new code were modified or deleted between step $N$ and $N+1$.
2. **Intermediate Scope Anchoring**: Insert an empty blank line after the preceding scope's closing brace.
3. **Escape Hatches**: For significant refactors, use `@Code(..., reset: true)` or specify `previousFile:`.

---

## Boilerplate Templates

Jumpstart new documentation or tutorial projects using ready-to-fill templates in `templates/`:

- `templates/tutorials/TableOfContents.tutorial`: Complete `@Tutorials` curriculum landing page.
- `templates/tutorials/StepByStep.tutorial`: Complete `@Tutorial` step-by-step page with sections, steps, and assessments.
- `templates/tutorials/ConceptualArticle.article`: `@Article` page for architectural deep-dives.
- `templates/reference/PackageLandingPage.md`: Reference catalog landing page with topic curation.

---

## Testing & Quality Assurance

Run the test suite via `just`:

```bash
just test
```

This executes unit tests verifying:
- Comment stripping and closing brace detection.
- Contiguous highlight block extraction.
- Synthetic detection of clean vs shifted brace tutorial JSON outputs.
- Diagnostic context formatting.

---

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.
