from selenium import webdriver

driver = webdriver.Chrome(executable_path="tempat file")
driver.get('https://web.whatsapp.com/')

name = input('Nama: ')
msg = input('Pesan: ')
count = int(input('Jumlah pesan: '))

input("Enter")


user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')
    button.click()

