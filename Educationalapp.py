
# import tkinter as tk
# from tkinter import ttk, messagebox

# # Apply styling
# style = ttk.Style()
# style.theme_use('default')
# style.configure('Menu.TButton', font=('Helvetica', 12, 'bold'), padding=(10, 10), relief='flat')
# style.map('Menu.TButton', background=[('active', '#d9d9d9')])
# style.configure('TFrame', background='#f5f5f5')
# style.configure('TLabel', background='#f5f5f5')

# class TradingApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Trading Education App")
#         self.geometry("900x650")
#         self.configure(bg='#f5f5f5')

#         # Side menu on the left with fixed width
#         side_menu = ttk.Frame(self, width=220, style='TFrame')
#         side_menu.pack(side="left", fill="y")
#         side_menu.pack_propagate(False)

#         ttk.Label(side_menu, text="Menu", font=('Helvetica', 16, 'bold')).pack(pady=(20,10))

#         # Home button
#         ttk.Button(side_menu, text="Home", style='Menu.TButton',
#                    command=lambda: self.show_frame(HomePage)).pack(fill="x", pady=5, padx=15)

#         # Lessons dropdown
#         self.lessons_expanded = False
#         lesson_btn = ttk.Button(side_menu, text="Lessons ▼", style='Menu.TButton',
#                                 command=self.toggle_lessons)
#         lesson_btn.pack(fill="x", pady=(5,0), padx=15)
#         self.lesson_btn = lesson_btn

#         # Submenu frame for lesson topics
#         topics = [
#             "What is a Stock?",
#             "Reading Candlestick Charts",
#             "Fundamental Analysis",
#             "Technical Indicators",
#             "Order Types",
#             "Risk Management"
#         ]
#         sub_frame = ttk.Frame(side_menu, style='TFrame')
#         self.sub_frame = sub_frame
#         for idx, topic in enumerate(topics):
#             btn = ttk.Button(sub_frame, text=topic, style='Menu.TButton',
#                              command=lambda i=idx: self.show_lesson(i))
#             btn.pack(fill="x", pady=2)

#         # Quiz and Simulator buttons
#         ttk.Button(side_menu, text="Quiz", style='Menu.TButton',
#                    command=lambda: self.show_frame(QuizPage)).pack(fill="x", pady=5, padx=15)
#         ttk.Button(side_menu, text="Simulator", style='Menu.TButton',
#                    command=lambda: self.show_frame(SimulatorPage)).pack(fill="x", pady=5, padx=15)

#         # Content container
#         container = ttk.Frame(self, style='TFrame')
#         container.pack(side="right", fill="both", expand=True, padx=20, pady=20)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         # Initialize frames
#         self.frames = {}
#         for F in (HomePage, LessonsPage, QuizPage, SimulatorPage):
#             frame = F(container, self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")

#         self.show_frame(HomePage)

#     def toggle_lessons(self):
#         # Expand/collapse lessons submenu
#         self.lessons_expanded = not self.lessons_expanded
#         if self.lessons_expanded:
#             self.sub_frame.pack(fill="x", padx=30, after=self.lesson_btn)
#             self.lesson_btn.config(text="Lessons ▲")
#         else:
#             self.sub_frame.pack_forget()
#             self.lesson_btn.config(text="Lessons ▼")

#     def show_frame(self, page):
#         frame = self.frames[page]
#         frame.tkraise()

#     def show_lesson(self, index):
#         lessons_page = self.frames[LessonsPage]
#         lessons_page.display_topic(index)
#         self.show_frame(LessonsPage)

# # Base for centered page content
# class CenteredPage(ttk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, style='TFrame')
#         wrapper = ttk.Frame(self, style='TFrame')
#         wrapper.place(relx=0.5, rely=0.5, anchor='center')
#         self.wrapper = wrapper

# class HomePage(CenteredPage):
#     def __init__(self, parent, controller):
#         super().__init__(parent, controller)
#         ttk.Label(self.wrapper, text="Welcome to Trading Education", font=('Helvetica', 20, 'bold')).pack(pady=10)
#         intro = (
#             "Learn the basics of trading, test your knowledge with quizzes, "
#             "and practice with a simple simulator.")
#         ttk.Label(self.wrapper, text=intro, wraplength=600, justify='center').pack(pady=10)

