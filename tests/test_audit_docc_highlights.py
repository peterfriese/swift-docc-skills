#!/usr/bin/env python3
"""
test_audit_docc_highlights.py

Unit tests for scripts/audit-docc-highlights.py.
"""

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

# Load audit-docc-highlights.py dynamically
REPO_ROOT = Path(__file__).resolve().parent.parent
script_path = REPO_ROOT / "scripts" / "audit-docc-highlights.py"
spec = importlib.util.spec_from_file_location("audit_docc_highlights", script_path)
audit_mod = importlib.util.module_from_spec(spec)
sys.modules["audit_docc_highlights"] = audit_mod
spec.loader.exec_module(audit_mod)

strip_comment = audit_mod.strip_comment
is_closing_brace = audit_mod.is_closing_brace
find_contiguous_blocks = audit_mod.find_contiguous_blocks
get_step_mapping = audit_mod.get_step_mapping
audit_tutorial_highlights = audit_mod.audit_tutorial_highlights
format_context_snippet = audit_mod.format_context_snippet


class TestAuditDoccHighlights(unittest.TestCase):
    def test_strip_comment(self):
        self.assertEqual(strip_comment("  } // close struct"), "}")
        self.assertEqual(strip_comment("  } /* inline comment */"), "}")
        self.assertEqual(strip_comment("let x = 10"), "let x = 10")
        self.assertEqual(strip_comment("    // comment only"), "")

    def test_is_closing_brace(self):
        self.assertTrue(is_closing_brace("}"))
        self.assertTrue(is_closing_brace("  } // comment"))
        self.assertTrue(is_closing_brace("  } /* comment */"))
        self.assertTrue(is_closing_brace("})"))
        self.assertTrue(is_closing_brace("},"))
        self.assertTrue(is_closing_brace("});"))
        self.assertTrue(is_closing_brace(");"))
        self.assertTrue(is_closing_brace("};"))
        self.assertFalse(is_closing_brace("func hello() {"))
        self.assertFalse(is_closing_brace("return 42"))

    def test_find_contiguous_blocks(self):
        self.assertEqual(find_contiguous_blocks([]), [])
        self.assertEqual(find_contiguous_blocks([1, 2, 3]), [[1, 2, 3]])
        self.assertEqual(find_contiguous_blocks([1, 2, 4, 5, 7]), [[1, 2], [4, 5], [7]])
        # Unsorted input handling
        self.assertEqual(find_contiguous_blocks([5, 1, 2, 4]), [[1, 2], [4, 5]])
        # Duplicate line numbers handling
        self.assertEqual(find_contiguous_blocks([1, 1, 2, 4, 4, 5]), [[1, 2], [4, 5]])

    def test_get_step_mapping(self):
        sample_doc = {
            "sections": [
                {
                    "kind": "tasks",
                    "tasks": [
                        {
                            "title": "Build View",
                            "stepsSection": [
                                {
                                    "code": "step1.swift",
                                    "content": [
                                        {
                                            "inlineContent": [
                                                {"text": "Create "},
                                                {
                                                    "type": "strong",
                                                    "inlineContent": [
                                                        {"text": "ContentView"}
                                                    ]
                                                },
                                                {"text": "."}
                                            ]
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                }
            ]
        }
        mapping = get_step_mapping(sample_doc)
        self.assertIn("step1.swift", mapping)
        self.assertEqual(mapping["step1.swift"]["task_title"], "Build View")
        self.assertEqual(mapping["step1.swift"]["step_number"], 1)
        self.assertEqual(mapping["step1.swift"]["step_caption"], "Create ContentView.")

    def test_audit_clean_data(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            clean_tutorial = {
                "sections": [],
                "references": {
                    "step1.swift": {
                        "content": [
                            "struct ContentView: View {",
                            "    var body: some View {",
                            "        Text(\"Hello\")",
                            "    }",
                            "}",
                        ],
                        "highlights": [
                            {"line": 3}
                        ],
                    }
                },
            }
            json_file = tmp_path / "tutorial.json"
            json_file.write_text(json.dumps(clean_tutorial), encoding="utf-8")

            # Test directory scan
            total_files, total_refs, total_blocks, shifted = audit_tutorial_highlights(tmp_path)
            self.assertEqual(total_files, 1)
            self.assertEqual(total_refs, 1)
            self.assertEqual(total_blocks, 1)
            self.assertEqual(len(shifted), 0)

            # Test single-file audit
            total_files_f, total_refs_f, total_blocks_f, shifted_f = audit_tutorial_highlights(json_file)
            self.assertEqual(total_files_f, 1)
            self.assertEqual(total_refs_f, 1)
            self.assertEqual(len(shifted_f), 0)

    def test_audit_closing_brace_not_shifted(self):
        """Verifies that a step legitimately adding a closing brace is not falsely flagged."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            legit_brace_tutorial = {
                "sections": [],
                "references": {
                    "step3.swift": {
                        "content": [
                            "struct MyView: View {",
                            "    var body: some View {",
                            "        Text(\"Hello\")",
                            "    }",
                            "}",
                        ],
                        # User added the closing brace at line 5; line after (line 6) does not exist (not a brace)
                        "highlights": [
                            {"line": 5},
                        ],
                    }
                },
            }
            (tmp_path / "tutorial.json").write_text(json.dumps(legit_brace_tutorial), encoding="utf-8")
            total_files, total_refs, total_blocks, shifted = audit_tutorial_highlights(tmp_path)
            self.assertEqual(len(shifted), 0)

    def test_audit_shifted_brace_detected(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            shifted_tutorial = {
                "sections": [],
                "references": {
                    "step2.swift": {
                        "content": [
                            "func oldScope() {",
                            "}",
                            "",
                            "func newScope() {",
                            "    doWork()",
                            "}",
                        ],
                        # Highlight starts on line 2 (erroneous closing brace of oldScope)
                        # and ends on line 5 (omits line 6 closing brace)
                        "highlights": [
                            {"line": 2},
                            {"line": 3},
                            {"line": 4},
                            {"line": 5},
                        ],
                    }
                },
            }
            (tmp_path / "tutorial.json").write_text(json.dumps(shifted_tutorial), encoding="utf-8")

            total_files, total_refs, total_blocks, shifted = audit_tutorial_highlights(tmp_path)
            self.assertEqual(total_files, 1)
            self.assertEqual(total_refs, 1)
            self.assertEqual(len(shifted), 1)
            self.assertEqual(shifted[0]["erroneous_brace_line"], 2)
            self.assertEqual(shifted[0]["omitted_brace_line"], 6)

    def test_format_context_snippet(self):
        content = ["line 1", "}", "func new() {", "}", "line 5"]
        snippet = format_context_snippet(content, block_start=2, block_end=3, omitted_line=4)
        self.assertIn("ERR-BRACE >", snippet)
        self.assertIn("MISSED >", snippet)


if __name__ == "__main__":
    unittest.main()
