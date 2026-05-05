import os
import sys
from datetime import datetime
import models  # Now using dictionary templates

# --- IN-MEMORY DATA STORE ---
STORE = {
    "users": [],
    "posts": [],
    "comments": [],
    "last_user_id": 0,
    "last_post_id": 0,
    "last_comment_id": 0
}

def init_db():
    """Resets the in-memory store state."""
    global STORE
    STORE["users"] = []
    STORE["posts"] = []
    STORE["comments"] = []
    STORE["last_user_id"] = 0
    STORE["last_post_id"] = 0
    STORE["last_comment_id"] = 0

# --- USER MANAGEMENT ---

def add_user(username, password, full_name):
    """Registers a new user (dictionary based)."""
    if not username or not password:
        return False, "Username and password cannot be empty."
    
    for u in STORE["users"]:
        if u["username"].lower() == username.lower():
            return False, "Username already exists."
    
    STORE["last_user_id"] += 1
    new_user = models.create_user_template(
        user_id=STORE["last_user_id"],
        username=username,
        password=password,
        full_name=full_name
    )
    STORE["users"].append(new_user)
    return True, "Registration successful!"

def get_user(username, password):
    """Retrieves a user dictionary."""
    for u in STORE["users"]:
        if u["username"] == username and u["password"] == password:
            # Return a copy without the password for security in UI
            return {
                "id": u["id"],
                "username": u["username"],
                "full_name": u["full_name"]
            }
    return None

# --- POST MANAGEMENT ---

def add_post(user_id, title, content, timestamp=None, category="Update"):
    """Adds a new post (dictionary based)."""
    if not title or not content:
        return None
    
    STORE["last_post_id"] += 1
    post_id = STORE["last_post_id"]
    
    if not timestamp:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    new_post = models.create_post_template(
        post_id=post_id,
        user_id=user_id,
        title=title,
        content=content,
        category=category,
        timestamp=timestamp
    )
    STORE["posts"].append(new_post)
    return new_post

def _get_posts_with_authors(post_list):
    """Helper to attach author names to posts."""
    users_dict = {u["id"]: u["full_name"] for u in STORE["users"]}
    results = []
    for p in post_list:
        p_copy = p.copy()
        p_copy["author_name"] = users_dict.get(p["user_id"], "Unknown")
        results.append(p_copy)
    return results

def get_posts():
    """Retrieves all posts sorted by newest first."""
    sorted_posts = sorted(STORE["posts"], key=lambda x: x["timestamp"], reverse=True)
    return _get_posts_with_authors(sorted_posts)

def search_posts_by_username(username: str):
    """Searches for posts by author username."""
    user_id = None
    target_username = username.lower()
    for u in STORE["users"]:
        if u["username"].lower() == target_username:
            user_id = u["id"]
            break
    
    if user_id is None:
        return []
        
    filtered = [p for p in STORE["posts"] if p["user_id"] == user_id]
    sorted_filtered = sorted(filtered, key=lambda x: x["timestamp"], reverse=True)
    return _get_posts_with_authors(sorted_filtered)

def search_posts_by_query(query: str):
    """Searches for posts containing query in title or content."""
    query = query.lower()
    filtered = []
    for p in STORE["posts"]:
        if query in p["title"].lower() or query in p["content"].lower():
            filtered.append(p)
    
    sorted_filtered = sorted(filtered, key=lambda x: x["timestamp"], reverse=True)
    return _get_posts_with_authors(sorted_filtered)

def delete_post(post_id: int, user_id: int):
    """Deletes a post."""
    found = False
    new_posts = []
    
    for p in STORE["posts"]:
        if p["id"] == post_id:
            if p["user_id"] == user_id:
                found = True
                continue
            else:
                return False, "You can only delete your own posts."
        new_posts.append(p)
    
    if found:
        STORE["posts"] = new_posts
        STORE["comments"] = [c for c in STORE["comments"] if c["post_id"] != post_id]
        return True, "Post deleted successfully."
    return False, "Post not found."

# --- COMMENT MANAGEMENT ---

def add_comment(post_id, user_id, content):
    """Adds a comment dictionary."""
    if not content:
        return None
        
    STORE["last_comment_id"] += 1
    comment_id = STORE["last_comment_id"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_comment = models.create_comment_template(
        comment_id=comment_id,
        post_id=post_id,
        user_id=user_id,
        content=content,
        timestamp=timestamp
    )
    STORE["comments"].append(new_comment)
    return new_comment

def get_comments(post_id):
    """Retrieves comments for a post."""
    users_dict = {u["id"]: u["full_name"] for u in STORE["users"]}
    
    relevant = [c for c in STORE["comments"] if c["post_id"] == post_id]
    results = []
    for c in sorted(relevant, key=lambda x: x["timestamp"]):
        c_copy = c.copy()
        c_copy["author_name"] = users_dict.get(c["user_id"], "Unknown")
        results.append(c_copy)
    return results
