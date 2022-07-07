from img2dataset import download
import shutil
import os
import time

jobfolder = "joblist/"
parts = range(64)

os.makedirs(jobfolder, exist_ok=True)

for part in parts:
    if os.path.isfile(jobfolder + f"{part:02d}"):
        ### Find the first unstarted job.
        pass
    else:
        ### Create file when starting job.
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
        with open(jobfolder + f"{part:02d}", "w") as f: 
            f.write(f"Started job {part} at {now}.\n")


        ### Append time when finishing job.
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
        with open(jobfolder + f"{part:02d}", "a") as f: 
            f.write(f"Finished job {part} at {now}.")

# if __name__ == '__main__':
#     output_dir = os.path.abspath("bench")

#     if os.path.exists(output_dir):
#         shutil.rmtree(output_dir)

#     download(
#         processes_count=16,
#         thread_count=32,
#         url_list="s3://s-laion/improved-aesthetics-laion-2B-en-subset/5/",
#         image_size=512,
#         output_folder=output_dir,
#         output_format="webdataset",
#         input_format="parquet",
#         url_col="URL",
#         caption_col="TEXT",
#         enable_wandb=False,
#         number_sample_per_shard=1000,
#         save_additional_columns=["similarity","hash","punsafe","pwatermark","AESTHETIC_SCORE"],
#         distributor="multiprocessing"
#     )

#     # rm -rf bench
