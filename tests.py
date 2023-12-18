import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

def test_youtube_btn(selenium):
    youtube_btn = selenium.find_element(By.CSS_SELECTOR, 'a[href="https://www.youtube.com/@pleasantildar"]')

    # Получим текущее количество окон
    current_windows = selenium.window_handles
    youtube_btn.click();
    # Ожидание появления нового окна
    WebDriverWait(selenium, 10).until(EC.new_window_is_opened(current_windows))

    # Получим все окна после нажатия кнопки
    new_windows = selenium.window_handles

    # Переключимся на новое окно
    selenium.switch_to.window(new_windows[-1])
    # Проверка, что текущий URL соответствует ожидаемому
    expected_url = "https://www.youtube.com/@pleasantildar"
    assert selenium.current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {selenium.current_url}"

def test_twitter_btn(selenium):
    twitter_btn =selenium.find_element(By.CSS_SELECTOR, 'a[href="https://www.twitter.com/master_ildar"]')
    
    current_windows = selenium.window_handles
    twitter_btn.click();
   
    WebDriverWait(selenium, 10).until(EC.new_window_is_opened(current_windows))

    new_windows = selenium.window_handles

    selenium.switch_to.window(new_windows[-1])

    expected_url = "https://twitter.com/i/flow/login?redirect_after_login=%2Fmaster_ildar"
    assert selenium.current_url == expected_url, f'Expected URL: {expected_url}, Actual URL: {selenium.current_url}'
    

def test_twitch_btn(selenium):
    twitch_btn =selenium.find_element(By.CSS_SELECTOR, 'a[href="https://www.twitch.tv/ildarzhe"]')
    current_windows = selenium.window_handles
    twitch_btn.click();

    WebDriverWait(selenium, 10).until(EC.new_window_is_opened(current_windows))

    new_windows = selenium.window_handles

    selenium.switch_to.window(new_windows[-1])

    expected_url = "https://www.twitch.tv/ildarzhe"
    assert selenium.current_url == expected_url, f'Expected URL: {expected_url}, Actual URL: {selenium.current_url}'

def test_telegram_btn_header(selenium):
    telegram_btn_header =selenium.find_element(By.XPATH, '//a[@href="https://www.t.me/unpleasent" and @class="header-link"]')
    current_windows = selenium.window_handles
    telegram_btn_header.click();

    WebDriverWait(selenium, 10).until(EC.new_window_is_opened(current_windows))

    new_windows = selenium.window_handles

    selenium.switch_to.window(new_windows[-1])

    expected_url = "https://www.t.me/unpleasent"
    assert selenium.current_url == expected_url, f'Expected URL: {expected_url}, Actual URL: {selenium.current_url}'

def test_instagram_btn(selenium):
    instagram_btn =selenium.find_element(By.CSS_SELECTOR, 'a[href="https://www.instagram.com/masterildar"]')
    current_windows = selenium.window_handles
    instagram_btn.click();

    WebDriverWait(selenium, 10).until(EC.new_window_is_opened(current_windows))

    new_windows = selenium.window_handles

    selenium.switch_to.window(new_windows[-1])

    expected_url = "https://www.instagram.com/masterildar/"
    assert selenium.current_url == expected_url, f'Expected URL: {expected_url}, Actual URL: {selenium.current_url}'
    
  
def test_vk_btn(selenium):   
    vk_btn =selenium.find_element(By.CSS_SELECTOR, 'a[href="https://vk.com/pleasentildar"]')
    current_windows = selenium.window_handles
    vk_btn.click();

    WebDriverWait(selenium, 10).until(EC.new_window_is_opened(current_windows))

    new_windows = selenium.window_handles

    selenium.switch_to.window(new_windows[-1])

    expected_url = "https://vk.com/pleasentildar"
    assert selenium.current_url == expected_url, f'Expected URL: {expected_url}, Actual URL: {selenium.current_url}'

def test_tg_bot_btn(selenium):
    telegram_bot_btn = selenium.find_element(By.XPATH, '//a[@href="https://t.me/PriyatniyIldar_bot" and @class="content-description__button button"]')
    current_windows = selenium.window_handles

    #Прокрутить страницу до элемента
    selenium.execute_script("arguments[0].scrollIntoView(true);", telegram_bot_btn)

    # Наведение курсора с использованием JavaScript
    selenium.execute_script("arguments[0].focus(); arguments[0].click();", telegram_bot_btn)

    WebDriverWait(selenium, 10).until(EC.new_window_is_opened(current_windows))

    new_windows = selenium.window_handles

    selenium.switch_to.window(new_windows[-1])

    expected_url = "https://t.me/PriyatniyIldar_bot"
    assert selenium.current_url == expected_url, f'Expected URL: {expected_url}, Actual URL: {selenium.current_url}'

def test_merch_btn(selenium):
   
    buy_btn = selenium.find_element(By.XPATH, '(//a[@class="card__link"])[1]')

    selenium.execute_script("arguments[0].scrollIntoView(true);", buy_btn)

    wait = WebDriverWait(selenium, 10)
    buy_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '(//a[@class="card__link"])[1]')))

    buy_btn.click()

    expected_url == EC.url_to_be("https://prostomerch.store/catalog/collections/priyatnyj-ildar/categories/merch")
    assert EC.Alert

def test_cooperation(selenium):
    cooperation_btn = selenium.find_element(By.XPATH, '//a[@href="mailto:priyatniyildar.ads@gmail.com"]')
    current_windows = selenium.window_handles

    # Прокрутить страницу до элемента
    selenium.execute_script("arguments[0].scrollIntoView(true);", cooperation_btn)

    # Наведение курсора с использованием JavaScript
    selenium.execute_script("arguments[0].focus(); arguments[0].click();", cooperation_btn)

    WebDriverWait(selenium, 10).until(EC.new_window_is_opened(current_windows))

    new_windows = selenium.window_handles

    selenium.switch_to.window(new_windows[-1])

    expected_url = "mailto:priyatniyildar.ads@gmail.co"
    assert selenium.current_url != expected_url
