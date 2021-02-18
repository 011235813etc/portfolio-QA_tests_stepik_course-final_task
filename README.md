# portfolio_QA_stepik_course

Example:

Элементы страниц в паттерне Page Object

Помните, мы говорили о том, что тесты почти соответствуют подходу Page Object? 

Сейчас разберемся, почему почти на примере короткой и поучительной истории.

У нас уже есть два тест-кейса, которые так или иначе взаимодействуют со ссылкой на логин. 
Представим себе ситуацию, что у нас модный быстрый agile: разработчики постоянно вносят изменения 
в продукт. В какой-то прекрасный момент изменения коснулись и шапки сайта. Вот приходит к вам разработчик 
с новой ссылкой и говорит протестировать.

Замените линк, на котором запускаются тесты на 
http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer 

Запустите тесты командой:

    pytest -v --tb=line --language=en test_main_page.py

Тесты упали, и теперь нам нужно их поддерживать, то есть чинить. Подберите новый селектор к ссылке на логин. 

Нам придется поправить в файле main_page.py несколько мест, где используется измененный селектор. 
Посчитайте, сколько строк вам нужно будет отредактировать, чтобы починить ваши тесты, и внесите 
полученное число в первое поле ответа ниже. 

Чтобы этого избежать, при проектировании тестов (да и вообще кода) хорошей практикой является 
выносить селектор во внешнюю переменную. 

Давайте этим и займемся: 

1. В папке pages создайте новый файл locators.py 

2. Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу PageObject: 


    from selenium.webdriver.common.by import By

    class MainPageLocators():
        LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

теперь каждый селектор — это пара: как искать и что искать. 

3. В файле main_page.py импортируйте новый класс с локаторами 

    from .locators import MainPageLocators

4. Теперь в классе MainPage замените все строки, где содержится "#login_link" таким образом:


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

Обратите внимание здесь на символ *, он указывает на то, что мы передали именно пару, и этот кортеж 
нужно распаковать. 

5. Запустите тесты с помощью той же самой команды: 


    pytest -v --tb=line --language=en test_main_page.py

Они, конечно, снова упадут. Но теперь посчитайте, сколько строк вам нужно будет отредактировать, 
когда тесты написаны в такой конфигурации? Внесите число во второе поле ответа. 


Итак, PageObject — это не только методы, но и элементы.  

Исправлять руками сломанные селекторы во всем проекте — долго и муторно, и есть большой риск забыть 
и оставить старый селектор. Когда мы выносим селекторы в отдельную сущность, мы уменьшаем время на 
поддержку тестов и сильно упрощаем себе жизнь в долгосрочной перспективе. 

А ещё спринт спустя промоакция закончилась, и фичу с изменением шапки откатили назад. Теперь ссылка 
работает так же, как раньше. Удалите ссылку с промоакцией, и верните обычную ссылку для запуска тестов: 

    link = "http://selenium1py.pythonanywhere.com/"

Не забудьте вернуть старый селектор #login_link, так чтобы тесты снова проходили. Они нам еще пригодятся!
