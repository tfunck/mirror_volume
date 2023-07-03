import numpy as np
import nibabel as nib
import argparse
import os
from sys import argv





if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='Mirorr a volume.')
    parser.add_argument('input_filename', help='Filename of brain volume to mirror.')
    parser.add_argument('output_filename', help='Output filename.')
    parser.add_argument('--template', '-t', dest='template_filename', default=None, help='Optional filename of brain template to use as reference.')
    parser.add_argument('--offset', dest='offset',default=1000, help='Value to add to mirrored region to create unique mirrored ROI.')
    parser.add_argument('--clobber', dest='clobber',default=False,action='store_true', help='Overwrite existing results')

    args =parser.parse_args()
   
    if not os.path.exists(args.out_filename) or args.clobber :
        img = nib.load(args.input_filename)

        if type(args.template_filename) != type(None):
            affine = nib.load(args.template_filename).affine
        else:
            affine = img.affine

        vol = img.get_fdata()

        vol2 = np.flip(vol,axis=0).copy()

        min_unique_value = np.unique(vol)[1]

        vol2[vol2 > min_unique_value] = vol2[vol2 > min_unique_value] + args.offset

        x=np.rint((vol2.shape[0])/2).astype(int)
        vol[x+1:,:,:] = vol2[x:-1,:,:]

        nib.Nifti1Image(vol, affine).to_filename(args.out_filename)

