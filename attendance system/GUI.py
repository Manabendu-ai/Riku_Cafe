import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QHBoxLayout, QComboBox, QMessageBox
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
matplotlib.use('Agg')


class AttendanceUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Attendance Dashboard")
        self.setGeometry(100, 100, 1000, 600)

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mk7riku23",
            database="attendance_system"
        )
        self.cursor = self.db.cursor()

        self.layout = QVBoxLayout()

        title = QLabel("📊 Attendance Dashboard")
        title.setFont(QFont("Arial", 20))
        title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title)

        self.student_selector = QComboBox()
        self.load_students()
        self.student_selector.currentIndexChanged.connect(self.plot_graph)
        self.layout.addWidget(self.student_selector)

        self.canvas = FigureCanvas(plt.Figure())
        self.layout.addWidget(self.canvas)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

        self.refresh_table()

    def load_students(self):
        self.cursor.execute("SELECT id, name FROM students")
        self.students = self.cursor.fetchall()
        self.student_selector.clear()
        for s in self.students:
            self.student_selector.addItem(f"{s[1]} (ID: {s[0]})", s[0])

    def refresh_table(self):
        self.cursor.execute("SELECT * FROM attendance_log")
        rows = self.cursor.fetchall()
        headers = [i[0] for i in self.cursor.description]

        self.table.setRowCount(len(rows))
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)

        for r_idx, row in enumerate(rows):
            for c_idx, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                self.table.setItem(r_idx, c_idx, item)

        self.table.cellDoubleClicked.connect(self.edit_attendance)

    def plot_graph(self):
        student_id = self.student_selector.currentData()
        self.cursor.execute("""
            SELECT mon, tue, wed, thu, fri, sat FROM attendance_log
            WHERE student_id = %s
        """, (student_id,))
        weekly_data = self.cursor.fetchall()

        days = ["mon", "tue", "wed", "thu", "fri", "sat"]
        count = {day: 0 for day in days}
        total = len(weekly_data)

        for row in weekly_data:
            for i, day in enumerate(days):
                if row[i] == "Present":
                    count[day] += 1

        percentages = [count[day] / total * 100 if total > 0 else 0 for day in days]

        ax = self.canvas.figure.subplots()
        ax.clear()
        bars = ax.bar(days, percentages, color=["green" if p >= 85 else "red" for p in percentages])
        ax.set_ylim(0, 100)
        ax.set_title("Weekly Attendance (%)")
        self.canvas.draw()

    def edit_attendance(self, row, col):
        col_name = self.table.horizontalHeaderItem(col).text()
        if col_name.lower() in ["mon", "tue", "wed", "thu", "fri", "sat"]:
            student_id = int(self.table.item(row, 1).text())
            log_id = int(self.table.item(row, 0).text())
            new_status = "Present" if self.table.item(row, col).text() != "Present" else "Absent"

            self.cursor.execute(f"""
                UPDATE attendance_log
                SET {col_name} = %s
                WHERE log_id = %s AND student_id = %s
            """, (new_status, log_id, student_id))
            self.db.commit()
            QMessageBox.information(self, "Success", f"Marked {col_name} as {new_status}")
            self.refresh_table()
            self.plot_graph()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AttendanceUI()
    win.show()
    sys.exit(app.exec_())