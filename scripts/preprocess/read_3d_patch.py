import os
import numpy as np
import tifffile as tiff  # Library to read .tif files
import matplotlib.pyplot as plt

# Function to read the first 5 2D slices and stack them into a 3D array
def read_3d_patch_top_slices(data_path, num_slices=5):
    # Get list of .tif files in the raw_data folder
    slice_files = sorted([f for f in os.listdir(data_path) if f.endswith('.tif')])

    if not slice_files:
        print("No .tif files found in the folder!")
        return None

    # Limit the number of slices to read
    total_slices = min(num_slices, len(slice_files))
    print(f"Reading top {total_slices} slices from {len(slice_files)} available slices.")

    # Stack only the first few slices into a 3D numpy array
    volume = []
    for slice_file in slice_files[:total_slices]:
        slice_path = os.path.join(data_path, slice_file)
        image_slice = tiff.imread(slice_path)  # Read a single 2D slice
        volume.append(image_slice)

    # Convert list to numpy array (shape: [z, y, x])
    volume = np.stack(volume, axis=0)
    print(f"3D Patch Shape (top slices): {volume.shape} (Z, Y, X)")

    return volume

# Function to save 2D slices of the 3D volume as images
def save_top_slices(volume, output_dir="output_images"):
    if volume is None:
        return

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    total_slices = volume.shape[0]
    for z_index in range(total_slices):
        # Save each slice as a PNG image
        file_path = os.path.join(output_dir, f"slice_z{z_index}.png")
        plt.imsave(file_path, volume[z_index], cmap='gray')
        print(f"Saved slice {z_index} as {file_path}")

if __name__ == "__main__":
    # Set the folder containing the 2D .tif slices (adjust the path as needed)
    data_path = "/homes/chunchieh/brain/data/20250110/X10xX10h_TH_L3p3_b2z2_p20xw_F006/raw_data"
    output_dir = "/homes/chunchieh/brain/output_image"
    # Read the top 5 2D slices of the 3D volume
    volume = read_3d_patch_top_slices(data_path, num_slices=5)

    # Show the top 5 slices (or less, depending on available slices)
    if volume is not None:
        save_top_slices(volume, output_dir=output_dir)
