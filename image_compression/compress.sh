resize_percentage=$1
FILE_MASK=$2
target_dir=$3
#mkdir $target_dir
for f in $FILE_MASK
do
	cp $f "$target_dir"/"$f"
	convert "$target_dir"/"$f" -resize "$resize_percentage"% "$target_dir"/"$f"
done
