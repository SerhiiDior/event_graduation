"""test data"""
import random
import os

# from Locators.locators import ProfilePageEventsMenuLocators as locator

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))


class Config: # pylint: disable=too-few-public-methods
    """TEST_MODE set to True, runs rests in silent mode: no UI while testing"""

    TEST_MODE = False  # False
    HOME_URL = "http://34.65.101.58:5002/home/events/?page=1"
    # BROWSER = 'Chrome'
    BROWSER = 'Firefox'


class CreateEventData():

    TITLE = random.choice(['New Year', 'Christmas', 'Malanka'])
    IMAGE = os.path.join(CURRENT_PATH, 'imageAddEvent\\party.jpg')
    LOGIN_USER = 'user@gmail.com'
    PASSWORD_USER = '1qaz1qaz'
    DESCRIPTION = {"New Year": "Happy 2020 Year!!!Weclome to the Party"}
    ATT_DATA = "innerHtml"


class ContactUsData:
    """Data for entering description into field in 'Contact us' page"""
    DESCRIPTION_FOR_CONTACT = "You have a very bed user and event!!!"


class ProfileMenuPageHeaderInfo:
    """Test data for userinfo header from profile menu - events panels page"""
    USER_NAME_LABEL = 'User Name:'
    USER_NAME_DATA = 'UserTest'
    USER_AGE_LABEL = 'Age:'
    USER_AGE_DATA = '19'
    USER_GENDER_LABEL = 'Gender:'
    USER_GENDER_DATA = 'Other'
    USER_EMAIL_LABEL = 'Email:'
    USER_EMAIL_DATA = 'user@gmail.com'
    USER_INTERESTS_LABEL = 'Interests:'
    USER_INTERESTS_DATA = {
        '#Mount',
        '#Golf',
        '#Team-Building',
        '#Swimming',
        '#Gaming',
        '#QC testing event',
        '#Meeting',
        '#Summer'}


class ProfilePageEventsMenu: # pylint: disable=too-few-public-methods
    ''' Testdata: Locators for event's menu.
    class ProfilePageEventsMenuLocators'''
    FUTURE_EVENTS = 'FUTURE EVENTS'
    ARCHIVE_EVENTS = 'ARCHIVE EVENTS'
    VISITED_EVENTS = 'VISITED EVENTS'
    EVENTS_TO_GO = 'EVENTS TO GO'
    ADD_EVENT = 'ADD_EVENT'

    # used for pairing menu tabs and locators for the tabs indicators
    # TAB_INDICATOR_DICT = {
    #     FUTURE_EVENTS: locator.locators_dict['FUTURE_EVENTS_TAB_INDICATOR'],
    #     ARCHIVE_EVENTS: locator.locators_dict['ARCHIVE_EVENTS_TAB_INDICATOR'],
    #     VISITED_EVENTS: locator.locators_dict['VISITED_EVENTS_TAB_INDICATOR'],
    #     EVENTS_TO_GO: locator.locators_dict['EVENTS_TO_GO_TAB_INDICATOR'],
    #     ADD_EVENT: locator.locators_dict['ADD_EVENT_TAB_INDICATOR']
    # }


class HomePageOptionsPanel: # pylint: disable=too-few-public-methods
    '''Left top menu (config, notification, logout) with user logo'''
    USER_NAME_DATA_DICT = {'user@gmail.com': 'UserTest'}


class CartPanelsAtProfilePage: # pylint: disable=too-few-public-methods
    """ Events menu -> panel(s) object locators testdata """
    CART_NTH = 'CART_NTH'
    BLANK_CART = 'No Results'
    CART_PANEL = 'CART_PANEL'
    BLANK_CART_TEXT = 'No Results'
    CART_NTH_ID = ''  # on mouse hover - tip arising


class EditProfileData: # pylint: disable=too-few-public-methods
    USER_NAME = 'Tester'
    CURRENT_PASS = '1qaz1qaz'
    NEW_PASS = '2qaz2qaz'


class CategoriesPage: # pylint: disable=too-few-public-methods
    category_old = 'Hello'
    category_new = 'Hello1'
