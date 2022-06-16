# file_object = open("input.txt", encoding="UTF-8")
# file_content = file_object.read()

# print(file_content)
# ================================================================
# file_object = open("input.txt", "w", encoding="UTF-8")
# file_object.write("hello world!\n")
# file_object.flush()
# # file_object.close()
# file_content = file_object.read()
# print(file_content)
# =================================================================

from csv import writer


input_name = "input.txt"
output_name = "output.txt"

reader = open(input_name)
writer = open(output_name, "w")

for line in reader:
    transform = line.upper()
    writer.write(transform)

reader.close()
writer.close()
