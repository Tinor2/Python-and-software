expoSetting = 2 #F: This will always return 2, does not change
expoFactor = 45 * 45 / (45 - 45 / expoSetting) #F: This will always return 90, and it does not eery change

print(expoFactor)