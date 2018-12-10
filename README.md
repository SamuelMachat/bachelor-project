# bachelor-project
Automatic Generation of Music Video by Neural Networks
The project works on the system of recording MilkDrop2 output, splitting it to frames and using DeepDream to edit each frame to psychedelic image.

##### MilkDrop2 useful visualisations
* Aderrasi - Potion of Spirits
* Eo.S. - glowsticks v2 05 madhatter
* Flexi - cell tissue
* Flexi - fractal remix weed
* Flexi - intensive shader fractal (suksma..)
* Flexi - oldschool tree
* Flexi - psychenapping
* Flexi - the distant point between
* Fvese - Rebirth
* Fvese - Zoom Effects
* Geiss - Motion Blur 2
* martin + suksma + fed + goody and others
* martin - fuggy notion
* martin - funky illusion
* martin - jellyfish dance
* martin - no religion
* martin - satellite view
* martin - the forge of Isengard
* Mstress - acoustic nerve impulses
* Phat+... (ten by šel použít čistej)
* Phat_Zylot_Eo.S. rainbow
* Reenen Geiss - Soft Triple Feedback
* Rovastar - Cerebral 
* Rovastar - Harlequin's fractal encounter
* Rovastar - Inner Thoughts
* shifter - spincycle c
* shifter - tadpole
* shifter - tumbling cubes (ripples)
* shifter - tumbling cubes (ripples) E.oS. remix1
* Stahlregen & flexi + Geiss + Rovastar + Shifter - Fractal Feedback
* Stahlregen & flexi + Geiss - Tiger n. 5
* Unchained & Rovastar - Wormholes Pillars
* Unchained - beat demo 2.4
* Unchaindéd - Fuzzy Sciences
* Unchained - Making a Science of It 3
* Unchained - Quine
* Unchained - rewop

##### Example of use:
python 2_dreaming_time.py -i frames_input -o frames_output --gpu 0 -it jpg --model_path caffe/models/bvlc_googlenet/ --model_name bvlc_googlenet.caffemodel -itr 150 -b 0.70

Last parameter is important for clarity and fluidity of the output video.
0.50 is clear and not much fast
0.60 is still clear and not much fast
0.70 is best default setting
0.80 is fast and not so clear
1.00 you do not know what to expect

#### Caffe models
https://github.com/BVLC/caffe/wiki/Model-Zoo

#### Making video out of frames:
https://ffmpeg.zeranoe.com/builds/

##### Example of use:
ffmpeg -framerate 30 -i "frames_folder/%08d.jpg" -i "music.mp3" -shortest deepdreamvideo.mp4

##### More info about DeepDream video here:
https://github.com/graphific/DeepDreamVideo

##### Link to Google Drive folder with images and videos made within this project:
https://drive.google.com/drive/folders/1XGhg_y6nON_iMeW4L9RgqPl_E7GZqkjM
