import numpy as np
import nibabel as nib
from sys import argv

if __name__ == '__main__':

    mebrains_fn=argv[1] #'MEBRAINS_T1.nii.gz'
    seg_fn = argv[2] #'seg_mn_lr/MEBRAINS_segmentation_mn.nii'
    out_fn = argv[3] #'seg_mn_lr/MEBRAINS_segmentation_mn_fliplr.nii.gz'

    ref_affine = nib.load(mebrains_fn).affine

    img = nib.load(seg_fn)
    affine = ref_affine

    vol = img.get_fdata()

    vol2 = np.flip(vol,axis=0).copy()

    min_unique_value = np.unique(vol)[1]

    vol2[vol2 > min_unique_value] = vol2[vol2 > min_unique_value] + 1000

    x=np.rint((vol2.shape[0])/2).astype(int)
    print(x)
    vol[x+1:,:,:] = vol2[x:-1,:,:]

    nib.Nifti1Image(vol, affine).to_filename(out_fn)
    #nib.Nifti1Image(vol2, img.affine).to_filename('seg_mn_lr/MEBRAINS_segmentation_mn_fliplr2.nii')
