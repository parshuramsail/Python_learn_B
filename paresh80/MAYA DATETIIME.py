
import  maya
n=maya.now()
print(n)
tomorrow=maya.when("tomorrow")
print(tomorrow)
print(tomorrow.slang_date())
print(tomorrow.slang_time())
print(tomorrow.datetime())

