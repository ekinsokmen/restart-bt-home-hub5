Python script to restart a BT Home Hub 5 router programmatically

Selenium Webdriver is used to connect and login to the routers web admin panel. The base URL of the router and the admin password should be provided as arguments. 

## Running using Docker
The script can be executed using Docker. Clone the code and run following command in the project directory:
```
docker run -w /usr/workspace -v $(pwd):/usr/workspace joyzoursky/python-chromedriver:3.8-selenium python restart_bt_hub5.py -p ADMIN_PASS http://192.168.0.1
```

Script based on router firmware version: `v0.07.06.01239-BT`. Tweaks may be necessary for different versions.