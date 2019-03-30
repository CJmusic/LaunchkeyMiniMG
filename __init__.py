#Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_Mini/__init__.py

import Live


from LaunchkeyMiniMG import LaunchkeyMiniMG

def create_instance(c_instance):
    return LaunchkeyMiniMG(c_instance) 
