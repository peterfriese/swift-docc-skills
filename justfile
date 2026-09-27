# swift-docc-skills command runner

default:
    @just --list

# Audit DocC static output for Myers diff brace shift defects
audit path=".build/docc-static/data/tutorials":
    python3 scripts/audit-docc-highlights.py {{path}}

# Compile static DocC documentation (requires Swift package with swift-docc-plugin)
docc target="MyTarget" output=".build/docc-static":
    swift package --allow-writing-to-directory {{output}} generate-documentation --target {{target}} --transform-for-static-hosting --output-path {{output}}

# Run test suite
test:
    python3 -m unittest discover -s tests -p "test_*.py" -v
