
#.......extract images from video(by dlib).............

import dlib
detector= dlib.get_frontal_face_detector()


def extract_face(frame,face):
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    face_frame = frame[y: y + h, x: x + w].copy()
    return face_frame
 

def extract_video(video,root_save_image):
     
    capture = cv2.VideoCapture(video)
    #print(capture)
    frames_num = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    #print(frames_num)

     
    for i in range(frames_num):
        capture.grab()
        #if i % 5 != 0:
            #continue
        success, frame = capture.retrieve()
        #print(frame) 
        if not success:
            continue
        id = os.path.splitext(os.path.basename(video))[0]
         
        #remove noise from frame_image
        #frame= cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21) 
        image_copy = np.copy(frame)
        
        #frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces=detector(frame)
        #draw a rectangle
        #face_crop = []
        #print(len(faces))
        if len(faces)>0:
             
            for face in faces:
                frame=extract_face(frame,face)
                cv2.imwrite(os.path.join(root_save_image,"{}_{}.jpg".format(id, i)),frame) 
                #cv2.imwrite(root_save_image, frame)

if __name__ == '__main__':
    
    root_save_image='E:/face_reconiger/person15.jpg/'
    videos='E:/individual_videos/person_15/person_15.mp4'
    #extract_video(videos,root_save_image)
    
#or,

#.......extract images from video(by MTCNN).............
from mtcnn import MTCNN
detector_1 = MTCNN()

def extract_face(frame,face):
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    face_frame = frame[y: y + h, x: x + w].copy()
    return face_frame
 

def extract_video(video,root_save_image):
     
    capture = cv2.VideoCapture(video)
    #print(capture)
    frames_num = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    #print(frames_num)

     
    for i in range(frames_num):
        capture.grab()
        #if i % 5 != 0:
            #continue
        success, frame = capture.retrieve()
        #print(frame) 
        if not success:
            continue
        id = os.path.splitext(os.path.basename(video))[0]
        
        #remove noise from frame_image
        frame= cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
         
        image_copy = np.copy(frame)
        #frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #faces=detector_1(frame)
        faces= detector_1.detect_faces(frame)
         
        if len(faces)>0:
             for face in faces:
                    print(face)
                    x, y, w,h = face['box']
                    frame=frame[y: y + h, x: x + w].copy()
             
                    cv2.imwrite(os.path.join(root_save_image,"{}_{}.jpg".format(id, i)),frame)
                     
                   

if __name__ == '__main__':
    
    root_save_image='E:/face_reconiger/person10.jpg/'
    videos='E:/individual_videos/person_10/person_10.mp4'
    #extract_video(videos,root_save_image)

