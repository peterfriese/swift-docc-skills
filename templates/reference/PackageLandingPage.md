# ``PackageName``

A concise, high-level summary sentence describing what the package does.

## Overview

Provide an architectural introduction explaining the package's purpose, design philosophy,
and primary integration patterns. Address the core capabilities in direct, pragmatic prose.

```swift
import PackageName

let client = ServiceClient(apiKey: "...")
let result = try await client.performOperation()
```

### Key Features

- **Swift 6 Strict Concurrency**: All core primitives conform to `Sendable` and respect actor isolation.
- **Zero Third-Party Dependencies**: Built exclusively on native Foundation and standard library APIs.
- **Progressive Disclosure**: Ergonomic convenience methods for common workflows alongside deep customization hooks.

## Topics

### Essentials

- <doc:GettingStarted>
- ``ServiceClient``
- ``Configuration``

### Core Workflows

- ``Operation``
- ``ResultHandler``
- ``BatchProcessor``

### Error Handling

- ``ServiceError``
- ``RetryPolicy``
