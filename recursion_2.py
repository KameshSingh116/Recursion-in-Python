#Radhe Radhe
#Another example for recursion


def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l=["shiddat","citadel","mahabharat","ramayan"]
print(l)
a=input("Enter the word/last_part to remove:")
print(rem(l,a))

