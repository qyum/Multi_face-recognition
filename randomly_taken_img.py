#combine images from multiple folders

import random 
folders = [
    'E:face_reconiger/person1.jpg','E:/face_reconiger/person2.jpg','E:/face_reconiger/person3.jpg',
    'E:/face_reconiger/person4.jpg','E:/face_reconiger/person5.jpg','E:/face_reconiger/person6.jpg',
    'E:/face_reconiger/person7.jpg','E:/face_reconiger/person8.jpg','E:/face_reconiger/person9.jpg',
    'E:/face_reconiger/person10.jpg','E:/face_reconiger/person11.jpg','E:/face_reconiger/person12.jpg',
    'E:/face_reconiger/person13.jpg','E:/face_reconiger/person14.jpg','E:/face_reconiger/person15.jpg',     
]

file=[]
for folder in folders:
    #images = load_images_from_folder(folder)
    for filename in os.listdir(folder):
        if any([filename.endswith(x) for x in ['.jpg']]):
            file.append(os.path.join(folder, filename))


#randomly taken the image from combine file............................ 
   
#print(len(file))
chosen_images = np.random.choice(file, size=500)
#print(len(chosen_images))


random_images=[]
for i in chosen_images:
    images=cv2.imread(i)
    #print(images)
    if images is not None:
        random_images.append(images)
         
print(random_images)
