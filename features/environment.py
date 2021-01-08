from selenium.webdriver import Firefox

def before_all(context):
    context.browser = Firefox()

def before_feature(context):
    ...

def before_scenario(context):
    ...

def before_step(context):
    ...

def after_all(context):
    context.browser.quit()

