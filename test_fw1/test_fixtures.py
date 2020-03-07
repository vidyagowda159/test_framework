import unittest
import HtmlTestRunner
class Testapps(unittest.TestCase):
    from settings import driver
    from selenium.webdriver.common.action_chains import ActionChains
    action = ActionChains(driver)
    i=0

    def setUp(self):
        print('\ngetting url')
        from settings import urls,urls1
        while Testapps.i<len(urls):
            self.driver.get(urls[Testapps.i])
            Testapps.i+=1

        '''
        while len(urls1)-len(urls)!=len(urls1):
            self.driver.get(urls[0])
            self.driver.maximize_window()
            urls.remove(urls[0])
            print('urls : ',urls)
            break
        '''
    def tearDown(self):
        print('finshed executing current method')

    def test_locators_w3(self):
        self.driver.implicitly_wait(30)
        print('in w3schools')
        self.driver.find_element_by_xpath('//a[@id="navbtn_examples"]').click()
        self.driver.find_element_by_xpath("//a[text()='HTML Examples']").click()

    def test_mmt(self):
        self.driver.implicitly_wait(10)
        import time
        print('in mmt')
        main_page=self.driver.current_window_handle
        self.driver.find_element_by_xpath("//p[contains(text(),'Login or Create Account')]").click()
        self.driver.find_element_by_xpath('//div[@class="makeFlex googleLoginBtn flexOne"]').click()
        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle
                self.driver.switch_to.window(login_page)
                self.driver.find_element_by_xpath('//input[@id="identifierId"]').send_keys('vidyagowda.temp1@gmail.com')
                self.driver.find_element_by_xpath('//span[contains(text(),"Next")]').click()
                time.sleep(2)
                self.driver.find_element_by_xpath('//input[@class="whsOnd zHQkBf"]').send_keys('159theju@')
                self.driver.find_element_by_xpath('//span[contains(text(),"Next")]').click()
        self.driver.switch_to.window(main_page)
        self.driver.find_element_by_xpath('//span[@class="crossIcon popupSprite popupCrossIcon"]').click()

    def test_mmt_booking(self):
        print('Booking started')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//span[text()="Buses"]').click()
        self.driver.find_element_by_xpath('//input[@id="fromCity"]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="From"]').send_keys('Bengaluru')
        self.driver.find_element_by_xpath('//span[text()="Bengaluru, Karnataka"]').click()
        self.driver.find_element_by_xpath('//input[@id="toCity"]').click()
        import time
        time.sleep(5)
        self.driver.find_element_by_xpath('//div[@id="webklipper-publisher-widget-container-notification-close-div"]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="To"]').send_keys('Pune')
        self.driver.find_element_by_xpath('//span[text()="Pune, Maharashtra"]').click()
        self.driver.find_element_by_xpath('//input[@id="travelDate"]').click()
        self.driver.find_element_by_xpath('//div[@aria-label="Sun Mar 15 2020"]').click()
        self.driver.find_element_by_xpath('//button[@id="search_button"]').click()
        self.driver.find_element_by_xpath('(//a[text()="Select Seats"])[1]').click()
        self.driver.find_element_by_xpath('//a[@class="btnClose latoBold font12 deepskyBlueText"]').click()

    #@pytest.mark.dependency(name="mmt_logout",depends=["mmt_booking"])
    def test_mmt_logout(self):
        print("loggging out")
        self.driver.find_element_by_xpath('//span[@class="chUserInfoName appendBottom2 latoBold"]').click()
        self.driver.find_element_by_xpath("//p[text()='Logout']").click()
        #updated

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\vidya gowda\PycharmProjects\test_framework\reports'),verbosity=2)