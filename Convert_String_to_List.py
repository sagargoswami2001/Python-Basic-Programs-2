# Write a Python Program to Print a long text, convert the string to a list and print all the words and their frequencies.

string_words = '''Bitcoin(₿) is the first decentralized digital currency created in January 2009. Bitcoin was
created by Satoshi Nakamoto. The word bitcoin first originated from a white paper published on 31 October 2008.
It is a compound of the words "bit" and "coin." Bitcoin uses peer-to-peer technology to operate with no central
authority or banks. Managing transactions and the issuing of bitcoins is carried out collectively by the whole
peer to peer network of bitcoin. Its implementation was released as open source for it can be seen and accessed
by anyone.

Bitcoins are created as a reward for a process known as Bitcoin mining. Bitcoin is widely accepted for
currencies, products, and services. Bitcoin has been censured for its use in illegal transactions,
the large amount of electricity used by mining, a purely peer-to-peer version of electronic cash would allow
online payments to be sent directly from one party to another without going through a central autority or
financial institution.

Bitcoin mining is a highly complex computing process that uses complicated computer code to create a secure
cryptographic system, as well as the process by which new bitcoin enters into circulation.
mining is a record-keeping service done through the use of bitcoin mining rigs processing power.
It involves very large, decentralized networks of computers connected through peer to peer technology
throughout the world that verify and secure blockchains. Bitcoin mining takes over the Bitcoin database,
which is called the blockchain.

Crypto miners compete to be the first one to verify Crypto transactions and earn rewards paid in
Cryptocurrencies for their efforts. Crypto miners need to first invest in computer equipment that is 
specialized for mining (usually high-end GPUs among other powerful PC components), and typically require
access to a low cost energy source.'''

words_list = string_words.split()

words_freq = [words_list.count(n) for n in words_list]

print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(words_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(words_list, words_freq)))))