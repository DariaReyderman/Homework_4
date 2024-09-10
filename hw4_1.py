# START

# condition 1
triangles: int = int(input("How many triangles of pizza Dany ordered? "))

for_each_friend: int = triangles // 4
remain_on_the_table: int = triangles % 4

print(for_each_friend, "triangles for each friend")

if triangles % 4 != 0:
    print(remain_on_the_table, "triangles Dany will take home")

# condition 2
friends: int = int(input("How many friends came to Dany's B-day? "))
triangles: int = int(input("How many triangles of pizza Dany ordered? "))

for_each_friend: int = triangles // friends
remain_on_the_table: int = triangles % friends

print(for_each_friend, "triangles for each friend")

if triangles % friends != 0:
    print(remain_on_the_table, "triangles Dany will take home")

# STOP
