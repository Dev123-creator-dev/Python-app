from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile, socket
s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()
o = Options()
o.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
o.add_argument(f"--remote-debugging-port={port}")
o.add_argument("--no-sandbox")
o.add_argument("--disable-dev-shm-usage")
try:
    d = webdriver.Chrome(options=o)
    print("Chrome:", d.capabilities["browserVersion"])
    print("Driver:", d.capabilities["chrome"]["chromedriverVersion"].split(" ")[0])
    d.get("https://biit.cs.ut.ee/gprofiler/gost")
    print("TITLE:", d.title, "\nSUCCESS ✅")
    d.quit()
except Exception as e:
    print("CHROME FAILED ❌:", str(e)[:300])
