import os
os.system("pip install -r requirements.txt")
import json
from src.config import EnvironmentConfig
from src.profile_dda import ProfileDDA
from src.reader import ReaderFactory
from src.utils import easy_log
from src.writer import WriterFactory

env = os.environ.get("ENVIRONMENT", None)
odate = os.environ.get("ODate", None)

print("")
print("Environment = " + str(env))
print("ODate = " + str(odate))
print("")

# Validate Odate
if odate is None:
    raise ValueError("oDate cannot be empty")

if env is None or len(env) == 0:
    env = "local"
    print("")
    easy_log("Environment is reading from local", level="warn")
    print("")
else:
    print("")
    easy_log(f"Reading files from {env}", level="warn")
    print("")

reader = ReaderFactory.get_reader(env)
writer = WriterFactory.get_writer(env)
spark = EnvironmentConfig.get_spark_session()

with open(EnvironmentConfig.get_config_file_path(env), "r") as f:
    config = json.load(f)


padding_config: None

with open(EnvironmentConfig.get_padding_D_file_path(), "r") as f:
    padding_D_config = json.load(f)

with open(EnvironmentConfig.get_padding_B_file_path(), "r") as f:
    padding_B_config = json.load(f)

print("")
easy_log(f"Detail padding config: {padding_D_config}", level="info")
print("")
easy_log(f"Bal padding config: {padding_B_config}", level="info")

profile_dda = ProfileDDA(spark, odate, config, padding_D_config, padding_B_config, reader)

output_path_base = config["output_path_base"]

output_bucket_prefix = config["output_bucket_prefix"]

temp_ouputFilname_data = "profile_dda_output_data"
temp_ouputFilname_PS = "profile_dda_output_ps"

local_s3_path = config["output_bucket_prefix"]

# Generate Profile DDA Output
profile_dda_output = profile_dda.get_data()

# Save Profile DDA Output
prfl_dda_outputpath = writer.save_output(profile_dda_output, temp_ouputFilname_data, odate, str(output_path_base + "data/"))
easy_log(f"prfl_dda_outputpath: {prfl_dda_outputpath}\n", level="info")

# Generate peoplesoft adapter df
ps_output_df = writer.generate_peoplesoft_adapter(odate, local_s3_path, spark)

# Save Profile DDA Output PS file
prfl_dda_ps_outputpath = writer.save_output(ps_output_df, temp_ouputFilname_PS, odate, str(output_path_base + "ps/"))
easy_log(f"prfl_dda_ps_outputpath: {prfl_dda_ps_outputpath}\n", level="info")

# Publish to stream
writer.stream_publish(config["PRF_DDA_Schema"], [prfl_dda_outputpath], odate, env)
writer.stream_publish(config["PRF_DDA_PS_ADPT_Schema"], [prfl_dda_ps_outputpath], odate, env)
