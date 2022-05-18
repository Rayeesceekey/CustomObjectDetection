# Custom Object Detection

This project is to train and detect humans cars from images

## Summary

### Approach

1. Custom dataset provided, which contains around ~2200 imges and all of them are annotated with person and car
2. I choose yolov5 architecture to train
3. Single annotation file(json) converted to individual txt files for each image(yolo format) using "convert_json.py"
4. Trained with 150 epochs and default hyper parameters.

### Model Details

#### About Model

* Used YoloV5 architecture and pre_trained weights to train our custom data.
  -  [Yolo-V5 Frameworkd](https://github.com/ultralytics/yolov5)
* Trained with pre-trained large model provided by yolo team.
* I used the default parameters to train the model and I didn't try with any other model as I got less time to work on this.

#### Results and Metrics

| Class | Images  | Labels  |Precision  | Recall  | mAP@.5  |mAP@.5:.95: 100%|
| ------| --------| --------|-----------| --------| --------|----------------|
|  all  |  110    |   872   |   0.773   | 0.609   |  0.67   |     0.414      |
| person|  110    |   601   |   0.722   | 0.546   |  0.614  |     0.318      |
| car   |  110    |   271   |   0.823   | 0.672   |  0.726  |     0.51       |

#### Assumptions and Conclusions

* Precision, Recall and mAP score are less
* I checked some annotations in the training set(visualize_bbox.py) ans found that some of the annotations are missing, thay may be one reason we are getting less accuracy.
* And I train with large model with less number of epochs with default parameters, so we have to play with the parameters and check which is working better for our dataset.

### Future work

There are some pre-trained weights available in the hub for general labels(including car and person), So we can use this as our initial model and use the output to fill where our annotations missing, then we can train with the model, it may improve accuracy.
And also we can use their pre-trained largest model to do the inference as it is trained with large set of data(for person and car).

### Install and Run

- Buil the docker container
    ```
    sudo docker build -t "image_name" ./
    ```
- Run the docker container
    ```
    sudo docker run -d --volume /absolute_path_to_project_in_local/app/output/:/app/yolov5/runs/ --name "container_name" -p 80:80 "image_name"
    ```
- Then open any API client or you can open swagger UI by :- http://127.0.0.1/docs
    - Train end point :- /model_train
        sample parameters:-
            {
                "yaml_file_path": "data.yaml",
                "yolo_weight_file": "yolov5l.pt",
                "epochs": 150
            }
    - Inference end point : /model_inference/from_path(Inference using folder path,will do inference for all images and output will be stored in "output" directory)
        sample parameters:-
            {
                "image_path": "DataSet/test",
                "yaml_file_path": "data.yaml",
                "model_path": "artifacts/weights/best.pt"
            }
    - Inference end point : /model_inference/from_image(Inference by image path and output will be stored in "output" directory) and it shows the output image in response body.
        sample parameters:-
            {
                "image_path": "DataSet/test",
                "yaml_file_path": "data.yaml",
                "model_path": "artifacts/weights/best.pt",
                "use_pretrained": false (if true, inference will do with pre-trained model from yolo hub)
            }
