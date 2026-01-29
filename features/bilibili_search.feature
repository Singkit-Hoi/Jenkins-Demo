Feature: Bilibili 搜索測試

  Scenario: 搜索 Jenkins 教程
    Given 我打開了 Bilibili 首頁
    When 我在搜索框輸入 "Jenkins"
    And 我點擊搜索按鈕
    Then 頁面標題應該包含 "Jenkins"
