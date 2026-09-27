---
name: swift-docc-techwriting
license: Apache-2.0
description: >-
  The Apple documentation style standard: down-to-earth pragmatic voice, anti-grandiose principle,
  3-Sentence Step Anatomy, prohibited vocabulary index, hero image standards, and visual safe margins.
  Use when reviewing or writing technical documentation, checking step structure, auditing vocabulary,
  or polishing tutorial prose to match Apple standards.
metadata:
  author: peterfriese
  version: "0.1.0"
---

# Apple Documentation Tech Writing Style Standard

This skill establishes the writing voice, linguistic rhythm, sentence construction, vocabulary prohibitions, and visual media guidelines required to author technical documentation and tutorials that mirror Apple's official documentation.

---

## 1. The Apple Pedagogical Voice & Tone

Apple documentation never reads like academic whitepapers, promotional press releases, or informal blog posts. It speaks with the voice of **The Empowering Guide**: warm, clear, calm, collaborative, humble, and authoritative.

```
               ┌────────────────────────────────────────────────────────┐
               │                THE EMPOWERING GUIDE                    │
               │  Warm • Clear • Collaborative • Humble • Authoritative  │
               └───────────────────────────┬────────────────────────────┘
                                           │
         ┌─────────────────────────────────┴─────────────────────────────────┐
         ▼                                                                   ▼
┌───────────────────────────────┐                   ┌─────────────────────────────────┐
│     DIRECT SECOND PERSON      │                   │    ANTI-GRANDIOSE PRINCIPLE     │
│  "You", "You'll", "In this..."│                   │  Pragmatic, concrete, direct    │
│  Never passive or 3rd-person  │                   │  Zero academic or pompous jargon│
└───────────────────────────────┘                   └─────────────────────────────────┘
```

### The Anti-Grandiose Principle

- **State what the code does; do not preach.**
- Never inflate simple engineering tasks with pretentious, self-important phrasing.
- Explain technical realities plainly. Readers are intelligent professionals seeking clarity, not an academic symposium or marketing pitch.

| ❌ Grandiose / Pretentious Phrasing | ✅ Apple Down-to-Earth Voice |
| :--- | :--- |
| *"This foundational paradigm encapsulates the epistemic duality of state synchronization."* | *"When the state changes, the view updates automatically to display the latest value."* |
| *"We orchestrate a multi-layered architectural abstraction over persistent data stores."* | *"The repository manages saving and loading records from disk."* |
| *"Leveraging cutting-edge heuristics, this method yields optimal computational throughput."* | *"This method caches calculations to avoid redundant computations."* |

---

## 2. Direct Address & Person

Always write in the **direct second person**:
- Address the reader directly as **"you"** or **"you'll"**.
- Never refer to the reader as *"the user"*, *"the developer"*, or *"the programmer"*.
- Never use the passive voice to avoid naming the actor.
- Never use the universal first-person plural (*"now we will write our code"*).

```markdown
<!-- ❌ Passive Voice -->
A new view model is initialized and bound to the navigation controller.

<!-- ❌ Detached Third Person -->
The developer should select ContentView.swift and add the modifier.

<!-- ❌ We / Us -->
Now let's create our list together.

<!-- ✅ Apple Standard (Direct Second Person) -->
In the Project navigator, select `ContentView.swift`.

Add the `padding()` modifier to inset the view's content from the screen edges.
```

---

## 3. The 3-Sentence Step Anatomy

Every `@Step` in an interactive tutorial must adhere to the **3-Sentence Anatomy**:

$$\text{Sentence 1: Imperative Action} \longrightarrow \text{Sentence 2: Context / Principle} \longrightarrow \text{Sentence 3: Observable Feedback}$$

| Sentence | Function | Objective | Example |
| :--- | :--- | :--- | :--- |
| **Sentence 1** | **Imperative Action** | Exact physical or navigational instruction with explicit UI coordinates and verbs. | *"In the Project navigator, select `LandmarkList.swift`."* |
| **Sentence 2** | **Principle / Context** | Single sentence explaining *why* or what this construct represents. | *"Lists organize data into scrollable rows and adapt to system dynamics like dark mode."* |
| **Sentence 3** | **Observable Feedback** | What the learner observes or what updates on the canvas/simulator. | *"The canvas preview updates immediately to display sample landmarks in a vertical list."* |

### Strict Step Length Rule
- A step consists of **1 to 3 sentences maximum**.
- Never write paragraphs, multi-step compound instructions, or conceptual treatises inside a `@Step`.
- If a concept requires deep explanation, place it in an accompanying `@Article` or the section's `@ContentAndMedia` overview.

---

## 4. Prohibited Vocabulary Index

