import os
import sys
from models import User, Post, Comment
import database as db

# --- ANSI COLOR CONSTANTS ---
# Using ANSI escape codes for terminal colors to provide a premium look.
CLR_HEADER = "\033[95m"   # Light Magenta
CLR_BLUE = "\033[94m"     # Light Blue
CLR_GREEN = "\033[92m"    # Light Green
CLR_YELLOW = "\033[93m"   # Light Yellow
CLR_RED = "\033[91m"      # Light Red
CLR_END = "\033[0m"       # Reset
CLR_BOLD = "\033[1m"      # Bold

def clear_screen():
    """Clears the terminal screen for a clean UI transitions."""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        # Fallback if clear command fails
        print("\n" * 5)

def print_header(title):
    """Prints a styled header with a title inside a box-drawing border."""
    width = 50
    print(f"{CLR_HEADER}{CLR_BOLD}┌" + "─" * (width - 2) + "┐")
    print(f"│{title:^{width-2}}│")
    print("└" + "─" * (width - 2) + f"┘{CLR_END}")

def print_separator(char="─", width=50):
    """Prints a separator line with color."""
    print(f"{CLR_BLUE}{char * width}{CLR_END}")

# --- AUTHENTICATION FLOWS ---

def main_menu():
    """Main entry point menu for registration and login."""
    while True:
        try:
            clear_screen()
            print_header("PostBoard - Internal System")
            print(f"\n  {CLR_BOLD}1.{CLR_END} Login")
            print(f"  {CLR_BOLD}2.{CLR_END} Register")
            print(f"  {CLR_BOLD}3.{CLR_END} Exit")
            choice = input(f"\n{CLR_BOLD}Select an option:{CLR_END} ").strip()
            
            if choice == '1':
                user = login_ui()
                if user:
                    dashboard_ui(user)
            elif choice == '2':
                register_ui()
            elif choice == '3':
                print(f"\n{CLR_GREEN}Thank you for using PostBoard. Goodbye!{CLR_END}")
                sys.exit()
            else:
                input(f"\n{CLR_RED}Invalid choice. Press Enter to retry...{CLR_END}")
        except EOFError:
            # Handle Ctrl+D or end of file input
            print(f"\n\n{CLR_GREEN}Exiting gracefully...{CLR_END}")
            sys.exit()
        except Exception as e:
            input(f"\n{CLR_RED}An unexpected error occurred: {e}. Press Enter to return to main menu.{CLR_END}")

def register_ui():
    """UI for user registration."""
    clear_screen()
    print_header("User Registration")
    username = input(f"{CLR_BOLD}Enter username:{CLR_END} ").strip()
    password = input(f"{CLR_BOLD}Enter password:{CLR_END} ").strip()
    full_name = input(f"{CLR_BOLD}Enter full name:{CLR_END} ").strip()
    
    if not username or not password or not full_name:
        input(f"\n{CLR_YELLOW}[!]{CLR_END} All fields are required. Press Enter to retry...")
        return

    user = User(username=username, password=password, full_name=full_name)
    try:
        if db.add_user(user):
            input(f"\n{CLR_GREEN}[✓]{CLR_END} Registration successful! Press Enter to login...")
        else:
            input(f"\n{CLR_RED}[X]{CLR_END} Username already exists. Press Enter to retry...")
    except Exception as e:
        input(f"\n{CLR_RED}[X]{CLR_END} Registration failed: {e}")

def login_ui():
    """UI for user login."""
    clear_screen()
    print_header("User Login")
    username = input(f"{CLR_BOLD}Enter username:{CLR_END} ").strip()
    password = input(f"{CLR_BOLD}Enter password:{CLR_END} ").strip()
    
    try:
        user = db.get_user(username, password)
        if user:
            return user
        else:
            input(f"\n{CLR_RED}[X]{CLR_END} Invalid username or password. Press Enter to retry...")
            return None
    except Exception as e:
        input(f"\n{CLR_RED}[X]{CLR_END} Login error: {e}")
        return None

