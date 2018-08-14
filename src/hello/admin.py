from helpers.director.shortcut import page_dc

class Home(object):
    template='hello/home.html'
    def __init__(self,request, engin):
        pass
    def get_context(self):
        return {}

page_dc.update({
    'home':Home
})