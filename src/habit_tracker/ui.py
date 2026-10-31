import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Setting the app's appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Setting the title and the default size
        self.title("Habit Tracker")
        self.geometry("800x600")

        # Configuring the grid for the app
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Configuring the header frame
        self.header = ctk.CTkFrame(master=self)
        self.header.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Making the header title label
        self.header_title = ctk.CTkLabel(
            master=self.header,
            text_color="white",
            text=" Habit Tracker",
            font=(ctk.CTkFont(family="Inter", size=50, weight="bold")),
        )
        self.header_title.grid(row=0, column=0, sticky="w")

        # Configuring the main content frame
        self.content = ctk.CTkFrame(master=self)
        self.content.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=0)

        # Configuring the daily overview frame
        self.daily_overview = ctk.CTkFrame(master=self.content)
        self.daily_overview.grid(row=0, column=0, sticky="ew")
        self.daily_overview.grid_rowconfigure(0, weight=1)
        self.daily_overview.grid_rowconfigure(1, weight=1)
        self.daily_overview.grid_rowconfigure(2, weight=3)
        self.daily_overview.grid_rowconfigure(3, weight=1)
        self.daily_overview.grid_columnconfigure(0, weight=1)

        # Configuring the daily overview header
        self.daily_overview_header = ctk.CTkLabel(
            master=self.daily_overview,
            text_color="white",
            text=" Daily Overview",
            font=ctk.CTkFont(family="Inter", size=24, weight="bold"),
        )
        self.daily_overview_header.grid(row=0, column=0, sticky="w", padx=10, pady=0)

        # Configuring the daily overview date
        self.daily_overview_date = ctk.CTkLabel(
            master=self.daily_overview,
            text_color="white",
            text=" Friday, 30 October",
            font=ctk.CTkFont(family="Inter", size=16, weight="bold"),
        )
        self.daily_overview_date.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        # Configuring the statistics frame inside the daily overview frame
        self.daily_overview_statistics = ctk.CTkFrame(master=self.daily_overview)
        self.daily_overview_statistics.grid(
            row=2, column=0, sticky="ew", padx=10, pady=10
        )
        self.daily_overview_statistics.grid_columnconfigure(0, weight=1)
        self.daily_overview_statistics.grid_columnconfigure(1, weight=1)
        self.daily_overview_statistics.grid_columnconfigure(2, weight=1)
        self.daily_overview_statistics.grid_rowconfigure(0, weight=1)

        # Configuring the habits done frame
        self.daily_overview_statistics_habits_done = ctk.CTkFrame(
            master=self.daily_overview_statistics
        )
        self.daily_overview_statistics_habits_done.grid(
            row=0, column=0, sticky="nsew", padx=10, pady=10
        )

        self.daily_overview_statistics_habits_done.grid_columnconfigure(0, weight=1)
        self.daily_overview_statistics_habits_done.grid_rowconfigure(0, weight=2)
        self.daily_overview_statistics_habits_done.grid_rowconfigure(1, weight=1)

        # Configuring the habits done fraction
        self.daily_overview_statistics_habits_done_fraction = ctk.CTkLabel(
            master=self.daily_overview_statistics_habits_done,
            text_color="white",
            text="4/6",
            font=ctk.CTkFont(family="Inter", size=50, weight="bold"),
        )

        self.daily_overview_statistics_habits_done_fraction.grid(
            row=0, column=0, sticky="nsew", padx=10, pady=10
        )

        # Configuring the habits done label
        self.daily_overview_statistics_habits_done_label = ctk.CTkLabel(
            master=self.daily_overview_statistics_habits_done,
            text_color="white",
            text="Habits done",
            font=ctk.CTkFont(family="Inter", size=14, weight="normal"),
        )

        self.daily_overview_statistics_habits_done_label.grid(
            row=1, column=0, sticky="nsew", padx=10, pady=10
        )

        # Configuring the aligner time frame
        self.daily_overview_statistics_aligner_time = ctk.CTkFrame(
            master=self.daily_overview_statistics
        )
        self.daily_overview_statistics_aligner_time.grid(
            row=0, column=1, sticky="nsew", padx=10, pady=10
        )
        self.daily_overview_statistics_aligner_time.grid_columnconfigure(0, weight=1)
        self.daily_overview_statistics_aligner_time.grid_rowconfigure(0, weight=2)
        self.daily_overview_statistics_aligner_time.grid_rowconfigure(1, weight=1)

        # Configuring the alginer time number
        self.daily_overview_statistics_aligner_time_number = ctk.CTkLabel(
            master=self.daily_overview_statistics_aligner_time,
            text_color="white",
            text="17h 32m",
            font=ctk.CTkFont(family="Inter", size=50, weight="bold"),
        )
        self.daily_overview_statistics_aligner_time_number.grid(
            row=0, column=0, sticky="nsew", padx=10, pady=10
        )

        # Configuring the aligner time label
        self.daily_overview_statistics_aligner_time_label = ctk.CTkLabel(
            master=self.daily_overview_statistics_aligner_time,
            text_color="white",
            text="Aligner wear",
            font=ctk.CTkFont(family="Inter", size=14, weight="normal"),
        )
        self.daily_overview_statistics_aligner_time_label.grid(
            row=1, column=0, sticky="nsew", padx=10, pady=10
        )

        # Configuring the daily progress frame
        self.daily_overview_statistics_daily_progress = ctk.CTkFrame(
            master=self.daily_overview_statistics
        )
        self.daily_overview_statistics_daily_progress.grid(
            row=0, column=2, sticky="nsew", padx=10, pady=10
        )
        self.daily_overview_statistics_daily_progress.grid_columnconfigure(0, weight=1)
        self.daily_overview_statistics_daily_progress.grid_rowconfigure(0, weight=2)
        self.daily_overview_statistics_daily_progress.grid_rowconfigure(1, weight=1)

        # Configuring the daily progress percentage
        self.daily_overview_statistics_daily_progress_percentage = ctk.CTkLabel(
            master=self.daily_overview_statistics_daily_progress,
            text_color="white",
            text="67%",
            font=ctk.CTkFont(family="Inter", size=50, weight="bold"),
        )

        self.daily_overview_statistics_daily_progress_percentage.grid(
            row=0, column=0, sticky="nsew", padx=10, pady=10
        )

        # Configuring the daily progress label
        self.daily_overview_statistics_daily_progress_label = ctk.CTkLabel(
            master=self.daily_overview_statistics_daily_progress,
            text_color="white",
            text="Daily progress",
            font=ctk.CTkFont(family="Inter", size=14, weight="normal"),
        )
        self.daily_overview_statistics_daily_progress_label.grid(
            row=1, column=0, sticky="nsew", padx=10, pady=10
        )

        # Configuring the progress bar frame
        self.daily_overview_progress_bar = ctk.CTkFrame(master=self.daily_overview)

        self.daily_overview_progress_bar.grid(
            row=3, column=0, sticky="ew", padx=10, pady=10
        )

        self.daily_overview_progress_bar.grid_columnconfigure(0, weight=1)
        self.daily_overview_progress_bar.grid_columnconfigure(1, weight=0, minsize=80)
        self.daily_overview_progress_bar.grid_rowconfigure(0, weight=1)
        self.daily_overview_progress_bar.grid_rowconfigure(1, weight=1)

        # Configuring the progress bar header
        self.daily_overview_progress_bar_header = ctk.CTkLabel(
            master=self.daily_overview_progress_bar,
            text_color="white",
            text="Overall Progress",
            font=ctk.CTkFont(family="Inter", size=20, weight="bold"),
        )
        self.daily_overview_progress_bar_header.grid(
            row=0, column=0, sticky="nw", padx=10, pady=10
        )

        # Configuring the daily progress bar percentage
        self.daily_overview_progress_bar_percentage = ctk.CTkLabel(
            master=self.daily_overview_progress_bar,
            text_color="white",
            text="67%",
            font=ctk.CTkFont(family="Inter", size=20, weight="normal"),
            width=60,
        )
        self.daily_overview_progress_bar_percentage.grid(
            row=0, column=1, sticky="e", padx=10, pady=10
        )

        # Configuring the daily progress bar bar
        self.daily_overview_progress_bar_bar = ctk.CTkProgressBar(
            master=self.daily_overview_progress_bar,
            width=300,
            height=15,
        )

        self.daily_overview_progress_bar_bar.grid(
            row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10
        )
        self.daily_overview_progress_bar_bar.set(0.67)

        self.daily_overview_statistics_daily_progress.configure(fg_color="transparent")
