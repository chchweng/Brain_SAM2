#%%
import os
import tifffile as tiff
from PIL import Image
import numpy as np
#%%
def convert_tif_to_jpeg(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # List of .tif files in the input directory
    tif_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.tif')])

    if not tif_files:
        print("No .tif files found in the input directory!")
        return

    # Convert each .tif file to .jpeg
    for tif_file in tif_files:
        input_path = os.path.join(input_dir, tif_file)
        output_path = os.path.join(output_dir, os.path.splitext(tif_file)[0] + '.jpeg')

        # Load the .tif file as a 16-bit image
        image = tiff.imread(input_path)

        # Convert 16-bit to 8-bit by scaling
        # image_8bit = ((image - image.min()) / (image.max() - image.min()) * 255).astype(np.uint8)
        image_8bit = image.astype(np.uint8)
        
        # Convert to a PIL image and save as .jpeg
        image_pil = Image.fromarray(image_8bit)
        image_pil.save(output_path, format='JPEG')
        print(f"Converted {tif_file} to {output_path}")
#%%
if __name__ == "__main__":
    # Set the input and output directories
    input_dir = "/homes/chunchieh/brain/data/20250120/X100-ExM_SDM40xw_TH_MB/Crop_Original_Data"
    output_dir = "/homes/chunchieh/brain/data_jpeg/20250120/X100-ExM_SDM40xw_TH_MB/Crop_Original_Data"

    # Convert .tif slices to .jpeg
    convert_tif_to_jpeg(input_dir, output_dir)
#%%