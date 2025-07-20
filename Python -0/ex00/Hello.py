ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Modify the data structures
ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "UAE!")  # tuple is immutable, so we need to reassign the tuple
ft_set.remove("tutu!")
ft_set.add("Abu Dhabi!") # We can’t directly replace a value, so we remove "tutu!" and add "Abu Dhabi!".
ft_dict["Hello"] = "42 Abu Dhabi!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)