To preserve Apple's signature polish and avoid condescending or bloated language, strictly eliminate three categories of words:

```
┌───────────────────────────────────────────────────────────────────────────┐
│                       STRICTLY PROHIBITED VOCABULARY                      │
├─────────────────────────────┬─────────────────────────────┬───────────────┤
│    ❌ Diminutives           │    ❌ Marketing Superlatives│ ❌ Academic   │
├─────────────────────────────┼─────────────────────────────┼───────────────┤
│ • simply                    │ • blazing-fast              │ • epistemic   │
│ • just                      │ • revolutionary             │ • paradigm    │
│ • easily                    │ • magical                   │ • dichotomy   │
│ • obviously                 │ • game-changing             │ • ontological │
│ • clearly                   │ • cutting-edge              │ • heuristics  │
│ • trivial                   │ • seamless                  │ • logits      │
│ • naturally                 │ • powerhouse                │ • synergetic  │
└─────────────────────────────┴─────────────────────────────┴───────────────┘
```

### Why Diminutives Are Forbidden
Words like *simply*, *just*, and *obviously* alienate readers. If an engineer is stuck or encountering an unfamiliar pattern, telling them to *"simply configure the delegate"* is patronizing and unhelpful.

### Prohibited Meta-Narration
Never describe the act of writing the tutorial itself:
- ❌ *"In this step, we will..."*
- ❌ *"As we saw in the previous section..."*
- ❌ *"Now that you've done that, let's move on to..."*
- ✅ Jump straight into the action: *"Embed the landmark title in an `HStack`."*

---

## 5. Visual Media Standards

Visual assets anchor the learner in reality. Low-quality, abstract, or clipped graphics undermine the authoritative tone of Apple documentation.

### The Hero Image Standard

```
┌───────────────────────────────────────────────────────────────────────────┐
│                           HERO IMAGE CRITERIA                             │
├─────────────────────────────────────┬─────────────────────────────────────┤
│             ✅ ALLOWED              │             ❌ FORBIDDEN            │
├─────────────────────────────────────┼─────────────────────────────────────┤
│ • High-resolution device mockup     │ • Architecture diagrams             │
│ • Running app screenshot on device  │ • Flowcharts and sequence diagrams  │
│ • Polished component preview render │ • Abstract shapes or icons          │
│ • Realistic photo of physical setup │ • Low-contrast wireframe sketches   │
└─────────────────────────────────────┴─────────────────────────────────────┘
```

> [!IMPORTANT]
> **Hero Slot Requirement**: Hero images (`@Intro` and `@Tutorials` hero banners) must **always** display the **running application or real device mockup**. Never place architectural flowcharts, entity diagrams, or raw text blocks into a hero image slot. Reserve diagrams exclusively for `@Section` `@ContentAndMedia` or conceptual `@Article` pages.

### Visual Safe Margins (The 32px Rule)

When authoring screenshots, UI mockups, or diagrams:
- **Maintain a minimum of $\ge 32\text{px}$ safe margin** around all text labels, badges, and callout boxes within the graphic.
- Never let UI labels touch or get clipped by canvas borders, device bezels, or image edges.
- Provide `@2x` assets with crisp retina resolution (e.g., `hero-mailtriage@2x.png`).
- Ensure high contrast in both Light and Dark appearances.

---

## 6. Official Apple Interface Terminology

Always use exact Apple capitalization and nomenclature for IDE controls and system UI:

| Correct Apple Term | Incorrect Variation |
| :--- | :--- |
| **Project navigator** | Project explorer, file tree, sidebar |
| **Canvas** | Preview pane, simulator view |
| **Attributes inspector** | Properties panel, attribute tab |
| **Library** | Object catalog, component palette |
| **Scheme menu** | Target dropdown, build selector |
| **Debug bar** | Console controls, runtime tray |
| **Dynamic Type** | System font scaling |
| **Control Center** | Control pane |

---

## 7. Style & Polish Review Checklist

- [ ] Written entirely in direct second person (*"you"*, *"you'll"*).
- [ ] Zero passive constructions (*"is created"*, *"are called"*).
- [ ] Anti-grandiose principle respected: zero academic jargon or inflated claims.
- [ ] All `@Step` directives follow the 3-Sentence Anatomy (Action $\to$ Context $\to$ Feedback).
- [ ] No prohibited diminutives (*simply*, *just*, *obviously*, *easily*).
- [ ] No marketing superlatives (*blazing-fast*, *revolutionary*, *magical*).
- [ ] Hero images exclusively feature running app screenshots or device mockups.
- [ ] All graphical assets have $\ge 32\text{px}$ safe margins around text labels.
- [ ] Official Xcode UI terms used with proper capitalization (*Project navigator*, *Canvas*).
