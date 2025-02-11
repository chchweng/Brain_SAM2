import os
import numpy as np
import tifffile as tiff

# Define input and output paths
input_dir = "/homes/chunchieh/brain/out_pred/X10xX10h_TH_L3p3_b2z2_p20xw_F017/0000_2000/seg004"  # Change to the folder containing slices
output_file = "/homes/chunchieh/brain/out_pred/X10xX10h_TH_L3p3_b2z2_p20xw_F017/0000_2000/stacked_seg004.tiff"  # Change to desired output path

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Get all .tif files and sort them by frame index
tif_files = sorted(
    [f for f in os.listdir(input_dir) if f.endswith(".tif")],
    key=lambda x: int(x.split(".")[0])  # Extract frame index
)

# Read all slices and stack into a 3D array
slices = [tiff.imread(os.path.join(input_dir, file)) for file in tif_files]
volume_3d = np.stack(slices, axis=0)  # Stack along the first axis (Z-axis)

# Save as a single 3D TIFF file
tiff.imwrite(output_file, volume_3d.astype(np.uint8))  # Ensure uint8 format

print(f"Saved 3D TIFF volume at {output_file}")
