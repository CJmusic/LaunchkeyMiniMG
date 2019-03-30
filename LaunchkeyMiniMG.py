#Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_Mini/LaunchkeyMini.py
#from Launchkey.Launchkey import Launchkey, LaunchkeyControlFactory, make_button
from __future__ import with_statement 

import sys
import Live

from _Framework.InputControlElement import *
from _Framework.ControlSurface import ControlSurface
from _Framework.TransportComponent import TransportComponent
from _Framework.MixerComponent import MixerComponent
from _Framework.EncoderElement import EncoderElement
from _Framework.SliderElement import SliderElement
from _Framework.ButtonElement import ButtonElement

from Launchkey.Launchkey import make_encoder

# copied from InputControlElement for debugging
MIDI_NOTE_TYPE = 0
MIDI_CC_TYPE = 1


KNOBS = [21, 22, 23, 24, 25, 26, 27, 28] # these are the midi control values for the knobs of the LK Mini 
PADS = [[40, 41, 42, 43, 48, 49, 50, 51], 
        [36, 37, 38, 39, 44, 45, 46, 47]] # this is the midi note values of the grid of 16 buttons arranged by row/column  
SCENES = [108, 109] # midi controller values for the two scene launch buttons 

class LaunchkeyMiniMG(ControlSurface):
    """ Script for Novation's Launchkey Mini keyboard """

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        #super(LaunchkeyMini, self).__init__(c_instance, control_factory=LaunchkeyMiniControlFactory(), identity_response=(240, 126, 127, 6, 2, 0, 32, 41, 53, 0, 0))
        self._suppress_send_midi = True
        self._suppress_session_highlight = True
        self._control_is_with_automap = False

        self._suggested_input_port = 'LK Mini MIDI'
        self._suggested_output_port = 'LK Mini MIDI'
        with self.component_guard():
            self._MG_setup()

    def _MG_setup(self): 
        mixer = MixerComponent(8)
        mixer.set_track_offset(0) #Sets start point for mixer strip (offset from left)
        transport = TransportComponent()
        mixer.set_track_offset(0)
        
        volume_knob = SliderElement(MIDI_CC_TYPE, 0, KNOBS[i])
        pan_knob = SliderElement(MIDI_CC_TYPE, 1, KNOBS[i])

        send_a = SliderElement(MIDI_CC_TYPE, 2, KNOBS[i])
        send_b = SliderElement(MIDI_CC_TYPE, 3, KNOBS[i])
        send_c = SliderElement(MIDI_CC_TYPE, 4, KNOBS[i])
        send_d = SliderElement(MIDI_CC_TYPE, 5, KNOBS[i])
        send_e = SliderElement(MIDI_CC_TYPE, 6, KNOBS[i])
        send_f = SliderElement(MIDI_CC_TYPE, 7, KNOBS[i])

        for i in xrange(len(KNOBS)): #set the functions of the knobs
          mixer.channel_strip(i).set_volume_control(volume_knob)
          mixer.channel_strip(i).set_pan_control(pan_knob)
          mixer.channel_strip(i).set_send_controls([send_a,
                                                    send_b,
                                                    send_c, 
                                                    send_d,
                                                    send_e,
                                                    send_f])

          # scenes are locked to channel 14
        transport.set_overdub_button(ButtonElement(False, MIDI_CC_TYPE, 0, SCENES[0]))
        transport.set_stop_button(ButtonElement(False, MIDI_CC_TYPE, 0, SCENES[1]))                 
          #transport.set_play_button(ButtonElement(False, MIDI_CC_TYPE, 1, SCENES[0]))
          #transport.set_stop_button(ButtonElement(False, MIDI_CC_TYPE, 1, SCENES[1]))                 
          # code left above so you cant replace either button with a play button
                                                                                                           
                                                                                                           
    def disconnect(self):
        ControlSurface.disconnect(self)
                                                                              
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
