#-------------------STARTUP-BOX--------------------------#
#-----Group-Task-On-Image-Processing---------------------#
#-----Group-Members--------------------------------------#
#------------------Krishna Prasad K----------------------#
#------------------Amal Dethan---------------------------#
#------------------Deepu SP------------------------------#
#------------------Manu Karthikeyan----------------------#
#---------------[Govt. RIT, Kottayam]--------------------#

import gtk
from PIL import Image,ImageChops
import math
import urllib

class comparison:
   def __init__(self):
      def message(msg):
         dialog=gtk.MessageDialog(win,type=gtk.MESSAGE_ERROR,buttons=gtk.BUTTONS_OK)
         dialog.set_title("Error")
         dialog.set_markup(msg)
         response=dialog.run()
         dialog.destroy()



      def result(res,data):
         dialog=gtk.MessageDialog(win,type=gtk.MESSAGE_INFO,buttons=gtk.BUTTONS_OK)
         dialog.set_title("Result")
         calc=str(100-float(res))
         if float(res)>100:
            d='0'
         else:
            d=str(100-(float(res)))

         dialog.set_markup('<span foreground="blue" size="16000" style="italic" weight="heavy">'+"Similarity: "+d+'</span>')

         response=dialog.run()
         dialog.destroy()



      def compare(self):
         try:
            url1=entry1.get_text()
            url2=entry2.get_text()
            new_file_type1=url1[-4:]
            new_file_type2=url2[-4:]
            if new_file_type1=='.jpe' or new_file_type2=='.jpe':
                new_file_type1='.jpeg'
                new_file_type2='.jpeg'

            urllib.urlretrieve(url1,'image1'+new_file_type1)
            urllib.urlretrieve(url2,'image2'+new_file_type2)

            image1=Image.open('image1'+new_file_type1)
            image2=Image.open('image2'+new_file_type2)
            image_height=image1.size[0]
            image_width=image1.size[1]

            mode='RGB'
            difference=ImageChops.difference(image1.convert(mode),image1.convert(mode))
            histo=difference.histogram()
            squares=(j*(i**2) for i, j in enumerate(histo))
            sum_of_squares=sum(squares)
            rms=math.sqrt(sum_of_squares/float(image_height * image_width))
            default_value=rms


            difference=ImageChops.difference(image1.convert(mode),image2.convert(mode))
            histo=difference.histogram()
            squares=(j*(i**2) for i, j in enumerate(histo))
            sum_of_squares=sum(squares)
            rms=math.sqrt(sum_of_squares/float(image_height * image_width))
            current_value=rms


            res=str(math.floor(abs(default_value-current_value)))
            result(res,default_value)

         except Exception as e:
            message(str(e))




      frame=gtk.Frame()
      hbox=gtk.HBox()
      vbox=gtk.VBox()
      label1=gtk.Label("Enter the first image url")
      label2=gtk.Label("Enter the second image url")
      entry1=gtk.Entry()
      entry2=gtk.Entry()
      button=gtk.Button("Compare")
      button.connect("clicked",compare)
      fixed=gtk.Fixed()
      fixed.put(label1,20,100)
      fixed.put(entry1,200,100)
      fixed.put(label2,20,150)
      fixed.put(entry2,200,150)
      fixed.put(button,170,200)
      frame.add(fixed)
      heading=gtk.Label()
      heading.set_markup('<span foreground="black" size="16000" style="normal" weight="bold">Image Comparison</span>')
      about=gtk.Label('''A Startup Box group task done by Krishna Prasad K, Manu Karthikeyan,
                                            Amal Dethan and Deepu SP.''')
      fixed.put(heading,100,30)
      fixed.put(about,10,260)
      win=gtk.Window()
      win.add(frame)
      win.set_size_request(400,300)
      win.connect('delete_event',gtk.main_quit)
      win.set_title('Image Comparison')
      win.set_position(gtk.WIN_POS_CENTER_ALWAYS)
      win.show_all()

if __name__=='__main__':
    comparison()
    gtk.main()

