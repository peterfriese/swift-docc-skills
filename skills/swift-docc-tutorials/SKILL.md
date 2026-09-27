---
name: swift-docc-tutorials
license: Apache-2.0
description: >-
  Authoritative guide and syntax specification for authoring interactive DocC tutorials,
  multi-chapter curricula, step-by-step code walkthroughs, and knowledge assessments.
  Use when authoring @Tutorials, @Tutorial, @Article pages, defining @Code steps, or
  preventing Myers diff code highlight shifts.
metadata:
  author: peterfriese
  version: "1.0.0"
---

# Swift DocC Interactive Tutorials

DocC interactive tutorials provide multi-page, step-by-step interactive learning experiences with synchronized code diffs, canvas media, and interactive knowledge checks—identical to Apple's official tutorials (*SwiftUI Tutorials*, *SwiftData Essentials*).

---

## 1. Directory Structure & File Hierarchy

DocC tutorials must be placed inside a `.docc` documentation catalog adhering to this exact directory hierarchy:

```
Sources/MyTarget/
└── MyTarget.docc/
    ├── MyTarget.md                            # Reference landing page
    ├── Tutorials/
    │   ├── MyCurriculum.tutorial              # Table of Contents (@Tutorials root)
    │   ├── 01-Essentials/
    │   │   ├── 01-CreatingViews.tutorial      # Interactive step-by-step (@Tutorial)
    │   │   └── 02-HandlingState.tutorial
    │   └── 02-Advanced/
    │       ├── 01-CustomLayouts.tutorial
    │       └── 02-DataFlow.article            # Conceptual tutorial article
    └── Resources/
        ├── code/                              # Incremental code listings (.swift)
        │   ├── 01-view-step1.swift
        │   ├── 01-view-step2.swift
        │   └── 01-view-step3.swift
        ├── images/                            # Hero images and canvas previews
        │   ├── hero-essentials@2x.png
        │   ├── canvas-step1@2x.png
        │   └── canvas-step2@2x.png
        └── downloads/                         # Starter / Finisher archives
            ├── Essentials-Starter.zip
            └── Essentials-Finisher.zip
```

---

## 2. Directive Architecture & Nesting Tree

DocC enforces strict parent-child relationships between directives. Violating these nesting hierarchies produces compilation errors.

### The Curriculum Tree (`@Tutorials`)

```
@Tutorials(name: "...")                 [Root directive for the curriculum]
├── @Intro(title: "...")                [Required: Overview banner & hero image]
│   └── @Image(source: "...", alt: "...")
├── @Volume(name: "...")                [Optional: Groups chapters into volumes]
├── @Chapter(name: "...")               [Required: 1 or more chapters]
│   ├── @Image(source: "...", alt: "...")
│   ├── @TutorialReference(tutorial: "...")  [Links to @Tutorial or @Article]
│   └── @TutorialReference(...)
└── @Resources                          [Required: Resource collection footer]
    ├── @Downloads(destination: "...")
    ├── @Documentation(destination: "...")
    ├── @SampleCode(destination: "...")
    ├── @Videos(destination: "...")
    └── @Forums(destination: "...")
```

### The Interactive Page Tree (`@Tutorial`)

```
@Tutorial(time: <minutes>, projectFiles: "...")  [Root directive for step-by-step tutorial]
├── @XcodeRequirement(title: "...", destination: "...") [Optional requirement notice]
├── @Intro(title: "...")                        [Required: Hero introduction]
│   ├── @Image(source: "...", alt: "...")
│   └── @Video(source: "...", poster: "...")    [Alternative to @Image]
├── @Section(title: "...")                      [Required: 1 or more task sections]
│   ├── @ContentAndMedia                        [Required: Conceptual section overview]
│   │   └── @Image(source: "...", alt: "...")
│   ├── @Steps                                  [Required: Ordered list of steps]
│   │   ├── @Step                               [Individual instruction step]
│   │   │   ├── @Code(name: "...", file: "...") [Synchronized code diff]
│   │   │   ├── @Image(source: "...", alt: "...")
│   │   │   └── @Video(source: "...", poster: "...")
│   │   └── @Step
│   └── @Stack                                  [Alternative 2-column layout]
└── @Assessments                                [Required: Knowledge checks]
    └── @MultipleChoice                         [1 or more questions]
        ├── Question markdown text
        ├── @Choice(isCorrect: true)
        │   ├── Choice text
        │   └── @Justification(reaction: "...")
        └── @Choice(isCorrect: false)
            ├── Choice text
            └── @Justification(reaction: "...")
```

