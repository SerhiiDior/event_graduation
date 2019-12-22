from Tests.test_init import TestInit
from Data.credentials import user,admin
from Data.test_data import CreateEventData
from Locators.locators import CreateEvent






class TestCreateEvent(TestInit):



    def setUp(self):
        super().setUp()
        self.event = CreateEventData
        self.locator = CreateEvent



    def test_create_event(self):
        self.exec.signin.enter_actor(user['email'],user['password'])
        self.exec.navigation.click_on_profile()
        self.exec.prof_menu.click_on_add_event()
        self.exec.creat_event.upload_image()
        self.exec.creat_event.add_title(self.event.TITLE)
        self.text = self.event.DESCRIPTION['New Year'] # text add into description field for testing
        self.exec.creat_event.add_desc(self.text)
        self.text2 = 'hello'
        self.assertFalse(self.exec.base.check_if_text_present(self.locator.DESC_TEXT, self.text2)), "not equal"
        # self.exec.base.get_element_text(self.locator.DESC_TEXT)
        self.exec.base.click_on_element(self.locator.CATEGORY)
        self.exec.creat_event.add_category(self.locator.LST_CATEGORIES)
        self.exec.base.click_action(0,0)

        self.exec.base.scroll_to_element(self.locator.COUNTRY_FIELD)

        self.exec.base.click_on_element(self.locator.COUNTRY_FIELD)


        self.exec.creat_event.select_country(self.locator.COUNTRY_FIELD)

        self.exec.base.click_on_element(self.locator.CITY)
        self.exec.creat_event.select_city(self.locator.CITY)

        # self.exec.creat_event.press_button_save()

        # self.exec.base.check_if_element_exists(self.locator.SUCCESS_MSG)
        # self.exec.base.get_element_text(self.locator.SUCCESS_MSG)







