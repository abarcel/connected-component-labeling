# Connected-Component Labeling

Two different classical algorithms, which is Recursive Connected Component Labeling and Two Pass Connected Component Labeling implemented with the help of NumPy to find and label connected components(pixel neighbors with the same value) in image files. While finding neigbors we have different direction options possible, which is only by cardinal directions(neighbor_size=4) or using both cardinal and ordinal directions(neighbor_size=8). Difference between them will be distinguishable in test images.

<br>
<br>

# RCCL: Recursive Connected Component Labeling

Basic idea behind this method is, first finding a non zero value by scanning from left to right and top to bottom. When a non zero value detected, all we have to do is looking for his neighbors(with neighbor_size 4 or 8). We will do this recursively and follow the every new neighbor with same value appears, we will continue our search from there and keep repeating until we no more find new neighbor with the same value. Then we assign all same valued neighbors to the same label value. Which is probably the simplest algorithm to implement in CCL. 

![shapiro_img](https://user-images.githubusercontent.com/88535469/129064371-67b01684-e741-4e0a-ba54-b0b52e82dcc5.png)

Shapiro and Stockman's pseudo code makes it very simple to understand the concept. All has to be done is implementing in Python.

# TSCLL: Two-Step Connected Component Labeling

The two-pass algorithm,(also known as the Hoshen–Kopelman algorithm) iterates through image. The algorithm makes two passes over the image. The first pass to assign temporary labels and record equivalences and the second pass to replace each temporary label by the smallest label of its equivalence class.

Connectivity checks are carried out by checking neighbor pixel labels (neighbor elements whose labels are not assigned yet are ignored), or say, the North-East, the North, the North-West and the West of the current pixel (neighbor_size=8). If neighbor size is selected 4, will use only North and West neighbors of the current pixel. This will happen only while checking for the forward pass, but in backward pass we will use the counters of these directions.

Like we did in RCCL we will again start by scanning from left to right and top to the bottom and as a second step we will scan from right to left and bottom to top. In both steps when nonzero values detected, connectivity check has to be carried out and if values are same, we assign same label to the detected non zero value and its neighbors. This time we are not going to recursively continue our search for each neighbor for the first found non zero values but keep the scanning process we started. Important part is we need to keep track of touching neighbors with different labels, later these labels should be merged so that we don't assign multiple labels to the same connected component.

# TEST

When we do tests for both of these algorithms received results didn't vary between them. So only the result difference for the neighbor size change will be shown.

![semboller](https://user-images.githubusercontent.com/88535469/129064957-c7096953-c257-4bc1-8acf-0b1a28d26690.png)

For the first image 'semboller' it is easy to notice that there is a difference between 4 and 8 neighbor selected, where difference happens because ordinal directions skipped and each small partition of the each shape labeled differently.

![labirent](https://user-images.githubusercontent.com/88535469/129065036-1516b2bc-29e2-4762-af78-eb17d76dc903.png)

'labirent' is a great example to test if the code doesn't have any problem like skipping the edges or has problems with recursiveness.


