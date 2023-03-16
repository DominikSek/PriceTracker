import sys
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from PyQt6.QtWidgets import QApplication, QDialog, QWidget, QVBoxLayout, QTableView, QDialogButtonBox, QLabel
from PyQt6.QtGui import QIcon
from price_tracker.constants import FILES_PATH, URL_FILE
import pandas as pd
import csv
import os


class DataModel(QAbstractTableModel):
    def __init__(self, data, header_data):
        super().__init__()
        self._data = data
        self._header_data = header_data

    def rowCount(self, parent=QModelIndex()):
        return self._data.shape[0]

    def columnCount(self, parent=QModelIndex()):
        return self._data.shape[1]

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
                value = self._data.iloc[index.row(), index.column()]
                return QVariant(str(value))
        else:
            return QVariant()

    def headerData(self, col, orientation=Qt.Orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self._data.columns[col]


class AlertDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("File missing")

        QBtn = QDialogButtonBox.StandardButton.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("CSV File was missing, so it was created with one example.")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)


class PCGui(QWidget):
    def __init__(self):
        super().__init__()

        self._header_data = None
        self.table = None
        self.model = None

        self.alert = AlertDialog()
        self.setWindowIcon(QIcon(f"{FILES_PATH}/Logo.png"))
        self.setWindowTitle("Price tracker")
        self.resize(720, 480)

        self._data = None
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.initialize_ui()

    def initialize_ui(self):
        self.table = QTableView()
        self.get_csv_data()
        self.model = DataModel(self._data, self._header_data)
        self.table.setModel(self.model)
        self.layout.addWidget(self.table)

    def get_csv_data(self):

        if not os.path.isfile(f"{FILES_PATH}/{URL_FILE}"):
            with open(f"{FILES_PATH}/{URL_FILE}", "w", newline="") as csv_file:
                self.alert.exec()
                header = ["ID", "url", "alert_price"]
                temp_data = [
                             ["1", "https://www.amazon.de/-/en/MOBIUZ-EX240N-Gaming-Monitor-Compatible/dp/B0B797ZPF5/", 160]]
                self._data = pd.DataFrame(temp_data, columns=header)
                print(1,self._data)
                writer = csv.writer(csv_file)
                writer.writerow(header)
                writer.writerows(temp_data)
        else:
            csv_data = pd.read_csv(f"{FILES_PATH}/{URL_FILE}")
            self._data = pd.DataFrame(csv_data)
            print(2,self._data)


app = QApplication(sys.argv)
window = PCGui()
window.show()
sys.exit(app.exec())