### The Conceptual Article Tree (`@Article`)

```
@Article(time: <minutes>)                       [Root directive for conceptual tutorial article]
├── @Intro(title: "...")                        [Required: Hero introduction & overview banner]
│   ├── @Image(source: "...", alt: "...")
│   └── @Video(source: "...", poster: "...")
├── @ContentAndMedia                            [1 or more conceptual overview blocks]
│   └── @Image(source: "...", alt: "...")
├── @Stack                                      [Optional horizontal multi-column container]
│   ├── @ContentAndMedia                        [1 to 3 columns required inside @Stack]
│   │   └── @Image(source: "...", alt: "...")
│   └── @ContentAndMedia
│       └── @Image(source: "...", alt: "...")
└── @Assessments                                [Optional knowledge checks]
    └── @MultipleChoice
```

---

## 3. Directives Reference

### `@Tutorials` (Table of Contents)

Defines the landing page for your tutorial curriculum.

```markdown
@Tutorials(name: "PhotoJournal Essentials") {
    @Intro(title: "Building PhotoJournal") {
        Learn how to craft a modern, responsive photo journaling app for iOS and macOS.
        You'll start by building views, wire them to SwiftData persistence, and finish
        with interactive animations.

        @Image(source: "hero-photojournal.png", alt: "PhotoJournal running on an iPhone display.")
    }

    @Chapter(name: "Layout and Views") {
        Create the core visual building blocks and compose dynamic lists.

        @Image(source: "chapter-layout.png", alt: "An iPad screen showing a grid of photos.")

        @TutorialReference(tutorial: "doc:01-CreatingViews")
        @TutorialReference(tutorial: "doc:02-BuildingLists")
    }

    @Resources {
        Explore developer guides, complete project downloads, and community forums.

        @Downloads(destination: "downloads/PhotoJournal-Starter.zip") {
            Download starter and completed Xcode project bundles.

            - [PhotoJournal Starter Project](downloads/PhotoJournal-Starter.zip)
            - [PhotoJournal Completed Project](downloads/PhotoJournal-Finisher.zip)
        }

        @Documentation(destination: "https://developer.apple.com/documentation/swiftui") {
            Browse official Apple documentation for SwiftUI and SwiftData:

            - [SwiftUI Documentation](https://developer.apple.com/documentation/swiftui)
            - [SwiftData Documentation](https://developer.apple.com/documentation/swiftdata)
        }
    }
}
```

### `@Tutorial` (Step-by-Step Tutorial Page)

Defines an individual tutorial page with step-by-step instructions.

- `time`: Estimated completion time in minutes (integer, e.g., `time: 20`).
- `projectFiles`: Name of the starter ZIP archive located in `Resources/downloads/`.

