import allure
from allure_commons.types import Severity
from selene import browser, by, be, have
from selene.support.shared.jquery_style import s

# Константы
REPO_NAME = "eroshenkoam/allure-example"
SEARCH_INPUT = '[data-target="qbsearch-input.inputButton"]'
QUERY_INPUT = '#query-builder-test'
ISSUES_TAB = "#issues-tab"
ISSUE_TEXT = "One piece"
ISSUE_SELECTOR = 'a[href="/eroshenkoam/allure-example/issues/94"] span'

@allure.tag('web')
@allure.feature("GitHub Issues")
@allure.story("Проверка Issues в репозитории")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Aleksandr Bardashevich")
@allure.description("Тест проверяет наличие репозитория и Issues")
@allure.link("https://github.com", name="GitHub")
def test_github_issue():
    @allure.step("Открываем GitHub")
    def open_github():
        browser.open("https://github.com")

    @allure.step("Ищем репозиторий: {repo}")
    def search_for_repository(repo: str):
        s(SEARCH_INPUT).click()
        s(QUERY_INPUT).should(be.visible).send_keys(repo).press_enter()

    @allure.step("Кликаем по репозиторию: {repo}")
    def open_repository(repo: str):
        s(by.link_text(repo)).should(be.visible).click()

    @allure.step("Открываем вкладку Issues")
    def open_issues_tab():
        s(ISSUES_TAB).should(be.visible).click()

    @allure.step(f"Проверяем, что Issue '{ISSUE_TEXT}' отображается")
    def should_see_issue(issue_text: str):
        s(ISSUE_SELECTOR).should(be.visible).should(have.text(issue_text))

    # Выполнение шагов
    open_github()
    search_for_repository(REPO_NAME)
    open_repository(REPO_NAME)
    open_issues_tab()
    should_see_issue(ISSUE_TEXT)