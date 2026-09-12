# Tflite_Model_Maker_can_work_in_Colab
Finally Tflite Model Maker can work in Colab!
How do we solve the perennial Tflite Model Maker issue? A lot of researchers was stuck when Google Colab updated to version 3.10 and yet Tflite-Model-Maker still remains at ver 3.9. 

Many researchers have tried to downgrade the Colab to version 3.9 using this command

```
!sudo apt-get install python3.9
```

but nothing works!

The solution: we need to run Google Colab at version 3.9 using virtual environment. We also need to run the training commands as a python script, not directly at the cells. Let’s see how does this.
