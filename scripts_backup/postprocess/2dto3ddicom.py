import os
import numpy as np
import pydicom
from pydicom.dataset import Dataset, FileDataset
import tifffile as tiff

# Define input and output paths
input_dir = "/homes/chunchieh/brain/data/20250110/X10xX10h_TH_L3p3_b2z2_p20xw_F017/Mask_labels/seg002"  # Folder containing slices
output_file = "/homes/chunchieh/brain/data/20250110/X10xX10h_TH_L3p3_b2z2_p20xw_F017/Mask_labels/stacked_seg002.dcm"  # Change to desired output path

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Get all .tif files and sort them numerically
tif_files = sorted(
    [f for f in os.listdir(input_dir) if f.endswith(".tif")],
    key=lambda x: int(x.split(".tif")[0].split("_z")[-1])  # Extract frame index
)

# Read all slices and stack into a 3D array
slices = [tiff.imread(os.path.join(input_dir, file)) for file in tif_files]
volume_3d = np.stack(slices, axis=0).astype(np.uint8)  # Ensure uint8 format

# Create a new DICOM dataset
ds = Dataset()
ds.file_meta = pydicom.Dataset()
ds.file_meta.MediaStorageSOPClassUID = pydicom.uid.SegmentationStorage
ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian
ds.is_little_endian = True
ds.is_implicit_VR = False

# Required DICOM metadata
ds.PatientName = "F017"
ds.PatientID = "F017"
ds.Modality = "SEG"
ds.SeriesInstanceUID = pydicom.uid.generate_uid()
ds.StudyInstanceUID = pydicom.uid.generate_uid()
ds.SeriesNumber = 1
ds.InstanceNumber = 1
ds.SOPInstanceUID = pydicom.uid.generate_uid()

# Set DICOM image properties
ds.Rows, ds.Columns = volume_3d.shape[1:]  # Image size
ds.NumberOfFrames = volume_3d.shape[0]  # Number of slices
ds.PixelData = volume_3d.tobytes()  # Convert 3D array to byte format

# DICOM segmentation-specific tags
ds.ImageType = ['DERIVED', 'PRIMARY', 'SEGMENTATION']
ds.SegmentationType = 'BINARY'
ds.SegmentationFractionalType = 'PROBABILITY'
ds.ContentLabel = 'MASK'
ds.ContentDescription = 'Segmentation Mask'
ds.ContentCreatorName = 'SAM2 Model'
ds.SegmentedPropertyCategoryCodeSequence = [Dataset()]
ds.SegmentedPropertyCategoryCodeSequence[0].CodeValue = "T-D0050"
ds.SegmentedPropertyCategoryCodeSequence[0].CodingSchemeDesignator = "SRT"
ds.SegmentedPropertyCategoryCodeSequence[0].CodeMeaning = "Tissue"

# DICOM pixel representation
ds.SamplesPerPixel = 1
ds.PhotometricInterpretation = "MONOCHROME2"
ds.BitsAllocated = 8
ds.BitsStored = 1
ds.HighBit = 0
ds.PixelRepresentation = 0

# Save the 3D DICOM file
pydicom.dcmwrite(output_file, ds)

print(f"Saved 3D DICOM file at {output_file}")
