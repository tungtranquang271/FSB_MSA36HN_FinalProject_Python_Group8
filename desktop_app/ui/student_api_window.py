from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem,
    QLineEdit, QFormLayout, QMessageBox, QLabel, QComboBox
)

from api.student_api import (
    get_students_paged,
    create_student,
    update_student,
    delete_student
)


class StudentApiWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student API Manager")
        self.setGeometry(300, 150, 1000, 600)

        # pagination state
        self.page = 1
        self.page_size = 10
        self.total_pages = 1
        self.keyword = None

        self.is_create_mode = True

        self._build_ui()
        self.load_data()

    # =====================================================
    # UI
    # =====================================================
    def _build_ui(self):
        layout = QVBoxLayout()

        # ---------- FORM ----------
        form = QFormLayout()

        self.txt_id = QLineEdit()
        self.txt_first = QLineEdit()
        self.txt_last = QLineEdit()
        self.txt_email = QLineEdit()
        self.txt_hometown = QLineEdit()
        self.txt_math = QLineEdit()
        self.txt_literature = QLineEdit()
        self.txt_english = QLineEdit()

        form.addRow("Student ID", self.txt_id)
        form.addRow("First Name", self.txt_first)
        form.addRow("Last Name", self.txt_last)
        form.addRow("Email", self.txt_email)
        form.addRow("Hometown", self.txt_hometown)
        form.addRow("Math", self.txt_math)
        form.addRow("Literature", self.txt_literature)
        form.addRow("English", self.txt_english)

        layout.addLayout(form)

        # ---------- CRUD BUTTONS ----------
        crud_row = QHBoxLayout()
        self.btn_create = QPushButton("Create")
        self.btn_update = QPushButton("Update")
        self.btn_delete = QPushButton("Delete")
        self.btn_new = QPushButton("New / Clear")

        crud_row.addWidget(self.btn_create)
        crud_row.addWidget(self.btn_update)
        crud_row.addWidget(self.btn_delete)
        crud_row.addWidget(self.btn_new)

        layout.addLayout(crud_row)

        # ---------- SEARCH + PAGE SIZE ----------
        search_row = QHBoxLayout()
        self.txt_search = QLineEdit()
        self.txt_search.setPlaceholderText("Search by ID / name / email / hometown")

        self.cbo_page_size = QComboBox()
        self.cbo_page_size.addItems(["10", "20", "50"])
        self.cbo_page_size.setCurrentText("10")

        self.btn_search = QPushButton("Search")

        search_row.addWidget(QLabel("Search:"))
        search_row.addWidget(self.txt_search)
        search_row.addWidget(QLabel("Page size:"))
        search_row.addWidget(self.cbo_page_size)
        search_row.addWidget(self.btn_search)

        layout.addLayout(search_row)

        # ---------- TABLE ----------
        self.columns = [
            "student_id", "first_name", "last_name",
            "email", "hometown", "math", "literature", "english"
        ]

        self.table = QTableWidget(0, len(self.columns))
        self.table.setHorizontalHeaderLabels(self.columns)
        self.table.cellClicked.connect(self.on_row_selected)

        layout.addWidget(self.table)

        # ---------- PAGINATION ----------
        page_row = QHBoxLayout()
        self.btn_prev = QPushButton("Previous")
        self.lbl_page = QLabel("Page 1 / 1")
        self.btn_next = QPushButton("Next")

        page_row.addWidget(self.btn_prev)
        page_row.addWidget(self.lbl_page)
        page_row.addWidget(self.btn_next)

        layout.addLayout(page_row)

        self.setLayout(layout)

        # ---------- SIGNALS ----------
        self.btn_create.clicked.connect(self.on_create)
        self.btn_update.clicked.connect(self.on_update)
        self.btn_delete.clicked.connect(self.on_delete)
        self.btn_new.clicked.connect(self.enter_create_mode)

        self.btn_search.clicked.connect(self.on_search)
        self.cbo_page_size.currentTextChanged.connect(self.on_page_size_change)

        self.btn_prev.clicked.connect(self.on_prev)
        self.btn_next.clicked.connect(self.on_next)

    # =====================================================
    # DATA
    # =====================================================
    def load_data(self):
        try:
            res = get_students_paged(
                page=self.page,
                page_size=self.page_size,
                keyword=self.keyword
            )

            items = sorted(res["items"], key=lambda x: x.get("student_id", ""))

            self.total_pages = res["total_pages"]
            self.lbl_page.setText(f"Page {self.page} / {self.total_pages}")

            self.table.setRowCount(len(items))
            for r, row in enumerate(items):
                for c, col in enumerate(self.columns):
                    self.table.setItem(
                        r, c,
                        QTableWidgetItem(str(row.get(col, "")))
                    )

            self.enter_create_mode()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # =====================================================
    # MODES
    # =====================================================
    def enter_create_mode(self):
        self.is_create_mode = True
        self.clear_form()
        self.txt_id.setReadOnly(False)
        self.table.clearSelection()

    def enter_view_mode(self):
        self.is_create_mode = False
        self.txt_id.setReadOnly(True)

    def clear_form(self):
        for w in [
            self.txt_id, self.txt_first, self.txt_last,
            self.txt_email, self.txt_hometown,
            self.txt_math, self.txt_literature, self.txt_english
        ]:
            w.clear()

    # =====================================================
    # EVENTS
    # =====================================================
    def on_row_selected(self, row, _):
        for i, field in enumerate(self.columns):
            getattr(self, f"txt_{field.split('_')[0]}", None)

        self.txt_id.setText(self.table.item(row, 0).text())
        self.txt_first.setText(self.table.item(row, 1).text())
        self.txt_last.setText(self.table.item(row, 2).text())
        self.txt_email.setText(self.table.item(row, 3).text())
        self.txt_hometown.setText(self.table.item(row, 4).text())
        self.txt_math.setText(self.table.item(row, 5).text())
        self.txt_literature.setText(self.table.item(row, 6).text())
        self.txt_english.setText(self.table.item(row, 7).text())

        self.enter_view_mode()

    # =====================================================
    # SEARCH & PAGINATION
    # =====================================================
    def on_search(self):
        self.keyword = self.txt_search.text().strip() or None
        self.page = 1
        self.load_data()

    def on_page_size_change(self):
        self.page_size = int(self.cbo_page_size.currentText())
        self.page = 1
        self.load_data()

    def on_prev(self):
        if self.page > 1:
            self.page -= 1
            self.load_data()

    def on_next(self):
        if self.page < self.total_pages:
            self.page += 1
            self.load_data()

    # =====================================================
    # CRUD
    # =====================================================
    def on_create(self):
        try:
            create_student(self.collect_form())
            QMessageBox.information(self, "Success", "Student created")
            self.load_data()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_update(self):
        try:
            if self.is_create_mode:
                raise ValueError("Select a student to update")

            update_student(self.txt_id.text(), self.collect_form())
            QMessageBox.information(self, "Success", "Student updated")
            self.load_data()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_delete(self):
        try:
            if self.is_create_mode:
                raise ValueError("Select a student to delete")

            delete_student(self.txt_id.text())
            QMessageBox.information(self, "Success", "Student deleted")
            self.load_data()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # =====================================================
    # FORM DATA
    # =====================================================
    def collect_form(self):
        def to_float(v):
            try:
                return float(v)
            except:
                return None

        return {
            "student_id": self.txt_id.text(),
            "first_name": self.txt_first.text(),
            "last_name": self.txt_last.text(),
            "email": self.txt_email.text() or None,
            "hometown": self.txt_hometown.text() or None,
            "math": to_float(self.txt_math.text()),
            "literature": to_float(self.txt_literature.text()),
            "english": to_float(self.txt_english.text()),
        }
