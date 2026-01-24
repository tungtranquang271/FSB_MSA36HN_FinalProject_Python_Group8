from PyQt5.QtWidgets import (
    QDialog, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QHBoxLayout, QPushButton, QLabel
)
from PyQt5.QtCore import Qt

STUDENTS_PER_PAGE = 10


class StudentPopup(QDialog):
    def __init__(self, df):
        super().__init__()
        self.setWindowTitle("Students Viewer")
        self.resize(900, 400)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.df = df.reset_index(drop=True)
        self.current_page = 0

        # ✅ FIX: correct total pages
        self.total_pages = (
            len(self.df) + STUDENTS_PER_PAGE - 1
        ) // STUDENTS_PER_PAGE

        self.updating_table = False

        # ---------- TABLE ----------
        self.table = QTableWidget()
        self.table.setColumnCount(len(self.df.columns))
        self.table.setHorizontalHeaderLabels(self.df.columns.tolist())
        self.table.itemChanged.connect(self.save_edit)

        # ---------- NAV ----------
        self.prev_btn = QPushButton("Previous")
        self.next_btn = QPushButton("Next")
        self.page_label = QLabel(alignment=Qt.AlignCenter)

        self.prev_btn.clicked.connect(self.prev_page)
        self.next_btn.clicked.connect(self.next_page)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.prev_btn)
        nav_layout.addWidget(self.page_label)
        nav_layout.addWidget(self.next_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(nav_layout)
        self.setLayout(layout)

        self.update_page()

    # =====================================================
    # PAGE RENDER
    # =====================================================
    def update_page(self):
        self.updating_table = True
        self.table.setRowCount(0)

        start = self.current_page * STUDENTS_PER_PAGE
        end = min(start + STUDENTS_PER_PAGE, len(self.df))
        page_df = self.df.iloc[start:end]

        for row_idx, (_, row) in enumerate(page_df.iterrows()):
            self.table.insertRow(row_idx)
            for col_idx, value in enumerate(row):
                item = QTableWidgetItem("" if value is None else str(value))
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                self.table.setItem(row_idx, col_idx, item)

        self.page_label.setText(
            f"Page {self.current_page + 1} / {self.total_pages}"
        )

        self.prev_btn.setEnabled(self.current_page > 0)
        self.next_btn.setEnabled(self.current_page < self.total_pages - 1)

        self.updating_table = False

    # =====================================================
    # EDIT HANDLING
    # =====================================================
    def save_edit(self, item):
        if self.updating_table:
            return

        table_row = item.row()
        table_col = item.column()

        df_row = self.current_page * STUDENTS_PER_PAGE + table_row
        df_col = self.df.columns[table_col]

        new_value = item.text().strip()

        # numeric fields
        if df_col in ["math", "literature", "english"]:
            try:
                new_value = float(new_value)
            except ValueError:
                return

        self.df.at[df_row, df_col] = new_value

    # =====================================================
    # NAV
    # =====================================================
    def next_page(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.update_page()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_page()
