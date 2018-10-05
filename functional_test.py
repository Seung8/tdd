import unittest

from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    """
    setup: 테스트 실행 시
    tearDown: 테스트 종료 시
    """
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    # 웹 페이지를 열고 해당 페이지가 맞는 지 테스트
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

# 커맨드 라인을 통해 직접 실행된 경우에도 unittest 실행자 실행(파일 내 테스트 클래스와 메소드를 찾아서 실행)
if __name__ == '__main__':
    # warnings 속성을 'ignore'로 주어 불필요한 경고 제거
    unittest.main(warnings='ignore')
