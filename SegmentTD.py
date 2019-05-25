%% TDeven
AD=imread('C:\ADthesis\ADpython\ADprocess3_19\Matlab_Process_3_25_19\TheDermatologist\TDeven.png');
%% Convert Image from RGB to L*a*b* Color Space
labAD=rgb2lab(AD);
imtool(labAD)
%% Thresholder:Classify Colors in 'a*b* using K-Means Clustering
ab=labAD(:,:,2:3);
ab=im2single(ab);
nColors=3;
ab_pixel_labels=imsegkmeans(ab,nColors,'NumAttempts',3);
%% red a*b*
mask1ab=ab_pixel_labels==1;
cluster1ab=AD .* uint8(mask1ab);
%% Hadamard product: dark and light red ab
L_ab=labAD(:,:,1);
L_ab_red=L_ab .* double(mask1ab);
L_ab_red=rescale(L_ab_red);
ab_idx_light_red=imbinarize(nonzeros(L_ab_red));
ab_red_idx=find(mask1ab);
ab_mask_dark_red=mask1ab;
ab_mask_dark_red(ab_red_idx(ab_idx_light_red))=0;%Binarize
ab_red_nuclei=AD .* uint8(ab_mask_dark_red);%Hadamard product
imtool(ab_mask_dark_red)
imtool(ab_red_nuclei)
%% Threshold/Mask RGB
% Use ColorDetection_Mean_Range.m
RGB  = AD;
R    = RGB(:, :, 1);
G    = RGB(:, :, 2);
B    = RGB(:, :, 3);
mask2D = (65 < R & R < 200) & ...  % [EDITED]: && -> &
         (0 < G & G < 100) & ...
         (0 < B & B < 90);
mask   = cat(3, mask2D, mask2D, mask2D);
mask=uint8(mask);
img=RGB.*mask;
imtool(img)
