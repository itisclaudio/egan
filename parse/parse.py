import requests
import lxml.html
from datetime import date, datetime

from parse.parseapp.models import Methodologies

url='https://ejproxy.com/methodologies/'
page = requests.get(url)
page_content = lxml.html.fromstring(page.content)
td_elements = page_content.xpath('//td')

for t in range(0, len(td_elements), 2):
	print("{} - {} - {}".format(t,td_elements[t].text_content().strip(),td_elements[t+1].text_content().strip()))
	table = Methodologies()
	table.title = td_elements[t].text_content().strip()
	table.dateadded = datetime.strptime(td_elements[t+1].text_content().strip(), "%B %d, %Y").date()
	table.save()