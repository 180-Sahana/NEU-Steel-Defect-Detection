import os
import random
import shutil

# Original dataset
image_folder = "dataset/train/images"
label_folder = "dataset/train/labels"

# New YOLO dataset
output_folder = "dataset_yolo"

# Split ratios
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# Create folders
for split in ["train", "val", "test"]:
    os.makedirs(f"{output_folder}/{split}/images", exist_ok=True)
    os.makedirs(f"{output_folder}/{split}/labels", exist_ok=True)

# Find all images inside class folders
images = []

for root, dirs, files in os.walk(image_folder):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            images.append(os.path.join(root, file))

# Keep only images that have labels
valid_images = []

for image_path in images:
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    label_path = os.path.join(label_folder, image_name + ".txt")

    if os.path.exists(label_path):
        valid_images.append((image_path, label_path))

print(f"Total images found: {len(images)}")
print(f"Images with labels: {len(valid_images)}")
print(f"Images without labels: {len(images) - len(valid_images)}")

# Shuffle reproducibly
random.seed(42)
random.shuffle(valid_images)

# Calculate split sizes
total = len(valid_images)
train_end = int(total * train_ratio)
val_end = train_end + int(total * val_ratio)

train_data = valid_images[:train_end]
val_data = valid_images[train_end:val_end]
test_data = valid_images[val_end:]

# Copy files
def copy_split(data, split):
    for image_path, label_path in data:
        image_name = os.path.basename(image_path)
        label_name = os.path.basename(label_path)

        shutil.copy2(
            image_path,
            os.path.join(output_folder, split, "images", image_name)
        )

        shutil.copy2(
            label_path,
            os.path.join(output_folder, split, "labels", label_name)
        )

    print(f"{split}: {len(data)} images and labels copied")


copy_split(train_data, "train")
copy_split(val_data, "val")
copy_split(test_data, "test")

print("Dataset organization completed!")