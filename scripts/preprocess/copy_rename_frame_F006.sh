#!/bin/bash

# create a video like 

# Source directory and target directory
src_dir="/homes/chunchieh/brain/data_jpeg/20250110/X10xX10h_TH_L3p3_b2z2_p20xw_F006/raw_data"
target_dir="/homes/chunchieh/brain/data_jpeg/20250110/X10xX10h_TH_L3p3_b2z2_p20xw_F006/raw_data_frame"

# Create target directory if not exists
mkdir -p "$target_dir"

# Counter for renaming
counter=0

# Loop through the range of files
for i in $(seq 1357 1500); do
  # Source file path
  src_file="${src_dir}/X10xX10h_TH_L3p3_b2z2_p20xw_F006_sT_z${i}.jpeg"

  # Target file name with padded zeroes
  printf -v new_name "%05d.jpeg" "$counter"

  # Copy and rename
  cp "$src_file" "${target_dir}/${new_name}"

  # Increment counter
  counter=$((counter + 1))
done

echo "Copy and rename completed."