import time

from chrome import Chrome
import Page
import Runtime

c = Chrome()
c.do(Page.navigate("http://adhocteam.us/our-team"))

# if we don't wait for the page to load, then we can run the script too
# early and get an empty array
time.sleep(3)

cmd = '[].map.call(document.querySelectorAll("h3.centered"), n => n.textContent)'
c.do(Runtime.evaluate(cmd, returnByValue=True))