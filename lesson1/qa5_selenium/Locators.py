# Locators
#==========
# id
# name
# class name
# css selector
# xpath
# link text
# partial link text
# tag name

# <input         class="gLFyf gsfi" maxlength="2048" name="q" type="text"

# Locator ID
# <element_name  attr1="aaa"  attr2="bbbb"  attr3="cccc"  id="123"
# driver.find_element(By.ID,"123")
# driver.find_element(By.CSS_SELECTOR,"#123")
# driver.find_element(By.CSS_SELECTOR,"[id='123']")

# Locator Name
# <element_name  attr1="aaa"  attr2="bbbb"  name="abc"  id="123"
# driver.find_element(By.NAME,"abc")

# CSS Selector
# <input  class="gLFyf gsfi" maxlength="2048" name="q" type="text"
# driver.find_element(By.CSS_SELECTOR,"input[type='text']")
# driver.find_element(By.CSS_SELECTOR,"input[name='q']")
# driver.find_element(By.CSS_SELECTOR,"input[name='q'][type='text']")
# driver.find_element(By.CSS_SELECTOR,"[name='q']")

# Class Name
#  <input     class="gLFyf gsfi" maxlength="2048" name="q" type="text"
# driver.find_element(By.CLASS_NAME,"gLFyf")
# driver.find_element(By.CSS_SELECTOR,".gLFyf")
# driver.find_element(By.CSS_SELECTOR,"input.gLFyf")
# driver.find_element(By.CSS_SELECTOR,"input[class='gLFyf gsfi']")
# driver.find_element(By.CLASS_NAME,"gsfi")
# driver.find_element(By.CSS_SELECTOR,".gsfi")

# XPATH
#  <input     class="gLFyf gsfi" maxlength="2048" name="q" type="text"
# driver.find_element(By.XPATH,"//input[@class='gLFyf gsfi']")

# <input
#   <a  attr1="abc"
#   <a  attr1="abc"
# driver.find_element(By.XPATH,"//input/a[1]")

# <i class="material-icons leading-icon">logout</i>
# driver.find_element(By.XPATH,"//i[text()='logout']")

# Link Text
# <a href="reservation.php" >Flights</a>
# driver.find_element(By.LINK_TEXT,"Flights")
# Partial Link Text
# driver.find_element(By.PARTIAL_LINK_TEXT,"Fli")

# Tag Name
#  <input     class="gLFyf gsfi" maxlength="2048" name="q" type="text"
# driver.find_element(By.TAG_NAME,"input")