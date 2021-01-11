from mycroft import MycroftSkill, intent_file_handler


class NextAppointment(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('nextappointment.intent')
    def handle_nextappointment(self, message):
        self.speak_dialog('nextappointment')


def create_skill():
    return NextAppointment()

