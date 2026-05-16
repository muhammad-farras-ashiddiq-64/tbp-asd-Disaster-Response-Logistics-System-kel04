from typing import Any, Optional

class LLNode:
    """Simpul dasar untuk Singly Linked List."""
    def __init__(self, data: Any = None):
        self.data = data
        self.next = None
