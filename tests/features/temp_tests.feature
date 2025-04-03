Feature: Test scenarios

  # ctrl + option + L - re-align gherkin statements

  @test_snkrs
  Scenario: snkrs landing custom method
    When snkrs landing custom method

  @test_walmart
  Scenario: walmart landing custom method
      When walmart landing custom method

  Scenario: Snkrs - Poll + add item to cart
    Given user navigates to "https://www.snkrs.com"
    Then user should be on the "landing" page of "snkrs" site
#        When user clicks on the "upcoming" button
#        Then user verifies product should have text "Air Jordan 3 'Black Cement' (DN3707-010) Release Date. Nike SNKRS"
#        Then user verifies product should have "air_jordan_3" text
#        Given user login to "snkrs"
#        When user select size "M 7 / W 8.5" to cart and proceed to checkout