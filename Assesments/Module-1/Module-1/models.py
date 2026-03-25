from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class User:
    """Represents an employee user in the system."""
    id: Optional[int] = None
    username: str = ""
    password: str = ""  # Note: Stored in plaintext for this simple implementation
    full_name: str = ""

@dataclass
class Post:
    """Represents a post shared on the community board."""
    id: Optional[int] = None
    user_id: int = 0
    title: str = ""
    content: str = ""
    category: str = "Update"  # Categories: Update, Issue, Discussion
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    author_name: str = ""

@dataclass
class Comment:
    """Represents a comment on a post."""
    id: Optional[int] = None
    post_id: int = 0
    user_id: int = 0
    content: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    author_name: str = ""
