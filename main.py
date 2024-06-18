import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from itertools import cycle
import backend as be

# Predefined username and password pairs
USERNAMES = ['user1', 'user2', 'user3', 'user4', 'user5']
PASSWORDS = ['password1', 'password2', 'password3', 'password4', 'password5']

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = "grey"
        self.default_fg_color = self["fg"]
        self.user = []
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)

        self.put_placeholder()

    def _on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg_color)

    def _on_focus_out(self, event):
        if not self.get():
            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(fg=self.placeholder_color)

class LoginApp:
    def __init__(self, root, bg_image_path, form_image_path):
        self.root = root
        self.root.title("FutureNse Login")
        self.root.geometry("1366x768")  # Full screen size

        # Create main frames for layout
        self.left_frame = tk.Frame(root, width=683, height=768)  # Half width for left frame
        self.left_frame.pack(side='left', fill='both', expand=True)
        self.right_frame = tk.Frame(root, width=683, height=768, bg='white')  # Half width for right frame
        self.right_frame.pack(side='right', fill='both', expand=True)

        # Load and display background image
        self.bg_image = self.load_image(bg_image_path, (683, 768))

        self.canvas = tk.Canvas(self.left_frame, width=683, height=768)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor='nw')

        # Load and display form image
        self.form_image = self.load_image(form_image_path, (409, 146))

        # Create login form in the right frame
        self.create_login_form()

    def load_image(self, path, size):
        if os.path.exists(path):
            image = Image.open(path)
            image = image.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(image)
        else:
            print(f"Image not found: {path}")
            return None

    def create_login_form(self):
        form_frame = tk.Frame(self.right_frame, bg='white', padx=20, pady=20)
        form_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Add form image
        image_label = tk.Label(form_frame, image=self.form_image, bg='white')
        image_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Username field
        username_label = tk.Label(form_frame, text="Username", font=("Helvetica", 12), bg='white')
        username_label.grid(row=1, column=0, sticky='w', pady=(20, 5))

        username_frame = tk.Frame(form_frame, bg='white')
        username_frame.grid(row=2, column=0, sticky='w')

        # Username entry
        self.username_entry = EntryWithPlaceholder(username_frame, placeholder="Username", width=30, font=("Helvetica", 12), bd=1)
        self.username_entry.grid(row=0, column=0, sticky="ew")

        # Password field
        password_label = tk.Label(form_frame, text="Password", font=("Helvetica", 12), bg='white')
        password_label.grid(row=3, column=0, sticky='w', pady=(20, 5))

        password_frame = tk.Frame(form_frame, bg='white')
        password_frame.grid(row=4, column=0, sticky='w')

        # Password entry
        self.password_entry = EntryWithPlaceholder(password_frame, placeholder="Password", width=30, font=("Helvetica", 12), show="*", bd=1)
        self.password_entry.grid(row=0, column=0, sticky="ew")

        # Remember username checkbox
        # remember_var = tk.IntVar()
        # remember_check = tk.Checkbutton(form_frame, text="Remember username", variable=remember_var, bg='white')
        # remember_check.grid(row=5, column=0, columnspan=2, pady=5, sticky='w')

        # Login button
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="black", foreground="black")
        login_button = ttk.Button(form_frame, text="Log in", style="TButton", command=self.check_credentials)
        login_button.grid(row=6, column=0, columnspan=2, pady=10, ipadx=100)  # Increase button width

        # Forgotten username or password
        forgotten_label = tk.Label(form_frame, text="Forgotten your username or password?", font=("Helvetica", 10), fg="blue", bg='white')
        forgotten_label.grid(row=7, column=0, columnspan=2, pady=5, sticky='w')

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if username and password are in predefined list
        # if username in USERNAMES and password == PASSWORDS[USERNAMES.index(username)]:
        #     messagebox.showinfo("Success", "Login Successful!")
        #     self.show_loading_page(username)
        # else:
        #     messagebox.showerror("Error", "Invalid username or password.")
        l = be.userinfo(username)
        self.user = l
        if l[0]:
            if password == l[0][2]:
                messagebox.showinfo("Success", "Login Successful!")
                self.show_loading_page()
            else:
                messagebox.showerror("Error", "Invalid username or password.")

    def show_loading_page(self):
        # Destroy the main window
        self.root.destroy()

        # Create a new window for the loading page
        loading_window = tk.Tk()
        loading_window.title("Loading")
        loading_window.geometry("1366x768")
        loading_window.configure(bg='white')

        # Display loading animation
        loading_frame = tk.Frame(loading_window, bg='white')
        loading_frame.place(relx=0.5, rely=0.5, anchor='center')

        loading_label = tk.Label(loading_frame, text="Logging in...", font=("Helvetica", 16), bg='white')
        loading_label.pack(pady=20)

        # Infinity symbol animation
        spinner = cycle(['|', '/', '-', '\\'])
        spinner_label = tk.Label(loading_frame, text="", font=("Helvetica", 24), bg='white')
        spinner_label.pack()

        def animate():
            spinner_label.config(text=next(spinner))
            loading_window.after(50, animate)

        animate()

        # Warning message
        warning_label = tk.Label(loading_frame, text="Please do not close the window until we redirect to your new window", font=("Helvetica", 12), fg='grey', bg='white')
        warning_label.pack(pady=20)

        # Show the loading page for 3 seconds before transitioning to the dashboard
        loading_window.after(2500, lambda: self.show_dashboard(loading_window))

    def show_dashboard(self, loading_window):
        loading_window.destroy()

        # Create a new window for the dashboard
        dashboard_window = tk.Tk()
        dashboard_window.title("Dashboard")
        dashboard_window.geometry("1366x768")
        dashboard_window.configure(bg='#F7F9F2')

        # Create top frame for user info and navigation
        top_frame = tk.Frame(dashboard_window, bg='#F5F5F5', height=100)
        top_frame.pack(fill='x')

        # Random text on left side of navigation bar
        random_text_label = tk.Label(top_frame, text="Welcome to Futurense!", font=("Helvetica", 16), bg='#F5F5F5')
        random_text_label.pack(side='left', padx=20)

        # User profile image placeholder
        user_image_path = r"C:\Users\Dell\Desktop\userimage.png"  # Replace with actual path
        user_image = self.load_image(user_image_path, (50, 50))
        user_image_label = tk.Label(top_frame, image=user_image, bg='#F5F5F5')
        user_image_label.image = user_image  # Keep a reference
        user_image_label.pack(side='right', padx=20)

        # User name label
        user_name_label = tk.Label(top_frame, text=self.user[0][4], font=("Helvetica", 16), bg='#F5F5F5')
        user_name_label.pack(side='right')

        # Dashboard content frame
        content_frame = tk.Frame(dashboard_window, bg='white')
        content_frame.pack(fill='both', expand=True)

        # Left portion for courses section
        left_courses_frame = tk.Frame(content_frame, bg='white', width=683, padx=20, pady=20)
        left_courses_frame.pack(side='left', fill='both', expand=True)

        # Paths for course images
        course_images = [
            r"images/c1.jpeg",  # Replace with actual paths
            r"images/c2.jpeg",
            r"images/c3.jpeg",
            r"images/c4.jpeg"
        ]

        # Create grid for courses
        for i in range(2):
            for j in range(2):
                course_frame = tk.Frame(left_courses_frame, bg='white', bd=1, relief='solid', width=500, height=500)

                course_frame.grid(row=i, column=j, padx=75, pady=50, sticky="nsew")

                # Load and display course cover image
                course_image_path = course_images[i*2 + j]
                course_cover_image = self.load_image(course_image_path, (300, 150))
                if course_cover_image:
                    course_cover_label = tk.Label(course_frame, image=course_cover_image, bg='white')
                    course_cover_label.image = course_cover_image  # Keep a reference
                    course_cover_label.pack(pady=(0, 5))

                # Course title label
                course_title_label = tk.Label(course_frame, text=f"Course {i*2 + j + 1}", font=("Helvetica", 12), bg='white')
                course_title_label.pack()

                # Get started button
                get_started_button = ttk.Button(course_frame, text="Get started", style="TButton")
                get_started_button.pack(pady=(5, 0))

        # Right portion for profile information, events, and navigation
        right_profile_frame = tk.Frame(content_frame, bg='grey', width=250)
        right_profile_frame.pack(side='right', fill='y')

        # Profile information section
        profile_frame = tk.Frame(right_profile_frame, bg='grey', bd=1, relief='solid')
        profile_frame.pack(padx=10, pady=10, fill='both', expand=True)

        profile_label = tk.Label(profile_frame, text="Profile Information", font=("Helvetica", 12), bg='grey', fg='white')
        profile_label.pack(pady=10)

        profile_info = {
            "Name": username,
            "Semester": "6th",
            "Year": "2024",
            "Course": "B.Tech CSE (AI & Data Engineering)",
            "Roll No.": "123456",
            "Registration Number": "9876543210"
        }

        for key, value in profile_info.items():
            info_label = tk.Label(profile_frame, text=f"{key}: {value}", font=("Helvetica", 10), bg='grey', fg='white')
            info_label.pack(anchor='w', padx=10, pady=5)

        # Upcoming events section
        events_frame = tk.Frame(right_profile_frame, bg='grey', bd=1, relief='solid')
        events_frame.pack(padx=10, pady=10, fill='both', expand=True)

        events_label = tk.Label(events_frame, text="Upcoming events", font=("Helvetica", 12), bg='grey', fg='white')
        events_label.pack()

        # Placeholder for events content
        events_content = tk.Label(events_frame, text="No upcoming events", font=("Helvetica", 10), bg='grey', fg='white')
        events_content.pack(pady=10)

        # Navigation buttons
        buttons_frame = tk.Frame(right_profile_frame, bg='grey')
        buttons_frame.pack(pady=20, fill='both', expand=True)

        logout_button = ttk.Button(buttons_frame, text="Logout", style="TButton", command=lambda: self.back_to_login(dashboard_window))
        logout_button.pack(pady=10)

        back_to_login_button = ttk.Button(buttons_frame, text="Back to Login Page", style="TButton", command=lambda: self.back_to_login(dashboard_window))
        back_to_login_button.pack(pady=10)

    def back_to_login(self, current_window):
        current_window.destroy()
        root = tk.Tk()
        app = LoginApp(root, bg_image_path, form_image_path)
        root.mainloop()

if __name__ == "__main__":
    # Provide the correct paths to your images
    bg_image_path = r"images/main.png"  # Correct the file path
    form_image_path = r"images/c6.jpeg"  # Provide the correct path to the form image
    root = tk.Tk()
    app = LoginApp(root, bg_image_path, form_image_path)
    root.mainloop()
