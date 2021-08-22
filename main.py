from selenium import webdriver

driver = webdriver.Firefox()

token = 'Token GOes Here'

script = "setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = " + f"'\"{token}\"'" + ";}, 50);setTimeout(() => {location.reload();});"
print(script)

pageurl = 'https://discord.com/login'
driver.get(pageurl)
driver.execute_script(script)
