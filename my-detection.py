
import jetson.inference
import jetson.utils
def detect_objects(image_path,output_path):
    net = jetson.inference.detectNet(network="ssd-mobilenet-v2", threshold=0.5)
    try:
        img=jetson.utils.loadImage(image_path)
    except Exception as e:
        print(f"Error loading image{image_path}: {e}")
        return none

    detections = net.Detect(img)
    print(f"\nthe number of detection objects is{len(detections)}")
    
    for detection in detections:
        class_desc = net.GetClassDesc(detection.ClassID)
        print(f"ClassID:{detection.ClassID}")
        print(f"Confidence:{detection.Confidence:.2f}")
        print(f"Left:{detection.Left}")
        print(f"Top:{detection.Top}")
        print(f"Right:{detection.Right}")
        print(f"Bottom:{detection.Bottom}")
        print(f"Width:{detection.Width}")
        print(f"Height:{detection.Height}")
        print(f"Area:{detection.Area}")
        print(f"Center:{detection.Center}")
    try:
    #   jetson.utils.saveImage(output_path,img)
            display=jetson.utils.videoOutput(output_path)
            display.Render(img)
            display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
    except Exception as e:
            print(f"Erroe during save: {e}")
    return detections
def main():
    output_path ="/home/nvidia/jetson-inference/detect"
    image_path="/home/nvidia/jetson-inference/detect/p.jpg"
    detect_objects(image_path,output_path)
if __name__=="__main__":
    main()

