import time
from plyer import notification

while True:
    notification.notify(
        title="Eye Strain Break",
        message=" Look at something >20ft away for 20 seconds to reduce eyestrain",
        timeout=25
    )
    time.sleep(1200)