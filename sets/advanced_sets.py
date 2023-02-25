
# difference()
friends = {"Bob", "Mike", "Josh"}
abroad = {"Bob", "Josh"}

local_friends = friends.difference(abroad)
print(local_friends) # => {'Mike'}

# union() gives the total 
friends = local_friends.union(friends)
print(friends) # => {'Josh', 'Bob', 'Mike'}

# intersection() reveals who is in both lists
art = {"Bob", "Josh", "Sam", "Tom"}
science = {"Bob", "Sam", "Tommy", "Samantha"}

both = art.intersection(science)
print(both) # => {'Bob', 'Sam'}
