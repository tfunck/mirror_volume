# mirror_volume

## Purpose

Mirror a volume through saggital plane through center from right to left

## Example:

`python3 mirror_volume.py -t MEBRAINS_T1.nii.gz  seg_mn_lr/MEBRAINS_segmentation_mn.nii seg_mn_lr/MEBRAINS_segmentation_mn_sym.nii.gz`

## Useage

`usage: mirror.py [-h] [--template TEMPLATE_FILENAME] [--offset OFFSET] [--clobber] input_filename output_filename`

Mirorr a volume.

positional arguments:
  input_filename        Filename of brain volume to mirror.
  output_filename       Output filename.

optional arguments:
  -h, --help            show this help message and exit
  --template TEMPLATE_FILENAME, -t TEMPLATE_FILENAME
                        Optional filename of brain template to use as reference.
  --offset OFFSET       Value to add to mirrored region to create unique mirrored ROI.
