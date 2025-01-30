import allure
from selene import be, by, have
from selene.support.shared.jquery_style import s

REPO_NAME = "eroshenkoam/allure-example"
ISSUE_NUMBER = "#94"

def test_steps():
    search_for_repository(REPO_NAME)
    go_to_repository(REPO_NAME)
    open_issue_tab()
    should_see_issue_with_number(ISSUE_NUMBER)

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s('[data-target="qbsearch-input.inputButton"]').click()
    s('#query-builder-test').should(be.visible).send_keys(repo).press_enter()

@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).should(be.visible).click()

@allure.step("Открываем вкладку Issues")
def open_issue_tab():
    s("#issues-tab").should(be.visible).click()

@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(f'a[href="/eroshenkoam/allure-example/issues/94"] span').should(be.visible).should(have.text("One piece"))
