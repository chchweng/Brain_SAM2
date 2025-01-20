#!/bin/bash

# create a video like 

# Source directory and target directory
src_dir="/homes/chunchieh/brain/data_jpeg/20250110/X10xX10h_TH_L3p3_b2z2_p20xw_F017/raw_data"
target_dir="/homes/chunchieh/brain/data_jpeg/20250110/X10xX10h_TH_L3p3_b2z2_p20xw_F017/raw_data_3500_4000_frame"

# Create target directory if not exists
mkdir -p "$target_dir"

# Counter for renaming
# counter=0

# Loop through the range of files
for i in $(seq 3500 4000); do

  # Format source file number with leading zeros (e.g., 0649, 0999)
  printf -v src_number "%04d" "$i"
  # Source file path
  src_file="${src_dir}/X10xX10h_TH_L3p3_b2z2_p20xw_F017_sT_Warpinp_z${src_number}.jpeg"
 
  # Target file name with padded zeroes
  # printf -v new_name "%05d.jpeg" "$counter"
  printf -v new_name "%05d.jpeg" "$i"
  # Copy and rename
  cp "$src_file" "${target_dir}/${new_name}"

  # Increment counter
  # counter=$((counter + 1))
done

echo "Copy and rename completed."


# /homes/chunchieh/brain/data_jpeg/20250110/X10xX10h_TH_L3p3_b2z2_p20xw_F017/raw_data/X10xX10h_TH_L3p3_b2z2_p20xw_F017_sT_Warpinp_z0000.jpeg