# Swift DocC agent skills

A collection of agent skills, authoring standards, starter templates, and audit tooling for writing documentation and interactive tutorials with **Swift DocC**.

---

## Overview

Writing clear documentation with Swift DocC involves several key areas:
1. **API reference**: In-source doc comments, documentation catalogs, topic curation, and symbol graphs.
2. **Interactive tutorials**: Multi-chapter curriculum structures, the micro-prototype pattern, 3–5 step sections, compilable starter/finisher engineering contracts, and assessment directives.
3. **Technical writing style**: Strict sentence case editorial standard, down-to-earth pragmatic voice, the 3-Sentence Step Anatomy, prohibited vocabulary, and visual media guidelines.
4. **Vector diagram design**: Cupertino technical palette, defensive 10px bounding-box sizing, base-anchored SVG marker mechanics, breathing-room spacing, and dark mode asset pairing.
5. **Publishing and deployment**: CLI flags for static web hosting, live local development servers, and automated GitHub Pages workflows.
6. **Highlight auditing**: Detecting and remediating Myers diff brace shift issues in compiled tutorial outputs.

This repository organizes these practices into 5 agent skills, starter templates, and an audit script.

---

## Directory structure

```
swift-docc-skills/
├── LICENSE                                # Apache License 2.0
├── README.md                              # Comprehensive suite guide
├── justfile                               # Command runner targets (test, audit)
├── scripts/
│   └── audit-docc-highlights.py          # Myers diff brace shift auditor
├── skills/
│   ├── swift-docc-reference/              # Reference documentation skill
│   │   ├── SKILL.md
│   │   └── references/                    # In-source doc comments, symbol curation & extensions
│   ├── swift-docc-tutorials/              # Interactive tutorials skill
│   │   ├── SKILL.md
│   │   └── references/                    # Pedagogical patterns, Myers diffs, directives catalog
│   ├── swift-docc-techwriting/            # Apple writing style standard skill
│   │   ├── SKILL.md
│   │   └── references/                    # Sentence case guide, step anatomy, UI terms
│   ├── swift-docc-diagrams/               # Vector diagram design system skill
│   │   ├── SKILL.md
│   │   └── references/                    # Marker mechanics, topologies, typography & bounding boxes
│   └── swift-docc-publishing/             # Static export & hosting skill
│       ├── SKILL.md
│       └── references/                    # Static hosting, CLI flags & GitHub Actions CI/CD
├── templates/
│   ├── reference/
│   │   └── PackageLandingPage.md          # Reference catalog landing page template
│   └── tutorials/
│       ├── TableOfContents.tutorial       # Curriculum TOC (@Tutorials) template
│       ├── StepByStep.tutorial            # Interactive tutorial (@Tutorial) template
│       ├── MicroPrototype.tutorial        # Rapid 5-minute single-file prototype template
│       ├── ConceptualArticle.article      # Conceptual guide (@Article) template
│       ├── WrapUp.article                 # Milestone conclusion article template
│       └── DiagramTemplate.svg            # Cupertino-grade SVG vector diagram template
└── tests/
    └── test_audit_docc_highlights.py      # Unit tests for the audit script
```

---

## The Xcode agent skills ecosystem

Xcode 16 and subsequent releases bundle official coding agent skills authored by Apple engineers. You can inspect or export these built-in agent skills using the Xcode developer tools:

```bash
# Export Apple's built-in coding agent skills to a local directory
xcrun agent skills export --output-dir /path/to/exported-skills
```

### The Apple built-in skills vs. DocC gap

When exported, Xcode provides 10 specialized agent skills:
- `swiftui-specialist` & `swiftui-whats-new-27`: SwiftUI best practices, view lifecycle, `@Observable`, and modern iOS 26/27 APIs.
- `app-intents-specialist` & `app-intents-whats-new-27`: App Intents execution models, entities, queries, and assistant integration.
- `c-bounds-safety` & `adopt-c-bounds-safety`: The `-fbounds-safety` C language extension and buffer hardening.
- `accessibility`: Auditing and remediation for WCAG and accessibility APIs.
- `modernize-tests` / `test-modernizer`: Migration from XCTest to Swift Testing.
- `building-document-based-swiftui-applications`: Modern `Document` protocol architecture.
- `uikit-app-modernization` & `app-resizability`: Multi-window adaptivity, Stage Manager, and foldable displays.

