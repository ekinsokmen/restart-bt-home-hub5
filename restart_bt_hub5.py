import argparse
from selenium import webdriver

parser = argparse.ArgumentParser(description='Restart BT Home Hub 5 Router')
parser.add_argument('-p', '--admin_pass', type=str, nargs=1, help='Admin password of the router', required=True)
parser.add_argument('base_url', type=str, nargs=1, help='Base URL of the router like http://192.168.0.1')
args = parser.parse_args()

base_url = args.base_url[0]
admin_pass = args.admin_pass[0]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

# Login
driver.get(base_url + '/index.htm?pg=settings.htm')
driver.switch_to.frame('mainFrame')
pass_input=driver.find_element_by_id('ob_text_1')
pass_input.send_keys(admin_pass)
ok_button=driver.find_element_by_id('submit_ok')
ok_button.click()

# Goto Advanced Settings/System and restart
driver.get(base_url + '/index.htm?pg=ad_S_restart.htm')
driver.switch_to.frame('mainFrame')
restart_button=driver.find_elements_by_name('restart')[0]

print(restart_button)
