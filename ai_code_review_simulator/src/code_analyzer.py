import ast
import re
from dataclasses import dataclass, asdict
from typing import Dict, List, Any

@dataclass
class AnalysisMetrics:
    complexity: int = 0
    security_risk: str = "Low"
    maintainability_score: int = 100

class CodeAnalyzer(ast.NodeVisitor):
    \"\"\"Advanced Code Analysis Engine with AI-driven optimizations.\"\"\"
    
    # Pre-compiling regex patterns for performance
    SECURITY_PATTERNS = {
        "SQL Injection": re.compile(r"(\.execute\(.*f['\"]|.*\.query\(.*['\"] \+)"),
        "Hardcoded Credential": re.compile(r"(password|api_key|secret)\s*=\s*['\"].*['\"]", re.IGNORECASE),
        "Insecure Random": re.compile(r"import random")
    }

    def __init__(self, source_code: str):
        self.source_code = source_code
        self.issues: List[str] = []
        self.metrics = AnalysisMetrics()

    def visit_If(self, node): self.metrics.complexity += 1; self.generic_visit(node)
    def visit_For(self, node): self.metrics.complexity += 1; self.generic_visit(node)
    def visit_While(self, node): self.metrics.complexity += 1; self.generic_visit(node)
    def visit_Try(self, node): self.metrics.complexity += 1; self.generic_visit(node)

    def run_analysis(self) -> None:
        \"\"\"Executes the full suite of analysis.\"\"\"
        try:
            tree = ast.parse(self.source_code)
            self.visit(tree)
            if self.metrics.complexity > 10:
                self.issues.append("High Cyclomatic Complexity: Consider refactoring.")
                self.metrics.maintainability_score -= 20
        except SyntaxError:
            self.issues.append("Syntax Error: Could not parse code.")
        
        self._check_security()

    def _check_security(self) -> None:
        for bug_type, pattern in self.SECURITY_PATTERNS.items():
            if pattern.search(self.source_code):
                msg = f"Security Vulnerability: {bug_type}"
                if bug_type == "Insecure Random":
                    msg += " (Use 'secrets' module instead)"
                self.issues.append(msg)
                self.metrics.security_risk = "High"
                self.metrics.maintainability_score -= 30

    def get_report(self) -> Dict[str, Any]:
        \"\"\"Generates the analysis report dictionary.\"\"\"
        return {
            "status": "Success" if not self.issues else "Needs Improvement",
            "metrics": asdict(self.metrics),
            "findings": self.issues
        }
