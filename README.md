# Brain neuron semi-automatic Segmentation by SAM2

This repository is for automatic segmentation on ExT Brain neuron segmentation
Our first attempt is applying [Segment Anything 2] (https://ai.meta.com/sam2/) ([github] (https://github.com/facebookresearch/sam2.git))

---

## Notebook testing

### Step1: Create Data Video frames like folder  
To implement our data (2D slices) to SAM2 video (examples:`/homes/chunchieh/brain/sam2/notebooks/videos/bedroom`). 
First we need to create a frame like data (folder)
Use `/homes/chunchieh/brain/data/20250110/X10xX10h_TH_L3p3_b2z2_p20xw_F006` patch as example.
run:
```bash
/homes/chunchieh/brain/scripts/preprocess/copy_rename_frame_F006.sh
```
This command will creata a folder `/homes/chunchieh/brain/data_jpeg/20250110/X10xX10h_TH_L3p3_b2z2_p20xw_F006/raw_data_frame`