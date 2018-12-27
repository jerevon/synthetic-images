import scipy.misc### import scipy not working, should be import scipy.misc
import numpy as np
import os

def aligned(image_folder, mask_folder, save_folder, HEIGHT=512, WIDTH=1024):
    """
    this function align image and its mask together for data preparation of condition-GAN
    aligned image can be split up two parts: image_A, image_B
    image_A = original image(left)
    image_B = mask image (right)
    -------------------
    edit image_folder, mask_folder and save_folder based on your own requirements
    -------------------
    """
    # image_path = glob('%s/*' % image_folder)
    # mask_path = glob('%s/*' % mask_folder)
    image_list = os.listdir(image_folder)
    mask_list = os.listdir(mask_folder)
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    for image in image_list:
        image_prefix = image.split('.')[0]
        image_path = os.path.join(image_folder,image)
        image = scipy.misc.imread(image_path, mode='RGB').astype(np.float)
        for i, mask in enumerate(mask_list):
            mask_prefix = mask.split('.')[0]
            if image_prefix == mask_prefix:
                mask_path = os.path.join(mask_folder, mask)
                mask = scipy.misc.imread(mask_path, mode='RGB').astype(np.float)
                aligned_image = np.zeros((HEIGHT, WIDTH, 3))
                aligned_image[:, :WIDTH//2, :] = image
                aligned_image[:, WIDTH//2:, :] = mask
                aligned_image_path = os.path.join(save_folder, str(i+1)+'.jpg')
                scipy.misc.imsave(aligned_image_path, aligned_image)
        # return aligned_image


if __name__ == '__main__':
    image_folder = 'E:\\PhD_annotated\\synthetic\\refine500'
    mask_folder = 'E:\\PhD_annotated\\synthetic\\refine500_mask'
    save_folder = 'E:\\PhD_annotated\\synthetic\\aligned'
    aligned(image_folder=image_folder, mask_folder=mask_folder, save_folder=save_folder)