# --- CORE FEATURES UI ---

def dashboard_ui(user):
    """User dashboard after successful login."""
    while True:
        clear_screen()
        print_header(f"PostBoard - Dashboard")
        print(f"\nWelcome, {CLR_GREEN}{CLR_BOLD}{user.full_name}{CLR_END}")
        print_separator("─", 50)
        print(f"\n  {CLR_BOLD}1.{CLR_END} View/Search Feed")
        print(f"  {CLR_BOLD}2.{CLR_END} Post Update/Issue")
        print(f"  {CLR_BOLD}3.{CLR_END} Logout")
        choice = input(f"\n{CLR_BOLD}Select an option:{CLR_END} ").strip()
        
        if choice == '1':
            post_feed_ui(user)
        elif choice == '2':
            create_post_ui(user)
        elif choice == '3':
            break
        else:
            input(f"\n{CLR_RED}Invalid choice. Press Enter to retry...{CLR_END}")

def create_post_ui(user):
    """Form to create a new post."""
    clear_screen()
    print_header("Create New Post")
    title = input(f"{CLR_BOLD}Title:{CLR_END} ").strip()
    content = input(f"{CLR_BOLD}Content:{CLR_END} ").strip()
    print(f"\n{CLR_BOLD}Categories:{CLR_END} Update, {CLR_RED}Issue{CLR_END}, {CLR_YELLOW}Discussion{CLR_END}")
    category = input(f"{CLR_BOLD}Category (default 'Update'):{CLR_END} ").strip() or "Update"
    
    if not title or not content:
        input(f"\n{CLR_YELLOW}[!]{CLR_END} Title and content are required. Press Enter to retry...")
        return

    try:
        post = Post(user_id=user.id, title=title, content=content, category=category)
        db.add_post(post)
        input(f"\n{CLR_GREEN}[✓]{CLR_END} Post created successfully! Press Enter to return...")
    except Exception as e:
        input(f"\n{CLR_RED}[X]{CLR_END} Error creating post: {e}")

def post_feed_ui(user):
    """Displays a list of posts with search functionality."""
    query = None
    while True:
        clear_screen()
        try:
            if query:
                print_header(f"Search: '{query}'")
                posts = db.search_posts(query)
            else:
                print_header("Community Board Feed")
                posts = db.get_posts()
            
            if not posts:
                print(f"\n  {CLR_YELLOW}No posts found matching your criteria.{CLR_END}")
            else:
                for i, post in enumerate(posts, 1):
                    category_color = CLR_BLUE
                    if post.category.lower() == "issue": category_color = CLR_RED
                    elif post.category.lower() == "discussion": category_color = CLR_YELLOW
                    
                    print(f"{CLR_BOLD}{i}.{CLR_END} {category_color}[{post.category}]{CLR_END} {CLR_BOLD}{post.title}{CLR_END}")
                    print(f"   By {CLR_GREEN}{post.author_name}{CLR_END} • {post.timestamp}")
                    print(f"   {CLR_BLUE}─{CLR_END}" * 30)
            
            print(f"\n{CLR_BOLD}Options:{CLR_END}")
            print("  [Number] View Details  [S] Search  [R] Reset  [B] Back")
            choice = input(f"\n{CLR_BOLD}Choice:{CLR_END} ").strip().lower()
            
            if choice == 'b':
                break
            elif choice == 's':
                query = input(f"\n{CLR_BOLD}Enter search term:{CLR_END} ").strip()
            elif choice == 'r':
                query = None
            elif choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(posts):
                    post_details_ui(user, posts[idx])
                else:
                    input(f"\n{CLR_RED}Invalid post number.{CLR_END}")
            else:
                input(f"\n{CLR_RED}Invalid input.{CLR_END}")
        except Exception as e:
            input(f"\n{CLR_RED}Error loading feed: {e}. Press Enter to return.{CLR_END}")
            break

