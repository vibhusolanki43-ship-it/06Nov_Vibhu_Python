import os

class BlogStorage:
    """Handles saving and loading blog posts from the local file system."""
    
    BASE_DIR = "posts"

    def __init__(self):
        # Ensure the storage directory exists
        if not os.path.exists(self.BASE_DIR):
            try:
                os.makedirs(self.BASE_DIR)
            except OSError as e:
                raise Exception(f"Could not create storage directory: {e}")

    def save_post(self, post):
        """
        Saves a Post object to a text file.
        Filename format: username_title.txt
        """
        filename = f"{post.author.username}_{post.title}.txt"
        # Sanitize filename (basic)
        filename = "".join([c for c in filename if c.isalnum() or c in (' ', '.', '_', '-')]).rstrip()
        filepath = os.path.join(self.BASE_DIR, filename)

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"Author: {post.author.username}\n")
                f.write(f"Title: {post.title}\n")
                f.write("-" * 20 + "\n")
                f.write(post.content)
        except IOError as e:
            raise Exception(f"Failed to save post: {e}")

    def list_posts(self):
        """Returns a list of all saved post filenames."""
        try:
            files = [f for f in os.listdir(self.BASE_DIR) if f.endswith('.txt')]
            return sorted(files)
        except FileNotFoundError:
            return []
        except Exception as e:
            raise Exception(f"Error listing posts: {e}")

    def read_post(self, filename):
        """Reads the content of a specific post file."""
        filepath = os.path.join(self.BASE_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise Exception("Post file not found.")
        except IOError as e:
            raise Exception(f"Could not read post: {e}")
