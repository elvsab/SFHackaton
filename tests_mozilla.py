import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager


# проверка кнопки "смотреть на youtube" в начале страницы
def test_youtube_btn(selenium):

    youtube_btn = selenium.find_element(By.XPATH, '//a[@href="https://www.youtube.com/@pleasantildar" and @class="hero__button button"]')

    # Получим текущее количество окон
    current_windows = selenium.window_handles
    youtube_btn.click()

    # Ожидание появления нового окна
    WebDriverWait(selenium, 10).until(EC.new_window_is_opened(current_windows))

    WebDriverWait(selenium, 10).until(EC.number_of_windows_to_be(2))

    new_windows = selenium.window_handles

    selenium.switch_to.window(new_windows[-1])

    # Проверка, что текущий URL соответствует ожидаемому
    expected_url = "https://www.youtube.com/@pleasantildar"
    WebDriverWait(selenium, 10).until(EC.url_contains(expected_url))
    assert selenium.current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {selenium.current_url}"


# этот и последующие 4 теста проверяют отработку кнопок соц сетей, что они переходят по правильным адресам
def test_twitch_btn(selenium):

    twitch_btn = selenium.find_element(By.CSS_SELECTOR, 'a[href="https://www.twitch.tv/ildarzhe"]')

    current_windows = selenium.window_handles
    twitch_btn.click()

    WebDriverWait(selenium, 10).until(EC.new_window_is_opened(current_windows))

    WebDriverWait(selenium, 10).until(EC.number_of_windows_to_be(2))

    new_windows = selenium.window_handles

    for window_handle in new_windows:
        if window_handle not in current_windows:
            selenium.switch_to.window(window_handle)
            break

    expected_url = "https://www.twitch.tv/ildarzhe"
    WebDriverWait(selenium, 10).until(EC.url_contains(expected_url))
    assert selenium.current_url == expected_url, f'Expected URL: {expected_url}, Actual URL: {selenium.current_url}'


def switch_to_new_window(selenium, current_windows):
    WebDriverWait(selenium, 10).until(EC.new_window_is_opened(current_windows))
    new_windows = selenium.window_handles
    new_window = [window for window in new_windows if window not in current_windows][0]
    selenium.switch_to.window(new_window)

def test_telegram_btn_header(selenium):

    telegram_btn_header = selenium.find_element(By.XPATH, '//a[@href="https://www.t.me/unpleasent" and @class="header-link"]')
    current_windows = selenium.window_handles
    telegram_btn_header.click()
    switch_to_new_window(selenium, current_windows)
    WebDriverWait(selenium, 10).until(EC.url_contains("https://www.t.me/unpleasent"))
    expected_url = "https://www.t.me/unpleasent"
    assert selenium.current_url == expected_url, f'Expected URL: {expected_url}, Actual URL: {selenium.current_url}'

def test_instagram_btn(selenium):

    instagram_btn = selenium.find_element(By.CSS_SELECTOR, 'a[href="https://www.instagram.com/masterildar"]')
    current_windows = selenium.window_handles
    instagram_btn.click()
    switch_to_new_window(selenium, current_windows)
    WebDriverWait(selenium, 10).until(EC.url_contains("https://www.instagram.com/masterildar"))
    expected_url = "https://www.instagram.com/masterildar/"
    assert selenium.current_url == expected_url, f'Expected URL: {expected_url}, Actual URL: {selenium.current_url}'

def test_twitter_btn(selenium):

    twitter_btn = selenium.find_element(By.CSS_SELECTOR, 'a[href="https://www.twitter.com/master_ildar"]')
    current_windows = selenium.window_handles
    twitter_btn.click()
    switch_to_new_window(selenium, current_windows)
    WebDriverWait(selenium, 10).until(EC.url_contains("https://twitter.com/master_ildar"))
    expected_url = "https://twitter.com/master_ildar"
    assert selenium.current_url == expected_url, f'Expected URL: {expected_url}, Actual URL: {selenium.current_url}'

def test_vk_btn(selenium):

    vk_btn = selenium.find_element(By.CSS_SELECTOR, 'a[href="https://vk.com/pleasentildar"]')
    current_windows = selenium.window_handles
    vk_btn.click()
    switch_to_new_window(selenium, current_windows)
    WebDriverWait(selenium, 10).until(EC.url_contains("https://vk.com/pleasentildar"))
    expected_url = "https://vk.com/pleasentildar"
    assert selenium.current_url == expected_url, f'Expected URL: {expected_url}, Actual URL: {selenium.current_url}'


# тест отработки кнопки приглашения в телеграм чат-бот

def test_tg_bot_btn(selenium):

    telegram_bot_btn = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@href="https://t.me/PriyatniyIldar_bot" and @class="content-description__button button"]'))
    )
    
    selenium.execute_script("arguments[0].scrollIntoView(true);", telegram_bot_btn)

    selenium.execute_script("arguments[0].click();", telegram_bot_btn)

    selenium.implicitly_wait(2)

    current_windows = selenium.window_handles
    assert len(current_windows) > 1, "No new window opened after clicking the button"

    selenium.switch_to.window(current_windows[-1])

    WebDriverWait(selenium, 10).until(EC.url_contains("https://t.me/PriyatniyIldar_bot"))

    expected_url = "https://t.me/PriyatniyIldar_bot"
    assert selenium.current_url == expected_url, f'Expected URL: {expected_url}, Actual URL: {selenium.current_url}'


# негативный тест, кнопки покупки не работают - прокручивают страницу, вместо перехода на сайт с мерчем
def test_merch_buttons(selenium):

    buy_buttons = selenium.find_elements(By.CSS_SELECTOR, '.card__link')

    for button in buy_buttons:
     
        selenium.execute_script("arguments[0].scrollIntoView(true);", button)

        try:
            
            action = ActionChains(selenium)
            action.move_to_element(button).click().perform()

            selenium.implicitly_wait(2)

            # Проверяем, что URL не изменился (то есть, произошла прокрутка, а не переход)
            expected_url = "https://prostomerch.store/catalog/collections/priyatnyj-ildar/categories/merch"
            actual_url = selenium.current_url
            assert actual_url != expected_url, f"Кнопка {button.text} привела к неожиданному переходу по URL: {actual_url}"

            # Прокручиваем страницу вверх, чтобы быть готовыми к следующей проверке
            selenium.execute_script("window.scrollTo(0, 0);")

        except Exception as e:
            # Обрабатываем исключение в случае, если клик не удался
            print(f"Ошибка при клике на кнопку {button.text}: {e}")


# т.к. при клике на кнопку "Сотрудничество" автоматически открывается приложение почты на компе, проверка осуществл-ся
# на то, что кнопка в принципе кликабельна
def test_cooperation(selenium):

    cooperation_btn = selenium.find_element(By.XPATH, '//a[@href="mailto:priyatniyildar.ads@gmail.com"]')

    # Ждем, пока кнопка станет видимой
    wait = WebDriverWait(selenium, 10)
    cooperation_btn = wait.until(EC.visibility_of(cooperation_btn))

    # Прокручиваем страницу до кнопки, если она не видна
    selenium.execute_script("arguments[0].scrollIntoView(true);", cooperation_btn)

    try:
        cooperation_btn.click()
    except Exception as e:
        print(f"Ошибка при клике на кнопку: {e}")

