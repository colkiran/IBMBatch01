
def outerFun(grt):

    def innerFun(sep):

        def innerMostFun(gnm):
            from emojis import emojis

            emojized = emojis.encode(grt + " :" + sep + ": " + gnm )

            print(emojized)

        return innerMostFun

    return innerFun

engGrt = outerFun("Welcome")

engGrtTgr = engGrt("tiger")

engGrtTgr("Sheroff")

kanGrt = outerFun('Namaskara')
kanGrtTgr = kanGrt("bear")
kanGrtTgr("Prabhakar")
kanGrtTgr = kanGrt("tiger")
kanGrtTgr("Prabhakar")
kanGrtTgr = kanGrt("wolf")
kanGrtTgr("Prabhakar")
kanGrtTgr = kanGrt("lion")
kanGrtTgr("Prabhakar")
kanGrtTgr = kanGrt("giraffe")
kanGrtTgr("Prabhakar")



'''
outerFun("Welcome")("----->")("Sachin")

engGrt = outerFun("Welcome")
tmlGrt = outerFun("Vannakam")
engGrtSngArw = engGrt("------>")
tmlGrtSngArw = tmlGrt("------>")

engGrtDblArw = engGrt("========>>")
tmlGrtDblArw = tmlGrt("========>>")


engGrtSngArw("Rahul")
engGrtDblArw("Sourav")

tmlGrtSngArw('Ashwin')
tmlGrtDblArw("Srikanth")

'''