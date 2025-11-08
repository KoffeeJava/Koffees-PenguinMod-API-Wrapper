import KPAW

KPAW.setUserAndToken("koffeejava", "16e6c1430dcd17089b5328a5afcce010164fd978651371aa8f791466bf94e528")

KPAW.getAmountMessage()
print(f"Unread messages: {KPAW.Message_Amount}")