from selenium import webdriver

events_dict = {}

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.python.org/')

events = driver.find_element_by_class_name('event-widget')
event_menu = events.find_element_by_class_name('menu')
# print(event_menu.text)
dates = event_menu.find_elements_by_tag_name('time')
event_name = event_menu.find_elements_by_tag_name('a')

for i in range(len(dates)):
    events_dict[i] = {'Time': dates[i].text, 'Event Name': event_name[i].text}

print(events_dict)
driver.quit()
