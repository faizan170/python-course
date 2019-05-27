import requests
import time
url = "http://localhost:5000/process"
filess = {"img": open("D:/UAF/PythonClasses/day9/flower_photos/daisy/21652746_cc379e0eea_m.jpg", "rb")}
starttime = time.time()
results = requests.post(url, files=filess)
print("time taken:", time.time() - starttime)
#results.raise_for_status()
print(results.text)
