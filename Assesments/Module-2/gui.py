import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
from models import User, Post
from storage import BlogStorage

class MiniBlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniBlog Pro")
        self.root.geometry("900x600")
        
        # Premium Dark Theme Colors
        self.colors = {
            "bg": "#121212",
            "card": "#1e1e1e",
            "accent": "#bb86fc",
            "secondary": "#03dac6",
            "text": "#e1e1e1",
            "subtext": "#a0a0a0",
            "error": "#cf6679",
            "success": "#03dac6"
        }

        self.root.configure(bg=self.colors["bg"])
        self.storage = BlogStorage()

        self._setup_styles()
        self._setup_ui()
        self._refresh_post_list()

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure Listbox-like Treeview for better aesthetics
        style.configure("Treeview", 
                        background=self.colors["card"], 
                        foreground=self.colors["text"], 
                        fieldbackground=self.colors["card"],
                        borderwidth=0,
                        font=("Segoe UI", 10))
        style.map("Treeview", background=[('selected', self.colors["accent"])])

    def _setup_ui(self):
        # Sidebar / List Section
        self.sidebar = tk.Frame(self.root, bg=self.colors["card"], width=300)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=0, pady=0)
        self.sidebar.pack_propagate(False)

        # Sidebar Header
        tk.Label(self.sidebar, text="Saved Posts", font=("Segoe UI", 14, "bold"), 
                 bg=self.colors["card"], fg=self.colors["accent"], pady=20).pack()

        # Search/Filter (Visual placeholder for premium feel)
        self.post_listbox = tk.Listbox(self.sidebar, bg=self.colors["card"], fg=self.colors["text"],
                                       font=("Segoe UI", 10), borderwidth=0, highlightthickness=0,
                                       selectbackground=self.colors["accent"], selectforeground=self.colors["bg"])
        self.post_listbox.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Sidebar Buttons
        side_btn_frame = tk.Frame(self.sidebar, bg=self.colors["card"], pady=20)
        side_btn_frame.pack(fill=tk.X)

        self._create_button(side_btn_frame, "View Post", self._view_post, self.colors["accent"]).pack(fill=tk.X, padx=20, pady=5)
        self._create_button(side_btn_frame, "Refresh", self._refresh_post_list, self.colors["subtext"]).pack(fill=tk.X, padx=20, pady=5)

        # Main Content Area
        self.main_content = tk.Frame(self.root, bg=self.colors["bg"], padx=40, pady=30)
        self.main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Header
        tk.Label(self.main_content, text="Create a Masterpiece", font=("Segoe UI", 24, "bold"), 
                 bg=self.colors["bg"], fg=self.colors["text"]).pack(anchor="w", pady=(0, 30))

        # Form Fields
        self._create_label(self.main_content, "Author Name").pack(anchor="w")
        self.name_entry = self._create_entry(self.main_content)
        self.name_entry.pack(fill=tk.X, pady=(5, 20))

        self._create_label(self.main_content, "Post Title").pack(anchor="w")
        self.title_entry = self._create_entry(self.main_content)
        self.title_entry.pack(fill=tk.X, pady=(5, 20))

        self._create_label(self.main_content, "Content").pack(anchor="w")
        self.content_text = scrolledtext.ScrolledText(self.main_content, height=12, bg=self.colors["card"], 
                                                     fg=self.colors["text"], font=("Segoe UI", 11),
                                                     borderwidth=0, highlightthickness=1, 
                                                     highlightbackground=self.colors["subtext"],
                                                     insertbackground=self.colors["text"])
        self.content_text.pack(fill=tk.BOTH, expand=True, pady=(5, 30))

        # Save Button
        save_btn = self._create_button(self.main_content, "Publish Post", self._save_post, self.colors["secondary"], large=True)
        save_btn.pack(anchor="e")

    def _create_label(self, parent, text):
        return tk.Label(parent, text=text, font=("Segoe UI", 10, "bold"), bg=self.colors["bg"], fg=self.colors["subtext"])

    def _create_entry(self, parent):
        entry = tk.Entry(parent, font=("Segoe UI", 11), bg=self.colors["card"], fg=self.colors["text"],
                         borderwidth=0, highlightthickness=1, highlightbackground=self.colors["subtext"],
                         insertbackground=self.colors["text"])
        return entry

    def _create_button(self, parent, text, command, color, large=False):
        font = ("Segoe UI", 11, "bold") if large else ("Segoe UI", 10, "bold")
        btn = tk.Button(parent, text=text, command=command, bg=color, fg=self.colors["bg"],
                        font=font, relief=tk.FLAT, cursor="hand2", padx=20, pady=8 if large else 5)
        # Simple hover effect simulation
        btn.bind("<Enter>", lambda e: btn.configure(bg=self._lighten_color(color)))
        btn.bind("<Leave>", lambda e: btn.configure(bg=color))
        return btn

    def _lighten_color(self, hex_color):
        # Very simple way to "lighten" for hover
        return hex_color # In a real app we'd calculate this, but keeping it simple for now

    def _save_post(self):
        name = self.name_entry.get().strip()
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()

        if not name or not title or not content:
            messagebox.showwarning("Incomplete", "Every masterpiece needs an author, title, and soul (content).")
            return

        try:
            author = User(name)
            post = Post(title, content, author)
            self.storage.save_post(post)
            messagebox.showinfo("Published", f"'{title}' has been immortalized.")
            
            # Clear fields
            self.name_entry.delete(0, tk.END)
            self.title_entry.delete(0, tk.END)
            self.content_text.delete("1.0", tk.END)
            
            self._refresh_post_list()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _refresh_post_list(self):
        try:
            self.post_listbox.delete(0, tk.END)
            posts = self.storage.list_posts()
            for post_file in posts:
                self.post_listbox.insert(tk.END, post_file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve archives: {e}")

    def _view_post(self):
        selection = self.post_listbox.curselection()
        if not selection:
            messagebox.showwarning("Select a Post", "Please choose a post from the archives to view.")
            return

        filename = self.post_listbox.get(selection[0])
        try:
            content = self.storage.read_post(filename)
            
            view_window = tk.Toplevel(self.root)
            view_window.title(f"Archive: {filename}")
            view_window.geometry("600x500")
            view_window.configure(bg=self.colors["bg"])
            
            display_text = scrolledtext.ScrolledText(view_window, padx=20, pady=20, font=("Segoe UI", 11),
                                                     bg=self.colors["card"], fg=self.colors["text"],
                                                     borderwidth=0, highlightthickness=0)
            display_text.insert(tk.END, content)
            display_text.configure(state="disabled")
            display_text.pack(fill=tk.BOTH, expand=True)
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
