from selenium import webdriver

chromDriver = webdriver.Chrome()
chromDriver.get("https://web.whatsapp.com/")
chromDriver.maximize_window()

again = True

while again:
    choose = input('wanna spam? 1 for YES, 2 for NO: ')
    if choose == '2':
        again = False
    elif choose == '1':
        name = input("Enter name or group: ")
        msg = input("Enter message: ")
        count = int(input("enter count: "))

        input("Enter X ")

        user = chromDriver.find_element_by_xpath("//span[@title='{}']".format(name))
        user.click()

        msg_box = chromDriver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

        for index in range(count):
            msg_box.send_keys(msg)
            chromDriver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

        print("success")
    else:
        print('invalid option...')
        again = False
