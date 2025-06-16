from PIL import Image, ImageChops

class ImageMC():

    def __init__ (self, ImageNumber, ImagePath):
        self.ImageNumber = ImageNumber;
        self.ImagePath =ImagePath;
  
    def ImageMerging(self):
        if self.ImageNumber == 1:
            Image1 =Image.open(self.ImagePath+'image_1.jpg').convert('RGB');
            Image1.save(self.ImagePath+'image_merged.jpg');
        if self.ImageNumber >= 2:
            Image1 = Image.open(self.ImagePath+'image_1.jpg').convert('RGB');
            Image2 = Image.open(self.ImagePath+'image_2.jpg').convert('RGB');
            MergeImage= Image.blend(Image1, Image2,alpha=0.5);
            for i in range(3,self.ImageNumber):
                Image1 = MergeImage;
                Image2 = Image.open(self.ImagePath+'image_'+str(i)+'.jpg').convert('RGB');
                alpha = 1.0 / i;
                MergeImage= Image.blend(Image1, Image2,alpha);
            MergeImage = MergeImage.convert('RGB');
            MergeImage.save(self.ImagePath+'image_merged.jpg');
            Image1.close();
            Image2.close();
            MergeImage.close();
    
    def ImageComparison(self,NewPath):
        MergeImage = Image.open(self.ImagePath+'image_merged.jpg');
        CompareImage = Image.open(NewPath).convert('RGB');
        Difference = ImageChops.difference(MergeImage, CompareImage);
        DifferencePixels = sum(map(sum, Difference.getdata()))
        ImageWidth, ImageLength = CompareImage.size  # Get dimensions of the merged image
        MergeImage.close()
        CompareImage.close()
        return (1 - (DifferencePixels / (ImageWidth * ImageLength * 255)))*100