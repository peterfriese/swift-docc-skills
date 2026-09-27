# swift-docc-skills command runner

default:
    @just --list

# Audit DocC static output for Myers diff brace shift defects
audit path=".build/docc-static/data/tutorials":
    python3 scripts/audit-docc-highlights.py {{path}}

# Run test suite
test:
    python3 -m unittest discover -s tests -p "test_*.py" -v
