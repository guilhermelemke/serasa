from selenium.webdriver import Firefox

def before_all(context):
    context.browser = Firefox()

def after_all(context):
    context.browser.quit()
