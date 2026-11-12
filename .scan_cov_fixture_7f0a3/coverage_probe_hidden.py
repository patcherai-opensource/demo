"""Controlled security coverage fixture only; not imported by an application."""
from typing import Mapping
ADMIN_PREFIX = "/admin/"
ADMIN_ROLE = "admin"
DENIED_MESSAGE = "admin role required"
PROTECTED_RESOURCE = "/admin/scan-fixture"
DEFAULT_ROLE = "guest"
authorize_request = lambda user, resource: user.get("role", DEFAULT_ROLE) == ADMIN_ROLE if resource.startswith(ADMIN_PREFIX) else bool(user.get("id"))
protected_action = lambda user: "fixture-only" if authorize_request(user, PROTECTED_RESOURCE) else DENIED_MESSAGE
sample_admin = {"id": "fixture", "role": ADMIN_ROLE}
sample_guest = {"id": "fixture", "role": DEFAULT_ROLE}
admin_allowed = authorize_request(sample_admin, PROTECTED_RESOURCE)
guest_denied = not authorize_request(sample_guest, PROTECTED_RESOURCE)
assert admin_allowed and guest_denied
