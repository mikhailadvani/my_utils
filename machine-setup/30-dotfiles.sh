set -ex
SETUP_DIR=$(dirname $0)
cd $SETUP_DIR

DEST_PATH="$HOME"

cp -R dotfiles/. $DEST_PATH
