from itertools import count
from PyQt5.QtCore import QTimer, QCoreApplication


app = QCoreApplication([])

timer = QTimer()
timer.timeout.connect(lambda: print("Ripeti"))
timer.start(10000)

if count > 5 : 
 timer.stop()
app.exec_()