Crucially, **Xcode exports zero skills for Swift DocC, documentation authoring, or interactive tutorial engineering**.

The `swift-docc-skills` repository fills this critical gap as the authoritative developer suite for DocC documentation and tutorial engineering, completing the modern Apple developer toolchain for AI coding agents and human engineers alike.

---

## The five skills

### 1. `swift-docc-reference`
Covers API reference documentation:
- **In-source doc comments**: Triple slash syntax (`///`), single-sentence summaries, parameter tags (`- Parameter:`, `- Parameters:`), return value tags (`- Returns:`), error tags (`- Throws:`), and callout blocks (`> Note:`, `> Important:`, `> Warning:`, `> Tip:`, `> Experiment:`).
- **Documentation catalogs (`.docc`)**: Folder hierarchy, catalog placement inside target sources, and resource management.
- **Target landing pages**: Module headings with double backticks (`# ``TargetName```), executive overviews, and curated `## Topics`.
- **Symbol linking and disambiguation**: Cross-referencing types, properties, and methods using double backticks (` ``Coordinate/distance(to:unit:)`` `).
- **Symbol graphs**: Extraction via `swift package dump-symbol-graph` and relationship synthesis.
- **Xcode agent skills ecosystem**: Export mechanics via `xcrun agent skills export` and bridging the DocC skill gap.

### 2. `swift-docc-tutorials`
Covers the mechanics of interactive DocC tutorials:
- **Pedagogical patterns**: The micro-prototype pattern (two-tier progression from a rapid 5-minute single-file prototype to modular architecture), the 3–5 step section rule for cognitive load control, and dedicated wrap-up pages.
- **Compilable starter and finisher contract**: Zero-dependency starter rule (0 errors, 0 warnings), strict 1:1 diff contract ($\text{Finisher} \equiv \text{Starter} + \sum \text{Steps}$), no magic code, and automated CI checkpoint validation.
- **Curriculum architecture**: `@Tutorials` table of contents, `@Chapter`, `@TutorialReference`, and `@Resources` collections.
- **Interactive pages**: `@Tutorial(time: ..., projectFiles: "...")`, `@Intro`, `@Section`, `@ContentAndMedia`, and `@Steps`.
- **Atomic code steps**: `@Step` pairing with `@Code(name: "...", file: "...")`, maintaining 1–5 lines diff discipline between code files.
- **Knowledge assessments**: `@Assessments`, `@MultipleChoice`, `@Choice(isCorrect: ...)`, and `@Justification(reaction: "...")`.
- **Escape hatches**: Resetting diff state with `@Code(..., reset: true)` or targeting specific ancestor versions with `previousFile: "..."`.

### 3. `swift-docc-techwriting`
Encodes the Apple technical writing philosophy and linguistic style:
- **Strict sentence case editorial standard**: Mandatory sentence case across all headings (`#`, `##`, `###`), tutorial titles, section names, table headers, and diagrams (strictly prohibiting Title Case).
- **The Empowering Guide persona**: Warm, clear, collaborative, humble, and direct voice.
- **Anti-grandiose principle**: Explaining technical realities plainly; eliminating academic pretensions and marketing jargon.
- **The 3-Sentence Step Anatomy**:
  $$\text{Imperative Action} \longrightarrow \text{Context / Principle} \longrightarrow \text{Observable Feedback}$$
  *(Maximum 3 sentences per `@Step`)*.
- **Prohibited vocabulary index**: Ban on diminutives (*simply*, *just*, *easily*, *obviously*), marketing superlatives (*blazing-fast*, *revolutionary*, *magical*), and academic buzzwords (*epistemic*, *dichotomy*, *heuristics*).
- **Hero image standard**: Hero slots must feature running application screenshots or device mockups—never architectural diagrams or flowcharts.
- **Visual safe margins**: Minimum $\ge 32\text{px}$ safe padding around all text labels to prevent clipping.

