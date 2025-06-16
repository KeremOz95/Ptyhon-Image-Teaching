import ImageTeaching  # Import the Image_MG class from ImageTeaching module
import CaptureCamera  # Import the CaptureCamera module
Objects = {}  # Dictionary of objects

def main():
    
    RootPath = "C:/Users/Kerem/Desktop/"  # Root path for images
    while True:
        UserInput = input('Create new Object ?(y/n)')  # Create new object
        if UserInput == 'y':
            ObjectName = input('Object Name ?')  # Object name (Compare_Image olamaz !!!)
            #ImagePath = f"{RootPath}{ObjectName}/"  # Path
            ImageNumber = CaptureCamera.main(f"{RootPath}{ObjectName}/")  # Number of images taken
            Objects[ObjectName] = ImageTeaching.ImageMC(int(ImageNumber), f"{RootPath}{ObjectName}/")  # Create object
            Objects[ObjectName].ImageMerging()
            print('New Object ', ObjectName, 'added. Number of Objects :', len(Objects))
        else :
            break # Exit the loop

    ObjectName = "Compare_Image" # Object name
    print('Get Ready for Comparison picture')
    CaptureCamera.main(f"{RootPath}{ObjectName}/")  # Number of images taken
    NewPath = f"{RootPath}{ObjectName}/Image_1.jpg"  # Path

    UserInput = input('Start Comparison ?(y/n)'); #Start comparison
    if UserInput == 'y':
        array = []  # Initialize an empty list to store object names and similarities
        for ObjectName, Object in Objects.items():  # Iterate through the objects
            Similarity = Object.ImageComparison(NewPath)  # Get similarity value
            array.append((ObjectName, Similarity))  # Append object name and similarity to the array
            print(ObjectName , ':' , Similarity, ' %')  # Print similarity value
            
        MaxValue = max(array, key=lambda x: x[1])  # Find the object with the highest similarity
        print('Most similar object:', MaxValue[0], 'with similarity:', MaxValue[1])  # Print resultn the array and return the name of the object

if __name__ == "__main__":
    main()