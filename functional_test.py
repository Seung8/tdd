from selenium import webdriver

browser = webdriver.Chrome()

# To-Do 리스트 웹 페이지 열기
browser.get('http://localhost:8000')

# 웹 페이지 타이틀과 헤더에 'To-Do'를 명시하는지(해당 웹 페이지가 맞는지) 확인
assert 'To-Do' in browser.title

browser.quit()
