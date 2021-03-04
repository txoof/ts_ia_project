#!/usr/bin/env python3
# coding: utf-8






import time
import selenium
from selenium import webdriver
from pathlib import Path
import os
import sys






try:
    local_path = os.path.dirname(os.path.realpath(__file__))
except NameError as e:
    local_path = os.getcwd()






PATH = os.environ.get("PATH")
os.environ['PATH'] = f'{PATH}:{local_path}'






class AIProject:
  def __init__(self, url, recentText, lastText, diffTexts, driver, i, allTextS):
     self.url = url
     self.recentText = recentText
     self.lastText = lastText
     self.diffTexts = diffTexts
     self.driver = driver
     self.i = i
     self.allText = allText
  def openBrowser(self):
     self.driver.get(url)
     self.driver.maximize_window()
     GetRidOfButton = self.driver.find_element_by_id("_evidon-accept-button")
     GetRidOfButton.click()
     time.sleep(5)
     self.driver.get(url)
     print("browser opened")


     
  def clickButton(self):
     button = self.driver.find_element_by_id("id-page-buttons")
     button.click()
     time.sleep(.5)
  def saveHTML(self):
     self.recentText = self.lastText
     self.lastText = self.driver.page_source
     if self.lastText == self.recentText:
         self.diffTexts = False
         self.lastText = ""
     else:
         self.allText += self.recentText
  def saveToFile(self):
     text_file = open("IAoutput", "w")
     text_file.truncate(0)
     text_file.write(self.allText)
     text_file.close()
     print("file updated")






begin = time.time()
url = "https://outlet.us.dell.com/ARBOnlineSales/Online/InventorySearch.aspx?brandid=2801&c=us&cs=28&l=en&s=dfb"
recentText = ""
lastText = ""
diffTexts = True
driver = webdriver.Firefox()
i = 0
allText = ""
runWholeProject = AIProject(url, recentText, lastText, diffTexts, driver, i, allText)
runWholeProject.openBrowser()
while runWholeProject.diffTexts:
  try:
     while runWholeProject.diffTexts:
        runWholeProject.clickButton()
        runWholeProject.saveHTML()
        runWholeProject.i = runWholeProject.i + 1
        print("times clicked:", runWholeProject.i)
        if runWholeProject.i >= 200:
           runWholeProject.diffTexts = False
           print("default end")
  except selenium.common.exceptions.StaleElementReferenceException:
     time.sleep(3)
     print("stale")
  except selenium.common.exceptions.ElementClickInterceptedException:
     print("click intercept")
  finally:
      print("Exception passed")
runWholeProject.saveToFile()
end = time.time()
elapsed = end - begin
print(f"This process took {elapsed} seconds to complete")






# import time
# import selenium
# from selenium import webdriver

# class AIProject:
#   def __init__(self, url, recentText, lastText, diffTexts, driver, i, allTextS):
#      self.url = url
#      self.recentText = recentText
#      self.lastText = lastText
#      self.diffTexts = diffTexts
#      self.driver = driver
#      self.i = i
#      self.allText = allText
#   def openBrowser(self):
#      self.driver.get(url)
#      self.driver.maximize_window()
#      GetRidOfButton = self.driver.find_element_by_id("_evidon-accept-button")
#      GetRidOfButton.click()
#      time.sleep(5)
#      self.driver.get(url)
#      print("browser opened")


     
#   def clickButton(self):
#      button = self.driver.find_element_by_id("id-page-buttons")
#      button.click()
#      time.sleep(.5)
#   def saveHTML(self):
#      self.recentText = self.lastText
#      self.lastText = self.driver.page_source
#      if self.lastText == self.recentText:
#          self.diffTexts = False
#          self.lastText = ""
#      else:
#          self.allText += self.recentText
#   def saveToFile(self):
#      text_file = open("IAoutput", "w")
#      text_file.truncate(0)
#      text_file.write(self.allText)
#      text_file.close()
#      print("file updated")

# begin = time.time()
# url = "https://outlet.us.dell.com/ARBOnlineSales/Online/InventorySearch.aspx?brandid=2801&c=us&cs=28&l=en&s=dfb"
# recentText = ""
# lastText = ""
# diffTexts = True
# driver = webdriver.Firefox()
# i = 0
# allText = ""
# runWholeProject = AIProject(url, recentText, lastText, diffTexts, driver, i, allText)
# runWholeProject.openBrowser()
# while runWholeProject.diffTexts:
#   try:
#      while runWholeProject.diffTexts:
#         runWholeProject.clickButton()
#         runWholeProject.saveHTML()
#         runWholeProject.i = runWholeProject.i + 1
#         print("times clicked:", runWholeProject.i)
#         if runWholeProject.i >= 200:
#            runWholeProject.diffTexts = False
#            print("default end")
#   except selenium.common.exceptions.StaleElementReferenceException:
#      time.sleep(3)
#      print("stale")
#   except selenium.common.exceptions.ElementClickInterceptedException:
#      print("click intercept")
#   finally:
#       print("Exception passed")
# runWholeProject.saveToFile()
# end = time.time()
# elapsed = end - begin
# print("This process took", elasped, "seconds to complete")


