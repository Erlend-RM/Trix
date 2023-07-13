#Spør etter preferansene til en person
#Om man spiser kjøtt eller vegetar
#og om man trenger glutenfritt eller ikke.
print("Hei og velkommen.")
kjøtt = input("Spiser du kjøtt? (ja/nei): ")
gluten = input("Trenger du glutenfri mat? (ja/nei): ")

if kjøtt == "ja" and gluten == "ja":
    print("Du kan spise Biff.")
elif kjøtt == "ja" and gluten == "nei":
    print("Du kan spise Lasagne.")
elif kjøtt == "nei" and gluten == "ja":
    print("Du kan spise Falafel.")
else:
    print("Du kan spise Pizza Margherita.")
    
