import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2

'''cmap
Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, 
BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, 
Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, 
PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, 
PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, 
PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, 
RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, 
Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, 
YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, 
afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, 
bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, 
copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, 
gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, 
gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, 
gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, 
inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, 
ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, 
rainbow_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, 
tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, 
twilight, twilight_r, twilight_shifted, twilight_shifted_r, viridis, viridis_r, winter, winter_r'''


file_path = input("Type in the absolute or relative to script file path (including extension): ")

img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

filter_choice = int(input("What filter to use(type in the number)?\n1. None\n2. Blur\n3. Gaussian blur\n4. Median blur\n5. Bilateral filter\n"))
while(filter_choice <= 0 and filter_choice >= 5):
    filter_choice = int(input("What filter to use(type in the number)?\n1. None\n2. Blur\n3. Gaussian blur\n4. Median blur\n5. Bilateral filter\n"))
if(filter_choice != 1):
    kernel_size = int(input("What size kernel do you want (odd numbers only)?\n"))
    while(kernel_size % 2 == 0 and kernel_size > 0):
        kernel_size = int(input("What size kernel do you want (odd numbers only)?\n"))
    if(filter_choice == 2):
        img = cv2.blur(img, (kernel_size, kernel_size))
    elif(filter_choice == 3):
        img = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    elif(filter_choice == 4):
        img = cv2.medianBlur(img, kernel_size)
    else:
        img = cv2.bilateralFilter(img, kernel_size, 90, 90)
preview_answer = input("Preview image?(Y/N)")
if(preview_answer == 'Y' or preview_answer == 'y'):
    cv2.imshow("Image preview", img)
    cv2.imwrite("temporary.png", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

#print(img.shape)
figure, ax = plt.subplots()
figure.canvas.set_window_title("3D preview")
ax = figure.add_subplot(111, projection='3d')
width = img.shape[1]
height = img.shape[0]
xx, yy = np.mgrid[0:height, 0:width]
stride_answer = input("high resolution of strides in 3D? (high means a lot of lag but more detail, no is width/100,height/100 for strides)(Y/N): ")
if(stride_answer == 'Y' or stride_answer == 'y'):
    ax.plot_surface(xx, yy, img, cmap='Greys_r',rstride=1, cstride=1, antialiased=False, linewidth=0)
else:
    ax.plot_surface(xx, yy, img, cmap='viridis',rstride=round(width/100), cstride=round(height/100), antialiased=False, linewidth=0)
ax.view_init(60, 45)
plt.show()