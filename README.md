## Install Prerequisites :

 1. Download Blender 2.82 [HERE](https://download.blender.org/release/Blender2.82/blender-2.82-windows64.msi)
 2. Install Requirement Modules <br>
       Windows : Open Command Prompt as Administrator 
       <br>` cd "C:\Program Files\Blender Foundation\Blender 2.82\2.82\python\bin"`
         <br> `python -m pip install --upgrade pip  `
         <br> `python -m pip install opencv-contrib-python numpy ` 

 ## Further Instructions :
 1. Open Blender 2.82.
 2. Go to the Scripting tab of Blender if the Blender file does not open to there already.
 3. Check that the OpenCVAnim.py and OpenCVAnimOperator.py files are present and registered. You can also run both scripts individually to ensure they do not have any errors.
 4. Go to the Layout tab of Blender.
 5. Click OpenCV Animation.
 6. You can reposition the model to get closer to the face.
 7. Click Capture.

 You should see a GUI presenting your camera footage with the facial landmark detection mesh as well as be able to move the model as you move your face.

## Reference YouTube Video :
We had to refer to the following video to complete the group project: https://youtu.be/tEmdLULBUTQ