from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QMessageBox, QApplication, QLabel, QGroupBox, QComboBox, QSpinBox
)
import sys

from crawler.student_crawler import crawl_students
from storage.file_storage import save_to_text_file, load_from_text_file
from preprocessing.data_cleaner import clean_student_data
from analysis.score_analysis import performance_level_distribution
from visualization.bar_chart import plot_performance_level

from analysis.score_analysis import (
    average_math_english_by_hometown,
    average_all_subjects_by_hometown,
    subject_difficulty,
    correlation_math_english,
    top_students_by_subject,
)

from visualization.bar_chart import (
    plot_grouped_math_english_by_hometown,
    plot_grouped_all_subjects_by_hometown,
    plot_subject_difficulty,
    plot_top_students,
)

from visualization.distribution_chart import (
    plot_histogram,
    plot_scatter,
)

DATA_FILE = "students.txt"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Data Analysis (FE3)")
        self.setGeometry(250, 120, 620, 420)
        self._build_ui()

    def _build_ui(self):
        root = QWidget()
        main_layout = QVBoxLayout()

        title = QLabel("Student Data Analysis Dashboard")
        title.setStyleSheet("font-size: 16px; font-weight: 600;")
        main_layout.addWidget(title)

        # --- Crawl section
        crawl_box = QGroupBox("Data")
        crawl_layout = QVBoxLayout()
        self.btn_crawl = QPushButton("Crawl Data (API) → Save to Text File")
        self.btn_crawl.clicked.connect(self.on_crawl)
        crawl_layout.addWidget(self.btn_crawl)
        crawl_box.setLayout(crawl_layout)
        main_layout.addWidget(crawl_box)

        # --- Analysis buttons
        analysis_box = QGroupBox("Analysis & Charts")
        analysis_layout = QVBoxLayout()

        self.btn_avg_math_eng = QPushButton("1) Avg Math vs English by Hometown (Grouped Bar)")
        self.btn_avg_math_eng.clicked.connect(self.on_avg_math_english_by_hometown)

        self.btn_avg_all = QPushButton("2) Avg All Subjects by Hometown (Grouped Bar)")
        self.btn_avg_all.clicked.connect(self.on_avg_all_subjects_by_hometown)

        self.btn_subject_diff = QPushButton("3) Subject Difficulty (Average Score Bar)")
        self.btn_subject_diff.clicked.connect(self.on_subject_difficulty)

        self.btn_corr = QPushButton("4) Correlation: Math vs English (Scatter + Value)")
        self.btn_corr.clicked.connect(self.on_correlation_math_english)

        # --- Top students controls (subject + limit)
        top_row = QHBoxLayout()
        self.cbo_subject = QComboBox()
        self.cbo_subject.addItems(["math", "english", "literature"])
        self.spin_limit = QSpinBox()
        self.spin_limit.setRange(3, 20)
        self.spin_limit.setValue(5)

        self.btn_top = QPushButton("5) Top Students by Subject (Horizontal Bar)")
        self.btn_top.clicked.connect(self.on_top_students)

        top_row.addWidget(QLabel("Subject:"))
        top_row.addWidget(self.cbo_subject)
        top_row.addWidget(QLabel("Top N:"))
        top_row.addWidget(self.spin_limit)
        top_row.addStretch(1)

        self.btn_performance = QPushButton("6) Performance Level Distribution (Bar Chart)")
        self.btn_performance.clicked.connect(self.on_performance_level)

        analysis_layout.addWidget(self.btn_avg_math_eng)
        analysis_layout.addWidget(self.btn_avg_all)
        analysis_layout.addWidget(self.btn_subject_diff)
        analysis_layout.addWidget(self.btn_corr)
        analysis_layout.addLayout(top_row)
        analysis_layout.addWidget(self.btn_top)
        analysis_layout.addWidget(self.btn_performance)

        analysis_box.setLayout(analysis_layout)
        main_layout.addWidget(analysis_box)

        root.setLayout(main_layout)
        self.setCentralWidget(root)

    # ---------- helpers ----------
    def _load_clean_df(self):
        raw = load_from_text_file(DATA_FILE)
        df = clean_student_data(raw)
        if df.empty:
            raise ValueError("No valid data after preprocessing.")
        return df

    # ---------- actions ----------
    def on_crawl(self):
        try:
            data = crawl_students()
            save_to_text_file(data, DATA_FILE)
            QMessageBox.information(self, "Success", f"Crawled & saved {len(data)} students to {DATA_FILE}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_avg_math_english_by_hometown(self):
        try:
            df = self._load_clean_df()
            result = average_math_english_by_hometown(df)
            plot_grouped_math_english_by_hometown(result)
        except FileNotFoundError:
            QMessageBox.warning(self, "Warning", "No data file found. Please click Crawl Data first.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_avg_all_subjects_by_hometown(self):
        try:
            df = self._load_clean_df()
            result = average_all_subjects_by_hometown(df)
            plot_grouped_all_subjects_by_hometown(result)
        except FileNotFoundError:
            QMessageBox.warning(self, "Warning", "No data file found. Please click Crawl Data first.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_subject_difficulty(self):
        try:
            df = self._load_clean_df()
            result = subject_difficulty(df)
            plot_subject_difficulty(result)
        except FileNotFoundError:
            QMessageBox.warning(self, "Warning", "No data file found. Please click Crawl Data first.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_correlation_math_english(self):
        try:
            df = self._load_clean_df()
            corr = correlation_math_english(df)
            # chart
            plot_scatter(df.dropna(subset=["math_score", "english_score"]),
                         "math_score", "english_score",
                         "Math vs English (Scatter)")
            QMessageBox.information(self, "Correlation Result", f"Correlation (Math, English) = {corr:.3f}")
        except FileNotFoundError:
            QMessageBox.warning(self, "Warning", "No data file found. Please click Crawl Data first.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_top_students(self):
        try:
            df = self._load_clean_df()
            subject = self.cbo_subject.currentText()
            limit = int(self.spin_limit.value())
            top_df = top_students_by_subject(df, subject=subject, limit=limit)
            plot_top_students(top_df, subject_label=subject.capitalize())
        except FileNotFoundError:
            QMessageBox.warning(self, "Warning", "No data file found. Please click Crawl Data first.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_performance_level(self):
        try:
            df = self._load_clean_df()
            subject = self.cbo_subject.currentText()  # dùng chung combo box
            result = performance_level_distribution(df, subject=subject)
            plot_performance_level(result, subject_label=subject.capitalize())
        except FileNotFoundError:
            QMessageBox.warning(self, "Warning", "No data file found. Please click Crawl Data first.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))



def run_app():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