```markdown
@Tutorial(time: 15, projectFiles: "PhotoJournal-Starter.zip") {
    @XcodeRequirement(title: "Xcode 16.0+", destination: "https://developer.apple.com/xcode/")

    @Intro(title: "Creating a Photo Card") {
        Build a reusable photo card view that displays a formatted image, title caption,
        and date stamp.

        @Image(source: "hero-photocard.png", alt: "The finished PhotoCard component.")
    }

    @Section(title: "Assemble the Card Layout") {
        @ContentAndMedia {
            Photo cards display an image framed with a rounded border and overlaid metadata.
            In this section, you’ll construct the component using SwiftUI layout stacks.

            @Image(source: "section-layout.png", alt: "A wireframe diagram of the card view.")
        }

        @Steps {
            @Step {
                In the Project navigator, create a new SwiftUI view file named `PhotoCard.swift`.

                SwiftUI files declare a `View` structure and a `#Preview` block.

                The canvas renders an initial preview displaying a placeholder text view.

                @Code(name: "PhotoCard.swift", file: "01-card-step1.swift")
            }

            @Step {
                Replace the default `Text` view with an `Image` view that loads the cover photo.

                Image views display bitmap assets stored in your asset catalog using asset name identifiers.

                The canvas preview updates immediately to render the unclipped photo.

                @Code(name: "PhotoCard.swift", file: "01-card-step2.swift")
            }

            @Step {
                Apply the `clipShape(_:)` modifier to give the image rounded corners.

                Clipping constrains the view's rendered bounds without modifying the underlying asset geometry.

                The image corners smooth into uniform rounded edges in the preview.

                @Code(name: "PhotoCard.swift", file: "01-card-step3.swift")
            }
        }
    }

    @Assessments {
        @MultipleChoice {
            Which layout container places child views along a horizontal axis?

            @Choice(isCorrect: true) {
                `HStack`

                @Justification(reaction: "Correct!") {
                    `HStack` arranges views horizontally in a line from leading to trailing.
                }
            }

            @Choice(isCorrect: false) {
                `VStack`

                @Justification(reaction: "Try again.") {
                    `VStack` arranges views vertically in a column from top to bottom.
                }
            }

            @Choice(isCorrect: false) {
                `ZStack`

                @Justification(reaction: "Try again.") {
                    `ZStack` overlays views on top of each other along the z-axis.
                }
            }
        }
    }
}
```

---

## 4. Code Directives & Myers Diff Mechanics

### `@Code` Directives and Parameters

- `name`: Display name shown in the interactive editor header tab (e.g., `"ContentView.swift"`).
- `file`: Path relative to `Resources/code/` (e.g., `"01-card-step1.swift"`).
- `reset`: Set to `true` (`reset: true`) to render the full file fresh without calculating an incremental diff against the previous step.
- `previousFile`: Explicitly names the predecessor file against which DocC computes the diff (e.g., `previousFile: "01-card-step1.swift"`).

### How DocC Diffing Works

Between Step $N$ (`fileA.swift`) and Step $N+1$ (`fileB.swift`), DocC executes a Myers diff:
1. Lines identified as insertions are highlighted in yellow/green in the tutorial viewer.
2. Unchanged lines remain neutral.
3. The reader sees a clean animated transition focusing their attention on the new code.

### The Myers Diff Brace Shift Defect & Prevention

Because the Myers diff algorithm has no syntax awareness, appending a new block ending with `}` right after an existing block ending with `}` frequently causes an ambiguous edit graph. DocC often highlights the *preceding* closing brace and leaves the *new* closing brace unhighlighted:

```swift
// ❌ Shifted Diff Defect:
   func existingMethod() {
   } // <-- DocC highlights this brace erroneously!
   
   func newMethod() {
       process()
   } // <-- DocC fails to highlight this brace!
```

To prevent this defect:
1. **Rule of Prefix Stability**: Never modify or reorder lines above the insertion point between step $N$ and $N+1$.
2. **Intermediate Scope Anchoring**: Always leave at least one empty blank line between scopes.
3. **Use `reset: true` on structural refactors**: If a step significantly restructures a file, suppress diff calculations using `@Code(name: "...", file: "...", reset: true)`.

---

## 5. Knowledge Assessments (`@Assessments`)

Every interactive tutorial must culminate in an `@Assessments` block:
- Include 1–3 `@MultipleChoice` questions.
- Every question must test a **conceptual rule, framework principle, or behavioral nuance**, never superficial syntax details.
- Exactly one `@Choice(isCorrect: true)` per question.
- Every `@Choice` must include a `@Justification(reaction: "...")`:
  - For correct choices: `@Justification(reaction: "Correct!")` explaining *why* it is right.
  - For incorrect choices: `@Justification(reaction: "Try again.")` explaining the misconception.

---

## 6. Tutorial Authoring Checklist

- [ ] Catalog contains `@Tutorials` table of contents linking every `@Tutorial`.
- [ ] Every `@Tutorial` includes `time` and `projectFiles` attributes.
- [ ] Every `@Section` has a `@ContentAndMedia` block with an illustration.
- [ ] Every `@Step` adheres to the 3-Sentence Anatomy (Action $\to$ Context $\to$ Feedback).
- [ ] Code files in `Resources/code/` change 1–5 lines per step.
- [ ] All code steps pass `scripts/audit-docc-highlights.py` with 0 shifted braces.
- [ ] Assessment questions provide clear justifications for all choices.
