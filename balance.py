from web3 import Web3

infura_url = 'https://opbnb-mainnet-rpc.bnbchain.org'
web3 = Web3(Web3.HTTPProvider(infura_url))

count = 0
count2 = 0
suma = 0
with open('adresses.txt', 'r') as file:
    addresses = file.read().splitlines()
for address in addresses:
    checksum_address = web3.to_checksum_address(address)
    balance = web3.eth.get_balance(checksum_address)
    sum = balance * 302
    formatted_balance = "{:.2f}".format(web3.from_wei(sum, 'ether'))
    if float(formatted_balance) >= 0.15:
        count2 += 1
        print(f"Balance for address {address}: {formatted_balance}$")
        with open('res.txt', 'a') as file:
            file.write(address + '\n')
        suma += float(formatted_balance)
    if float(formatted_balance) <= 0:

        count += 1
print("Всього аккаунтів з 0 балансом:", count)
print("Всього аккаунтів з балансом менше 0.15$:", count2)
resl = round(suma, 2)
print("Всього кошштів:", resl, "$")
































# if connected:
#     # Читання адресів з файлу
#     with open('adresses.txt', 'r') as file:
#         addresses = file.read().splitlines()

#     # Перевірка балансу для кожного адресу
#     for address in addresses:
#         # Перетворення адреси на адресу з контрольною сумою
#         checksum_address = Web3.to_checksum_address(address)

#         balance_wei = web3.eth.get_balance(checksum_address)
#         balance_eth = web3.from_wei(balance_wei, 'ether')

#         # Розрахунок балансу в доларах
#         eth_to_usd_rate = 321  # Замініть це на реальний курс ETH/USD
#         balance_usd = balance_eth * eth_to_usd_rate

#         # Заокруглення до двох знаків після коми
#         balance_usd_rounded = round(balance_usd, 2)

#         if (balance_usd <= 0.10):
#             print(f"Баланс для адреси {address} {balance_usd_rounded} $")
#             time.sleep(0.5)
# else:
#     print("Неможливо підключитися до вузла Ethereum.")
