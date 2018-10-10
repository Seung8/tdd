#!/usr/bin/env python3

import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    """
    setup: 테스트 실행 시
    tearDown: 테스트 종료 시
    """

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # 웹 페이지를 열고 해당 페이지가 맞는 지 테스트
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8001')
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )

        inputbox.send_keys('공작깃털 사기')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: 공작깃털 사기', [row.text for row in rows])
        self.assertIn('2: 공작깃털을 이용해서 그물 만들기', [row.text for row in rows])
        self.fail('Finish the test!')


# 커맨드 라인을 통해 직접 실행된 경우에도 unittest 실행자 실행(파일 내 테스트 클래스와 메소드를 찾아서 실행)
if __name__ == '__main__':
    # warnings 속성을 'ignore'로 주어 불필요한 경고 제거
    unittest.main(warnings='ignore')