def post_details_ui(user, post):
    """Detailed view of a single post with comments and deletion."""
    while True:
        clear_screen()
        try:
            category_color = CLR_BLUE
            if post.category.lower() == "issue": category_color = CLR_RED
            elif post.category.lower() == "discussion": category_color = CLR_YELLOW

            print_header(f"Post Details")
            print(f"\n{CLR_BOLD}Title:{CLR_END} {post.title}")
            print(f"{CLR_BOLD}Type: {CLR_END} {category_color}{post.category}{CLR_END}")
            print(f"{CLR_BOLD}Author:{CLR_END} {CLR_GREEN}{post.author_name}{CLR_END} ({post.timestamp})")
            print_separator("━", 50)
            print(f"\n{post.content}\n")
            print_separator("━", 50)
            
            print(f"{CLR_BOLD}Comments:{CLR_END}")
            comments = db.get_comments(post.id)
            if not comments:
                print(f"  {CLR_YELLOW}No comments yet be the first to share your thoughts!{CLR_END}")
            else:
                for comment in comments:
                    print(f"  ┌── {CLR_GREEN}{comment.author_name}{CLR_END} • {comment.timestamp}")
                    print(f"  └─ {comment.content}")
            
            is_owner = (post.user_id == user.id)
            options = f"[{CLR_BOLD}C{CLR_END}] Comment, [{CLR_BOLD}B{CLR_END}] Back"
            if is_owner: options += f", [{CLR_RED}{CLR_BOLD}D{CLR_BOLD}{CLR_END}{CLR_RED}] Delete Post{CLR_END}"
            
            print(f"\n{CLR_BOLD}Quick Action:{CLR_END} {options}")
            choice = input(f"\n{CLR_BOLD}Choice:{CLR_END} ").strip().lower()
            
            if choice == 'b':
                break
            elif choice == 'c':
                add_comment_ui(user, post.id)
            elif choice == 'd' and is_owner:
                if delete_post_ui(user, post):
                    break
            else:
                input(f"\n{CLR_RED}Invalid choice.{CLR_END}")
        except Exception as e:
            input(f"\n{CLR_RED}Error showing details: {e}. Press Enter to return.{CLR_END}")
            break

def add_comment_ui(user, post_id):
    """Small form to add a comment."""
    try:
        content = input(f"\n{CLR_BOLD}Your comment:{CLR_END} ").strip()
        if content:
            comment = Comment(post_id=post_id, user_id=user.id, content=content)
            db.add_comment(comment)
            input(f"\n{CLR_GREEN}[✓] Comment added!{CLR_END}")
        else:
            input(f"\n{CLR_RED}[!] Comment cannot be empty.{CLR_END}")
    except Exception as e:
        input(f"\n{CLR_RED}[X] Error adding comment: {e}")

def delete_post_ui(user, post):
    """Confirmation and deletion of a post."""
    try:
        confirm = input(f"\n{CLR_RED}{CLR_BOLD}⚠️  Are you sure you want to delete this post? (y/n): {CLR_END}").lower()
        if confirm == 'y':
            success, message = db.delete_post(post.id, user.id)
            if success:
                input(f"\n{CLR_GREEN}[✓] {message}{CLR_END}")
                return True
            else:
                input(f"\n{CLR_RED}[X] {message}{CLR_END}")
    except Exception as e:
        input(f"\n{CLR_RED}[X] Error deleting post: {e}")
    return False

# --- ENTRY POINT ---

if __name__ == "__main__":
    try:
        db.init_db()
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{CLR_GREEN}Application exited. Goodbye!{CLR_END}")
        sys.exit()
    except Exception as e:
        print(f"\n\n{CLR_RED}Critical Application Error: {e}{CLR_END}")
        sys.exit(1)