# class LessonsPage(CenteredPage):
#     def __init__(self, parent, controller):
#         super().__init__(parent, controller)
#         ttk.Label(self.wrapper, text="Lessons", font=('Helvetica', 18, 'bold')).pack(pady=10)
#         self.content = ttk.Label(self.wrapper, text="Select a lesson from the menu.",
#                                  wraplength=700, justify='left', font=('Helvetica', 12))
#         self.content.pack(pady=20)
#         # Predefined lesson contents
#         self.topics = [
#             "Stocks are shares representing ownership in a company. When you buy a stock, you own a fraction of that company. Stocks trade on exchanges, and prices fluctuate based on supply, demand, and company performance.",
#             "Candlestick charts display price data for a set period. Each candlestick shows the open, high, low, and close. The body color indicates market sentiment: green for upward movement, red for downward.",
#             "Fundamental analysis evaluates a company's intrinsic value by examining financial statements, revenue, earnings, growth prospects, and economic indicators. It helps determine if a stock is undervalued or overvalued.",
#             "Technical indicators are mathematical calculations based on price and volume. Common ones include Moving Averages, RSI (Relative Strength Index), and MACD (Moving Average Convergence Divergence). They help identify trends and potential reversal points.",
#             "Order types dictate how trades are executed. Market orders fill immediately at current prices. Limit orders set a specific price. Stop orders trigger once a price threshold is met, often used for stop-loss to manage risk.",
#             "Risk management involves setting position sizes, using stop-loss orders, diversifying portfolios, and understanding your risk tolerance. Effective risk management preserves capital and controls drawdowns."
#         ]

#     def display_topic(self, index):
#         if 0 <= index < len(self.topics):
#             self.content.config(text=self.topics[index])
#         else:
#             self.content.config(text="Topic not found.")

# class QuizPage(CenteredPage):
#     def __init__(self, parent, controller):
#         super().__init__(parent, controller)
#         ttk.Label(self.wrapper, text="Quiz", font=('Helvetica', 18, 'bold')).pack(pady=10)
#         self.questions = [
#             {"q": "What does IPO stand for?", "options": ["Initial Price Offering", "Initial Public Offering", "Internal Public Offering"], "answer": 1},
#             {"q": "A 'bull market' means prices are...?", "options": ["Falling", "Rising", "Stable"], "answer": 1},
#             {"q": "What is a pip in forex trading?", "options": ["Price interest point", "Percentage in point", "Price increment point"], "answer": 2},
#             {"q": "Which order type guarantees execution but not price?", "options": ["Limit order", "Stop order", "Market order"], "answer": 2},
#             {"q": "What does RSI measure?", "options": ["Volume","Momentum","Volatility"], "answer": 1},
#             {"q": "A red candlestick indicates...", "options": ["Price closed higher","Price closed lower","No change"], "answer": 1}
#         ]
#         self.current = 0
#         self.score = 0
#         self.question_label = ttk.Label(self.wrapper, wraplength=600, font=('Helvetica', 14))
#         self.question_label.pack(pady=10)
#         self.var = tk.IntVar()
#         self.opts = []
#         for i in range(3):
#             rb = ttk.Radiobutton(self.wrapper, variable=self.var, value=i)
#             rb.pack(anchor='w', pady=2)
#             self.opts.append(rb)
#         ttk.Button(self.wrapper, text="Submit", style='Menu.TButton', command=self.check_answer).pack(pady=10)
#         self.result = ttk.Label(self.wrapper, text="", font=('Helvetica', 12))
#         self.result.pack(pady=5)
#         self.load_question()

#     def load_question(self):
#         qdata = self.questions[self.current]
#         self.question_label.config(text=qdata["q"])
#         for i, opt in enumerate(qdata["options"]):
#             self.opts[i].config(text=opt)
#         self.var.set(-1)
#         self.result.config(text="")

