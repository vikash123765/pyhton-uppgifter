import Rövar_pråk


with open("rövarspråk_test.txt") as f:
    fulletext=f.read()


översättning = Rövar_pråk.translate(fulletext)


with open("översatttillrövartext","w",encoding="utf-8") as f:
    f.write(översättning)