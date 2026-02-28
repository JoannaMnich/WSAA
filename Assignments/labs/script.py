import requests 
import urllib.parse 
import config
 
# I found that this program would not work with wikepedia 
#targetUrl = "https://en.wikipedia.org/wiki/Main_Page" 
# so I am using my URL 
targetUrl = "https://andrewbeatty1.pythonanywhere.com/bookviewer.html" 
 
apiKey = config.apikeys["htmltopdfkey"]
#api = "XXXXXXXX" 
apiurl = 'https://api.html2pdf.app/v1/generate' 
 
params = {'url': targetUrl,'apiKey': apiKey} 
parsedparams = urllib.parse.urlencode(params) 
requestUrl = apiurl +"?" + parsedparams  
 
response = requests.get(requestUrl) 
print (response.status_code) 
print (response.text)
 
result =response.content 
with open("document.pdf", "wb") as f: 
    f.write(result)
