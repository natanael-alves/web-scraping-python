import requests
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas

URL = "https://www.nike.com.br/snkrs/calendario"
page = requests.get(URL, headers={"User-Agent": "Requests"})

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("h2", class_="Typographystyled__StyledHeading-sc-1h4c8w0-1 jWzglM GridProductCard-styled__ProductNickname-sc-d7c375f9-10 ipmgHq")


tenis_disponiveis = []

for element in job_elements:
    tenis_disponiveis.append(element.text)

print(tenis_disponiveis)

c = canvas.Canvas("tenis_disponiveis.pdf")
c.setFont("Helvetica", 12)
c.drawString(100,750, "TÊNIS DISPONÍVEIS")

horizontal = 100
vertical = 700

for item in tenis_disponiveis:
    c.drawString(horizontal, vertical, item)
    vertical-=20

c.showPage()
c.save()