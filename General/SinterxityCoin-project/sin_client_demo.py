import requests

BASE = "http://localhost:5000"


print("Starting SinCoin demo\n")

print("Sending transaction Alice -> Bob 100")

requests.post(
    BASE + "/transaction",
    json={
        "from": "Alice",
        "to": "Bob",
        "amount": 100
    }
)


print("Sending transaction Bob -> Charlie 20")

requests.post(
    BASE + "/transaction",
    json={
        "from": "Bob",
        "to": "Charlie",
        "amount": 20
    }
)


print("\nMining block")

res = requests.get(BASE + "/mine")

print(res.json())


print("\nDownloading blocks")

blocks = requests.get(BASE + "/blocks")

print("Blocks count:", len(blocks.json()))


print("\nValidating blockchain")

val = requests.get(BASE + "/validate")

print("Valid:", val.json())
