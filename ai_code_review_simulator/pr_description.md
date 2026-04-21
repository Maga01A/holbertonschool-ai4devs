# Pull Request: Add Advanced Analysis & Reporting Module

## Summary
Implements a new CodeAnalyzer engine that performs static analysis on Python code to identify complexity issues and security vulnerabilities (SQLi, Hardcoded secrets).

## Changes
- Created src/code_analyzer.py: Core logic for AST-based complexity and regex-based security scanning.
- Created 	ests/test_analyzer.py: Unit tests for vulnerability detection and metrics accuracy.
- Integrated automated reporting structure.

## Context
~150 LOC. This feature addresses the need for the simulator to provide quantitative metrics (Maintainability Score) alongside qualitative feedback.
