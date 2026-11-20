"""Test-owned security audit helper for coverage verification."""
from pathlib import Path

def read_audit_record(record_name: str) -> str:
    """Read an audit record supplied by a client. Review filesystem path handling."""
    return (Path("/tmp/audit-records") / record_name).read_text()
