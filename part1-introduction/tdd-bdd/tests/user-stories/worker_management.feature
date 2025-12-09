Feature: Worker management

  Scenario: Creating a worker
    Given a worker named "John" with salary 30 and work hours 80 and ID 1234
    Then the worker name should be "John"
    And the salary should be 30
    And the work hours should be 80

  Scenario: Getting the annual salary
    Given a worker named "John" with salary 30 and work hours 150 and ID 1234
    When I calculate the annual salary
    Then the result should be 54000

  Scenario: Getting filial number
    Given a worker named "John" with salary 30 and work hours 150 and ID 1234
    Then the filial number should be "0001"

  Scenario: Creating a worker without filial
    When I try to create a worker named "Peter" with salary 30 and work hours 150 and ID 9099
    Then a KeyError should be raised

  Scenario: Creating a worker with less than 30 hours
    When I try to create a worker named "Peter" with salary 30 and work hours 10 and ID 9099
    Then a ValueError should be raise