import json
import os
import sys
from models import User, Post, Comment

DB_NAME = "posts.json"

def init_db():
    """Initializes the JSON database if it doesn't exist."""
    try:
        if not os.path.exists(DB_NAME):
            with open(DB_NAME, 'w') as f:
                json.dump({"users": [], "posts": [], "comments": []}, f, indent=4)
    except (IOError, OSError) as e:
        print(f"Error initializing database: {e}")
        sys.exit(1)

def _read_data():
    """Reads all data from the JSON file with error handling."""
    if not os.path.exists(DB_NAME):
        init_db()
    
    try:
        with open(DB_NAME, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        # If file is corrupted, backup and re-initialize
        print(f"\nWarning: Database file is corrupted or unreadable. Backing up and resetting.")
        if os.path.exists(DB_NAME):
            os.rename(DB_NAME, DB_NAME + ".bak")
        init_db()
        return {"users": [], "posts": [], "comments": []}

def _write_data(data):
    """Writes all data to the JSON file with error handling."""
    try:
        with open(DB_NAME, 'w') as f:
            json.dump(data, f, indent=4)
    except (IOError, OSError) as e:
        print(f"\nError writing to database: {e}")
        # In a real app, we might want to retry or log this more seriously

# --- USER MANAGEMENT ---

def add_user(user: User):
    """Registers a new user if the username is unique."""
    data = _read_data()
    for u in data["users"]:
        if u["username"] == user.username:
            return False
    
    user.id = len(data["users"]) + 1
    data["users"].append({
        "id": user.id,
        "username": user.username,
        "password": user.password,
        "full_name": user.full_name
    })
    _write_data(data)
    return True

def get_user(username, password):
    """Retrieves a user by username and password."""
    data = _read_data()
    for u in data["users"]:
        if u["username"] == username and u["password"] == password:
            return User(id=u["id"], username=u["username"], full_name=u["full_name"])
    return None

# --- POST MANAGEMENT ---

def add_post(post: Post):
    """Adds a new post to the database."""
    data = _read_data()
    post.id = len(data["posts"]) + 1
    data["posts"].append({
        "id": post.id,
        "user_id": post.user_id,
        "title": post.title,
        "content": post.content,
        "category": post.category,
        "timestamp": post.timestamp
    })
    _write_data(data)
    return post

def get_posts():
    """Retrieves all posts with author names, sorted by timestamp (newest first)."""
    data = _read_data()
    users_dict = {u["id"]: u["full_name"] for u in data["users"]}
    
    posts = []
    for p in sorted(data["posts"], key=lambda x: x["timestamp"], reverse=True):
        posts.append(Post(
            id=p["id"],
            user_id=p["user_id"],
            title=p["title"],
            content=p["content"],
            category=p["category"],
            timestamp=p["timestamp"],
            author_name=users_dict.get(p["user_id"], "Unknown")
        ))
    return posts

def search_posts(query: str):
    """Searches for posts containing the query in title or content."""
    data = _read_data()
    users_dict = {u["id"]: u["full_name"] for u in data["users"]}
    query = query.lower()
    
    results = []
    for p in data["posts"]:
        if query in p["title"].lower() or query in p["content"].lower():
            results.append(Post(
                id=p["id"],
                user_id=p["user_id"],
                title=p["title"],
                content=p["content"],
                category=p["category"],
                timestamp=p["timestamp"],
                author_name=users_dict.get(p["user_id"], "Unknown")
            ))
    # Return sorted by newest first
    return sorted(results, key=lambda x: x.timestamp, reverse=True)

def delete_post(post_id: int, user_id: int):
    """Deletes a post if the user is the author."""
    data = _read_data()
    new_posts = []
    found = False
    
    for p in data["posts"]:
        if p["id"] == post_id:
            if p["user_id"] == user_id:
                found = True
                continue
            else:
                return False, "You can only delete your own posts."
        new_posts.append(p)
    
    if found:
        data["posts"] = new_posts
        # Also delete associated comments
        data["comments"] = [c for c in data["comments"] if c["post_id"] != post_id]
        _write_data(data)
        return True, "Post deleted successfully."
    return False, "Post not found."

# --- COMMENT MANAGEMENT ---

def add_comment(comment: Comment):
    """Adds a comment to a post."""
    data = _read_data()
    comment.id = len(data["comments"]) + 1
    data["comments"].append({
        "id": comment.id,
        "post_id": comment.post_id,
        "user_id": comment.user_id,
        "content": comment.content,
        "timestamp": comment.timestamp
    })
    _write_data(data)
    return comment

def get_comments(post_id):
    """Retrieves all comments for a specific post."""
    data = _read_data()
    users_dict = {u["id"]: u["full_name"] for u in data["users"]}
    
    comments = []
    relevant_comments = [c for c in data["comments"] if c["post_id"] == post_id]
    for c in sorted(relevant_comments, key=lambda x: x["timestamp"]):
        comments.append(Comment(
            id=c["id"],
            post_id=c["post_id"],
            user_id=c["user_id"],
            content=c["content"],
            timestamp=c["timestamp"],
            author_name=users_dict.get(c["user_id"], "Unknown")
        ))
    return comments
