#!/usr/bin/env python
import os, sys
import math
import boto
import argparse

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
MULTIPART_THRESHOLD = 10000*1024*1024
BYTES_PER_CHUNK = 5000*1024*1024

def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bucket", type=str, help="Selects the S3 bucket to upload data to")
    parser.add_argument("-f", "--file_path", type=str, help="Path of the file to be uploaded")
    parser.add_argument("-k", "--key", type=str, default=None, help="Key of the object. Same as file_path is undefined")
    parser.add_argument("--report", default='html', help="Prints test execution on the console rather than generating a HTML report")
    args = parser.parse_args()

    if args.key is None:
        args.key = args.file_path
    return args

def multipart_upload_to_be_used(file_path):
    file_size = os.stat(file_path).st_size
    return file_size > MULTIPART_THRESHOLD

def simple_upload(s3_connection, bucket_name, file_path, s3_path):
    bucket = s3_connection.get_bucket(bucket_name)
    key = boto.s3.key.Key(bucket, s3_path)
    key.set_contents_from_filename(file_path)

if __name__ == "__main__":
    args = usage()
    s3_connection = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    if not multipart_upload_to_be_used(args.file_path):
        simple_upload(s3_connection, args.bucket, args.file_path, args.key)

