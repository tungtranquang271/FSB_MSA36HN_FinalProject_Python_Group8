import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QMessageBox, QApplication, QLabel, QGroupBox, QComboBox, QSpinBox
)

from crawler.student_crawler import crawl_students
from storage.file_storage import save_to_text_file, load_from_text_file
from preprocessing.data_cleaner import clean_and_save_students
from display.display_student import StudentPopup
from ui.student_api_window import StudentApiWindow


from analysis.score_analysis import (
    average_math_english_by_hometown,
    average_all_subjects_by_hometown,
    subject_difficulty,
    correlation_math_english,
    top_students_by_subject,
    performance_level_distribution,
)

from visualization.bar_chart import (
    plot_grouped_math_english_by_hometown,
    plot_grouped_all_subjects_by_hometown,
    plot_subject_difficulty,
    plot_top_students,
    plot_performance_level,
)

from visualization.distribution_chart import (
    plot_histogram,
    plot_scatter,
)

# =====================
# FILE PATHS
# =====================
RAW_DATA_FILE = "students_raw.txt"
CLEAN_DATA_FILE = "students_clean.txt"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Data Analysis Dashboard")
        self.setGeometry(250, 120, 650, 450)
        self.dialogs = []

        self._build_ui()

    # =====================================================
    # UI
    # =====================================================
    def _build_ui(self):
        root = QWidget()
        main_layout = QVBoxLayout()

        # ---------- TITLE ----------
        title = QLabel("Student Data Analysis Dashboard")
        title.setStyleSheet("font-size: 16px; font-weight: 600;")
        main_layout.addWidget(title)

        # ---------- DATA (CRAWL / CLEAN) ----------
        data_box = QGroupBox("Data")
        data_layout = QVBoxLayout()

        self.btn_crawl = QPushButton("1) Crawl Data (API → RAW file)")
        self.btn_crawl.clicked.connect(self.on_crawl)

        self.btn_clean = QPushButton("2) Clean Data (RAW → CLEAN file)")
        self.btn_clean.clicked.connect(self.on_clean)

        data_layout.addWidget(self.btn_crawl)
        data_layout.addWidget(self.btn_clean)
        data_box.setLayout(data_layout)
        main_layout.addWidget(data_box)

        # ---------- DISPLAY ----------
        display_box = QGroupBox("Data Display")
        display_layout = QVBoxLayout()

        self.cbo_data = QComboBox()
        self.cbo_data.addItems(["raw data", "clean data"])

        self.btn_display = QPushButton("Display Data")
        self.btn_display.clicked.connect(self.on_open_popup)

        display_layout.addWidget(QLabel("Select data:"))
        display_layout.addWidget(self.cbo_data)
        display_layout.addWidget(self.btn_display)

        display_box.setLayout(display_layout)
        main_layout.addWidget(display_box)

        # ---------- API OPERATIONS ----------
        api_box = QGroupBox("API Operations")
        api_layout = QVBoxLayout()

        self.btn_api_manager = QPushButton("Open Student API Manager (CRUD)")
        self.btn_api_manager.clicked.connect(self.on_open_api_manager)

        api_layout.addWidget(self.btn_api_manager)
        api_box.setLayout(api_layout)

        main_layout.addWidget(api_box)

        # ---------- ANALYSIS ----------
        analysis_box = QGroupBox("Analysis & Charts")
        analysis_layout = QVBoxLayout()

        self.btn_avg_math_eng = QPushButton("Avg Math vs English by Hometown")
        self.btn_avg_math_eng.clicked.connect(self.on_avg_math_english_by_hometown)

        self.btn_avg_all = QPushButton("Avg All Subjects by Hometown")
        self.btn_avg_all.clicked.connect(self.on_avg_all_subjects_by_hometown)

        self.btn_subject_diff = QPushButton("Subject Difficulty")
        self.btn_subject_diff.clicked.connect(self.on_subject_difficulty)

        self.btn_corr = QPushButton("Correlation: Math vs English")
        self.btn_corr.clicked.connect(self.on_correlation_math_english)

        # ---- top students ----
        top_row = QHBoxLayout()
        self.cbo_subject = QComboBox()
        self.cbo_subject.addItems(["math", "english", "literature"])
        self.spin_limit = QSpinBox()
        self.spin_limit.setRange(3, 20)
        self.spin_limit.setValue(5)

        self.btn_top = QPushButton("Top Students by Subject")
        self.btn_top.clicked.connect(self.on_top_students)

        top_row.addWidget(QLabel("Subject:"))
        top_row.addWidget(self.cbo_subject)
        top_row.addWidget(QLabel("Top N:"))
        top_row.addWidget(self.spin_limit)

        self.btn_performance = QPushButton("Performance Level Distribution")
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

    # =====================================================
    # HELPERS
    # =====================================================
    def _load_raw_df(self):
        data = load_from_text_file(RAW_DATA_FILE)
        if not data:
            raise ValueError("Raw data file is empty. Please crawl data first.")
        return pd.DataFrame(data)

    def _load_clean_df(self):
        data = load_from_text_file(CLEAN_DATA_FILE)
        if not data:
            raise ValueError("Clean data file is empty. Please clean data first.")
        return pd.DataFrame(data)

    # =====================================================
    # ACTIONS
    # =====================================================
    def on_crawl(self):
        try:
            data = crawl_students()
            save_to_text_file(data, RAW_DATA_FILE)
            QMessageBox.information(
                self, "Success",
                f"Crawled & saved {len(data)} students to {RAW_DATA_FILE}"
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_clean(self):
        try:
            clean_and_save_students()
            QMessageBox.information(
                self, "Success",
                f"Clean data saved to {CLEAN_DATA_FILE}"
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_open_popup(self):
        try:
            if self.cbo_data.currentText() == "clean data":
                df = self._load_clean_df()
            else:
                df = self._load_raw_df()

            popup = StudentPopup(df)
            popup.show()
            self.dialogs.append(popup)

        except Exception as e:
            QMessageBox.warning(self, "Warning", str(e))

    def on_open_api_manager(self):
        try:
            win = StudentApiWindow()
            win.show()
            self.dialogs.append(win)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


    # ================= ANALYSIS =================
    def on_avg_math_english_by_hometown(self):
        df = self._load_clean_df()
        result = average_math_english_by_hometown(df)
        plot_grouped_math_english_by_hometown(result)

    def on_avg_all_subjects_by_hometown(self):
        df = self._load_clean_df()
        result = average_all_subjects_by_hometown(df)
        plot_grouped_all_subjects_by_hometown(result)

    def on_subject_difficulty(self):
        df = self._load_clean_df()
        result = subject_difficulty(df)
        plot_subject_difficulty(result)

    def on_correlation_math_english(self):
        df = self._load_clean_df()
        corr = correlation_math_english(df)

        plot_scatter(
            df.dropna(subset=["math", "english"]),
            "math", "english",
            "Math vs English"
        )

        QMessageBox.information(
            self, "Correlation Result",
            f"Correlation (Math, English) = {corr:.3f}"
        )

    def on_top_students(self):
        df = self._load_clean_df()
        subject = self.cbo_subject.currentText()
        limit = int(self.spin_limit.value())
        top_df = top_students_by_subject(df, subject=subject, limit=limit)
        plot_top_students(top_df, subject_label=subject.capitalize())

    def on_performance_level(self):
        df = self._load_clean_df()
        subject = self.cbo_subject.currentText()
        result = performance_level_distribution(df, subject=subject)
        plot_performance_level(result, subject_label=subject.capitalize())


# =====================================================
# RUN APP
# =====================================================
def run_app():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
