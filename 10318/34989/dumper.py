#dumper script
np.savez('result_dist.npz',normal_dist=normal_dist,diff=diff)
import zlib
import zipfile

def compress(file_names):
    print("File Paths:")
    print(file_names)

    # Select the compression mode ZIP_DEFLATED for compression
    # or zipfile.ZIP_STORED to just store the file
    compression = zipfile.ZIP_DEFLATED

    # create the zip file first parameter path/name, second mode
    with zipfile.ZipFile("result.zip", mode="w") as zf:
        for file_name in file_names:
            # Add file to the zip file
            # first parameter file to zip, second filename in zip
            zf.write('./'+file_name, file_name, compress_type=compression)


file_names= ["result_dist.npz","dists_diff.py", "solution.ipynb"]
compress(file_names)