@team_cubivue @bk @release_sprint_24.02.13
Feature: BK Cubivue product api validation
  As an SQA
  I want to verify BK platform API functions are working
  So that user can perform successfull jobs


  @api @priority_high @regression
    Scenario: Verify Get Job Status endpoint
    Given I login to BK platorm
    Then I must see success response in job status