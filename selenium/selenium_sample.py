#!/usr/bin/env python3
#
# Install the Selenium (>v4) and Webdriver Manager packages:
#   pip install selenium webdriver-manager
# or
#   conda install selenium
#   conda install -c conda-forge webdriver-manager
#

import sys
import time
import signal
import platform

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def signal_handler(signum, frame):
    print("End of app...")
    exit(0)


def main(argv):
    # Set the signal handler to deal with CTRL+C presses:
    signal.signal(signal.SIGINT, signal_handler)

    print("Load selenium...")
    chrome_options = Options()
    # Find a list of arguments here:
    #   https://peter.sh/experiments/chromium-command-line-switches/
    chrome_options.add_argument("window-position=10,10")
    chrome_options.add_argument("window-size=500,700")
    # Set the Google Chrome user profile dir:
    # (see "Profile Path" when you navigate to "chrome://version" in your browser)
    #   Mac:   ~/Library/Application Support/Google/Chrome/Default
    #   Linux: ~/.config/google-chrome/default
    chrome_options.add_argument("user-data-dir='/Users/JCREYF/Library/Application Support/Google/Chrome/Default'")

    webbrowser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Now open the web browser and navigate to some web page:
    print("Load web page...")
    webbrowser.get("https://www.google.com/finance/")
    action = ActionChains(webbrowser)

#    workspace = WebDriverWait(webbrowser, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='domain']")))
#    workspace.clear()
#    workspace.send_keys(SLACK_WORKSPACE)

#    button = WebDriverWait(webbrowser, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
#    button.click()

#    logon = WebDriverWait(webbrowser, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-clog-event='WEBSITE_CLICK']")))
#    logon.click()

#    signin = WebDriverWait(webbrowser, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']")))
#    signin.click()

    # Zoom out by clicking <CTRL><-> a number of times:
    if platform.system() == "Darwin":
        print("Running on a Mac")
        ctrl_key = Keys.COMMAND
    else:
        ctrl_key = Keys.CONTROL

    # Any of these should work to achieve "<CTLR>+<-/+>" to zoom in or out in the browser,
    # but they don't seem to work for some reason :-(
    # Executing the javascript below to zoom does work though!
#    action.send_keys(ctrl_key, Keys.SUBTRACT).perform()
#    page = webbrowser.find_element(by=By.TAG_NAME, value="html")
#    page.send_keys(ctrl_key, Keys.SUBTRACT)
    webbrowser.execute_script(f"document.body.style.zoom='50%'")

    # Loop forever, scrolling the page up and down every so many seconds:
    y = 400
    while True:
        print("move...")
        action.scroll_by_amount(0, y)
        if y == 400:
            y = -400
        else:
            y = 400
        time.sleep(5)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
