#!/usr/bin/env python3
"""
Remove LaTeX \\changed[approved]{...} commands while preserving content.

This script processes LaTeX files to remove track-changes markup of the form
\\changed[approved]{content}, replacing it with just the content. It properly
handles nested braces within the content.
"""

import argparse
import re
import sys
from pathlib import Path


def find_matching_brace(text, start_pos):
    """
    Find the position of the matching closing brace.

    Args:
        text: The text to search in
        start_pos: Position after the opening brace

    Returns:
        Position after the matching closing brace, or -1 if not found
    """
    count = 1
    pos = start_pos
    while pos < len(text) and count > 0:
        if text[pos] == "{":
            count += 1
        elif text[pos] == "}":
            count -= 1
        pos += 1
    return pos if count == 0 else -1


def remove_changed_approved(text):
    """
    Remove \\changed[approved]{...} preserving content and handling nested braces.

    Args:
        text: Input LaTeX text

    Returns:
        Modified text with \\changed[approved]{...} patterns removed
    """
    pattern = r"\\changed\[approved\]{"
    result = []
    pos = 0
    count = 0

    while pos < len(text):
        match = re.search(pattern, text[pos:])
        if not match:
            result.append(text[pos:])
            break

        # Add text before the match
        result.append(text[pos : pos + match.start()])

        # Find matching closing brace
        brace_start = pos + match.end()
        brace_end = find_matching_brace(text, brace_start)

        if brace_end == -1:
            # No matching brace found, keep original
            result.append(match.group())
            pos = brace_start
        else:
            # Extract content between braces
            content = text[brace_start : brace_end - 1]
            result.append(content)
            pos = brace_end
            count += 1

    return "".join(result), count


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Remove \\changed[approved]{...} commands from LaTeX files while preserving content.",
        epilog="""
Examples:
  %(prog)s input.tex output.tex
  %(prog)s --inplace main.tex
  %(prog)s -i --backup main.tex
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("input", type=str, help="Input LaTeX file to process")

    parser.add_argument(
        "output",
        type=str,
        nargs="?",
        help="Output file (if not specified, uses --inplace)",
    )

    parser.add_argument(
        "-i",
        "--inplace",
        action="store_true",
        help="Edit the file in-place (modifies the input file directly)",
    )

    parser.add_argument(
        "-b",
        "--backup",
        action="store_true",
        help="Create a backup file with .bak extension when using --inplace",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print verbose output showing number of replacements",
    )

    args = parser.parse_args()

    # Validate arguments
    if not args.inplace and not args.output:
        parser.error("Either provide an output file or use --inplace")

    if args.backup and not args.inplace:
        parser.error("--backup can only be used with --inplace")

    input_path = Path(args.input)

    if not input_path.exists():
        print(f"Error: Input file '{args.input}' not found", file=sys.stderr)
        sys.exit(1)

    # Read input file
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        sys.exit(1)

    # Process content
    modified, count = remove_changed_approved(content)

    # Determine output path
    if args.inplace:
        output_path = input_path
        # Create backup if requested
        if args.backup:
            backup_path = input_path.with_suffix(input_path.suffix + ".bak")
            try:
                backup_path.write_text(content, encoding="utf-8")
                if args.verbose:
                    print(f"Backup created: {backup_path}")
            except Exception as e:
                print(f"Error creating backup: {e}", file=sys.stderr)
                sys.exit(1)
    else:
        output_path = Path(args.output)

    # Write output file
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(modified)
    except Exception as e:
        print(f"Error writing output file: {e}", file=sys.stderr)
        sys.exit(1)

    # Print summary
    if args.verbose or not args.inplace:
        print(f"Processed: {input_path} -> {output_path}")
        print(f"Removed {count} \\changed[approved]{{...}} pattern(s)")


if __name__ == "__main__":
    main()
