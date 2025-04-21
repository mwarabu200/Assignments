class oppo:
    def ring(self):
        return "vibrate"

class samsung:
    def ring(self):
        return "buzz"


for phone in[oppo(), samsung()]:
    print(phone.ring())