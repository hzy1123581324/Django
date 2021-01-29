from mnemonic import Mnemonic
'''
english
chinese_simplified
chinese_traditional
french
italian
japanese
korean
spanish
'''
mnemo = Mnemonic("english")
words = mnemo.generate(strength=256)
# 取值范围  128 - 256
seed = mnemo.to_seed(words, passphrase="123456")
entropy = mnemo.to_entropy(words)
print(words, seed, entropy)
