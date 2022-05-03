import requests
import lxml.html
from datetime import date, datetime

from parse.parseapp.models import Methodologies

url='https://ejproxy.com/methodologies/'
page = requests.get(url)
page_content = lxml.html.fromstring(page.content)
td_elements = page_content.xpath('//td')

bulk_list = list()
for t in range(0, len(td_elements), 2):
	print("{} - {} - {}".format(t,td_elements[t].text_content().strip(),td_elements[t+1].text_content().strip()))
	bulk_list.append(Methodologies(
		title=td_elements[t].text_content().strip(),
		dateadded = datetime.strptime(td_elements[t+1].text_content().strip(), "%B %d, %Y").date()
		))
Methodologies.objects.bulk_create(bulk_list)