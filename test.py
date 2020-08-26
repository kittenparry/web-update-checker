import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

total_time = 0
start_time = time.time()
website = 'http://www.python.org'
print('connecting to %s' % website)

driver_options = Options()
driver_options.add_argument('--headless')

driver = webdriver.Firefox(firefox_options=driver_options)
driver.get(website)

end_time = time.time()
passed_time = end_time - start_time
total_time += passed_time
print('connection complete. %.2f seconds.' % passed_time)

# TODO: maybe only fetch body rather than the whole source
content = driver.page_source

start_time = time.time()
print('downloading page.')

with open('tests/test.txt', 'w', encoding='utf-8') as f:
	f.write(content)

end_time = time.time()
passed_time = end_time - start_time
total_time += passed_time
print('download complete. %.2f seconds.\ntotal of %.2f seconds.' % (passed_time, total_time))

driver.close()
