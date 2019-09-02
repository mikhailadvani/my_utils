set -ex
SETUP_DIR=$(dirname $0)
cd $SETUP_DIR

DEST_PATH="/tmp"

cp -R dotfiles/. $DEST_PATH
