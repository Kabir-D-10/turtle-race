# names = {
#     "Me":"Kabir",
#     "You":"Danstan"
# }
# print(names.get("Me"))
# print(names["You"])
# names["You"]="Dalip"
# names["Him"]="Danstan"
# print(names)






friends = {
    "a":"red",
    "b":"green",
    "c":"blue"
}
# print(friends["a"])
# friends["b"] = "orange"
# print(friends["b"])
# friends["d"] = "purple"
# print(friends["d"])
# friends.pop("a")
# friends.popitem()
# print(friends)
# friends.clear()
# print(friends)
# del friends
for key in friends.keys():
    print(key)
for val in friends.values():
    print(val)
for item in friends.items():
    print(item)