#     def check_answer(self):
#         selected = self.var.get()
#         correct = self.questions[self.current]["answer"]
#         if selected == correct:
#             self.score += 1
#             self.result.config(text="Correct!", foreground="green")
#         else:
#             self.result.config(text="Incorrect.", foreground="red")
#         self.current += 1
#         if self.current < len(self.questions):
#             self.after(500, self.load_question)
#         else:
#             messagebox.showinfo("Quiz Results", f"Your score: {self.score}/{len(self.questions)}")

# class SimulatorPage(CenteredPage):
#     def __init__(self, parent, controller):
#         super().__init__(parent, controller)
#         ttk.Label(self.wrapper, text="Simulator", font=('Helvetica', 18, 'bold')).pack(pady=10)
#         ttk.Label(self.wrapper, text="Enter an amount to invest:", font=('Helvetica', 12)).pack(pady=5)
#         self.amount = tk.DoubleVar()
#         ttk.Entry(self.wrapper, textvariable=self.amount, font=('Helvetica', 12)).pack(pady=5)
#         ttk.Button(self.wrapper, text="Simulate Growth", style='Menu.TButton', command=self.simulate).pack(pady=10)
#         self.result = ttk.Label(self.wrapper, text="", font=('Helvetica', 12))
#         self.result.pack(pady=5)

#     def simulate(self):
#         start = self.amount.get()
#         value = start
#         for _ in range(12):
#             value *= 1.05
#         self.result.config(text=f"Value after 1 year: {value:.2f}")

# if __name__ == "__main__":
#     app = TradingApp()
#     app.mainloop()












import tkinter as tk
from tkinter import ttk, messagebox

# Apply styling
ttstyle = ttk.Style()
ttstyle.theme_use('default')
ttstyle.configure('Menu.TButton', font=('Helvetica', 12, 'bold'), padding=(10, 10), relief='flat')
ttstyle.map('Menu.TButton', background=[('active', '#d9d9d9')])
ttstyle.configure('TFrame', background='#f5f5f5')
ttstyle.configure('TLabel', background='#f5f5f5')

class TradingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trading Education App")
        self.geometry("900x650")
        self.configure(bg='#f5f5f5')

        # Side menu on the left
        side_menu = ttk.Frame(self, width=220, style='TFrame')
        side_menu.pack(side="left", fill="y")
        side_menu.pack_propagate(False)

        ttk.Label(side_menu, text="Menu", font=('Helvetica', 16, 'bold')).pack(pady=(20,10))
        ttk.Button(side_menu, text="Home", style='Menu.TButton',
                   command=lambda: self.show_frame(HomePage)).pack(fill="x", pady=5, padx=15)

        # Lessons dropdown
        self.lessons_expanded = False
        self.lesson_btn = ttk.Button(side_menu, text="Lessons ▼", style='Menu.TButton',
                                     command=self.toggle_lessons)
        self.lesson_btn.pack(fill="x", pady=(5,0), padx=15)
        topics = ["What is a Stock?","Reading Candlestick Charts","Fundamental Analysis",
                  "Technical Indicators","Order Types","Risk Management"]
        self.sub_frame = ttk.Frame(side_menu, style='TFrame')
        for idx, topic in enumerate(topics):
            btn = ttk.Button(self.sub_frame, text=topic, style='Menu.TButton',
                             command=lambda i=idx: self.show_lesson(i))
            btn.pack(fill="x", pady=2)

        ttk.Button(side_menu, text="Quiz", style='Menu.TButton',
                   command=lambda: self.show_frame(QuizPage)).pack(fill="x", pady=5, padx=15)
        ttk.Button(side_menu, text="Simulator", style='Menu.TButton',
                   command=lambda: self.show_frame(SimulatorPage)).pack(fill="x", pady=5, padx=15)

        # Container for main content
        container = ttk.Frame(self, style='TFrame')
        container.pack(side="right", fill="both", expand=True, padx=20, pady=20)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, LessonsPage, QuizPage, SimulatorPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def toggle_lessons(self):
        self.lessons_expanded = not self.lessons_expanded
        if self.lessons_expanded:
            self.sub_frame.pack(fill="x", padx=30, after=self.lesson_btn)
            self.lesson_btn.config(text="Lessons ▲")
        else:
            self.sub_frame.pack_forget()
            self.lesson_btn.config(text="Lessons ▼")

    def show_frame(self, page):
        self.frames[page].tkraise()

    def show_lesson(self, index):
        lessons_page = self.frames[LessonsPage]
        lessons_page.display_topic(index)
        self.show_frame(LessonsPage)

class CenteredPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='TFrame')
        wrapper = ttk.Frame(self, style='TFrame')
        wrapper.place(relx=0.5, rely=0.5, anchor='center')
        self.wrapper = wrapper

class HomePage(CenteredPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        ttk.Label(self.wrapper, text="Welcome to Trading Education", font=('Helvetica', 20, 'bold')).pack(pady=10)
        intro = ("Learn the basics of trading, test your knowledge with quizzes, and practice with a smart simulator.")
        ttk.Label(self.wrapper, text=intro, wraplength=600, justify='center').pack(pady=10)

class LessonsPage(CenteredPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        ttk.Label(self.wrapper, text="Lessons", font=('Helvetica', 18, 'bold')).pack(pady=10)
        self.content = ttk.Label(self.wrapper, text="Select a lesson from the menu.",
                                 wraplength=700, justify='left', font=('Helvetica', 12))
        self.content.pack(pady=20)
        self.topics = [
            "Stocks are shares representing ownership in a company. When you buy a stock, you own a fraction of that company. Stocks trade on exchanges, and prices fluctuate based on supply, demand, and company performance.",
            "Candlestick charts display price data for a set period. Each candlestick shows the open, high, low, and close. The body color indicates market sentiment: green for upward movement, red for downward.",
            "Fundamental analysis evaluates a company's intrinsic value by examining financial statements, revenue, earnings, growth prospects, and economic indicators. It helps determine if a stock is undervalued or overvalued.",
            "Technical indicators are mathematical calculations based on price and volume. Common ones include Moving Averages, RSI (Relative Strength Index), and MACD (Moving Average Convergence Divergence). They help identify trends and potential reversal points.",
            "Order types dictate how trades are executed. Market orders fill immediately at current prices. Limit orders set a specific price. Stop orders trigger once a price threshold is met, often used for stop-loss to manage risk.",
            "Risk management involves setting position sizes, using stop-loss orders, diversifying portfolios, and understanding your risk tolerance. Effective risk management preserves capital and controls drawdowns."
        ]

    def display_topic(self, index):
        if 0 <= index < len(self.topics):
            self.content.config(text=self.topics[index])
        else:
            self.content.config(text="Topic not found.")

class QuizPage(CenteredPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        ttk.Label(self.wrapper, text="Quiz", font=('Helvetica', 18, 'bold')).pack(pady=10)
        self.questions = [
            {"q": "What does IPO stand for?", "options": ["Initial Price Offering", "Initial Public Offering", "Internal Public Offering"], "answer": 1},
            {"q": "A 'bull market' means prices are...?", "options": ["Falling", "Rising", "Stable"], "answer": 1},
            {"q": "What is a pip in forex trading?", "options": ["Price interest point", "Percentage in point", "Price increment point"], "answer": 1},
            {"q": "Which order type guarantees execution but not price?", "options": ["Limit order", "Stop order", "Market order"], "answer": 2},
            {"q": "What does RSI measure?", "options": ["Volume", "Momentum", "Volatility"], "answer": 1},
            {"q": "A red candlestick indicates...", "options": ["Price closed higher", "Price closed lower", "No change"], "answer": 1}
        ]
        self.current = 0
        self.score = 0
        self.question_label = ttk.Label(self.wrapper, wraplength=600, font=('Helvetica', 14))
        self.question_label.pack(pady=10)
        self.var = tk.IntVar(value=-1)
        self.opts = []
        for i in range(3):
            rb = ttk.Radiobutton(self.wrapper, variable=self.var, value=i)
            rb.pack(anchor='w', pady=2)
            self.opts.append(rb)
        ttk.Button(self.wrapper, text="Submit", style='Menu.TButton', command=self.check_answer).pack(pady=10)
        self.result = ttk.Label(self.wrapper, text="", font=('Helvetica', 12))
        self.result.pack(pady=5)
        self.load_question()

    def load_question(self):
        qdata = self.questions[self.current]
        self.question_label.config(text=qdata["q"])
        for idx, opt in enumerate(qdata["options"]):
            self.opts[idx].config(text=opt)
        self.var.set(-1)
        self.result.config(text="")

    def check_answer(self):
        selected = self.var.get()
        if selected < 0:
            messagebox.showwarning("No selection", "Please select an answer before submitting.")
            return
        correct = self.questions[self.current]["answer"]
        if selected == correct:
            self.score += 1
            self.result.config(text="Correct!", foreground="green")
        else:
            correct_text = self.questions[self.current]["options"][correct]
            self.result.config(text=f"Incorrect. Correct answer: {correct_text}", foreground="red")
        self.current += 1
        if self.current < len(self.questions):
            self.after(800, self.load_question)
        else:
            messagebox.showinfo("Quiz Results", f"Your score: {self.score}/{len(self.questions)}")
            # Reset for retry
            self.current = 0
            self.score = 0
            self.load_question()

class SimulatorPage(CenteredPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        ttk.Label(self.wrapper, text="Simulator", font=('Helvetica', 18, 'bold')).pack(pady=10)
        ttk.Label(self.wrapper, text="Principal Amount:", font=('Helvetica', 12)).pack(pady=5)
        self.principal = tk.DoubleVar(value=1000)
        ttk.Entry(self.wrapper, textvariable=self.principal, font=('Helvetica', 12)).pack(pady=5)
        ttk.Label(self.wrapper, text="Annual Rate (%) :", font=('Helvetica', 12)).pack(pady=5)
        self.rate = tk.DoubleVar(value=5)
        ttk.Entry(self.wrapper, textvariable=self.rate, font=('Helvetica', 12)).pack(pady=5)
        ttk.Label(self.wrapper, text="Years:", font=('Helvetica', 12)).pack(pady=5)
        self.years = tk.IntVar(value=1)
        ttk.Entry(self.wrapper, textvariable=self.years, font=('Helvetica', 12)).pack(pady=5)
        ttk.Button(self.wrapper, text="Calculate Growth", style='Menu.TButton', command=self.simulate).pack(pady=10)
        self.result = ttk.Label(self.wrapper, text="", font=('Helvetica', 12))
        self.result.pack(pady=5)

    def simulate(self):
        P = self.principal.get()
        r = self.rate.get() / 100
        t = self.years.get()
        # Compound annually
        A = P * ((1 + r) ** t)
        self.result.config(text=f"After {t} year(s): ₦{A:,.2f}")

if __name__ == "__main__":
    app = TradingApp()
    app.mainloop()







# import tkinter as tk
# from tkinter import ttk, messagebox

# # Apply styling
# ttstyle = ttk.Style()
# ttstyle.theme_use('default')
# ttstyle.configure('Menu.TButton', font=('Helvetica', 12, 'bold'), padding=(10, 10), relief='flat')
# ttstyle.map('Menu.TButton', background=[('active', '#d9d9d9')])
# ttstyle.configure('TFrame', background='#f5f5f5')
# ttstyle.configure('TLabel', background='#f5f5f5')

# class TradingApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Trading Education App")
#         self.geometry("900x650")
#         self.configure(bg='#f5f5f5')

#         # Side menu on the left
#         side_menu = ttk.Frame(self, width=220, style='TFrame')
#         side_menu.pack(side="left", fill="y")
#         side_menu.pack_propagate(False)

#         ttk.Label(side_menu, text="Menu", font=('Helvetica', 16, 'bold')).pack(pady=(20,10))
#         ttk.Button(side_menu, text="Home", style='Menu.TButton',
#                    command=lambda: self.show_frame(HomePage)).pack(fill="x", pady=5, padx=15)

#         # Lessons dropdown
#         self.lessons_expanded = False
#         self.lesson_btn = ttk.Button(side_menu, text="Lessons ▼", style='Menu.TButton',
#                                      command=self.toggle_lessons)
#         self.lesson_btn.pack(fill="x", pady=(5,0), padx=15)
#         topics = ["What is a Stock?","Reading Candlestick Charts","Fundamental Analysis",
#                   "Technical Indicators","Order Types","Risk Management"]
#         self.sub_frame = ttk.Frame(side_menu, style='TFrame')
#         for idx, topic in enumerate(topics):
#             btn = ttk.Button(self.sub_frame, text=topic, style='Menu.TButton',
#                              command=lambda i=idx: self.show_lesson(i))
#             btn.pack(fill="x", pady=2)

#         ttk.Button(side_menu, text="Quiz", style='Menu.TButton',
#                    command=lambda: self.show_frame(QuizPage)).pack(fill="x", pady=5, padx=15)
#         ttk.Button(side_menu, text="Simulator", style='Menu.TButton',
#                    command=lambda: self.show_frame(SimulatorPage)).pack(fill="x", pady=5, padx=15)

#         # Container for main content
#         container = ttk.Frame(self, style='TFrame')
#         container.pack(side="right", fill="both", expand=True, padx=20, pady=20)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         self.frames = {}
#         for F in (HomePage, LessonsPage, QuizPage, SimulatorPage):
#             frame = F(container, self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")

#         self.show_frame(HomePage)

#     def toggle_lessons(self):
#         self.lessons_expanded = not self.lessons_expanded
#         if self.lessons_expanded:
#             self.sub_frame.pack(fill="x", padx=30, after=self.lesson_btn)
#             self.lesson_btn.config(text="Lessons ▲")
#         else:
#             self.sub_frame.pack_forget()
#             self.lesson_btn.config(text="Lessons ▼")

#     def show_frame(self, page):
#         self.frames[page].tkraise()
#         self.frames[page].update_title(page.__name__.replace('Page', ''))

#     def show_lesson(self, index):
#         lessons_page = self.frames[LessonsPage]
#         lessons_page.display_topic(index)
#         self.show_frame(LessonsPage)

# class CenteredPage(ttk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, style='TFrame')
#         wrapper = ttk.Frame(self, style='TFrame')
#         wrapper.place(relx=0.5, rely=0.5, anchor='center')
#         self.wrapper = wrapper
#         self.title_label = ttk.Label(wrapper, text="", font=('Helvetica', 20, 'bold'))
#         self.title_label.pack(pady=(0, 10))

#     def update_title(self, title):
#         self.title_label.config(text=title)

# class HomePage(CenteredPage):
#     def __init__(self, parent, controller):
#         super().__init__(parent, controller)
#         intro = ("Learn the basics of trading, test your knowledge with quizzes, and practice with a smart simulator.")
#         ttk.Label(self.wrapper, text=intro, wraplength=600, justify='center').pack(pady=10)

# class LessonsPage(CenteredPage):
#     def __init__(self, parent, controller):
#         super().__init__(parent, controller)
#         self.content = ttk.Label(self.wrapper, text="Select a lesson from the menu.",
#                                  wraplength=700, justify='left', font=('Helvetica', 12))
#         self.content.pack(pady=20)
#         self.topics = [
#             "Stocks are shares representing ownership in a company...",
#             "Candlestick charts display price data...",
#             "Fundamental analysis evaluates a company's intrinsic value...",
#             "Technical indicators are calculations based on price and volume...",
#             "Order types dictate how trades are executed...",
#             "Risk management involves setting position sizes..."
#         ]

#     def display_topic(self, index):
#         if 0 <= index < len(self.topics):
#             self.content.config(text=self.topics[index])
#         else:
#             self.content.config(text="Topic not found.")

# class QuizPage(CenteredPage):
#     def __init__(self, parent, controller):
#         super().__init__(parent, controller)
#         self.questions = [
#             {"q": "What does IPO stand for?", "options": ["Initial Price Offering", "Initial Public Offering", "Internal Public Offering"], "answer": 1},
#             {"q": "A 'bull market' means prices are...?", "options": ["Falling", "Rising", "Stable"], "answer": 1},
#             {"q": "What is a pip in forex trading?", "options": ["Price interest point", "Percentage in point", "Price increment point"], "answer": 1},
#             {"q": "Which order type guarantees execution but not price?", "options": ["Limit order", "Stop order", "Market order"], "answer": 2},
#             {"q": "What does RSI measure?", "options": ["Volume", "Momentum", "Volatility"], "answer": 1},
#             {"q": "A red candlestick indicates...", "options": ["Price closed higher", "Price closed lower", "No change"], "answer": 1}
#         ]
#         self.current = 0
#         self.score = 0
#         self.question_label = ttk.Label(self.wrapper, wraplength=600, font=('Helvetica', 14))
#         self.question_label.pack(pady=10)
#         self.var = tk.IntVar(value=-1)
#         self.opts = []
#         for i in range(3):
#             rb = ttk.Radiobutton(self.wrapper, variable=self.var, value=i)
#             rb.pack(anchor='w', pady=2)
#             self.opts.append(rb)
#         ttk.Button(self.wrapper, text="Submit", style='Menu.TButton', command=self.check_answer).pack(pady=10)
#         self.result = ttk.Label(self.wrapper, text="", font=('Helvetica', 12))
#         self.result.pack(pady=5)
#         self.load_question()

#     def load_question(self):
#         qdata = self.questions[self.current]
#         self.question_label.config(text=qdata["q"])
#         for idx, opt in enumerate(qdata["options"]):
#             self.opts[idx].config(text=opt)
#         self.var.set(-1)
#         self.result.config(text="")

#     def check_answer(self):
#         selected = self.var.get()
#         if selected not in [0, 1, 2]:
#             messagebox.showwarning("No selection", "Please select an answer before submitting.")
#             return
#         correct = self.questions[self.current]["answer"]
#         if selected == correct:
#             self.score += 1
#             self.result.config(text="Correct!", foreground="green")
#         else:
#             correct_text = self.questions[self.current]["options"][correct]
#             self.result.config(text=f"Incorrect. Correct answer: {correct_text}", foreground="red")
#         self.current += 1
#         if self.current < len(self.questions):
#             self.after(800, self.load_question)
#         else:
#             messagebox.showinfo("Quiz Results", f"Your score: {self.score}/{len(self.questions)}")
#             self.current = 0
#             self.score = 0
#             self.load_question()

# class SimulatorPage(CenteredPage):
#     def __init__(self, parent, controller):
#         super().__init__(parent, controller)
#         ttk.Label(self.wrapper, text="Principal Amount:", font=('Helvetica', 12)).pack(pady=5)
#         self.principal = tk.DoubleVar(value=1000)
#         ttk.Entry(self.wrapper, textvariable=self.principal, font=('Helvetica', 12)).pack(pady=5)
#         ttk.Label(self.wrapper, text="Annual Rate (%) :", font=('Helvetica', 12)).pack(pady=5)
#         self.rate = tk.DoubleVar(value=5)
#         ttk.Entry(self.wrapper, textvariable=self.rate, font=('Helvetica', 12)).pack(pady=5)
#         ttk.Label(self.wrapper, text="Years:", font=('Helvetica', 12)).pack(pady=5)
#         self.years = tk.IntVar(value=1)
#         ttk.Entry(self.wrapper, textvariable=self.years, font=('Helvetica', 12)).pack(pady=5)
#         ttk.Button(self.wrapper, text="Calculate Growth", style='Menu.TButton', command=self.simulate).pack(pady=10)
#         self.result = ttk.Label(self.wrapper, text="", font=('Helvetica', 12))
#         self.result.pack(pady=5)

#     def simulate(self):
#         P = self.principal.get()
#         r = self.rate.get() / 100
#         t = self.years.get()
#         A = P * ((1 + r) ** t)
#         self.result.config(text=f"After {t} year(s): ₦{A:,.2f}")

# if __name__ == "__main__":
#     app = TradingApp()
#     app.mainloop()
