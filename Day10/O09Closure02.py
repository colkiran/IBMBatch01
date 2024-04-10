
def outerFun(grt):

    # simple curry
    def innerFun(gnm):

        print(grt, gnm)

    return innerFun

outerFun("Welcome")("Sachin")

engGrt = outerFun("Welcome")
tmlGrt = outerFun("Vannakam")

engGrt("Sachin")
engGrt("Rahul")

tmlGrt("Ashwin")
tmlGrt("Natrajan")
