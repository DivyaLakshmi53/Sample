# Created by DivyaSivakumar at 4/09/2020
Feature: Products API Tests
  # Enter feature description here

  Scenario: Verify Get All Products api call gets all products in db
  
  Given I execute get all products rest api
  When I get all products from db
  Then Total no of products in get call matches products count from db