class Accident(Exception):
    def __int__(self, msg):
        self.msg=msg

    def handle(self):
        print("Accident occured, take a detour")

try:
    raise Accident('Crash between two cars')
except Accident as e:
    e.handle()




