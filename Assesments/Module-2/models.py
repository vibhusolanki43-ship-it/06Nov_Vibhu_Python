class User:
    """Represents a blog author."""
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


class Post:
    """Represents a blog post."""
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author  # Expecting a User object

    def __str__(self):
        return f"{self.title} by {self.author}"
