"""
Audit logging utilities.
"""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo


LOG_FILE = "logs/audit.log"


def log_event(event):
    """
    Write security event to audit log.

    Args:
        event (str): Event description
    """

    timestamp = datetime.now(timezone.utc).isoformat()

    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {event}\n")