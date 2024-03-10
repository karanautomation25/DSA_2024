# # USe wait and then click()
#
# def click(driver,locator):
#     wait = WebDriverWait(driver, 15)
#     wait.until(EC.presence_of_element_located(Page.xpath)).click()
#
#
# click(driver,(By.id,'username'))
#
#
# driver = context.browser.driver
# wait = WebDriverWait(driver, 15)
# page = CmsAuthenticationPage()
#
# action = ActionChains(driver)
# action.double_click(today_date).perform()
# issue_type_dropdown = wait.until(EC.element_to_be_clickable(page.issue_type_dropdown),'')
#
# date_on_drop_down = wait.until(EC.visibility_of_element_located(page.date_on_issue_type_dropdown), msg)
# date_value = date_on_drop_down.get_attribute("value")
#
# Actions Class---------------------------------------------------------------------------------
# actions = ActionChains(driver)
# actions.move_to_element(issue_type_dropdown).perform()
# actions.click(issue_type_dropdown).perform()
#actions.context_click(first_company).perform()

# actions.move_to_element(date_today).pause(0.3).perform()
# driver.execute_script("arguments[0].click();", an_issue)
#
# page = CmsPage()
# add_new_button_locator = page.add_new_button
#
# Class CMSPAge(BasePage):
#     def __init__():
#         super(CMSPage,self).__init__(context=context)
#         self.username =(By.CSS_SELECTOR,'#id')
#         self.pswd = (By.CSS_SELECTOR,'.class')
#         self.kk = (By.XPATH,"//input[@attribute = 'val']")
#         self.custom_email_tab = (By.CSS_SELECTOR, '.ant-menu-inline li:nth-child(4)')
#         self.first_image_in_media_gallery = (By.XPATH, "(//div[contains(@class,'ant-card')])[1]")
#         self.tables_tab = (By.XPATH, "//span[text()='Tables']")
#         self.dynamic_year_to_select = "//div[@class='ant-select-item-option-content' and text()='{}']"
#         self.dyn_popup = "//*[contains(text(),'dyn_popup_text')]"
#         self.search_issues_button = (By.CSS_SELECTOR, '#header-dashboard-tools > button:nth-child(2)')
#         self.publish_issue_button_enabled = (
#             By.XPATH, "//*[contains(@id, 'top-editor-tools')]//*[text()='Publish']/parent::button[not(@disabled)]")
#
#
#         self.newsletter_cont_video_thumbnail = (
#         By.XPATH, ".//ancestor::div[@class='mjml-story-box']//div[contains(@class,'thumbnail')]")
#         self.head_abs_group_locator_email_preview = (By.XPATH, "//div[@class='description']/parent::div")


# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
#
# tag_editor_search_field.send_keys(Keys.CONTROL + "a")


# images_attributes = page.images_attributes
#     if first_image.is_displayed():
#         wait.until(EC.visibility_of_element_located(images_attributes), "Not able to locate images.")
#         elements = driver.find_elements(*page.images_attributes)
#     else:
#         assert False, "Cannot find first image"

# driver.execute_script("window.scrollTo(0,0);")

# context.original_window = driver.current_window_handle
# time.sleep(10)
# wait.until(EC.element_to_be_clickable(page.issue_preview_new_version), 'New issue preview option not found').click()
# wait.until(EC.number_of_windows_to_be(2))
# for window_handle in driver.window_handles:
#     if window_handle != context.original_window:
#         driver.switch_to.window(window_handle)
#         break
# context.browser.switch_to_next_window(0)
# wait.until(EC.visibility_of_element_located(page.add_content_dropdown), msg).click()

# dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
# dropdown.select_by_visible_text("Female")
# dropdown.select_by_index(0)

# from selenium import webdriver
#
# #chrome driver
# from selenium.webdriver.chrome.service import Service
# #-- Chrome
# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)