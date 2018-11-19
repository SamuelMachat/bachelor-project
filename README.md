# bachelor-project
Automatic Generation of Music Video by Neural Networks
The project works on the system of recording MilkDrop2 output, splitting it to frames and using DeepDream to edit each frame to psychedelic image.

Example of use:
python 2_dreaming_time.py -i frames_input -o frames_output --gpu 0 -it jpg --model_path caffe/models/bvlc_googlenet/ --model_name bvlc_googlenet.caffemodel -itr 150 -b 0.85

More info here:
https://github.com/graphific/DeepDreamVideo