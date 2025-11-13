web_dev = ["Ravi", "Meera", "Kiran"]
data_science = ["Anjali", "Vikram", "Neha"]
ui_ux = ["Divya", "Sahil", "Tanya"]
all_participants = [web_dev, data_science, ui_ux]
web_dev.append("Arjun")
data_science.insert(1, "Sneha")
ui_ux.pop()
copied_data_science = data_science.copy()
data_science.clear()
first_two_web_dev = web_dev[:2]
name_lengths = [len(name) for name in copied_data_science]
asha_present = "Asha" in web_dev or "Asha" in copied_data_science or "Asha" in ui_ux
first_participants = (web_dev[0], copied_data_science[0], ui_ux[0])
print("All participants:", all_participants)
print("Copied Data Science list:", copied_data_science)
print("First two Web Dev participants:", first_two_web_dev)
print("Name lengths in copied Data Science list:", name_lengths)
print("Is 'Asha' present in any list?", asha_present)
print("Tuple of first participants:", first_participants)

