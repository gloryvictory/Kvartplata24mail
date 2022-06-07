
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("!!!!!!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Сортировка закончена успешно! Открыть проводник ?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
