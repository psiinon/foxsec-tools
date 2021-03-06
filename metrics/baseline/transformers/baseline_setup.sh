# Wrapper for running the main baseline transformer against ALL of the existing baseline files

# Install aws_cli
pip3 install awscli --upgrade

# Set up the aws credentials
mkdir ~/.aws
cat > ~/.aws/credentials <<DELIM
[default]
aws_access_key_id = $AWS_ACCESS_KEY
aws_secret_access_key = $AWS_SECRET_KEY
DELIM

mkdir s3bucket
aws s3 sync s3://foxsec-metrics/baseline/ s3bucket/

# Run transformer for all days
python3 transformers/baseline.py -s s3bucket/raw/ -d s3bucket/
 
# Write all files to aws
aws s3 sync s3bucket/ s3://foxsec-metrics/baseline/ 
