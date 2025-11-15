import cv2
import pytesseract

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

if __name__ == "__main__":
    sample_image = "data/sample.jpg"
    text = extract_text_from_image(sample_image)
    print("Extracted Text:\n", text)