import os
componets = ["Slider","DARKMODE","Nav","Button","icons","Input","Link","FAB","RATING","TOGGLE","FORM","SWITCH","AVATAR","LIST","TABLE","DIVIDER","ALERT","SNACKBAR","TYPOGRAPHY","BADGE","TOOLTIP","MODAL","PROGRESS","SKELETON","CARD","ACCORDION","DRAWER","BOTTOMNAVIGARION","PAPER","BREADCRUMPS","TABS","BOX","STEPPER","MENU","PAGINATION","SPEEDDIAL","IMAGE","VIDEO","ICON"]
for item in componets:
    os.mkdir(item.lower().capitalize())
    #os.rmdir(item)