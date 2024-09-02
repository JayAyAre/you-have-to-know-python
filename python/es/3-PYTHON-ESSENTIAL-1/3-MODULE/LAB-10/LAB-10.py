blocks = int(input("Enter the number of blocks: "))
new_num_blocks = blocks
#
# Write your code here.
#
height = 0
for num_blocks in range(1, blocks):
    layer = new_num_blocks - num_blocks
    if layer > 0:
        new_num_blocks = layer
        height += 1
    elif layer == 0:
        height += 1
        break
    else:
        break

print("The height of the pyramid:", height)
