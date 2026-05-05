"""
This module defines the data templates for the PostBoard application.
Using only basic Python Collections (Dictionaries) as per assessment requirements.
"""

def create_user_template(user_id=None, username="", password="", full_name=""):
    """Creates a user dictionary."""
    return {
        "id": user_id,
        "username": username,
        "password": password,
        "full_name": full_name
    }

def create_post_template(post_id=None, user_id=0, title="", content="", category="Update", timestamp="", author_name=""):
    """Creates a post dictionary."""
    return {
        "id": post_id,
        "user_id": user_id,
        "title": title,
        "content": content,
        "category": category,
        "timestamp": timestamp,
        "author_name": author_name
    }

def create_comment_template(comment_id=None, post_id=0, user_id=0, content="", timestamp="", author_name=""):
    """Creates a comment dictionary."""
    return {
        "id": comment_id,
        "post_id": post_id,
        "user_id": user_id,
        "content": content,
        "timestamp": timestamp,
        "author_name": author_name
    }
