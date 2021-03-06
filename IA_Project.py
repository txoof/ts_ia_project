#!/usr/bin/env python3
# coding: utf-8






VERSION = "2021.03.11_20.25"
import time
import selenium
from selenium import webdriver
from pathlib import Path
import os
# import sys
import my_path






PATH = os.environ.get("PATH")
os.environ['PATH'] = f'{my_path.absolute_path}:{PATH}'






print(f'VERSION: {VERSION}')
print(f'PATH: {os.environ["PATH"]}')






class AIProject:
  def __init__(self, url, recentText, lastText, diffTexts, driver, i, allTextS):
     self.url = url
     self.recentText = recentText
     self.lastText = lastText
     self.diffTexts = diffTexts
     self.driver = driver
     self.i = i
     self.allText = allText
     self.output_path = Path('~/Desktop/IA_Project_output.txt').expanduser()
     self.path_string = str(self.output_path)
  def openBrowser(self):
     self.driver.get(url)
     self.driver.maximize_window()
     try:
         GetRidOfButton = self.driver.find_element_by_id("_evidon-accept-button")
         GetRidOfButton.click()
     except selenium.common.exceptions.NoSuchElementException as e:
        print(f'yaaarg! couldn\'t get rid of button! {e}')
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
     text_file = open(self.path_string, "w")
     text_file.truncate(0)
     text_file.write(self.allText)
     final_output = os.path.splitext(self.path_string)[0]
     #os.system(f"open {self.path_string}")
     #os.rename(self.path_string, final_output + '.html')
     #os.system(f"open {final_output + '.html'}")
     #print(final_output + '.html')
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
  #added try/except for case of missing consent button
  except selenium.common.exceptions.StaleElementReferenceException:
     time.sleep(3)
     print("stale")
  except selenium.common.exceptions.ElementClickInterceptedException:
     print("click intercept")
runWholeProject.saveToFile()
runWholeProject.driver.close()
end = time.time()
elapsed = end - begin
print(f"This process took {elapsed} seconds to complete")






# class AIProject:
#   def __init__(self, url, recentText, lastText, diffTexts, driver, i, allTextS):
#      self.url = url
#      self.recentText = recentText
#      self.lastText = lastText
#      self.diffTexts = diffTexts
#      self.driver = driver
#      self.i = i
#      self.allText = allText
#      self.output_path = Path('~/Desktop/IA_Project_output').expanduser()
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
# print(f"This process took {elapsed} seconds to complete")






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


