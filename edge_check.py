from selenium import webdriver
from selenium.webdriver.edge.options import Options
import tempfile
o = Options()
o.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
o.add_argument("--no-sandbox")
o.add_argument("--disable-dev-shm-usage")
try:
    d = webdriver.Edge(options=o)
    print("Edge:", d.capabilities["browserVersion"])
    d.get("https://biit.cs.ut.ee/gprofiler/gost")
    print("TITLE:", d.title, "\nSUCCESS ✅  Edge works — we'll use Edge.")
    d.quit()
except Exception as e:
    print("EDGE FAILED ❌:", str(e)[:300])
