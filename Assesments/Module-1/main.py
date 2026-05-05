import os
import sys
from datetime import datetime
import database as db

# --- SIMPLE UI HELPERS ---
# Removed all ANSI colors and complex ASCII art for a minimalist look.

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Prints a simple plain-text header."""
    print(f"\n{'=' * 10} {title.upper()} {'=' * 10}")

def print_separator(char="-", width=40):
    """Prints a simple separator line."""
    print(char * width)

# --- AUTHENTICATION FLOWS ---

def main_menu():
    """Main entry point menu."""
    while True:
        try:
            print_header("PostBoard Main Menu")
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            choice = input("\nSelect an option: ").strip()
            
            if choice == '1':
                user = login_ui()
                if user:
                    dashboard_ui(user)
            elif choice == '2':
                register_ui()
            elif choice == '3':
                print("\nGoodbye!")
                sys.exit()
            else:
                input("\nInvalid choice. Press Enter to retry...")
        except EOFError:
            sys.exit()
        except Exception as e:
            input(f"\nAn error occurred: {e}. Press Enter...")

def register_ui():
    """UI for user registration."""
    print_header("User Registration")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    full_name = input("Enter full name: ").strip()
    
    if not username or not password or not full_name:
        input("\n[!] All fields are required. Press Enter...")
        return

    success, message = db.add_user(username, password, full_name)
    input(f"\n{message} Press Enter...")

def login_ui():
    """UI for user login with attempt limits."""
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        print_header(f"Login (Attempt {attempts + 1}/{max_attempts})")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        user = db.get_user(username, password)
        if user:
            return user
        else:
            attempts += 1
            if attempts < max_attempts:
                input(f"\nInvalid credentials. {max_attempts - attempts} left. Press Enter...")
            else:
                input("\nToo many failed attempts. Returning...")
    return None

# --- CORE FEATURES UI ---

def dashboard_ui(user):
    """User dashboard."""
    while True:
        print_header("PostBoard Dashboard")
        print(f"Logged in as: {user['full_name']}")
        print_separator("=")
        print("1. View All Posts")
        print("2. Create New Post")
        print("3. Search Posts")
        print("4. Logout")
        choice = input("\nSelect an option: ").strip()
        
        if choice == '1':
            post_feed_ui(user)
        elif choice == '2':
            create_post_ui(user)
        elif choice == '3':
            search_menu_ui(user)
        elif choice == '4':
            break
        else:
            input("\nInvalid choice. Press Enter...")

def create_post_ui(user):
    """Form to create a new post."""
    print_header("Create New Post")
    title = input("Title: ").strip()
    content = input("Description: ").strip()
    date_input = input("Date (leave blank for auto): ").strip()
    
    if not title or not content:
        input("\n[!] Title and Description are required.")
        return

    if db.add_post(user['id'], title, content, timestamp=date_input or None):
        input("\nPost created successfully!")
    else:
        input("\nFailed to create post.")

def post_feed_ui(user):
    """Displays all posts."""
    while True:
        print_header("Post Feed")
        posts = db.get_posts()
        
        if not posts:
            print("\nNo posts available.")
        else:
            for i, post in enumerate(posts, 1):
                print_separator("-")
                print(f"{i}. Title: {post['title']}")
                print(f"   Author: {post['author_name']}")
                print(f"   Date:   {post['timestamp']}")
                print(f"   Desc:   {post['content']}")
            print_separator("-")
        
        print("\nOptions: [Number] Details  [B] Back")
        choice = input("Choice: ").strip().lower()
        
        if choice == 'b':
            break
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(posts):
                post_details_ui(user, posts[idx])
            else:
                input("\nInvalid post number.")
        else:
            input("\nInvalid input.")

def search_menu_ui(user):
    """Search submenu."""
    while True:
        print_header("Search Posts")
        print("1. Search by Username")
        print("2. Search by Keyword")
        print("3. Back")
        choice = input("\nSelect an option: ").strip()
        
        if choice == '1':
            username = input("\nEnter username: ").strip()
            display_search_results(user, db.search_posts_by_username(username), f"User: {username}")
        elif choice == '2':
            query = input("\nEnter keyword: ").strip()
            display_search_results(user, db.search_posts_by_query(query), f"Keyword: {query}")
        elif choice == '3':
            break
        else:
            input("\nInvalid choice.")

def display_search_results(user, posts, criteria):
    """Helper to display search results."""
    while True:
        print_header(f"Search Results: {criteria}")
        
        if not posts:
            print(f"\nNo posts found matching '{criteria}'.")
            input("\nPress Enter to return...")
            break
        else:
            for i, post in enumerate(posts, 1):
                print_separator("-")
                print(f"{i}. Title: {post['title']}")
                print(f"   Author: {post['author_name']}")
                print(f"   Date:   {post['timestamp']}")
            print_separator("-")
            
            print("\nOptions: [Number] Details  [B] Back")
            choice = input("Choice: ").strip().lower()
            
            if choice == 'b':
                break
            elif choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(posts):
                    post_details_ui(user, posts[idx])
                else:
                    input("\nInvalid post number.")
            else:
                input("\nInvalid input.")

def post_details_ui(user, post):
    """Detailed view of a single post."""
    while True:
        print_header("Post Details")
        print(f"Title:  {post['title']}")
        print(f"Author: {post['author_name']}")
        print(f"Date:   {post['timestamp']}")
        print_separator("-")
        print(f"{post['content']}")
        print_separator("-")
        
        print("Comments:")
        comments = db.get_comments(post['id'])
        if not comments:
            print("  No comments yet.")
        else:
            for c in comments:
                print(f"  - {c['author_name']}: {c['content']}")
        
        is_owner = (post['user_id'] == user['id'])
        options = "[C] Comment, [B] Back"
        if is_owner: options += ", [D] Delete"
        
        print(f"\nAction: {options}")
        choice = input("Choice: ").strip().lower()
        
        if choice == 'b':
            break
        elif choice == 'c':
            content = input("\nEnter comment: ").strip()
            if content:
                db.add_comment(post['id'], user['id'], content)
                input("\nComment added!")
            else:
                input("\n[!] Empty comment.")
        elif choice == 'd' and is_owner:
            if input("\nConfirm delete? (y/n): ").lower() == 'y':
                success, message = db.delete_post(post['id'], user['id'])
                input(f"\n{message}")
                if success: break
        else:
            input("\nInvalid choice.")

# --- ENTRY POINT ---

if __name__ == "__main__":
    try:
        db.init_db()
        main_menu()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
    except Exception as e:
        print(f"\nCritical Error: {e}")
        sys.exit(1)
