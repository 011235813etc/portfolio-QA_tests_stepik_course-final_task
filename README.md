# portfolio_QA_stepik_course

Example:

Рассмотрим такой простой тест-кейс:

   1. Открыть главную страницу
   2. Перейти на страницу логина

Ожидаемый результат:

Открыта страница логина

 

Давайте посмотрим на кусочек кода теста из предыдущего модуля, который реализует первую часть этого теста:

test_main_page.py:

      link = "http://selenium1py.pythonanywhere.com/"
      
      
      def test_guest_can_go_to_login_page(browser):
          browser.get(link)
          login_link = browser.find_element_by_css_selector("#login_link")
          login_link.click()

Что здесь происходит?

Мы открываем ссылку, находим элемент с определенным селектором и нажимаем на этот элемент.

Что мы на самом деле имеем в виду?

Мы хотим открыть страницу логина. Давайте выделим это действие в отдельную функцию с понятным названием, 
пока все в том же файле test_main_page.py :

      def go_to_login_page(browser):
          login_link = browser.find_element_by_css_selector("#login_link")
          login_link.click()

и наш тест упрощается:

      def test_guest_can_go_to_login_page(browser): 
         browser.get(link) 
         go_to_login_page(browser) 

При написании следующих тестов, когда нам понадобится перейти к странице логина с главной страницы, 
нам не нужно будет копировать этот кусочек кода или писать заново — мы сможем переиспользовать уже 
написанный метод.

