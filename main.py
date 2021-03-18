emojiList = ["🤬", "👌", "6️⃣ 9️⃣","🤡", "👋", "👍", "👆" ] 

# Using a for loop, print out each emoji in your list
# print out the length of your list
# print out the 4th item in your list
for counter in emojiList:
  print(counter)
print(len(emojiList))
print(emojiList[3])

# create a favoriteEmoji variable and set that equal to your favorite emoji in the list
favoriteEmoji = emojiList[2] 
# Using a for loop, make a pyramid with your favorite emoji 
for counter in range(1, 11): 
  print((favoriteEmoji + " ") * counter)

for counter in range(10, 0, -1):
  print((favoriteEmoji + " ") * counter)

for index in range(10, 0, -1):
  print((" " * index) + favoriteEmoji* (10-index) )