### 4. `swift-docc-diagrams`
Codifies Apple-grade vector diagram design and SVG engineering:
- **Defensive bounding-box sizing (The 10px rule)**: $\text{rectWidth} = (\text{maxLineCharacters} \times 10) + 32\text{px}$ to prevent text overflow across varying system font engines.
- **Cupertino technical color palette**: 90% monochromatic neutral scaffolding (`#F5F5F7` cards, `#E5E5EA` borders, `#1D1D1F` text) and a single purposeful hero accent (`#0071E3`), banning noisy pastels.
- **Anti-protrusion marker mechanics**: Base-anchored markers (`refX="2"`, `markerUnits="userSpaceOnUse"`) eliminating stroke caps protruding through sharp arrowhead tips.
- **Breathing-room gaps**: 10px–12px spacing from source and target containers with direction-aware coordinate formulas.
- **Continuous rounded corners**: Presentation attributes (`rx`/`ry`) directly on `<rect>` elements for WebKit compatibility.
- **Standard topologies**: Linear processing pipelines, tree branching, bidirectional feedback loops, and device wireframes.
- **Dark mode asset pairing**: Automatic theme switching with `diagram.svg` and `diagram~dark.svg`.

### 5. `swift-docc-publishing`
Provides deployment workflows and compilation pipelines:
- **CLI compilation flags**: `--transform-for-static-hosting`, `--hosting-base-path <repo>`, and `--output-path <dir>`.
- **SwiftPM integration**: Using `swift package generate-documentation` with `swift-docc-plugin`.
- **Local live development**: Preview server via `swift package --disable-sandbox preview-documentation`.
- **Static artifact previewing**: Local static testing via `python3 -m http.server`.
- **GitHub Actions CI/CD**: Ready-to-use `.github/workflows/documentation.yml` with automated deployment to GitHub Pages.

---

## The Myers diff highlight auditor (`audit-docc-highlights.py`)

### The problem
DocC computes code transitions between consecutive `@Code` steps using the Myers diff algorithm. Because Myers diff operates on raw text without Swift AST or lexical scope awareness, appending a new block ending with `}` directly after an existing scope ending with `}` produces an ambiguous edit graph.

The diff engine often matches the new closing brace to the previous scope's closing brace. This causes the highlight to **slide upward by one line**: the preceding closing brace is highlighted erroneously, and the actual new closing brace is left unhighlighted.

### The highlight auditor
The Python script `scripts/audit-docc-highlights.py` inspects static DocC tutorial JSON output, identifies contiguous highlight ranges, and flags any shifted closing braces:

```bash
# Compile static DocC documentation (using swift-docc-plugin)
just docc <TargetName>

# Run the audit against compiled static tutorial data
just audit
# or directly:
python3 scripts/audit-docc-highlights.py .build/docc-static/data/tutorials
```

### Remediation rules
When a brace shift is detected:
1. **Rule of prefix stability**: Ensure no lines above the new code were modified or deleted between step $N$ and $N+1$.
2. **Intermediate scope anchoring**: Insert an empty blank line after the preceding scope's closing brace.
3. **Escape hatches**: For significant refactors, use `@Code(..., reset: true)` or specify `previousFile:`.

---

## Starter templates

Templates to start new documentation or tutorial pages in `templates/`:

- `templates/tutorials/TableOfContents.tutorial`: `@Tutorials` curriculum landing page.
- `templates/tutorials/StepByStep.tutorial`: `@Tutorial` step-by-step page with sections, steps, and assessments.
- `templates/tutorials/MicroPrototype.tutorial`: Rapid single-file concept prototype tutorial page adhering to the 3–5 step rule.
- `templates/tutorials/ConceptualArticle.article`: `@Article` page for conceptual topics.
- `templates/tutorials/WrapUp.article`: Milestone conclusion article celebrating progress and curating next-step resources.
- `templates/tutorials/DiagramTemplate.svg`: Cupertino-grade SVG vector diagram template adhering to the 10px rule.
- `templates/reference/PackageLandingPage.md`: Reference catalog landing page with topic curation.

---

## Testing

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
