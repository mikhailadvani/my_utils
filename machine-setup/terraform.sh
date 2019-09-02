set -e

TERRAFORM_DOWNLOAD_URL="https://releases.hashicorp.com/terraform/0.12.7/terraform_0.12.7_darwin_amd64.zip"
TERRAFORM_TMP_DIR="/tmp/terraform"

mkdir -p $TERRAFORM_TMP_DIR
curl -o $TERRAFORM_TMP_DIR/terraform.zip $TERRAFORM_DOWNLOAD_URL
unzip $TERRAFORM_TMP_DIR/terraform.zip -d $TERRAFORM_TMP_DIR
mv $TERRAFORM_TMP_DIR/terraform /usr/local/bin/
chmod +x /usr/local/bin/terraform
rm -rf $TERRAFORM_TMP_DIR
