__author__ = 'iamrishap'
from splinter.browser import Browser
from time import sleep
USER = 'z5202535'
PASS = 'Rs625005'
BASE_URL = 'https://my.unsw.edu.au/'
br = ''

LEC = {'DWDM': '5082', 'BIG': '8532', 'ML': '2113', 'PM': '6290'}  # 'DS': '2024'
LAB = {'bigLf5_1': '8533', 'bigLf5_2': '10333', 'bigLth1': '10721', 'bigLth6': '8534',
       'bigLm4_1': '8535', 'bigLm4_1': '10505', 'mlLth5': '2114', 'mlLth6_1': '2115',
       'mlLth6_2': '2116', 'mlLth7_1': '2117', 'mlLth7_2': '2118', 'mlLth8': '2119',
       'mlLm5': '2120', 'mlLm6': '2121', 'mlLm7': '2122', 'mlLtu4': '2123',
       'mlLtu5': '2124','mlLth6': '2125', 'mlLth7': '2126', 'mlLw4': '2127',
       'mlLw5_1': '2128', 'mlLw5_2': '2129'}


def load_login_page(br):
    br.visit(BASE_URL)
    br.find_by_text('Sign On').first.click()
    # sleep(5)


def login(br):
    # alert = br.get_alert()
    # print(alert.text)
    # alert.dismiss()
    # br.find_by_tag('button').first.click()
    # br.fill('q', 'intp\n')
    br.fill('username', USER)
    br.fill('password', PASS + '\n')
    # br.find_by_value('Agree and sign on').first.click()


def navigate_to_course_enrol(br):
    br.visit('https://my.unsw.edu.au/admitted/admittedClassEnrol/programs.xml')
    # sleep(3)
    br.find_by_value('Update Enrolment').first.click()
    # sleep(3)
    br.find_by_value('Proceed to Enrol').first.click()
    # sleep(3)
    found = find_course_avail(br)
    if found != '':
        print('Found on page 1')
        send_notification(found)
        return
    br.find_by_value('Add Classes').first.click()
    found = find_course_avail(br)
    if found != '':
        print('Found on page 2')
        send_notification(found)


def find_course_avail(br):
    text = ''
    for lecture, code in LEC.items():
        if br.is_text_present(code):
            text += lecture + ' '
    return text


def send_notification(text):
    import smtplib

    gmail_user = 'iamrishap@gmail.com'
    gmail_password = 'ris625005'

    sent_from = gmail_user
    to = ['sharmarishap@gmail.com']
    subject = 'Course Available'
    body = text + 'course is available now.'
    email_text = """\r\nFrom: %s\r\nTo: %s\r\nSubject: %s\r\n%s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
    except:
        print('Your code sucks')


def scrap_send_notification():
    '''
    Calling all the module functions to do the work. This is just a wrapper function to scrap and update instances.
    '''
    br = Browser('chrome')
    load_login_page(br)
    login(br)
    navigate_to_course_enrol(br)
    br.quit()
    exit(0)


if __name__ == '__main__':
    scrap_send_notification()