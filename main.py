from rvc_infer import rvc_inference



if __name__ == "__main__":
    """
    Example Usage and Instructions

    1- put the model in the "assets/weights" folder
    2- replace th 3 paths in the function with the path to audios, index, and output folder
    3- there is also another parameter you can change in the function but i put in them the default values as in 
       the web version
    """

    rvc_inference(
        "model.pt",
        "path/to/audios",
        "path/to/index",
        "path/to/output/folder"
    )


