from userimageski import UserData

if __name__ == '__main__':
   
    ##### the following code includes all the steps to get from a raw image to a prediction.
    ##### the working code is the uncommented one. 
    ##### the two pickle models which are passed as argument to the select_text_among_candidates
    ##### and classify_text methods are obviously the result of a previously implemented pipeline.
    ##### just for the purpose of clearness below the code is provided. 
    ##### I want to emphasize that the commented code is the one necessary to get the models trained.
    
    # creates instance of class and loads image    
    user = UserData('a.gif')
    # plots preprocessed imae 
    user.plot_preprocessed_image()
    candidates = user.get_text_candidates()
    # plots objects detected
    user.plot_to_check(candidates, 'Total Objects Detected')
    
