from mycroft import MycroftSkill, intent_file_handler


class Hwskilltest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hwskilltest.intent')
    def handle_hwskilltest(self, message):
        self.speak_dialog('hwskilltest')


def create_skill():
    return Hwskilltest()

