import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class LearningManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lovely Professional University")
        self.geometry("1200x800")
        
        # Header Frame
        header_frame = tk.Frame(self)
        header_frame.pack(side=tk.TOP, fill=tk.X)
        
        university_label = tk.Label(header_frame, text="Lovely Professional University", font=("Arial", 16))
        university_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        profile_name_label = tk.Label(header_frame, text="Madhav Hemakumar Hemakumar", font=("Arial", 14))
        profile_name_label.pack(side=tk.RIGHT, padx=20, pady=10)
        
        profile_image_label = tk.Label(header_frame, text="[Profile Image]", font=("Arial", 14))
        profile_image_label.pack(side=tk.RIGHT, padx=10, pady=10)

        # Program Overview
        program_label = tk.Label(self, text="Program Overview : B.Tech CSE (AI & Data Engineering)", font=("Arial", 14))
        program_label.pack(pady=10)

        # Courses Frame
        courses_frame = tk.Frame(self)
        courses_frame.pack(pady=10)

        # Load images and create labels
        image_paths = [
            r"C:\Users\devua\OneDrive\Desktop\MADHAV\bootcamp\Data Structures   Algorithms.png",
            r"C:\Users\devua\OneDrive\Desktop\MADHAV\bootcamp\Database Design  and Modelling  (SQL).png",
            r"C:\Users\devua\OneDrive\Desktop\MADHAV\bootcamp\Data  Communication  and Computer  Networks.png"
        ]
        
        for path in image_paths:
            if os.path.exists(path):
                img = Image.open(path)
                img = img.resize((150, 150), Image.LANCZOS)  # Resize image using LANCZOS
                photo = ImageTk.PhotoImage(img)
                course_label = tk.Label(courses_frame, image=photo, relief="solid")
                course_label.image = photo  # Keep a reference to avoid garbage collection
                course_label.pack(side=tk.LEFT, padx=10)
            else:
                course_label = tk.Label(courses_frame, text="[Image Not Found]", font=("Arial", 14), width=20, height=10, relief="solid")
                course_label.pack(side=tk.LEFT, padx=10)

        # Sidebar Frame
        sidebar_frame = tk.Frame(self)
        sidebar_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20)

        total_courses_label = tk.Label(sidebar_frame, text="Total Courses: 8", font=("Arial", 14))
        total_courses_label.pack(pady=10)

        timetable_label = tk.Label(sidebar_frame, text="Timetable", font=("Arial", 14))
        timetable_label.pack(pady=10)

        timetable_days_frame = tk.Frame(sidebar_frame)
        timetable_days_frame.pack(pady=5)
        
        days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
        for day in days:
            day_button = tk.Button(timetable_days_frame, text=day, font=("Arial", 10))
            day_button.pack(side=tk.LEFT, padx=2)

        no_events_label = tk.Label(sidebar_frame, text="There are no upcoming events", font=("Arial", 12))
        no_events_label.pack(pady=10)

        calendar_button = tk.Button(sidebar_frame, text="Go to calendar", font=("Arial", 12))
        calendar_button.pack(pady=5)

if __name__ == "__main__":
    app = LearningManagementSystem()
    app.mainloop()

