posts = [
  {"user": "alice", "post": "hi"},
  {"user": "bob", "post": "hello"},
  {"user": "alice", "post": "again"},
  {"user": "x", "post": "xyz"},
  {"user": "bob", "post": "again"},
  {"user" : "Ram" , "post" : "today"},
  {"user" : "Jas" , "post" : "tom"}
]

freq_map = { 
}

for i in posts:
    if i["user"] in freq_map:
        freq_map[i["user"]] = freq_map[i["user"]] + 1
    else:
        freq_map[i["user"]] = 1

print(freq_map)