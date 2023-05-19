import threading
from .utils import *

class EmailThread(threading.Thread):
    def __init__(self, send_campaign, campaign):
        self.send_campaign = send_campaign
        self.campaign = campaign
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.send_campaign(self.campaign)
        except Exception as e:
            # Handling the exception
            print(f"An error occurred: {str(e)}")
