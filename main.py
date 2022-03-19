# pip install translate

from translate import Translator

s = Translator(from_lang="english",to_lang = "portuguese")
res = s.translate("Hello Guys")
print(res)


from translate import Translator

s = Translator(from_lang="english",to_lang = "spanish")
res = s.translate("Hello Guys")
print(res)

from translate import Translator

s = Translator(from_lang="english",to_lang = "german")
res = s.translate("Hello Guys")
print(res)

from translate import Translator

s = Translator(from_lang="english",to_lang = "dutch")
res = s.translate("Hello Guys")
print(res)

from translate import Translator

s = Translator(from_lang="english",to_lang = "french")
res = s.translate("Hello Guys")
print(res)