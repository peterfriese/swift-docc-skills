---
name: swift-docc-reference
license: Apache-2.0
description: >-
  Guide for authoring Swift DocC API reference documentation,
  in-source doc comments, documentation catalogs, topic curation, and symbol graphs.
  Use when writing triple-slash doc comments, designing landing pages, curating Topics sections,
  linking symbols, or resolving DocC reference warnings.
metadata:
  author: peterfriese
  version: "0.1.0"
---

# Swift DocC API Reference Documentation

This skill covers the syntax and conventions for writing API reference documentation with Swift DocC—from in-source documentation comments to curated `.docc` documentation catalogs, topic hierarchies, and symbol graphs.

---

## 1. In-Source Documentation Comments

Swift DocC extracts API reference documentation directly from doc comments attached to declarations in your Swift source code.

### Comment Syntax

- **Always prefer triple slashes (`///`)** over block comments (`/** ... */`). Triple slashes blend cleanly with standard Swift source code formatting.
- Attach the doc comment immediately preceding the declaration with no blank line in between.

```swift
/// An immutable representation of a geographic coordinate.
///
/// A coordinate encapsulates latitude and longitude measured in degrees according
/// to the World Geodetic System 1984 (WGS 84) reference frame.
public struct Coordinate: Sendable, Hashable {
    /// The latitude in degrees.
    public let latitude: Double

    /// The longitude in degrees.
    public let longitude: Double
}
```

### The Single-Sentence Summary Rule

The first paragraph of a doc comment serves as the **summary sentence**:
- It appears in Xcode Quick Help tooltips, code completion popovers, and DocC topic listings.
- Write it in the present tense, third person (e.g., *"Creates a new session"*, *"Calculates the distance"*), or as a clear noun phrase (*"An immutable representation..."*).
- Keep it concise (1 sentence, under 120 characters).
- Separate the summary from the extended discussion with an empty `///` line.

### Documenting Parameters, Returns, and Errors

Use standard Markdown list syntax with dedicated parameter tags:

```swift
/// Computes the great-circle distance between this coordinate and another coordinate.
///
/// Uses the Haversine formula to determine distance across a spherical Earth model.
/// For highly accurate geodetic calculations over long distances, use an ellipsoidal model instead.
///
/// - Parameter destination: The target coordinate to measure distance toward.
/// - Parameter unit: The unit of length for the result. Defaults to `.meters`.
/// - Returns: The distance between the two points expressed in the requested unit.
/// - Throws: `NavigationError.invalidCoordinates` if either coordinate contains NaN or infinite values.
public func distance(
    to destination: Coordinate,
    unit: DistanceUnit = .meters
) throws -> Double { ... }
```

When documenting multiple parameters, you may also use a grouped `- Parameters:` block:

```swift
/// - Parameters:
///   - destination: The target coordinate to measure distance toward.
///   - unit: The unit of length for the result.
```

### Callout Directives

DocC parses GitHub-style blockquote callouts to highlight notes, warnings, and tips:

```swift
/// > Note:
/// > Coordinates use the standard WGS 84 datum.

/// > Important:
/// > Always check network reachability before initiating batch geocoding.

/// > Warning:
/// > Calling this method from a background thread while the view is animating may cause dropped frames.

/// > Tip:
/// > Cache the computed bounding box if performing repeated hit tests.

/// > Experiment:
/// > Try adjusting the convergence threshold to observe performance differences.
```

Supported callout heads: `Note`, `Important`, `Warning`, `Tip`, `Experiment`.

---

## 2. Documentation Catalogs (`.docc`)

A documentation catalog is a folder with the `.docc` extension placed inside your target's source directory (e.g., `Sources/MyFramework/MyFramework.docc`). It holds:
- The target landing page (`MyFramework.md`)
- Conceptual articles (`.article` or `.md`)
- Documentation extension files (`.md`)
- Media assets (`Resources/images/`, `Resources/videos/`)

### Catalog Directory Layout

```
Sources/
└── MyFramework/
    ├── MyFramework.docc/
    │   ├── MyFramework.md              # Target landing page
    │   ├── Articles/
    │   │   ├── GettingStarted.md       # Conceptual guide
    │   │   └── ConcurrencyModel.md
    │   ├── Extensions/
    │   │   └── Coordinate+Extensions.md # Supplemental symbol doc
    │   └── Resources/
    │       └── hero-overview@2x.png
    ├── Coordinate.swift
    └── Engine.swift
```

---

## 3. The Target Landing Page

The landing page introduces the library or module. The top-level heading must match the module name wrapped in double backticks:

```markdown
# ``MyFramework``

A high-performance geodetic calculation engine with built-in spatial indexers.

## Overview

MyFramework provides spatial primitives and spatial indexing structures for mapping
and route optimization applications. Designed for Swift 6, all public types conform to
`Sendable` and integrate with modern concurrency.

### Key Capabilities

- **Deterministic Math**: Rigorous Haversine and Vincenty geodesic implementations.
- **Spatial Indexing**: Quadtree and R-Tree implementations optimized for low-latency queries.
- **Strict Concurrency**: Fully validated under `-strict-concurrency=complete`.

## Topics

### Essentials

- <doc:GettingStarted>
- ``Coordinate``
- ``DistanceUnit``

### Spatial Queries

- ``SpatialIndex``
- ``BoundingBox``
- <doc:ConcurrencyModel>

### Supporting Types

- ``NavigationError``
```

