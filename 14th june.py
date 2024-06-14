import tkinter as tk
from tkinter import ttk

class StudentDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Dashboard")
        self.geometry("1200x600")
        self.configure(bg="#f5f5f5")

        # Header
        header_frame = tk.Frame(self, bg="white", padx=10, pady=10)
        header_frame.pack(fill=tk.X)

        logo = tk.Label(header_frame, text="Lovely Professional University", font=("Arial", 14))
        logo.pack(side=tk.LEFT)

        user_info = tk.Frame(header_frame, bg="white")
        user_info.pack(side=tk.RIGHT)

        user_name = tk.Label(user_info, text="Madhav Hemakumar Hemakumar", font=("Arial", 12))
        user_name.pack(side=tk.LEFT, padx=5)

        profile_image = tk.Label(user_info, text="[Profile Image]", font=("Arial", 12))
        profile_image.pack(side=tk.LEFT, padx=5)

        # Program Overview
        program_frame = tk.Frame(self, bg="#f5f5f5", padx=20, pady=20)
        program_frame.pack(fill=tk.X)

        program_title = tk.Label(program_frame, text="Program Overview : B.Tech CSE (AI & Data Engineering)", font=("Arial", 18), bg="#f5f5f5")
        program_title.pack(anchor=tk.W)

        # Courses
        courses_frame = tk.Frame(program_frame, bg="#f5f5f5")
        courses_frame.pack(fill=tk.X, pady=10)

        courses = [
            ("LPU Bootcamp 1", "bootcamp.png", "Get started", 0),
            ("Data Communication and Computer Networks", "course1.png", "Get started", 100),
            ("Data Structures & Algorithms", "course2.png", "Get started", 100),
            ("Database Design and Modelling (SQL)", "course3.png", "Get started", 0),
        ]

        for course in courses:
            course_card = self.create_course_card(courses_frame, *course)
            course_card.pack(side=tk.LEFT, padx=10)

        # Sidebar
        sidebar_frame = tk.Frame(self, bg="#f5f5f5", padx=20, pady=20)
        sidebar_frame.pack(fill=tk.Y, side=tk.LEFT, anchor=tk.N)

        courses_label = tk.Label(sidebar_frame, text="Total Courses: 8", font=("Arial", 12), bg="#f5f5f5")
        courses_label.pack(anchor=tk.NW)

        timetable_label = tk.Label(sidebar_frame, text="Timetable", font=("Arial", 12), bg="#f5f5f5")
        timetable_label.pack(anchor=tk.NW, pady=(20, 5))

        # Timetable frame
        timetable_frame = tk.Frame(sidebar_frame, bg="white", bd=1, relief=tk.SOLID)
        timetable_frame.pack(fill=tk.X, pady=5)

        days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
        for day in days:
            day_label = tk.Label(timetable_frame, text=day, font=("Arial", 10), bg="white", padx=5, pady=5)
            day_label.pack(side=tk.LEFT, padx=2)

        no_events_label = tk.Label(sidebar_frame, text="There are no upcoming events", font=("Arial", 10), bg="#f5f5f5")
        no_events_label.pack(anchor=tk.NW, pady=10)

        calendar_button = tk.Button(sidebar_frame, text="Go to calendar", font=("Arial", 10))
        calendar_button.pack(anchor=tk.NW)

    def create_course_card(self, parent, title, image_path, button_text, progress):
        card_frame = tk.Frame(parent, bg="white", bd=1, relief=tk.SOLID, width=200, height=150)
        card_frame.pack_propagate(False)

        # Placeholder for course image
        course_image = tk.Label(card_frame, text="[Image]", font=("Arial", 12), width=30, height=10)
        course_image.pack()

        course_title = tk.Label(card_frame, text=title, font=("Arial", 12), wraplength=180, bg="white")
        course_title.pack(pady=5)

        if progress:
            progress_label = tk.Label(card_frame, text=f"{progress}% complete", font=("Arial", 10), bg="white")
            progress_label.pack()

        start_button = tk.Button(card_frame, text=button_text, font=("Arial", 10))
        start_button.pack(pady=5)

        return card_frame

if __name__ == "__main__":
    app = StudentDashboard()
    app.mainloop()
