Feature: Buy items

    # ctrl + option + L - re-align gherkin statements


  Scenario: Target - login, add item, checkout
    # goto page + search item
    Given user navigates to "target" site "landing" page
    Then user should be on the "landing" page of "target" site
    When user fills text "playstation console" in "search" field
    And user clicks on the "search" button
    Then user should be on the "products_list" page of "target" site
    # sign-in account
    When user clicks on the "sign_in" button
    And user clicks on the "signin_sidebar" button
    Then user should be on the "login" page of "target" site
    When user login to account with username "oaklandtest@proton.me" and password "$oaklandTest1"
    # add item to cart
    Then user should be on the "products_list" page of "target" site
    When user clicks on product "1" in the products list page
    Then user should be on the "product" page of "target" site
    When user adds item on product page to cart and navigates to checkout page
    # checkout page
    Then user should be on the "checkout" page of "target" site
    When user clicks on the "address_edit" button if visible
    And user clicks on the "address_edit2" button if visible
    And fills out form based on table
      | first_name | last_name | address            | zip   | city    | state | phone        |
      | test       | test      | 1200 lakeshore ave | 94606 | oakland | CA    | 510-555-5555 |
    And user clicks on the "save_continue" button
    And user clicks on the "use_verified_address" button
#    When user pause test


  Scenario: Target - Product list page sorting and filtering
    Given user navigates to "target" site "landing" page
    Then user should be on the "landing" page of "target" site
    When user fills text "playstation console" in "search" field
    And user clicks on the "search" button
    Then user should be on the "products_list" page of "target" site
    When user selects by text the "Sort" element of locator "filters" and type "button"
    Then user verifies prices are sorted in "ASC" order
    When user filters the items from price range of "0" to "30"
    Then user verifies prices are filtered correctly
    # TODO: complete validation steps to verify sort order + filtering


  Scenario Outline: Target - Multiple logins
    Given user navigates to "target" site "landing" page
    Then user should be on the "landing" page of "target" site
    When user clicks on the "sign_in" button
    And user clicks on the "signin_sidebar" button
    Then user should be on the "login" page of "target" site
    When user login to account with username "<username>" and password "<password>"
    Then the "<button>" button should be visible
    @positive
    Examples: Valid users
      | username               | password      | button  |
      | oaklandtest@proton.me  | $oaklandTest1 | sign_in |
#      | oaklandtest2@proton.me | $oaklandTest2 | sign_in |
    @negative
    Examples: Invalid users
      | username              | password     | button |
      | invaliduser@gmail.com | invalid_user | login  |


  Scenario: Snkrs - Poll + add item to cart
    Given user navigates to "https://www.snkrs.com"
    Then user should be on the "landing" page of "snkrs" site
#        When user clicks on the "upcoming" button
#        Then user verifies product should have text "Air Jordan 3 'Black Cement' (DN3707-010) Release Date. Nike SNKRS"
#        Then user verifies product should have "air_jordan_3" text
#        Given user login to "snkrs"
#        When user select size "M 7 / W 8.5" to cart and proceed to checkout

