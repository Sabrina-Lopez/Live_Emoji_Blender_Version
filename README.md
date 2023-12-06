## Install Prerequisites :

 1. Download Blender 2.82 [HERE](https://download.blender.org/release/Blender2.82/blender-2.82-windows64.msi)
 2. Install Requirement Modules <br>
       Windows : Open Command Prompt as Administrator 
       <br>` cd "C:\Program Files\Blender Foundation\Blender 2.82\2.82\python\bin"`
         <br> `python -m pip install --upgrade pip  `
         <br> `python -m pip install opencv-contrib-python numpy ` 
  3. Download project repo.

 ## Further Instructions :
 1. Open Blender 2.82.
 2. Go to the Scripting tab of Blender if the Blender file does not open to there already.
 3. Check that the OpenCVAnim.py and OpenCVAnimOperator.py files are present.
 4. Update the landmark_path to in OpenCVAnimOperator.py to the location of the lbfmodel.yaml file in the project repo.
 5. Reregister the OpenCVAnim.py and OpenCVAnimOperator.py files with the Register button. 
 6. Run both scripts individually to ensure they do not have any errors.
 7. Go to the Layout tab of Blender.
 8. Click OpenCV Animation.
 9. You can reposition the model to get closer to the face.
 10. Click Capture.

 You should see a GUI presenting your camera footage with the facial landmark detection mesh as well as be able to move the model as you move your face.

## Reference YouTube Video :
We had to refer to the following video to complete the group project: https://youtu.be/tEmdLULBUTQ