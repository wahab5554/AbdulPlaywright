@team_cubivue @pakke @release_sprint_24.02.13
Feature: Pakke Cubivue product validation
  As an SQA
  I want to verify Pakke platform functions are working
  So that user can perform successfull delivery orders



@team_cubivue @pakke @release_sprint_24.02.13
Feature: Pakke Cubivue product validation
  As an SQA
  I want to verify Pakke platform functions are working
  So that user can perform successfull delivery orders


  @api @priority_high @regression @e2e
    Scenario: Verify Package daoShop delivery for 0-1 kg for Guest
    Given I land on Pakke Home page
    When  I select Package
    And I select daoShop
    And I select parcel weight 0-1 kg
    And  I land on Information screen
    And  I submit information with daiPickup enabled address
    And I select daoPickup
    And I enter receipent Details
    And I click on confirm check box
    Then I must see log in or register here
    And I must see Continue as Guest
    When I click on contuinue as Guest
    Then I must see parcel ready for pick up details
    And I must see package for collection option
    When I select At Front door with checked confirmation
    Then  I must see To Payment button is enabled
    When I click on To Payement Button
    Then I am navigated to Checkout screen
    And I must see voucher code apply text box
    And I must see +Add New parcel button
    And I must see total Kr is correct
    When I check terms and condition with VISA
    Then I must see Pay button is enabled
    When I click Pay button
    Then I must see payment card screen
    When I enter valid card number
    Then I must see generate Label button
    When I click generate label button
    Then I must get order confirmation email
    And I must see Prepare Your parcel screen information