---

## 4. Symbol Links & Cross-Referencing

DocC uses double backticks to reference symbols and `<doc:...>` to reference articles and pages.

### Symbol Reference Syntax

| Syntax | Target | Example |
| :--- | :--- | :--- |
| ` ``TypeName`` ` | Type in current module | ` ``Coordinate`` ` |
| ` ``TypeName/property`` ` | Member property | ` ``Coordinate/latitude`` ` |
| ` ``TypeName/method(_:)`` ` | Member method | ` ``Coordinate/distance(to:unit:)`` ` |
| ` ``Module/TypeName`` ` | Scoped to specific module | ` ``SpatialKit/Coordinate`` ` |

### Disambiguating Overloads

When multiple methods share the same base name, specify the argument labels:
- ` ``Engine/start()`` `
- ` ``Engine/start(withConfiguration:)`` `
- ` ``Engine/start(retries:timeout:)`` `

When symbols share identical base names and argument labels, DocC provides disambiguation suffixes based on symbol kind, parameter types, return types, or collision hashes:

| Disambiguation Type | Suffix Syntax | Example |
| :--- | :--- | :--- |
| **Symbol Kind** | `-<kind>` | ` ``Coordinate-struct`` `, ` ``Coordinate-enum`` ` |
| **Parameter Types** | `-(<types>)` | ` ``distance(to:)-(Coordinate,_)`` ` |
| **Return Type** | `-><type>` | ` ``distance(to:)->Double`` ` |
| **Parameters & Return** | `-(<types>)-><type>` | ` ``process(_:)-(Data)->Bool`` ` |
| **Unique Identifier Hash** | `-<hash>` | ` ``update(value:)-4gcpg`` ` |

### Article & Path Links

- Link to articles: `<doc:GettingStarted>` or `<doc:ConcurrencyModel>` (DocC resolves articles by filename without catalog subfolder prefixes)
- Link to external URLs: standard Markdown `[Apple Developer](https://developer.apple.com)`

---

## 5. Topic Curation & Organization

By default, DocC lists all uncurated symbols under auto-generated headings like "Structures", "Classes", and "Protocols". **High-quality documentation replaces auto-generation with intentional curation.**

### Curating Topics on Landing Pages and Symbols

Add a `## Topics` section to any landing page, article, or symbol extension:

```markdown
## Topics

### Spatial Computation

- ``Coordinate``
- ``BoundingBox``
- ``distance(from:to:)``

### Data Storage

- ``SpatialIndex``
- ``SpatialCache``
```

When a symbol is placed in a `## Topics` section, DocC removes it from the automatic fallback bucket and nests it under your curated task group.

---

## 6. Documentation Extension Files

When in-source comments become too verbose, or when you want to curate child symbols without cluttering Swift source files, use a **Documentation Extension File**.

Create a Markdown file inside the catalog (e.g., `Extensions/Coordinate.md`):

```markdown
# ``MyFramework/Coordinate``

Supplemental architectural guide for coordinate precision and coordinate systems.

## Overview

While `Coordinate` represents WGS 84 points by default, you can convert coordinates
to projected planar coordinate systems using projection adapters.

### Precision Guidelines

Floating-point precision limits can affect calculation accuracy near the poles.
Refer to the geodesic accuracy table below when choosing between Haversine and Vincenty algorithms.

## Topics

### Geodesic Distance

- ``distance(to:unit:)``
- ``bearing(to:)``
```

The content in this extension file merges directly with the in-source comments attached to `Coordinate`.

---

## 7. Symbol Graphs & Compilation

DocC operates on **Symbol Graph JSON files** produced by the Swift compiler:
1. `swift build` or Xcode builds the target with `-emit-symbol-graph`.
2. The compiler writes JSON symbol graphs describing declarations, doc comments, protocols, and relationships.
3. DocC consumes the symbol graphs together with the `.docc` catalog to produce the final website or `.doccarchive`.

To inspect symbol graphs directly via Swift Package Manager:
```bash
swift package dump-symbol-graph
```

This dumps the generated symbol graph JSON files into `.build/extracted-symbols/`.

---

## 8. Reference Documentation Quality Checklist

- [ ] All public APIs have a single-sentence summary followed by detailed context.
- [ ] Every parameter, return value, and thrown error is explicitly documented.
- [ ] Code examples within doc comments use triple-backtick ```swift blocks.
- [ ] All symbol links (` ``SymbolName`` `) resolve without DocC compile-time warnings.
- [ ] Landing page (`<TargetName>.md`) curates symbols into logical, task-oriented `## Topics`.
- [ ] No uncurated symbols fall into default, auto-generated category buckets.
